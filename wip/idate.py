"""Print the CG-DL upload stamp and S.O./Act lines of e-Gazette PDFs by id (private)."""
import os, sys, re, warnings
os.environ.setdefault('GITLAW_SESSION', 'global-law-main-composer-india')
sys.path.insert(0, r'~/Documents/lexifina/scripts/gitlaw_common')
import fetch_scheduler as fs
import pymupdf
from pathlib import Path
warnings.filterwarnings('ignore')
C = Path(__file__).parent / '.cache' / 'eg'
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
    t = ''.join(p.get_text() for p in list(d)[:2])
    t = re.sub(r'[^\x20-\x7e\n]', '', t)
    st = re.search(r'CG-[A-Z]{2}-E-(\d{8})-\d+', t)
    so = re.findall(r'(?:S\.O\.|G\.S\.R\.)\s*\d+\s*\(E\)', t)[:3]
    ti = [l.strip() for l in t.splitlines() if re.search(r'\bCODE\b|\bACT, 20|Code, 20', l)][:3]
    print(i, len(d), 'pp', st.group(1) if st else '-', so, ti)
