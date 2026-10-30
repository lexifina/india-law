"""Add core statutes (phase 2) to corpus.json without touching the Constitution act (private). Reads only .cache/."""
import hashlib, json, re
from pathlib import Path
import parse_acts as P
H = P.H
corpus = json.loads((H / 'corpus.json').read_text('utf-8'))
EGZ = 'https://egazette.gov.in/WriteReadData/2023/250883.pdf'
EGZ2 = 'https://egazette.gov.in/WriteReadData/2013/E_27_2013_425.pdf'

ACTS = [
    dict(end=None, slug='bharatiya-nyaya-sanhita', short='BNS', title='The Bharatiya Nyaya Sanhita, 2023 (Act 45 of 2023)', pdf='bns.pdf',
         start='An Act to consolidate', url=EGZ, law='bns-2023', in_force='2024-07-01',
         law_entry=dict(label='Act 45 of 2023', title='The Bharatiya Nyaya Sanhita, 2023', kind='law', enacted='2023-12-25', published='2023-12-25', url=EGZ,
                        temporary_until=None, restores=None,
                        note='Enacted 25 December 2023; brought into force on 1 July 2024 by notification S.O. 850(E) of 23 February 2024, except section 106(2).'),
         note='The Act as enacted, from the Gazette of India Extraordinary of 25 December 2023 (Part II, Section 1, No. 53). It came into force on 1 July 2024, except section 106(2), which the notification left for a later date. This record holds the as-enacted text only: later amendments, if any, are not replayed.'),
    dict(end=r'^SCHEDULE I$', slug='companies-act', short='Companies Act', title='The Companies Act, 2013 (Act 18 of 2013)', pdf='companies-act.pdf',
         start='An Act to consolidate', url=EGZ2, law='companies-act-2013', in_force='2013-08-30',
         law_entry=dict(label='Act 18 of 2013', title='The Companies Act, 2013', kind='law', enacted='2013-08-29', published='2013-08-30', url=EGZ2,
                        temporary_until=None, restores=None,
                        note='Assented to on 29 August 2013 and published on 30 August 2013. Section 1 came into force at once; other provisions came into force on dates the Central Government appointed by notification.'),
         note='The Act as enacted, from the Gazette of India Extraordinary of 30 August 2013 (Part II, Section 1). Section 1 came into force at once (30 August 2013); the other provisions came into force in stages by notification, which this record does not replay. Schedules I to VII and later amendments are not included.'),
]
for a in ACTS:
    pdf = H / '.cache' / a['pdf']
    units, seen = P.parse_act(pdf, a['start'], re.compile(a['end']) if a['end'] else None)
    corpus['laws'][a['law']] = a['law_entry']
    act = dict(slug=a['slug'], short=a['short'], title=a['title'], url=a['url'], first_law=a['law'], earlier_laws=[],
               versions=[dict({'from': a['in_force']}, source_url=a['url'], sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(), units=units, credits={}, note=a['note'])])
    corpus['acts'] = [x for x in corpus['acts'] if x['slug'] != a['slug']] + [act]
    print(a['slug'], len(units), 'units', len(seen), 'sections')
SRCS = [
    {'name': 'The Gazette of India, Extraordinary, Part II Section 1, No. 53 of 25 December 2023: The Bharatiya Nyaya Sanhita, 2023 (Ministry of Law and Justice, Legislative Department)',
     'url': EGZ, 'retrieved': '2026-10-30', 'requests': 1, 'licence': 'Government of India publication in the e-Gazette (egazette.gov.in); no licence statement on the file.',
     'notes': 'English text layer of the PDF read with PyMuPDF; the Hindi cover page and marginal notes (section headings in the margin) are not included; no OCR.'},
    {'name': 'The Gazette of India, Extraordinary, Part II Section 1, 30 August 2013: The Companies Act, 2013 (Ministry of Law and Justice, Legislative Department)',
     'url': EGZ2, 'retrieved': '2026-10-30', 'requests': 1, 'licence': 'Government of India publication in the e-Gazette (egazette.gov.in); no licence statement on the file.',
     'notes': 'English text layer of the PDF read with PyMuPDF; the Hindi cover page and marginal notes (section headings in the margin) are not included; Schedules I to VII are not included; no OCR.'}]
urls = [x['url'] for x in SRCS]
corpus['sources'] = [x for x in corpus['sources'] if x['url'] not in urls] + SRCS
D = ['Phase 2 statutes are added as their own acts; the Constitution act is unchanged.',
     'Bharatiya Nyaya Sanhita: one version, the as-enacted gazette text, dated 1 July 2024 (the commencement date in notification S.O. 850(E), except section 106(2)) and credited to Act 45 of 2023. Later amendments are not replayed.',
     "Bharatiya Nyaya Sanhita: the gazette prints each section's heading in the margin; those marginal notes are not included. Chapter titles and the sub-headings printed between sections are kept (sub-headings as the first line of the next section).",
     'Companies Act, 2013 (the nearest equivalent of a commercial code; India has no single civil or commercial code): one version, the as-enacted gazette text, dated 30 August 2013 (section 1 in force at once) and credited to Act 18 of 2013. Staged commencement of the other provisions and later amendments are not replayed.',
     'Companies Act, 2013: Sections 1 to 470 and chapter titles are included; Schedules I to VII and the marginal section headings are not.']
corpus['decisions'] = [x for x in corpus['decisions'] if x not in D] + D
(H / 'corpus.json').write_text(json.dumps(corpus, ensure_ascii=False, indent=1) + '\n', 'utf-8')
