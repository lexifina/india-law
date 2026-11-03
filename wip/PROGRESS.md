# India: progress (private)

## Queue job 36, depth, 2026-11-03 (gitlaw-scraper-hp-omen)
- Added a second, wording-unchanged version of the Code on Wages, 2019 dated 2025-11-21 from official notification
  S.O. 5322(E) (e-Gazette 2025/267885). The notification commences all or specified parts of sections 1 to 69 and
  expressly excludes section 42(1)-(3), (10)-(11), section 67(2)(s)-(t), and the section 69 provisions already named
  at serial 3 of S.O. 4604(E). The exact exclusions are in the version note.
- The notification PDF was already in the scheduler-fed cache. Its English page is born-digital (no OCR), two pages,
  SHA-256 45105d4da240440cf43b3d0565c8f615d5ac705be807a87212ada95df92d58cc.
- `parts.py code-on-wages` parsed twice to identical SHA-256
  d85592fe6a837dcb6e4532cc5a9ab5b3c85e2cac06d269cc19d3fab973162545. Final build/check results are in the q-36 report.
- The existing India Code/Legislative Department listing stop remains: their robots endpoints return 403 and the
  shared scheduler has stopped both hosts. No request was made to either host, and no breadth-completeness claim is made.

## Phase 2, 2026-10-30 (gitlaw-scraper-hp-omen)
- FIXED the Constitution: the corpus that was on main had every article file holding the whole document text (~850 KB x 434 files, 370 MB). parse.py run again from .cache/coi.txt gives 500 units, 496 KB; checked line by line against the PDF text (scratch charcheck.py). Article 238 is not printed in the source (Part VII omitted, 1956): decision added in corpus_head.json.
- Added corpus.d parts (parts.py, via parse_acts.parse_act; marginal notes excluded), from egazette.gov.in (robots.txt 404, so no rules):
  - 20 Bharatiya Nagarik Suraksha Sanhita 2023 (Act 46), WriteReadData/2023/250884.pdf, in force 2024-07-01; ss 1-531, no Schedules.
  - 21 Bharatiya Sakshya Adhiniyam 2023 (Act 47), WriteReadData/2023/250882.pdf, in force 2024-07-01; ss 1-170, no Schedule.
  - 22 Code on Wages 2019 (Act 29), WriteReadData/2019/210356.pdf, dated 2020-12-18 (first commencement; later staged commencements not replayed).
- BNS and Companies Act (corpus.json, earlier session) rechecked: 0 lines not found.
- Skipped: Indian Contract Act 1872 (and other pre-1950 Acts). No e-Gazette copy; indiacode.nic.in and legislative.gov.in answer 403 to this machine (treated as a block, not worked round). The Legislative Department's document store (cdnbbsr.s3waas.gov.in, where the Constitution PDF came from) may hold it, but no URL was found in the time box.
- Candidates next: Industrial Relations Code 2020 (Act 35 of 2020, egazette WriteReadData/2020/222118.pdf; check its commencement notification first; reported in force 21-11-2025), Code on Social Security 2020, OSH Code 2020 (e-Gazette 2020), Insolvency and Bankruptcy Code 2016.

## Phase 3, 2026-11-02/03 (global-law-main-composer-india; populous sprint)
- Sources re-checked 2026-11-02: www.indiacode.nic.in and legislative.gov.in both answer 403 to robots.txt; fetch_scheduler
  stopped both hosts for good (not worked round). egazette.gov.in: robots.txt 404 (no rules); About page: Gazette of
  India "can be accessed free of cost by the general public being available in the public domain"; Disclaimer page has
  no body text; no prohibition on reproduction found. cdnbbsr.s3waas.gov.in (Legislative Department's file store): robots
  404; NOT used this phase (the origin site is stopped, so using its CDN would arguably get round that; decision for Alan).
- Copyright Act 1957 s.52(1)(q)(ii): an Act may be reproduced only "together with any commentary thereon or any other
  original matter" (not a blanket exemption). LICENSE now quotes (q)(i)-(ii) and says what original matter the repo
  publishes with the Acts. The quote was read from a secondary copy (advocatekhoj), since India Code is blocked.
- Published (append-only, fast-forward, check.py 0 mismatches / 0 trailer errors each time):
  - part 1, main 7cd9c2d -> feaf27cd8: 23 Industrial Relations Code 2020 (eg 2020/222118), 24 Code on Social Security
    2020 (2020/222111), 25 OSH Code 2020 (2020/222112); all dated 2025-11-21 from S.O. 5320(E)/5319(E)/5321(E)
    (eg 2025/267883, 267882, 267884, read). 3 commits + docs, 6 tags.
  - part 2, main ba76ac9 -> 26d4e90e7: 26 Income-tax Act 2025 (eg 2025/265620, 572 pp), ss 1-536, dated 2026-04-01
    (s.1(3)); Schedules and any Finance Act 2026 amendments not applied. 1 commit + docs, 2 tags.
  - (7cd9c2d and ba76ac9 are documentation refreshes pushed by another process, bot identity; my appends sit on top.)
- Clone note: ~/Documents/india-law is rebuilt by some other job (fast-import at 2026-11-02 23:08, index left with
  every file staged deleted). Appends were made in ~/Documents/india-law-append (fresh clone of origin) instead.
- Parser (parse_acts.py) gained opt-in options, all off for parts 20-25 (their JSON is byte-identical):
  monotonic (numbered lists inside a section, e.g. CSS s.164(1) items 1-9, stay in the section; a section number may
  not jump by more than 10), line_level (margin filter per line: the 2025 layout puts the margin note and the section's
  first line in one block; bold section numbers mark section starts, including "173 For ..." printed without its full
  stop; centred lines are headings only if capitals or italic; italic "X.-" sub-headings join their italic second line).
- Verification: verify_parts.py (in order, bounded gaps; gaps read by hand) for 23-25; verify_window.py (each line
  inside its own section's span; tables out of order allowed) for 26. Results in .cache/verify-*.log and each .PUBLISH.
- e-Gazette ids: WriteReadData/<upload year>/<id>.pdf, ids rise by upload time (~25/day in 2023-25); each file is
  stamped CG-DL-E-<ddmmyyyy>-<id>. Found by date bisection (idate.py, idscan.py). Known: DPDP Act 2023 = 2023/248045
  (21 pp, fetched, not parsed: commencement is staged from Nov 2025 and the notification is not yet read).
- Detached loop: egz_discover.py (PID in egz_discover.pid, BelowNormal, log egz_discover.log/.out, resumable via
  egz_state.json, catalogue in catalogue.jsonl). It only finds and caches Acts by publication day (IBC 2016, CPA 2019,
  CGST 2017, RERA 2016, Companies (Amendment) Acts 2017/2019/2020, Finance Acts 2025/2026, ...); it does not parse or
  publish. Older year folders may use other file names (2013 used E_27_2013_425.pdf), so a target can end NO-DAY.
- Next: DPDP Act 2023 (read its commencement notifications, Nov 2025); acts from catalogue.jsonl; Code on Wages full
  commencement 21-11-2025 (S.O. 5322(E), eg 2025/267885) as a wording-unchanged version; Companies Act amendments
  (needs the amending Acts and hand-applied changes). Not reachable without India Code: Constitution amendment history,
  CPC 1908, Indian Contract Act 1872 (pre-gazette-online).
