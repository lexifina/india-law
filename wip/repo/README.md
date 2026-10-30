# India: law history in git

The law of India as a git history: one file per provision, and each version credited to the body that published it. `git blame` names the source of every paragraph; picking a date gives the text in force that day, within the limits below. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `in/`.

**What is in it now (a first build)**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | The Constitution of India: the Preamble and Articles 1 to 395 | 1 | One version: the text as on 1 May 2024, brought up to date to the Constitution (One Hundred and Sixth Amendment) Act, 2023, as the Legislative Department published it |
| `bharatiya-nyaya-sanhita/` | The Bharatiya Nyaya Sanhita, 2023 (Act 45 of 2023), the penal code that replaced the Indian Penal Code | 1 | One version: the Act as enacted (Gazette of India Extraordinary, 25 December 2023), dated 1 July 2024, when it came into force (section 106(2) excepted). Later amendments are not replayed |
| `companies-act/` | The Companies Act, 2013 (Act 18 of 2013), India's main commercial statute (there is no single commercial code): Sections 1 to 470 | 1 | One version: the Act as enacted (Gazette of India Extraordinary, 30 August 2013), dated 30 August 2013, when section 1 came into force. The other provisions commenced in stages by notification, and later amendments are not replayed; the Schedules are not included |
| `bharatiya-nagarik-suraksha-sanhita/` | The Bharatiya Nagarik Suraksha Sanhita, 2023 (Act 46 of 2023), the code of criminal procedure that replaced the Code of Criminal Procedure, 1973: Sections 1 to 531 | 1 | One version: the Act as enacted (Gazette of India Extraordinary, 25 December 2023), dated 1 July 2024, when it came into force. The Schedules and later amendments are not included |
| `bharatiya-sakshya-adhiniyam/` | The Bharatiya Sakshya Adhiniyam, 2023 (Act 47 of 2023), the law of evidence that replaced the Indian Evidence Act, 1872: Sections 1 to 170 | 1 | One version: the Act as enacted (Gazette of India Extraordinary, 25 December 2023), dated 1 July 2024, when it came into force. The Schedule and later amendments are not included |
| `code-on-wages/` | The Code on Wages, 2019 (Act 29 of 2019), the first of the four labour codes: Sections 1 to 69 | 1 | One version: the Act as enacted (Gazette of India Extraordinary, 8 August 2019), dated 18 December 2020, when its first provisions came into force. The other provisions commenced later by notification; that and any amendments are not replayed |

Language: the text is the official English text. The same PDF also carries the Hindi text, which is not included.

**What it does not show**

- Only one version exists here. The official source is a single consolidated edition, so the repository is dated from that edition (1 May 2024), not from the Constitution's adoption (26 November 1949, in force 26 January 1950) or from each of the 106 amendments. It is the oldest version available (not the original text), and the amendments are not yet replayed.
- The Schedules, the Appendices and the amendment footnotes are not included. Amendment markers are removed from the text. Article 238 (repealed in 1956) has no text in the source and is absent.
- Other statutes are not included yet (India has no single civil or commercial code; further core statutes are being added one at a time).
- Part and chapter headings are not kept as separate files.

**Source**

*The Constitution of India* (as on 1st May, 2024), Legislative Department, Official Languages Wing, Ministry of Law and Justice, Government of India: <https://legislative.gov.in/constitution-of-india/>. The PDF used was retrieved on 29 October 2026 from the Government's document store. Only the PDF's text layer was read.

*The Bharatiya Nyaya Sanhita, 2023*: The Gazette of India, Extraordinary, Part II, Section 1, No. 53, 25 December 2023, Ministry of Law and Justice (Legislative Department), retrieved from <https://egazette.gov.in/> on 30 October 2026. English text layer only; the marginal section headings are not included.

*The Bharatiya Nagarik Suraksha Sanhita, 2023* and *The Bharatiya Sakshya Adhiniyam, 2023*: The Gazette of India, Extraordinary, Part II, Section 1, 25 December 2023, Ministry of Law and Justice (Legislative Department), retrieved from <https://egazette.gov.in/> on 30 October 2026. English text layer only; the marginal section headings and the Schedules are not included.

*The Code on Wages, 2019*: The Gazette of India, Extraordinary, Part II, Section 1, 8 August 2019, Ministry of Law and Justice (Legislative Department), retrieved from <https://egazette.gov.in/> on 30 October 2026. English text layer only; the marginal section headings are not included.

*The Companies Act, 2013*: The Gazette of India, Extraordinary, Part II, Section 1, 30 August 2013, Ministry of Law and Justice (Legislative Department), retrieved from <https://egazette.gov.in/> on 30 October 2026. English text layer only; the marginal section headings and the Schedules are not included.

Dates are the dates the source gives. Nothing here is legal advice; for anything that matters, read the original. How the files were made is in [REPRODUCE.md](REPRODUCE.md).

## Licence

See [LICENSE](LICENSE).
