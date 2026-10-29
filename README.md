# India: law history in git

The law of India as a git history: one file per provision, and each version credited to the body that published it. `git blame` names the source of every paragraph; picking a date gives the text in force that day, within the limits below. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `in/`.

**What is in it now (a first build)**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | The Constitution of India: the Preamble and Articles 1 to 395 | 1 | One version: the text as on 1 May 2024, brought up to date to the Constitution (One Hundred and Sixth Amendment) Act, 2023, as the Legislative Department published it |

Language: the text is the official English text. The same PDF also carries the Hindi text, which is not included.

**What it does not show**

- Only one version exists here. The official source is a single consolidated edition, so the repository is dated from that edition (1 May 2024), not from the Constitution's adoption (26 November 1949, in force 26 January 1950) or from each of the 106 amendments. It is the oldest version available (not the original text), and the amendments are not yet replayed.
- The Schedules, the Appendices and the amendment footnotes are not included. Amendment markers are removed from the text. Article 238 (repealed in 1956) has no text in the source and is absent.
- Statutes other than the Constitution are not included.
- Part and chapter headings are not kept as separate files.

**Source**

*The Constitution of India* (as on 1st May, 2024), Legislative Department, Official Languages Wing, Ministry of Law and Justice, Government of India: <https://legislative.gov.in/constitution-of-india/>. The PDF used was retrieved on 29 October 2026 from the Government's document store. Only the PDF's text layer was read.

Dates are the dates the source gives. Nothing here is legal advice; for anything that matters, read the original. How the files were made is in [REPRODUCE.md](REPRODUCE.md).

## Licence

See [LICENSE](LICENSE).
