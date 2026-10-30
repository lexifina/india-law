# India: progress (private)

## Phase 2, 2026-10-30 (gitlaw-scraper-hp-omen)
- FIXED the Constitution: the corpus that was on main had every article file holding the whole document text (~850 KB x 434 files, 370 MB). parse.py run again from .cache/coi.txt gives 500 units, 496 KB; checked line by line against the PDF text (scratch charcheck.py). Article 238 is not printed in the source (Part VII omitted, 1956): decision added in corpus_head.json.
- Added corpus.d parts (parts.py, via parse_acts.parse_act; marginal notes excluded), from egazette.gov.in (robots.txt 404, so no rules):
  - 20 Bharatiya Nagarik Suraksha Sanhita 2023 (Act 46), WriteReadData/2023/250884.pdf, in force 2024-07-01; ss 1-531, no Schedules.
  - 21 Bharatiya Sakshya Adhiniyam 2023 (Act 47), WriteReadData/2023/250882.pdf, in force 2024-07-01; ss 1-170, no Schedule.
  - 22 Code on Wages 2019 (Act 29), WriteReadData/2019/210356.pdf, dated 2020-12-18 (first commencement; later staged commencements not replayed).
- BNS and Companies Act (corpus.json, earlier session) rechecked: 0 lines not found.
- Skipped: Indian Contract Act 1872 (and other pre-1950 Acts). No e-Gazette copy; indiacode.nic.in and legislative.gov.in answer 403 to this machine (treated as a block, not worked round). The Legislative Department's document store (cdnbbsr.s3waas.gov.in, where the Constitution PDF came from) may hold it, but no URL was found in the time box.
- Candidates next: Industrial Relations Code 2020 (Act 35 of 2020, egazette WriteReadData/2020/222118.pdf; check its commencement notification first; reported in force 21-11-2025), Code on Social Security 2020, OSH Code 2020 (e-Gazette 2020), Insolvency and Bankruptcy Code 2016.
