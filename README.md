# India: law history in git

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is India's national law, which global-law reads at `india/national/acts/`.

The law of India as a git history: one file per provision, and each version credited to the body that published it. `git blame` names the source of every paragraph; picking a date gives the text in force that day, within the limits below. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `in/`.

**What is in it now (a first build)**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | The Constitution of India: the Preamble and Articles 1 to 395 | 1 | One version: the text as on 1 May 2024, brought up to date to the Constitution (One Hundred and Sixth Amendment) Act, 2023, as the Legislative Department published it |
| `bharatiya-nyaya-sanhita/` | The Bharatiya Nyaya Sanhita, 2023 (Act 45 of 2023), the penal code that replaced the Indian Penal Code | 1 | One version: the Act as enacted (Gazette of India Extraordinary, 25 December 2023), dated 1 July 2024, when it came into force (section 106(2) excepted). Later amendments are not replayed |
| `companies-act/` | The Companies Act, 2013 (Act 18 of 2013), India's main commercial statute (there is no single commercial code): Sections 1 to 470 | 1 | One version: the Act as enacted (Gazette of India Extraordinary, 30 August 2013), dated 30 August 2013, when section 1 came into force. The other provisions commenced in stages by notification, and later amendments are not replayed; the Schedules are not included |
| `bharatiya-nagarik-suraksha-sanhita/` | The Bharatiya Nagarik Suraksha Sanhita, 2023 (Act 46 of 2023), the code of criminal procedure that replaced the Code of Criminal Procedure, 1973: Sections 1 to 531 | 1 | One version: the Act as enacted (Gazette of India Extraordinary, 25 December 2023), dated 1 July 2024, when it came into force. The Schedules and later amendments are not included |
| `bharatiya-sakshya-adhiniyam/` | The Bharatiya Sakshya Adhiniyam, 2023 (Act 47 of 2023), the law of evidence that replaced the Indian Evidence Act, 1872: Sections 1 to 170 | 1 | One version: the Act as enacted (Gazette of India Extraordinary, 25 December 2023), dated 1 July 2024, when it came into force. The Schedule and later amendments are not included |
| `code-on-wages/` | The Code on Wages, 2019 (Act 29 of 2019), the first of the four labour codes: Sections 1 to 69 | 2 | The as-enacted text from its first commencement on 18 December 2020, then the further commencement under S.O. 5322(E) on 21 November 2025 (wording unchanged) |
| `industrial-relations-code/` | The Industrial Relations Code, 2020 (Act 35 of 2020), the second labour code (trade unions, standing orders, industrial disputes, lay-off, retrenchment and closure): Sections 1 to 104 | 1 | One version: the Code as enacted (Gazette of India Extraordinary, 29 September 2020), dated 21 November 2025, when notification S.O. 5320(E) brought it into force. The Schedules and later amendments, if any, are not included |
| `code-on-social-security/` | The Code on Social Security, 2020 (Act 36 of 2020), the third labour code (provident fund, state insurance, gratuity, maternity benefit, employee's compensation, gig and platform workers): Sections 1 to 164 | 1 | One version: the Code as enacted (Gazette of India Extraordinary, 29 September 2020), dated 21 November 2025, when notification S.O. 5319(E) brought most of it into force (a few provisions commenced earlier or await notification). The Schedules and later amendments, if any, are not included |
| `occupational-safety-health-and-working-conditions-code/` | The Occupational Safety, Health and Working Conditions Code, 2020 (Act 37 of 2020), the fourth labour code: Sections 1 to 143 | 1 | One version: the Code as enacted (Gazette of India Extraordinary, 29 September 2020), dated 21 November 2025, when notification S.O. 5321(E) brought it into force. The Schedules and later amendments, if any, are not included |
| `income-tax-act/` | The Income-tax Act, 2025 (Act 30 of 2025), which replaced the Income-tax Act, 1961: Sections 1 to 536 | 1 | One version: the Act as enacted (Gazette of India Extraordinary, 21 August 2025), dated 1 April 2026, when section 1(3) brings it into force. Schedules I to XVI and amendments (including any made by a Finance Act before it commenced) are not included; tables inside sections are flattened, one cell per line |

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

*The Code on Wages, 2019*: The Gazette of India, Extraordinary, Part II, Section 1, 8 August 2019, Ministry of Law and Justice (Legislative Department), retrieved from <https://egazette.gov.in/> on 30 October 2026. The later commencement is notification S.O. 5322(E), Ministry of Labour and Employment, Gazette of India Extraordinary, Part II, Section 3(ii), 21 November 2025. It commenced the provisions it lists that day, with the subsection and clause exclusions stated in the commit; the statutory wording did not change. English text layer only; the marginal section headings are not included.

*The Industrial Relations Code, 2020*, *The Code on Social Security, 2020* and *The Occupational Safety, Health and Working Conditions Code, 2020*: The Gazette of India, Extraordinary, Part II, Section 1, 29 September 2020, Ministry of Law and Justice (Legislative Department), retrieved from <https://egazette.gov.in/> on 2 November 2026. Their commencement dates are from the Ministry of Labour and Employment's notifications S.O. 5319(E), 5320(E) and 5321(E) of 21 November 2025 (Gazette of India Extraordinary, Part II, Section 3(ii)), retrieved the same day. English text layer only; the marginal section headings and the Schedules are not included.

*The Income-tax Act, 2025*: The Gazette of India, Extraordinary, Part II, Section 1, No. 35, 21 August 2025, Ministry of Law and Justice (Legislative Department), retrieved from <https://egazette.gov.in/> on 2 November 2026. English text layer only; the marginal section headings and the Schedules are not included.

*The Companies Act, 2013*: The Gazette of India, Extraordinary, Part II, Section 1, 30 August 2013, Ministry of Law and Justice (Legislative Department), retrieved from <https://egazette.gov.in/> on 30 October 2026. English text layer only; the marginal section headings and the Schedules are not included.

Dates are the dates the source gives. Nothing here is legal advice; for anything that matters, read the original. How the files were made is in [REPRODUCE.md](REPRODUCE.md).

## Licence

See [LICENSE](LICENSE).
