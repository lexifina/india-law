"""Check each corpus.d part line by line against its gazette PDF text layer (private).
Every unit line (headings excepted) must be found, letters and digits only, in order in the PDF's text.
Usage: python -X utf8 verify_parts.py <part.json> <pdf>"""
import json, re, sys, warnings
warnings.filterwarnings('ignore')
import pymupdf
from parse_acts import norm


def key(s):
    return re.sub(r'[^a-z0-9]', '', norm(s).lower())


part, pdf = sys.argv[1], sys.argv[2]
d = json.load(open(part, encoding='utf-8'))
src = key(''.join(p.get_text() for p in pymupdf.open(pdf)))
for act in d['acts']:
    units = act['versions'][0]['units']
    pos = 0; n = 0; bad = []; out = []; gaps = []; split = 0
    for k in sorted(units, key=lambda k: (k != 'preamble', k)):
        if not k.startswith(('preamble', 'sec-')):
            continue
        for ln in units[k]['text'].splitlines():
            if ln.startswith('# '):
                continue
            kk = key(ln)
            if not kk:
                continue
            n += 1
            j = src.find(kk, pos)
            if j >= 0 and j - pos < 5000:
                pos = j + len(kk); continue
            # greedy pieces with bounded gaps (marginal notes and page heads interleave in the text layer)
            q = pos; r = kk; ok = True; first = True
            while r:
                lo = 0
                for i in range(min(len(r), 12), len(r) + 1):
                    jj = src.find(r[:i], q)
                    if jj < 0 or (not first and jj - q > 600):
                        break
                    lo = i; at = jj
                if lo == 0 or (lo < 12 and lo < len(r)):
                    ok = False; break
                if not first:
                    gaps.append(src[q:at])
                first = False; q = at + lo; r = r[lo:]
            if ok:
                pos = q; split += 1
            else:
                bad.append((k, ln[:100]))
    secs = sorted(int(re.match(r'sec-(\d+)', k).group(1)) for k in units if k.startswith('sec-'))
    miss = sorted(set(range(1, max(secs) + 1)) - set(secs))
    print(act['slug'], 'lines', n, 'split by page/margin', split, 'gaps', len(gaps), 'gap chars', sum(map(len, gaps)), 'not found', len(bad), 'out of order', len(out), 'sections', len(units), 'max', max(secs), 'missing', miss)
    for b in bad[:10]: print('  NOT FOUND', b)
    if '-v' in sys.argv:
        for g in gaps: print('  GAP', g[:200])
    for b in out[:10]: print('  ORDER', b)
