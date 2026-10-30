# How this repository was made (India)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| The Constitution of India, as on 1st May, 2024 (Legislative Department, Official Languages Wing) | <https://cdnbbsr.s3waas.gov.in/s380537a945c7aaa788ccfcdf1b99b5d8f/uploads/2024/07/20240716890312078.pdf> | 2026-10-29 | Government of India publication, https://legislative.gov.in |
| The Gazette of India, Extraordinary, Part II Section 1, No. 53 of 25 December 2023: The Bharatiya Nyaya Sanhita, 2023 (Ministry of Law and Justice, Legislative Department) | <https://egazette.gov.in/WriteReadData/2023/250883.pdf> | 2026-10-30 | Government of India publication in the e-Gazette (egazette.gov.in); no licence statement on the file. |
| The Gazette of India, Extraordinary, Part II Section 1, 30 August 2013: The Companies Act, 2013 (Ministry of Law and Justice, Legislative Department) | <https://egazette.gov.in/WriteReadData/2013/E_27_2013_425.pdf> | 2026-10-30 | Government of India publication in the e-Gazette (egazette.gov.in); no licence statement on the file. |
| The Gazette of India, Extraordinary, Part II Section 1, 25 December 2023: The Bharatiya Nagarik Suraksha Sanhita, 2023 (Ministry of Law and Justice, Legislative Department) | <https://egazette.gov.in/WriteReadData/2023/250884.pdf> | 2026-10-30 | Government of India publication in the e-Gazette (egazette.gov.in); no licence statement on the file. |
| The Gazette of India, Extraordinary, Part II Section 1, 25 December 2023: The Bharatiya Sakshya Adhiniyam, 2023 (Ministry of Law and Justice, Legislative Department) | <https://egazette.gov.in/WriteReadData/2023/250882.pdf> | 2026-10-30 | Government of India publication in the e-Gazette (egazette.gov.in); no licence statement on the file. |
| The Gazette of India, Extraordinary, Part II Section 1, 8 August 2019: The Code on Wages, 2019 (Ministry of Law and Justice, Legislative Department) | <https://egazette.gov.in/WriteReadData/2019/210356.pdf> | 2026-10-30 | Government of India publication in the e-Gazette (egazette.gov.in); no licence statement on the file. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | The Constitution of India | 1 | 2024-05-01 to 2024-05-01 |
| `bharatiya-nyaya-sanhita` | The Bharatiya Nyaya Sanhita, 2023 (Act 45 of 2023) | 1 | 2024-07-01 to 2024-07-01 |
| `companies-act` | The Companies Act, 2013 (Act 18 of 2013) | 1 | 2013-08-30 to 2013-08-30 |
| `bharatiya-nagarik-suraksha-sanhita` | The Bharatiya Nagarik Suraksha Sanhita, 2023 (Act 46 of 2023) | 1 | 2024-07-01 to 2024-07-01 |
| `bharatiya-sakshya-adhiniyam` | The Bharatiya Sakshya Adhiniyam, 2023 (Act 47 of 2023) | 1 | 2024-07-01 to 2024-07-01 |
| `code-on-wages` | The Code on Wages, 2019 (Act 29 of 2019) | 1 | 2020-12-18 to 2020-12-18 |

The build made 6 commits:

| Commits | Kind |
| ---: | --- |
| 6 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 5 laws in the record.
- 11 tags.

## Dates

Each commit is dated at noon (Asia/Kolkata) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Constitution of India art. 394: the Constitution came into force on 26 January 1950. This record holds one version, the text as brought up to date by the Legislative Department on 1 May 2024, so no per-amendment in-force days are derived. https://legislative.gov.in/constitution-of-india/

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `423ff43104b5ac720f2a21d1bbc91543be6dd30d427d1fdc019cac7187f8a29e` (2689171 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

6 versions of 6 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 6 history commits and 11 tags (history tip `f94d73091d31c7f20f871cbd5cb1dcd14b50816b`).

## Decisions made by hand

- One version only: the official PDF gives the text as on 1 May 2024 and no earlier consolidated text, so this is the oldest version available (first_law null), dated from the publication date on the PDF's own cover.
- The Preamble and Articles 1 to 395 are included. The Schedules, Appendices and amendment footnotes are left out of this first build.
- Amendment footnote markers (N[ ... ] and N***) are removed from the text; omitted articles remain as units carrying their own 'Omitted' note.
- Part and chapter headings between articles are not kept as units in this first build.
- Phase 2 statutes are added as their own acts; the Constitution act is unchanged.
- Bharatiya Nyaya Sanhita: one version, the as-enacted gazette text, dated 1 July 2024 (the commencement date in notification S.O. 850(E), except section 106(2)) and credited to Act 45 of 2023. Later amendments are not replayed.
- Bharatiya Nyaya Sanhita: the gazette prints each section's heading in the margin; those marginal notes are not included. Chapter titles and the sub-headings printed between sections are kept (sub-headings as the first line of the next section).
- Companies Act, 2013 (the nearest equivalent of a commercial code; India has no single civil or commercial code): one version, the as-enacted gazette text, dated 30 August 2013 (section 1 in force at once) and credited to Act 18 of 2013. Staged commencement of the other provisions and later amendments are not replayed.
- Companies Act, 2013: Sections 1 to 470 and chapter titles are included; Schedules I to VII and the marginal section headings are not.
- Bharatiya Nagarik Suraksha Sanhita: one version, the as-enacted gazette text, dated 1 July 2024 (the commencement date in notification S.O. 848(E)) and credited to Act 46 of 2023; sections 1 to 531 and chapter titles are included, the First and Second Schedules and the marginal section headings are not. Later amendments are not replayed.
- Bharatiya Sakshya Adhiniyam: one version, the as-enacted gazette text, dated 1 July 2024 (the commencement date in notification S.O. 849(E)) and credited to Act 47 of 2023; sections 1 to 170 and chapter titles are included, the Schedule and the marginal section headings are not. Later amendments are not replayed.
- Code on Wages, 2019 (the first of the four labour codes): one version, the as-enacted gazette text, dated 18 December 2020, when its first provisions came into force by notification, and credited to Act 29 of 2019; the staged commencement of the other provisions and later amendments are not replayed. Sections 1 to 69 and chapter titles are included, the marginal section headings are not.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code (Claude Sonnet 5.5) wrote the parser. No model wrote, edited or summarised legal text.
- none
- none
- none
