"""Parse Indian Gazette-extraordinary act PDFs (English, text layer) in .cache/ into units. Used by parse.py (private)."""
import re, pathlib, warnings
warnings.filterwarnings('ignore')
import pymupdf
H = pathlib.Path(__file__).parent

SEC = re.compile(r'^(\d+[A-Z]{0,2})\.\s*(?=[A-Z(\"])')
BOLDSEC = re.compile(r'^(\d+[A-Z]{0,2})\.?\s*(?=[A-Z(\"])')
CH = re.compile(r'^(CHAPTER|PART)\s+([IVXLC]+[A-Z]?)$')


def norm(s):
    s = s.replace('\xa0', ' ').replace('­', '')
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('–', '-').replace('—', '-').replace('−', '-')
    return re.sub(r'\s+', ' ', s).strip()


JUNK = re.compile(r'^\[PART II|vlk/kkj|Hkkx II|izkf/kdkj|lañ|bl Hkkx|xxx|jftLV|CG-DL|[ऀ-ॿ]|^EXTRAORDINARY|^PART II|PUBLISHED BY AUTHORITY|REGISTERED NO|Separate paging')


def body_lines(pdf, margin_x=484, left_x=110, top=80, line_level=False):
    d = pymupdf.open(str(pdf))
    for pi, page in enumerate(d):
        for b in page.get_text('dict')['blocks']:
            if b.get('type') != 0:
                continue
            x0, y0, x1, y1 = b['bbox']
            if not line_level and (x0 >= margin_x or x0 < left_x):
                continue
            for li, ln in enumerate(b['lines']):
                t = ''.join(s['text'] for s in ln['spans'])
                if not t.strip():
                    continue
                lx0, ly0, lx1, ly1 = ln['bbox']
                if line_level and (lx0 >= margin_x or lx0 < left_x):
                    continue
                first = li == 0 or (line_level and b['lines'][li - 1]['bbox'][0] < left_x)
                if ly0 < top and ('GAZETTE OF INDIA' in t.replace('_', '') or re.match(r'^\s*(Sec\.|\d+\]|_)', t)):
                    continue
                if t.strip().replace('_', '') == '' or re.match(r'^[_\s\d]*T[_\s]*H[_\s]*E[_\s]*G', t) or 'T___H___E' in t:
                    continue
                if line_level:
                    sp = [x for x in ln['spans'] if x['text'].strip()]
                    bold = bool(sp) and bool(sp[0]['flags'] & 16) and bool(re.match(r'\s*\d+[A-Z]{0,2}\.?\s*$', sp[0]['text']))
                    yield pi, lx0, lx1, norm(t), first, bold
                else:
                    yield pi, lx0, lx1, norm(t), first


HDR = re.compile(r'^\[\s*part\s+ii.*|^sec\.\s*\d+\]?$', re.I)
PAGE0 = re.compile(r'NEW DELHI, MONDAY|^No\. \d+\]|MINISTRY OF LAW|Legislative Department|^New Delhi, the|The following Act of Parliament|ubZ fnYyh|^25th December, 2023 and is hereby|^-{3,}$|and is hereby published for general information')
START = re.compile(r'^(\(\w{1,4}\)|\d+[A-Z]{0,2}\.|Explanation|Exception|Illustration|Provided|Proviso|CHAPTER|PART |SCHEDULE|THE )')


def parse_act(pdf, start_text, end_re=None, monotonic=False, line_level=False):
    """monotonic: a numbered paragraph whose number does not exceed the last section's is text of that section (lists inside a section)."""
    lines = [l for l in body_lines(pdf, line_level=line_level) if not JUNK.search(l[3]) and not HDR.match(l[3]) and not re.fullmatch(r'\d{1,3}', l[3]) and not (l[0] == 0 and PAGE0.search(l[3]))]
    i0 = next(i for i, l in enumerate(lines) if l[3].startswith(start_text))
    lines = lines[i0:]
    end = next((i for i, l in enumerate(lines) if (end_re.search(l[3]) if end_re else re.fullmatch(r'-{3,}', l[3]))), len(lines))
    lines = lines[:end]
    bolds = {}
    if line_level:   # a bold section number printed alone on its line belongs to the next line
        joined = []
        for l in lines:
            if joined and joined[-1][5] and re.fullmatch(r'\d+[A-Z]{0,2}\.?', joined[-1][3]) and joined[-1][0] == l[0]:
                pi, x0, x1, t, first, bold = joined.pop()
                l = (pi, x0, l[2], t + ' ' + l[3], first, bold)
            joined.append(l)
        lines = []
        for l in joined:
            if l[5]:
                bolds[len(lines)] = True
            lines.append(l[:5])
    # group lines into paragraphs
    paras = []   # (kind, text, x0)
    prev = ''
    for li_, (pi, x0, x1, t, first) in enumerate(lines):
        centred = x0 > 170 and (x1 - x0) < 300 and abs((x0 + x1) / 2 - 298) < 30 and not re.match(r'^(Illustrations?\.?|\(\w{1,4}\))', t)
        if line_level and SEC.match(t):
            centred = False
        if centred:
            paras.append(['head', t, x0]); prev = ''; continue
        starts = (first and (not prev or prev[-1:] in '.;:-,?' or bool(START.match(t)))) or (x0 > 125 and (bool(START.match(t)) or prev[-1:] in '.;:-,?'))
        if paras and paras[-1][0] == 'text' and not starts:
            paras[-1][1] += ' ' + t
        else:
            paras.append(['text', t, x0, bolds.get(li_, False)])
        prev = t
    units = {}; cur = None; pending = []; seen = []
    i = 0
    while i < len(paras):
        k, t, x0 = paras[i][:3]
        m = CH.match(t) if k == 'head' else None
        if m:
            title = []
            j = i + 1
            while j < len(paras) and paras[j][1] == paras[j][1].upper() and len(paras[j][1]) > 3 and not SEC.match(paras[j][1]) and not CH.match(paras[j][1]):
                title.append(paras[j][1]); j += 1
            head = ('%s %s. %s' % (m.group(1).title(), m.group(2), ' '.join(title))).strip()
            units['chapter-' + m.group(2).lower()] = {'label': head, 'kind': 'part', 'lines': ['# ' + head]}
            pending = []; cur = None; i = j; continue
        s = SEC.match(t) if k == 'text' else None
        if line_level and k == 'text':   # sections start with a bold number (the full stop is sometimes missing)
            s = BOLDSEC.match(t) if len(paras[i]) > 3 and paras[i][3] else None
        if s and monotonic and seen:
            n_new, n_last = int(re.match(r'\d+', s.group(1)).group()), int(re.match(r'\d+', seen[-1]).group())
            if n_new < n_last or n_new > n_last + 10:
                s = None
        if False:
            s = None
        if s:
            num = s.group(1)
            key = 'sec-' + re.sub(r'^(\d+)', lambda mm: '%03d' % int(mm.group(1)), num).lower()
            units[key] = {'label': 'Section %s' % num, 'kind': 'section', 'lines': ['# Section %s' % num] + pending + [t]}
            pending = []; cur = key; seen.append(num); i += 1; continue
        if k == 'head':
            pending.append(t); i += 1; continue
        if cur is None:
            units.setdefault('preamble', {'label': 'Preamble', 'kind': 'preamble', 'lines': ['# Preamble']})['lines'].append(t)
        else:
            units[cur]['lines'].extend(pending); pending = []
            units[cur]['lines'].append(t)
        i += 1
    out = {k: {'label': u['label'], 'kind': u['kind'], 'text': '\n'.join(u['lines']) + '\n'} for k, u in units.items()}
    return out, seen
