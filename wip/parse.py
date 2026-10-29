"""Parse .cache/coi.txt (Constitution of India, as on 1 May 2024) into corpus.json (private)."""
import re, json, hashlib, pathlib, sys
H = pathlib.Path(__file__).parent
raw = (H / '.cache' / 'coi.txt').read_bytes()
SHA = hashlib.sha256((H / '.cache' / 'coi.pdf').read_bytes()).hexdigest()
txt = raw.decode('utf-8', 'replace')
pages = txt.split('\f')

def key(n):
    m = re.fullmatch(r'(\d+)([A-Z]*)', n)
    return (int(m.group(1)), m.group(2))

# contents -> expected article sequence
lines = txt.split('\n')
start = next(i for i, l in enumerate(lines) if l.strip() == 'PREAMBLE')
end = next(i for i, l in enumerate(lines) if re.match(r'\s*395\.\s+Repeals', l))
exp = []
for l in lines[start:end + 1]:
    m = re.match(r'\s*\[?(\d+[A-Z]*)\.(?:\s+\S|\s*$)', l)
    if m and int(re.match(r'[0-9]+', m.group(1)).group()) <= 395 and (not exp or key(m.group(1)) > key(exp[-1])):
        exp.append(m.group(1))
assert exp[0] == '1' and exp[-1] == '395', (exp[:3], exp[-3:])

# body pages
body_start = next(i for i, p in enumerate(pages) if 'PREAMBLE' in p and 'WE, THE PEOPLE' in p)
body_end = next(i for i, p in enumerate(pages) if re.search(r'^\s*395\.\s+Repeals\.--', p, re.M))
out = []
for p in pages[body_start:body_end + 1]:
    ls = p.split('\n')
    cut = next((i for i, l in enumerate(ls) if re.match(r'\s*_{10,}\s*$', l)), None)
    # footnote rule: drop from the rule to page end, except the rule right under the preamble title lines
    if cut is not None:
        ls = ls[:cut]
    for l in ls:
        s = l.strip()
        if not s: continue
        if re.fullmatch(r'\d+', s): continue
        if re.fullmatch(r'(\d+\s+)?THE CONSTITUTION OF INDIA(\s+\d+)?', s): continue
        if re.fullmatch(r'\((Part|PART)[^)]*\)', s) or re.fullmatch(r'\(Part [^)]*\)\s*\d*', s): continue
        if re.fullmatch(r'\d+\s+\(Part.*\)|\(Part.*\)\s+\d+', s): continue
        out.append(s)
body = out

# split by expected articles
idx = {}
pos = 0
for a in exp:
    pat = re.compile(r'^(?:\d+\*?\[)*\[?' + re.escape(a) + r'\.\s*\S')
    pat2 = re.compile(r'^\d{1,2}\*?\[?\[?' + re.escape(a) + r'\.\s*\S')
    for j in range(pos, len(body)):
        if pat.match(body[j]) or pat2.match(body[j]):
            idx[a] = j; pos = j + 1; break
    else:
        print('MISSING', a, file=sys.stderr)
missing = [a for a in exp if a not in idx]
order = [a for a in exp if a in idx]

def clean(t):
    t = t.replace(' ', ' ')
    t = re.sub(r'\d+\*{3}', '', t)           # footnote on omitted words
    # strip amendment brackets "N[ ... ]" keeping plain brackets
    res = []; stack = []; i = 0
    while i < len(t):
        m = re.compile(r'(?<![\w.])\d{1,2}\*?\[').match(t, i) if (i == 0 or not t[i-1].isalnum()) else None
        if m:
            stack.append('n'); i = m.end(); continue
        c = t[i]
        if c == '[': stack.append('b'); res.append(c)
        elif c == ']':
            if stack and stack[-1] == 'n': stack.pop()
            else:
                if stack: stack.pop()
                res.append(c)
        else: res.append(c)
        i += 1
    t = ''.join(res)
    return t

def paragraphs(block):
    # join wrapped lines: a new paragraph starts at "(1)", "(a)", "Provided", "Explanation", article head, list items
    paras = []
    for s in block:
        if not paras or re.match(r'(\(\w{1,4}\)|\[?\(\w{1,4}\)|Provided|Explanation|\d+[A-Z]*\.\s|—|-)', s) or re.match(r'\d+\[\(', s) or re.match(r'\d+\[(Provided|Explanation)', s):
            paras.append(s)
        else:
            paras[-1] += ' ' + s
    return paras

units = {}; credits = {}
# preamble
pre = body[:idx[order[0]] if False else idx['1']]
pre = [l for l in pre if not re.fullmatch(r'(PART [IVXLC]+|THE UNION AND ITS TERRITORY|PREAMBLE)', l)]
units['preamble'] = {'label': 'Preamble', 'kind': 'preamble', 'text': '# Preamble\n' + '\n'.join(re.sub(r'\s+', ' ', p).strip() for p in clean('\n'.join(paragraphs(pre))).split('\n')) + '\n'}
HEAD = re.compile(r'^(?:PART [IVXLC]+[A-Z]?|CHAPTER [IVXLC]+\.?.*|THE [A-Z ,\-]+|[A-Z][A-Z ,\-\.\'’]+|[A-Z][a-z]+(?: [A-Za-z,’\']+)*)$')
for n, a in enumerate(order):
    s, e = idx[a], (idx[order[n + 1]] if n + 1 < len(order) else len(body))
    block = body[s:e]
    # trailing part/chapter headings belong to the next article: trim lines that are Part/Chapter titles at the end
    for q in range(1, len(block)):
        if re.fullmatch(r'(PART [IVXLC]+[A-Z]?|CHAPTER [IVXLC]+\.?.*)', block[q]):
            block = block[:q]; break
    while block and re.match(r'(PART [IVXLC]+[A-Z]?\b|CHAPTER [IVXLC]+\.?\b|THE [A-Z ,\-]{6,}$|[A-Z][A-Z ,\-\.’\']{5,}$)', block[-1]) :
        block.pop()
    while len(block) > 1 and len(block[-1]) <= 75 and not re.search(r'[.;:,\]\)—\-]$|(and|or)$', block[-1]) and not re.search(r'^\(', block[-1]):
        block.pop()
    ps = paragraphs(block)
    t = clean('\n'.join(ps))
    ps = [re.sub(r'\s+', ' ', p).strip() for p in t.split('\n') if p.strip()]
    ps = [re.sub(r'^(\[?)\s*', r'\1', p) for p in ps]
    head = ps[0]
    label = 'Art. ' + a
    k = 'art-%03d%s' % (key(a)[0], ('-' + key(a)[1].lower()) if key(a)[1] else '')
    units[k] = {'label': label, 'kind': 'art', 'text': '# ' + label + '\n' + '\n'.join(ps) + '\n'}
for u in units.values(): pass
corpus = json.loads((H / 'corpus_head.json').read_text('utf-8'))
corpus['acts'][0]['versions'][0]['units'] = units
corpus['acts'][0]['versions'][0]['sha256'] = SHA
(H / 'corpus.json').write_text(json.dumps(corpus, ensure_ascii=False, indent=1) + '\n', 'utf-8')
print(len(units), 'units; missing', missing)
