"""Parse Indian Gazette-extraordinary act PDFs (English, text layer) in .cache/ into units. Used by parse.py (private)."""
import re, pathlib, warnings
warnings.filterwarnings('ignore')
import pymupdf
H = pathlib.Path(__file__).parent

SEC = re.compile(r'^(\d+[A-Z]{0,2})\.\s*(?=[A-Z(\"])')
CH = re.compile(r'^(CHAPTER|PART)\s+([IVXLC]+[A-Z]?)$')


def norm(s):
    s = s.replace('\xa0', ' ').replace('­', '')
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('–', '-').replace('—', '-').replace('−', '-')
    return re.sub(r'\s+', ' ', s).strip()


JUNK = re.compile(r'^\[PART II|vlk/kkj|Hkkx II|izkf/kdkj|lañ|bl Hkkx|xxx|jftLV|CG-DL|[ऀ-ॿ]|^EXTRAORDINARY|^PART II|PUBLISHED BY AUTHORITY|REGISTERED NO|Separate paging')


def body_lines(pdf, margin_x=484, left_x=110, top=80):
    d = pymupdf.open(str(pdf))
    for pi, page in enumerate(d):
        for b in page.get_text('dict')['blocks']:
            if b.get('type') != 0:
                continue
            x0, y0, x1, y1 = b['bbox']
            if x0 >= margin_x or x0 < left_x:
                continue
            for li, ln in enumerate(b['lines']):
                t = ''.join(s['text'] for s in ln['spans'])
                if not t.strip():
                    continue
                lx0, ly0, lx1, ly1 = ln['bbox']
                if ly0 < top and ('GAZETTE OF INDIA' in t.replace('_', '') or re.match(r'^\s*(Sec\.|\d+\]|_)', t)):
                    continue
                if t.strip().replace('_', '') == '' or re.match(r'^[_\s\d]*T[_\s]*H[_\s]*E[_\s]*G', t) or 'T___H___E' in t:
                    continue
                yield pi, lx0, lx1, norm(t), li == 0


HDR = re.compile(r'^\[\s*part\s+ii.*|^sec\.\s*\d+\]?$', re.I)
PAGE0 = re.compile(r'NEW DELHI, MONDAY|^No\. \d+\]|MINISTRY OF LAW|Legislative Department|^New Delhi, the|The following Act of Parliament|ubZ fnYyh|^25th December, 2023 and is hereby|^-{3,}$|and is hereby published for general information')
START = re.compile(r'^(\(\w{1,4}\)|\d+[A-Z]{0,2}\.|Explanation|Exception|Illustration|Provided|Proviso|CHAPTER|PART |SCHEDULE|THE )')


def parse_act(pdf, start_text, end_re=None, monotonic=False):
    """monotonic: a numbered paragraph whose number does not exceed the last section's is text of that section (lists inside a section)."""
    lines = [l for l in body_lines(pdf) if not JUNK.search(l[3]) and not HDR.match(l[3]) and not re.fullmatch(r'\d{1,3}', l[3]) and not (l[0] == 0 and PAGE0.search(l[3]))]
    i0 = next(i for i, l in enumerate(lines) if l[3].startswith(start_text))
    lines = lines[i0:]
    end = next((i for i, l in enumerate(lines) if (end_re.search(l[3]) if end_re else re.fullmatch(r'-{3,}', l[3]))), len(lines))
    lines = lines[:end]
    # group lines into paragraphs
    paras = []   # (kind, text, x0)
    prev = ''
    for pi, x0, x1, t, first in lines:
        centred = x0 > 170 and (x1 - x0) < 300 and abs((x0 + x1) / 2 - 298) < 30 and not re.match(r'^(Illustrations?\.?|\(\w{1,4}\))', t)
        if centred:
            paras.append(['head', t, x0]); prev = ''; continue
        starts = (first and (not prev or prev[-1:] in '.;:-,?' or bool(START.match(t)))) or (x0 > 125 and (bool(START.match(t)) or prev[-1:] in '.;:-,?'))
        if paras and paras[-1][0] == 'text' and not starts:
            paras[-1][1] += ' ' + t
        else:
            paras.append(['text', t, x0])
        prev = t
    units = {}; cur = None; pending = []; seen = []
    i = 0
    while i < len(paras):
        k, t, x0 = paras[i]
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
        if s and monotonic and seen and int(re.match(r'\d+', s.group(1)).group()) < int(re.match(r'\d+', seen[-1]).group()):
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
