"""Section-windowed check of a corpus.d part against its gazette PDF text layer (private).
Each section's span in the PDF runs from its first line to the next section's first line. Every unit line must be found
inside its section's span (letters and digits only): in order, or (table cells) anywhere in the span, or in pieces
split by page heads / marginal notes. Usage: python -X utf8 verify_window.py <part.json> <pdf> [-v]"""
import json, re, sys, warnings
warnings.filterwarnings('ignore')
import pymupdf
from parse_acts import norm


def key(s):
    return re.sub(r'[^a-z0-9]', '', norm(s).lower())


def pieces(src, kk, lo, hi):
    """Greedy longest pieces of kk found in order within src[lo:hi]; True if all of kk is covered by pieces >= 12 chars."""
    q = lo; r = kk
    while r:
        best = 0
        for i in range(min(len(r), 12), len(r) + 1):
            j = src.find(r[:i], q, hi)
            if j < 0:
                break
            best, at = i, j
        if best == 0 or (best < 12 and best < len(r)):
            return False
        q = at + best; r = r[best:]
    return True


part, pdf = sys.argv[1], sys.argv[2]
d = json.load(open(part, encoding='utf-8'))
src = key(''.join(p.get_text() for p in pymupdf.open(pdf)))
for act in d['acts']:
    units = act['versions'][0]['units']
    keys = [k for k in sorted(units, key=lambda k: (k != 'preamble', k)) if k.startswith(('preamble', 'sec-'))]
    body = {k: [key(ln) for ln in units[k]['text'].splitlines() if not ln.startswith('# ') and key(ln)] for k in keys}
    # locate each section's first line in order
    starts = []; pos = 0; lost = []
    for k in keys:
        first = body[k][0] if body[k] else ''
        j = src.find(first[:80], pos) if first else -1
        if j < 0:
            lost.append(k); starts.append(None)
        else:
            starts.append(j); pos = j + 1
    n = inorder = table = split = 0; bad = []
    for idx, k in enumerate(keys):
        if starts[idx] is None:
            bad.extend((k, '(section start not found)') for _ in body[k]); continue
        lo = starts[idx]
        hi = next((s for s in starts[idx + 1:] if s is not None), len(src))
        q = lo
        for kk in body[k]:
            n += 1
            j = src.find(kk, q, hi)
            if j >= 0:
                inorder += 1; q = j + len(kk); continue
            if src.find(kk, lo, hi) >= 0:
                table += 1; continue
            if pieces(src, kk, lo, hi):
                split += 1; continue
            bad.append((k, kk[:90]))
    secs = sorted(int(re.match(r'sec-(\d+)', k).group(1)) for k in units if k.startswith('sec-'))
    miss = sorted(set(range(1, max(secs) + 1)) - set(secs))
    print(act['slug'], 'lines', n, 'in order', inorder, 'out of order within section (tables)', table, 'split by page/margin', split,
          'not found', len(bad), 'sections not located', len(lost), 'units', len(units), 'max', max(secs), 'missing', miss)
    for b in bad[:40 if '-v' in sys.argv else 10]:
        print('  NOT FOUND', b)
