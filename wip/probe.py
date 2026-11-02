"""Probe robots.txt and a few pages for Indian official sources (private)."""
import os, sys
os.environ.setdefault('GITLAW_SESSION', 'global-law-main-composer-india')
sys.path.insert(0, r'~/Documents/lexifina/scripts/gitlaw_common')
import fetch_scheduler as fs
from pathlib import Path
C = Path(__file__).parent / '.cache' / 'probe'
for u in sys.argv[1:]:
    try:
        b = fs.get(u, cache=C, tries=2, timeout=60, caller='india-probe')
        print('==', u, fs.last_status(), None if b is None else len(b))
        if b is not None and len(sys.argv) <= 6:
            print(b[:1500].decode('utf-8', 'replace'))
    except Exception as e:
        print('==', u, 'EXC', type(e).__name__, str(e)[:300])
