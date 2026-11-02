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
                             'with the exceptions that notification states.'),
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
    dict(part='22-code-on-wages', slug='code-on-wages', short='Code on Wages',
         title='The Code on Wages, 2019 (Act 29 of 2019)', pdf='code-on-wages.pdf', url='https://egazette.gov.in/WriteReadData/2019/210356.pdf',
         start='An Act to amend and consolidate', end=r'^-{3,}$', law='code-on-wages-2019', in_force='2020-12-18',
         law_entry=dict(label='Act 29 of 2019', title='The Code on Wages, 2019', kind='law', enacted='2019-08-08', published='2019-08-08',
                        note='Assented to and published on 8 August 2019. Its provisions came into force on dates the Central Government '
                             'appointed by notification, the first of them on 18 December 2020.'),
         note='The Act as enacted, from the Gazette of India Extraordinary of 8 August 2019 (Part II, Section 1). Its provisions came into '
              'force in stages by notification, the first on 18 December 2020; this record dates the as-enacted text from that first '
              'commencement and does not replay the later commencements or any amendments.',
         src='The Gazette of India, Extraordinary, Part II Section 1, 8 August 2019: The Code on Wages, 2019 '
             '(Ministry of Law and Justice, Legislative Department)',
         dec='Code on Wages, 2019 (the first of the four labour codes): one version, the as-enacted gazette text, dated 18 December 2020, '
             'when its first provisions came into force by notification, and credited to Act 29 of 2019; the staged commencement of the '
             'other provisions and later amendments are not replayed. Sections 1 to 69 and chapter titles are included, the marginal '
             'section headings are not.'),
]

LC_NOTE = ('The Code as enacted, from the Gazette of India Extraordinary of 29 September 2020 (Part II, Section 1). {force} This record '
           'holds the as-enacted text of sections 1 to {last} and chapter titles; the Schedules, the marginal section headings and later '
           'amendments, if any, are not included.')
LC = [
    ('23-industrial-relations-code', 'industrial-relations-code', 'Industrial Relations Code', 'The Industrial Relations Code, 2020 (Act 35 of 2020)',
     'irc.pdf', 222118, 'An Act to consolidate', 'irc-2020', 'Act 35 of 2020', 'The Industrial Relations Code, 2020', 104,
     'S.O. 5320(E)', 267883, 'sub-section (3) of section 1',
     'It came into force on 21 November 2025, when notification S.O. 5320(E) of that day brought all its provisions into force.'),
    ('24-code-on-social-security', 'code-on-social-security', 'Code on Social Security', 'The Code on Social Security, 2020 (Act 36 of 2020)',
     'code-on-social-security.pdf', 222111, 'An Act to amend and consolidate', 'code-on-social-security-2020', 'Act 36 of 2020',
     'The Code on Social Security, 2020', 164, 'S.O. 5319(E)', 267882, 'sub-section (3) of section 1',
     'Notification S.O. 5319(E) of 21 November 2025 brought most of its provisions into force that day (sections 1 to 14, 17 to 141, '
     '143 and 144 to 163, and parts of sections 15, 16 and 164); some provisions had been brought into force earlier by other '
     'notifications (among them S.O. 2060(E) of 3 May 2023), and the rest await notification. This record dates the whole text from 21 November 2025.'),
    ('25-occupational-safety-health-code', 'occupational-safety-health-and-working-conditions-code', 'OSH Code',
     'The Occupational Safety, Health and Working Conditions Code, 2020 (Act 37 of 2020)', 'osh-code.pdf', 222112, 'An Act to consolidate',
     'osh-code-2020', 'Act 37 of 2020', 'The Occupational Safety, Health and Working Conditions Code, 2020', 143, 'S.O. 5321(E)', 267884,
     'sub-section (2) of section 1',
     'It came into force on 21 November 2025, when notification S.O. 5321(E) of that day brought all its provisions into force.'),
]
for part, slug, short, title, pdf, eid, start, law, label, ltitle, last, so, nid, power, force in LC:
    url = 'https://egazette.gov.in/WriteReadData/2020/%d.pdf' % eid
    nurl = 'https://egazette.gov.in/WriteReadData/2025/%d.pdf' % nid
    ACTS.append(dict(
        part=part, slug=slug, short=short, title=title, pdf=pdf, url=url, start=start, end=r'^THE FIRST SCHEDULE$', law=law,
        in_force='2025-11-21', retrieved='2026-11-02', monotonic=True,
        law_entry=dict(label=label, title=ltitle, kind='law', enacted='2020-09-28', published='2020-09-29',
                       note='Assented to on 28 September 2020 and published on 29 September 2020. ' + force.replace('It came', 'It came')
                            + ' (notification %s, made under %s, Gazette of India Extraordinary of 21 November 2025: %s)' % (so, power, nurl)),
        note=LC_NOTE.format(force=force, last=last),
        src='The Gazette of India, Extraordinary, Part II Section 1, 29 September 2020: %s (Ministry of Law and Justice, Legislative '
            'Department); commencement: notification %s of 21 November 2025, Ministry of Labour and Employment, Gazette of India '
            'Extraordinary, Part II Section 3(ii), %s' % (ltitle, so, nurl),
        dec='%s (one of the four labour codes): one version, the as-enacted gazette text, dated 21 November 2025 (notification %s) and '
            'credited to %s; sections 1 to %d and chapter titles are included, the Schedules and the marginal section headings are not. '
            'Later amendments, if any, are not replayed.' % (ltitle, so, label, last)))

ITA_URL = 'https://egazette.gov.in/WriteReadData/2025/265620.pdf'
ACTS.append(dict(
    part='26-income-tax-act-2025', slug='income-tax-act', short='Income-tax Act', title='The Income-tax Act, 2025 (Act 30 of 2025)',
    pdf='income-tax-act-2025.pdf', url=ITA_URL, start='An Act to consolidate and amend the law relating to income-tax', end=r'^SCHEDULE I$',
    law='income-tax-act-2025', in_force='2026-04-01', retrieved='2026-11-02', monotonic=True, line_level=True,
    law_entry=dict(label='Act 30 of 2025', title='The Income-tax Act, 2025', kind='law', enacted='2025-08-21', published='2025-08-21',
                   note='Assented to and published on 21 August 2025. Section 1(3): "Save as otherwise provided in this Act, it shall come '
                        'into force on the 1st April, 2026." It replaced the Income-tax Act, 1961.'),
    note='The Act as enacted, from the Gazette of India Extraordinary of 21 August 2025 (Part II, Section 1, No. 35). Section 1(3) brings '
         'it into force on 1 April 2026, save as otherwise provided in the Act. This record holds the as-enacted text of the sections and '
         'chapter titles; Schedules I to XVI, the marginal section headings and any amendment made before or after 1 April 2026 (for '
         'example by a Finance Act) are not included. Tables inside sections are flattened: each cell is a line, in the order of the '
         'PDF text layer, and the column letters printed above a table (A, B, C) may appear as a line of their own or at the end of a cell.',
    src='The Gazette of India, Extraordinary, Part II Section 1, No. 35, 21 August 2025: The Income-tax Act, 2025 (Ministry of Law and '
        'Justice, Legislative Department)',
    dec='Income-tax Act, 2025: one version, the as-enacted gazette text, dated 1 April 2026 (section 1(3)) and credited to Act 30 of 2025; '
        'the sections and chapter titles are included, Schedules I to XVI and the marginal section headings are not. Amendments, '
        'including any made by a Finance Act with effect from 1 April 2026, are not applied, so the text may differ from what was in '
        'force on that day where it was amended before commencement.'))


def build(a):
    pdf = H / '.cache' / a['pdf']
    units, seen = P.parse_act(pdf, a['start'], re.compile(a['end']), monotonic=a.get('monotonic', False), line_level=a.get('line_level', False))
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
            'sources': [{'name': a['src'], 'url': a['url'], 'retrieved': a.get('retrieved', '2026-10-30'), 'requests': 2 if a.get('retrieved') else 1,
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
