"""Find Acts of Parliament in the e-Gazette (egazette.gov.in) by publication day (private; never published).

The e-Gazette files every upload as WriteReadData/<year>/<id>.pdf, with ids rising by upload time, and stamps each file
'CG-DL-E-<ddmmyyyy>-<id>'. For each target (an Act and the day it was published), this bisects the id space by that
stamp to the day, then reads every file of the day (and the next) and records each Act of Parliament it finds
(Part II Section 1: 'The following Act of Parliament received the assent ...') in catalogue.jsonl.

All requests go through gitlaw_common/fetch_scheduler.get (robots, pacing, Retry-After, challenge stops). Resumable:
state.json records finished targets and every id read; a rerun skips them. Stops on HostStopped.

    python -X utf8 egz_discover.py            (targets from TARGETS below)
"""
import datetime as dt
import json
import os
import re
import sys
import time
import warnings
from pathlib import Path

os.environ.setdefault('GITLAW_SESSION', 'global-law-main-composer-india')
sys.path.insert(0, r'~/Documents/lexifina/scripts/gitlaw_common')
import fetch_scheduler as fs  # noqa: E402
import pymupdf  # noqa: E402

warnings.filterwarnings('ignore')
H = Path(__file__).resolve().parent
CACHE = H / '.cache' / 'eg'
CACHE.mkdir(parents=True, exist_ok=True)
STATE = H / 'egz_state.json'
CAT = H / 'catalogue.jsonl'
LOG = H / 'egz_discover.log'

# (label, publication day). Days are as reported for each Act's Gazette of India publication; the scan reads the day
# and the next one, so a day out by one still finds it. Each found Act is checked against its own first page.
TARGETS = [
    ('Insolvency and Bankruptcy Code, 2016', '2016-05-28'),
    ('Consumer Protection Act, 2019', '2019-08-09'),
    ('Central Goods and Services Tax Act, 2017', '2017-04-12'),
    ('Real Estate (Regulation and Development) Act, 2016', '2016-03-26'),
    ('Companies (Amendment) Act, 2017', '2018-01-03'),
    ('Companies (Amendment) Act, 2019', '2019-07-31'),
    ('Companies (Amendment) Act, 2020', '2020-09-28'),
    ('Finance Act, 2026', '2026-03-30'),
    ('Finance Act, 2025', '2025-03-29'),
    ('Arbitration and Conciliation (Amendment) Act, 2019', '2019-08-09'),
    ('Motor Vehicles (Amendment) Act, 2019', '2019-08-09'),
    ('Juvenile Justice (Care and Protection of Children) Act, 2015', '2016-01-01'),
    ('Bharatiya Nyaya Sanhita (amendments), 2024-2026', '2025-08-21'),
]
# Known (id, upload day) anchors per year folder, from files already read.
ANCHORS = {
    2019: [(210356, '2019-08-08')], 2020: [(222118, '2020-09-30')], 2023: [(248000, '2023-08-10'), (250883, '2023-12-25')],
    2025: [(265620, '2025-08-22'), (267000, '2025-10-17'), (268000, '2025-11-27')], 2026: [(269000, '2026-01-01')],
}
RATE_PER_DAY = 25   # ids per day, roughly (2023-2025)


def log(*a):
    line = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()) + ' ' + ' '.join(str(x) for x in a)
    print(line, flush=True)
    with LOG.open('a', encoding='utf-8') as f:
        f.write(line + '\n')


def load_state():
    if STATE.exists():
        return json.loads(STATE.read_text('utf-8'))
    return {'done': [], 'read': {}}


def save_state(st):
    tmp = STATE.with_suffix('.tmp')
    tmp.write_text(json.dumps(st, indent=0), 'utf-8')
    tmp.replace(STATE)


def read_id(st, year, i):
    """{'day': 'YYYY-MM-DD' or None, 'acts': [...]} for one file, or None if absent. Cached in state."""
    k = f'{year}/{i}'
    if k in st['read']:
        return st['read'][k]
    u = f'https://egazette.gov.in/WriteReadData/{year}/{i}.pdf'
    b = fs.get(u, cache=CACHE, tries=3, timeout=180, caller='india-egz-discover')
    if not b or not b.startswith(b'%PDF'):
        st['read'][k] = None
        return None
    try:
        d = pymupdf.open(stream=b, filetype='pdf')
        t = ''.join(p.get_text() for p in list(d)[:2])
    except Exception:
        st['read'][k] = {'day': None, 'acts': [], 'pages': 0}
        return st['read'][k]
    t = re.sub(r'[^\x20-\x7e\n]', ' ', t)
    m = re.search(r'CG-[A-Z]{2}-E-(\d{2})(\d{2})(\d{4})-\d+', t)
    day = f'{m.group(3)}-{m.group(2)}-{m.group(1)}' if m else None
    acts = []
    if 'Act of Parliament' in t or 'ACT of Parliament' in t:
        flat = re.sub(r'\s+', ' ', t)
        for mm in re.finditer(r'THE ([A-Z][A-Z ,()\-\']+?(?:ACT|CODE|SANHITA|ADHINIYAM),? \d{4}) (?:\(?No\.? ?(\d+) OF (\d{4}))?', flat):
            acts.append({'title': mm.group(1).strip(), 'no': mm.group(2), 'of': mm.group(3)})
        nos = re.findall(r'No\. (\d+) of (\d{4})', flat)
        if nos and acts and not acts[0]['no']:
            acts[0]['no'], acts[0]['of'] = nos[0]
    r = {'day': day, 'acts': acts[:1], 'pages': len(d)}
    st['read'][k] = r
    if acts:
        rec = dict(id=i, year=year, url=u, day=day, pages=len(d), **acts[0])
        with CAT.open('a', encoding='utf-8') as f:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')
        log('ACT', json.dumps(rec, ensure_ascii=False))
    return r


def day_of(st, year, i, span=6):
    """Upload day at or just after id i (skips missing or unstamped files)."""
    for j in range(i, i + span):
        r = read_id(st, year, j)
        if r and r.get('day'):
            return j, r['day']
    return None, None


def guess(year, day):
    a = ANCHORS.get(year)
    t = dt.date.fromisoformat(day)
    if a:
        i0, d0 = min(a, key=lambda x: abs((dt.date.fromisoformat(x[1]) - t).days))
        return i0 + (t - dt.date.fromisoformat(d0)).days * RATE_PER_DAY
    # extrapolate from the nearest year with anchors at ~9000 ids a year
    y0 = min(ANCHORS, key=lambda y: abs(y - year))
    i0, d0 = ANCHORS[y0][0]
    return i0 + (t - dt.date.fromisoformat(d0)).days * RATE_PER_DAY


def find_day(st, year, day):
    """First id whose upload day is >= day (bisection on the stamp)."""
    g = guess(year, day)
    lo, hi = g - 1500, g + 1500
    jl, dl = day_of(st, year, lo)
    jh, dh = day_of(st, year, hi)
    tries = 0
    while (dl is None or dl >= day) and tries < 6:
        lo -= 3000; jl, dl = day_of(st, year, lo); tries += 1
    while (dh is None or dh < day) and tries < 12:
        hi += 3000; jh, dh = day_of(st, year, hi); tries += 1
    if dl is None or dh is None:
        return None
    while hi - lo > 8:
        mid = (lo + hi) // 2
        jm, dm = day_of(st, year, mid)
        if dm is None:
            return None
        if dm < day:
            lo = mid
        else:
            hi = mid
        save_state(st)
    return lo


def main():
    st = load_state()
    for label, day in TARGETS:
        if label in st['done']:
            continue
        year = int(day[:4])
        log('TARGET', label, day)
        try:
            start = find_day(st, year, day)
            if start is None:
                log('NO-DAY', label, day, '(id space not resolved; the year folder may use another naming)')
                st['done'].append(label); save_state(st); continue
            end_day = (dt.date.fromisoformat(day) + dt.timedelta(days=2)).isoformat()
            i = start; misses = 0
            while misses < 40:
                r = read_id(st, year, i)
                if r is None:
                    misses += 1
                elif r.get('day') and r['day'] >= end_day:
                    break
                else:
                    misses = 0
                i += 1
                if i % 10 == 0:
                    save_state(st)
            log('SCANNED', label, f'{year}/{start}-{i}')
        except fs.HostStopped as e:
            log('STOP', type(e).__name__, str(e)[:300])
            save_state(st)
            return
        st['done'].append(label)
        save_state(st)
    log('ALL DONE')


if __name__ == '__main__':
    main()
