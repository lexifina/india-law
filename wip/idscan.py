"""Fetch e-Gazette WriteReadData PDFs by id and print each one's title lines (private)."""
import os, sys, re, warnings
os.environ.setdefault('GITLAW_SESSION', 'global-law-main-composer-india')
sys.path.insert(0, r'~/Documents/lexifina/scripts/gitlaw_common')
import fetch_scheduler as fs
import pymupdf
from pathlib import Path
warnings.filterwarnings('ignore')
C = Path(__file__).parent / '.cache' / 'eg'
C.mkdir(parents=True, exist_ok=True)
year = sys.argv[1]
for i in sys.argv[2:]:
    u = f'https://egazette.gov.in/WriteReadData/{year}/{i}.pdf'
    try:
        b = fs.get(u, cache=C, tries=2, timeout=120, caller='india-idscan')
    except Exception as e:
        print(i, 'EXC', type(e).__name__, str(e)[:200]); break
    if not b or not b.startswith(b'%PDF'):
        print(i, 'none', fs.last_status()); continue
    (C / f'{year}-{i}.pdf').write_bytes(b)
    d = pymupdf.open(stream=b, filetype='pdf')
    t = d[0].get_text() + (d[1].get_text() if len(d) > 1 else '')
    t = re.sub(r'[^\x20-\x7e\n]', '', t)
    keys = [l.strip() for l in t.splitlines() if re.search(r'\b(ACT|CODE|SANHITA|ADHINIYAM|Act No|No\. \d+ OF|S\.O\.|G\.S\.R)\b', l)]
    print(i, len(d), 'pp', ' | '.join(keys[:6])[:260])
