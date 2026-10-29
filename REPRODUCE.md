# How this repository was made (India)

This file is written by the build on 2026-10-29, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| The Constitution of India, as on 1st May, 2024 (Legislative Department, Official Languages Wing) | <https://cdnbbsr.s3waas.gov.in/s380537a945c7aaa788ccfcdf1b99b5d8f/uploads/2024/07/20240716890312078.pdf> | 2026-10-29 | Government of India publication, https://legislative.gov.in |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | The Constitution of India | 1 | 2024-05-01 to 2024-05-01 |

The build made 1 commits:

| Commits | Kind |
| ---: | --- |
| 1 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-29.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 0 laws in the record.
- 1 tags.

## Dates

Each commit is dated at noon (Asia/Kolkata) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Constitution of India art. 394: the Constitution came into force on 26 January 1950. This record holds one version, the text as brought up to date by the Legislative Department on 1 May 2024, so no per-amendment in-force days are derived. https://legislative.gov.in/constitution-of-india/

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `27d761754121a08a03881ad2aa398b0dd5840259c11e92d7f16733cdf921e8b0` (552562 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `6229396f41c9d7f1d6f405becfbe4097b35b82da`, `check.py` `5e112e6a33b7e93d00112e55f01fbb4fb3fdd8da`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- One version only: the official PDF gives the text as on 1 May 2024 and no earlier consolidated text, so this is the oldest version available (first_law null), dated from the publication date on the PDF's own cover.
- The Preamble and Articles 1 to 395 are included. The Schedules, Appendices and amendment footnotes are left out of this first build.
- Amendment footnote markers (N[ ... ] and N***) are removed from the text; omitted articles remain as units carrying their own 'Omitted' note.
- Part and chapter headings between articles are not kept as units in this first build.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code (Claude Sonnet 5.5) wrote the parser. No model wrote, edited or summarised legal text.
