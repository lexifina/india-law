# India: law history in git

**English** · [हिन्दी](README.hi.md)

<picture>
<source media="(prefers-color-scheme: dark)" srcset="data/effort-dark.svg">
<img alt="Indian law in this repository: what it holds, changes by the year they took effect, completeness against the official sources, and the correctness of what is held" src="data/effort-light.svg" width="880">
</picture>

The law of India as a git history: one file per section (per article for the Constitution), one commit per version on the day it took effect, and the law that made each version as the commit's author. `git blame` names the law behind every line; `git log` lists every change to a section; picking a date gives the text in force that day.

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is India's national law, which global-law reads at `india/national/acts/`.

**What is in it now:** 2,153,798 commits, as of 22 November 2026. The Constitution (1 May 2024 edition) and 75 central Acts with their sections, plus 233 amending Acts and 20 ordinances as enacted. 12,680 Gazette of India rules, notifications and orders, 2022 to 2026. State law: 217 Acts, 335 amending Acts and 160 ordinances of Maharashtra and Goa, and 21,628 gazette items from 25 states and 5 union territories. 1,547 circulars, directions, notifications and regulations of IBBI, IRDAI, PFRDA and TRAI. 35,262 Supreme Court judgments, 1950 to 2026. 2,077,365 judgments and final orders of all 25 High Courts, so far mostly from 2024 to 2026. 4,233 NCLAT orders, 2017 to 2021.

**Held back for now:**

- about 400,000 interim High Court orders (orders not marked final in the courts' records), pending a decision on whether interim orders belong here;
- about 50,000 land-acquisition notices (23,198 in the Gazette of India, 26,875 in state gazettes), pending a decision;
- about 240 central Acts that come into force on a day the Government notifies, until that notification is found (45 dated so far);
- about 360 state reprints "as modified up to" a date, pending a decision on whether that date may date a version;
- about 235,000 High Court PDFs whose text layer is broken or missing, and 7,000 not in English, for a later pass.

Judgments in sexual-offence, POCSO, juvenile-justice and matrimonial cases are never included: they are left out, not held.

Each Act is a folder under `central/acts/` named by its short title and year, with one file per section, a file per chapter title and the preamble (`central/acts/occupational-safety-health-and-working-conditions-code-2020/sec-032.md` is section 32, annual leave with wages, of the Occupational Safety, Health and Working Conditions Code, 2020, Act 37 of 2020); the Constitution is `constitution/art-001.md` to `art-395.md`, with inserted articles such as `art-021-a.md`. Everything else is one file per document: Gazette of India items under `central/gazette/<yyyy>/<mm>/<dd>/`, state law under `states/<state>/` and `union-territories/<ut>/`, regulators under `regulators/<name>/`, judgments under `courts/supreme-court/<yyyy>/<mm>/` and `courts/high-courts/<court>/<bench>/<yyyy>/<mm>/<dd>/`, and NCLAT orders under `tribunals/nclat/<bench>/<yyyy>/<mm>/`.

The text is in English, the official English text as the Gazette of India and the Legislative Department print it. The Hindi text is not part of this record.

## Questions as git commands

| Question | Command |
| --- | --- |
| Every change to section 32 of the OSH Code | `git log -p --follow --word-diff -- central/acts/occupational-safety-health-and-working-conditions-code-2020/sec-032.md` |
| Which law wrote each line of section 32? | `git blame central/acts/occupational-safety-health-and-working-conditions-code-2020/sec-032.md` |
| Every version of the OSH Code, with the day each took effect | `git log --format="%h %(trailers:key=In-force,valueonly,separator=) %an" -- central/acts/occupational-safety-health-and-working-conditions-code-2020 occupational-safety-health-and-working-conditions-code ':!*/README.md'` |
| Section 32 as in force on 1 January 2026 | `python tools/on.py 2026-01-01 central/acts/occupational-safety-health-and-working-conditions-code-2020 32` |

**Outside git**, we also host this record publicly, for free:

- **[Ask Claude about Indian law](https://global-law.lexifina.com/v1/try_claude?country=india)**: opens Claude with a first question ready.
- **[Ask ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=india)**: the same question in ChatGPT.
- **[Search Indian law on our site](https://lexifina.com/law?country=india&q=annual+leave)**: a search for "annual leave", with each provision's text and its versions, no account needed.
- **[Developer REST API](https://global-law.lexifina.com/v1/search_law?query=annual+leave&jurisdiction=india)**: the same search as JSON, with no key. See the [documentation here](https://lexifina.com/api/global-law).

Both assistants read the record through the free Global law connector (MCP, `https://global-law.lexifina.com/mcp`); the first time, the chat gives you the link that adds it. Ask in English.

**Host it yourself easily.** All it takes is git and Python, and the tools run on your machine:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add india/national/acts
python3 tools/law.py show 2026-01-01 india/national/acts/central/acts/occupational-safety-health-and-working-conditions-code-2020/sec-032.md
```

Opened in Claude Code, Cursor, VS Code or Codex, the clone also starts a local MCP server with the same tools ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dates

Each commit is dated at noon, Asia/Kolkata, on the day the version took effect, and carries it in its `In-force:` trailer:

- for an Act, the day its commencement notification or its own commencement clause gives: 1 July 2024 for the three 2023 codes, 21 November 2025 for three of the labour codes, 1 April 2026 for the Income-tax Act;
- for an Act brought into force in stages, its first commencement: 30 August 2013 (section 1) for the Companies Act, and 18 December 2020 for the Code on Wages, with a second commit for notification S.O. 5322(E) of 21 November 2025, which commenced further provisions without changing a word (`Words-changed: no`);
- for the Constitution, the day of the Legislative Department's edition, 1 May 2024, not 26 January 1950;
- for a judgment or order, the day it was decided; for a gazette item, the day it was published, unless it states another commencement day.

Each Act's version is credited to the Act itself (`Act 37 of 2020`), and the Code on Wages' second commit to the notification. The Constitution's one version is the oldest version available, credited to its publisher, the Legislative Department, Ministry of Law and Justice. Judgments are credited to their court, and gazette items to the ministry or body that issued them.

## How it is checked

- `tools/check_repo.py` reads every act back from git on the day each version took effect and on the day before, and compares it with the corpus the history was built from; the result is in [`REPRODUCE.md`](REPRODUCE.md).
- `tools/verify_parts.py` and `tools/verify_window.py` check each act line by line against the text layer of its Gazette PDF (letters and digits only, each line within its own section).
- History is append-only: no merge commits, committer dates never go backwards, nothing is dated after the build, and every commit's trailers parse.
- The same corpus always gives the same commit hashes; no second build has been compared yet.
- [vulnerabilities/](vulnerabilities/): possible drafting mistakes in this law, found by global-law's detectors and checked by hand. Not run yet.

## What it does not show

- **Amendments.** Each Act is its text as enacted, and the Constitution one consolidated edition; amendments are not replayed (the Constitution's 106, or any Finance Act changes to the Income-tax Act).
- **Staged commencement.** The Companies Act, 2013 and the Code on Social Security, 2020 commenced in stages; each Act here carries one day.
- **Schedules and margins.** The Schedules, the marginal section headings, the Constitution's Appendices and its amendment footnotes are left out; tables in the Income-tax Act are flattened, one cell per line.
- **Most of India's law, so far.** About nine in ten central Acts, Gazette of India items before 2022, the Acts of every state but Maharashtra and Goa, most High Court judgments before 2024 (that pass runs from the newest year back), and the lower courts and most tribunals are not here yet.

## Sources

| Source | Kind | Past versions | Notes |
| --- | --- | --- | --- |
| [e-Gazette](https://egazette.gov.in) (Gazette of India) | Official Gazette | no, each Act as enacted | Acts and ordinances as enacted, commencement notifications, and Gazette of India rules, notifications and orders |
| [Legislative Department](https://legislative.gov.in/constitution-of-india/) (Ministry of Law and Justice) | Official consolidated text | no, the edition as on 1 May 2024 | The Constitution of India, Preamble and Articles 1 to 395 |
| [Internet Archive](https://archive.org/details/gazetteofindia) (gazetteofindia and the state gazette collections) | Copies of the official Gazette PDFs | no, each item as published | Most Acts and Gazette of India items, and the state gazette items; each commit also names the official file |
| [AWS Open Data](https://registry.opendata.aws/indian-supreme-court-judgments/) (Indian Supreme Court and [High Court](https://registry.opendata.aws/indian-high-court-judgments/) Judgments, Dattam Labs, CC BY 4.0) | Judgments, collected from the courts' portals | no, each judgment as decided | The Supreme Court and High Court judgments |
| [Law and Judiciary Department, Maharashtra](https://old-lj.maharashtra.gov.in) and [Government of Goa](https://www.goa.gov.in/government/acts-and-rules/) | Official reprints and Acts | no, the current reprint or the Act as enacted | Maharashtra and Goa Acts and ordinances |
| [IBBI](https://ibbi.gov.in), [IRDAI](https://irdai.gov.in), [PFRDA](https://www.pfrda.org.in), [TRAI](https://www.trai.gov.in) | Regulators' own sites | no | Circulars, directions, notifications and regulations |
| [NCLAT](https://nclat.nic.in/judgement-data) | Tribunal's own site | no | NCLAT orders before 31 May 2021 |

## Licence

See [`LICENSE`](LICENSE). Section 52(1)(q) of the Copyright Act, 1957 allows Gazette matter, and judgments and orders, to be reproduced, and an Act of a Legislature together with commentary or other original matter, here the commit records, per-version notes, tables and tools; the Supreme Court and High Court judgments come from Dattam Labs' datasets on AWS Open Data under CC BY 4.0; the Constitution is published by the Government of India for public use, and this repository makes no claim over it. Lexifina's own work (the commits, notes, tables, tools and READMEs) is dedicated to the public domain under CC0 1.0; [`LICENSE`](LICENSE) gives each source's own terms.

No AI model wrote, translated or corrected legal text, and none runs when the history is built; the scripts were written by an AI model (see [`REPRODUCE.md`](REPRODUCE.md)).

## Visualisations

- [visualisations/](visualisations/): charts drawn from this repository. Not drawn yet.

## More

From [lexifina/global-law](https://github.com/lexifina/global-law):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): every feature, and what every corpus must support (`git blame`, `law.py`, the MCP tools)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions and answers · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposing changes · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): the MCP server · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): how it was built · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): how current each corpus is · [Monitoring](https://github.com/lexifina/global-law/tree/main/monitoring): whether updates are running · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): how each official source is watched for changes
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): how fast the tools are, measured
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): charts and bridges across the world's law
- [Vulnerabilities](https://github.com/lexifina/global-law/tree/main/vulnerabilities): mistakes in legislation as published
