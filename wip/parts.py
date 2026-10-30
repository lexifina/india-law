"""India phase 2 parts (private): one corpus.d part per Act, from Gazette of India Extraordinary PDFs in .cache/.
Uses parse_acts.parse_act (English text layer, marginal notes excluded). Reads .cache only; deterministic.
Usage: python -X utf8 parts.py [slug ...]"""
import hashlib, json, re, sys
from pathlib import Path
import parse_acts as P

H = P.H
EG = 'https://egazette.gov.in/WriteReadData/2023/{}.pdf'
ACTS = [
    dict(part='20-bharatiya-nagarik-suraksha-sanhita', slug='bharatiya-nagarik-suraksha-sanhita', short='BNSS',
         title='The Bharatiya Nagarik Suraksha Sanhita, 2023 (Act 46 of 2023)', pdf='bnss.pdf', url=EG.format(250884),
         start='An Act to consolidate', end=r'^THE FIRST SCHEDULE$', law='bnss-2023', in_force='2024-07-01',
         law_entry=dict(label='Act 46 of 2023', title='The Bharatiya Nagarik Suraksha Sanhita, 2023', kind='law', enacted='2023-12-25',
                        published='2023-12-25',
                        note='Enacted 25 December 2023; brought into force on 1 July 2024 by notification S.O. 848(E) of 23 February 2024, '
                             'except the provisions of the First Schedule entry for section 106(2) of the Bharatiya Nyaya Sanhita and section 530.'),
         note='The Act as enacted, from the Gazette of India Extraordinary of 25 December 2023 (Part II, Section 1). It came into force on '
              '1 July 2024 (notification S.O. 848(E)), with stated exceptions. This record holds the as-enacted text of sections 1 to 531 '
              'only: the First and Second Schedules and later amendments are not included.',
         src='The Gazette of India, Extraordinary, Part II Section 1, 25 December 2023: The Bharatiya Nagarik Suraksha Sanhita, 2023 '
             '(Ministry of Law and Justice, Legislative Department)',
         dec='Bharatiya Nagarik Suraksha Sanhita: one version, the as-enacted gazette text, dated 1 July 2024 (the commencement date in '
             'notification S.O. 848(E)) and credited to Act 46 of 2023; sections 1 to 531 and chapter titles are included, the First and '
             'Second Schedules and the marginal section headings are not. Later amendments are not replayed.'),
    dict(part='21-bharatiya-sakshya-adhiniyam', slug='bharatiya-sakshya-adhiniyam', short='BSA',
         title='The Bharatiya Sakshya Adhiniyam, 2023 (Act 47 of 2023)', pdf='bsa.pdf', url=EG.format(250882),
         start='An Act to consolidate', end=r'^THE SCHEDULE$', law='bsa-2023', in_force='2024-07-01',
         law_entry=dict(label='Act 47 of 2023', title='The Bharatiya Sakshya Adhiniyam, 2023', kind='law', enacted='2023-12-25',
                        published='2023-12-25',
                        note='Enacted 25 December 2023; brought into force on 1 July 2024 by notification S.O. 849(E) of 23 February 2024.'),
         note='The Act as enacted, from the Gazette of India Extraordinary of 25 December 2023 (Part II, Section 1). It came into force on '
              '1 July 2024 (notification S.O. 849(E)). This record holds the as-enacted text of sections 1 to 170; the Schedule (the form '
              'of certificate under section 63) and later amendments are not included.',
         src='The Gazette of India, Extraordinary, Part II Section 1, 25 December 2023: The Bharatiya Sakshya Adhiniyam, 2023 '
             '(Ministry of Law and Justice, Legislative Department)',
         dec='Bharatiya Sakshya Adhiniyam: one version, the as-enacted gazette text, dated 1 July 2024 (the commencement date in notification '
             'S.O. 849(E)) and credited to Act 47 of 2023; sections 1 to 170 and chapter titles are included, the Schedule and the marginal '
             'section headings are not. Later amendments are not replayed.'),
]


def build(a):
    pdf = H / '.cache' / a['pdf']
    units, seen = P.parse_act(pdf, a['start'], re.compile(a['end']))
    print(a['slug'], len(units), 'units', len(seen), 'sections, last', seen[-1], file=sys.stderr)
    nums = [int(re.match(r'\d+', s).group()) for s in seen]
    miss = [n for n in range(1, max(nums) + 1) if n not in nums]
    if miss:
        print('  missing section numbers', miss, file=sys.stderr)
    e = dict(a['law_entry'], url=a['url'], temporary_until=None, restores=None)
    act = dict(slug=a['slug'], short=a['short'], title=a['title'], url=a['url'], first_law=a['law'], earlier_laws=[],
               versions=[{'from': a['in_force'], 'source_url': a['url'], 'sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
                          'units': units, 'credits': {}, 'note': a['note']}])
    return {'acts': [act], 'laws': {a['law']: e}, 'decisions': [a['dec']], 'ai_use': ['none'],
            'sources': [{'name': a['src'], 'url': a['url'], 'retrieved': '2026-10-30', 'requests': 1,
                         'licence': 'Government of India publication in the e-Gazette (egazette.gov.in); no licence statement on the file.',
                         'notes': 'English text layer of the PDF read with PyMuPDF; the Hindi cover lines and the marginal notes (section '
                                  'headings in the margin) are not included; no OCR.'}]}


if __name__ == '__main__':
    only = set(sys.argv[1:])
    out = H / 'corpus.d'
    out.mkdir(exist_ok=True)
    for a in ACTS:
        if only and a['slug'] not in only:
            continue
        doc = build(a)
        tmp = out / (a['part'] + '.json.tmp')
        tmp.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + '\n', encoding='utf-8', newline='\n')
        tmp.replace(out / (a['part'] + '.json'))
