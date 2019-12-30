""" Scrape HTML output from ET engineer list, check against data.
"""
import os.path as op

import numpy as np
import pandas as pd

from bs4 import BeautifulSoup

ET_URL = 'https://www.encyclopedia-titanica.org'
HERE = op.dirname(__file__)

def read_page(html_fname):
    # Read the HTML into memory.
    with open(html_fname, 'rt') as fobj:
        html_doc = fobj.read()

    # Parse HTML into objects.
    return BeautifulSoup(html_doc, 'html.parser')


def page2people(page):
    people_rows = page.find_all(itemtype="http://schema.org/Person")
    return [person2dict(row) for row in people_rows]


def person2dict(row):
    details, age, category, picture = row.find_all('td')
    details_a = details.find('a')
    title = details_a['title']
    in_detail = details_a.find('span', class_='fn').find_all('span')
    p_dict = {e.attrs['itemprop']: e.text for e in in_detail}
    p_dict['age'] = float(age.text.strip())
    p_dict['category'] = category.find('span').text.strip()
    p_dict['url'] = details_a['href']
    low_family = p_dict['familyName'].lower()
    where_title = title.lower().find(low_family)
    assert where_title != -1
    title_surname = title[where_title:where_title + len(low_family)]
    p_dict['familyName'] = title_surname
    return p_dict


def people2df(people):
    names = [dict2name(d) for d in people]
    raw_df = pd.DataFrame(people)
    out_df = pd.DataFrame(data=names, columns=['name'])
    return out_df.assign(**{'age': raw_df['age'],
                            'class': raw_df['category'],
                            'honorific': raw_df['honorificPrefix'],
                            'given_name': raw_df['givenName'],
                            'family_name': raw_df['familyName'],
                            'url': raw_df['url']})


def dict2name(d):
    return '{familyName}, {honorificPrefix}. {givenName}'.format(**d)


# Read data from page, write to CSV.
page = read_page(op.join(HERE, 'et_engineering_crew.html'))
people = page2people(page)
et_df = people2df(people)
et_df.to_csv('et_engineers.csv', index=None)

# Read data from original CSV.
st_df = pd.read_csv(op.join(HERE, '..', 'processed', 'titanic_stlearn.csv'))
st_engineers = st_df[st_df['class'] == 'engineering crew']

# Write to txt files to check with diff utility.
for df, fname in [(st_engineers, 'et_names.txt'),
                  (et_df, 'st_names.txt')]:
    names_ages = sorted(zip(df['name'], df['age']), key=lambda e: e[0])
    with open(fname, 'wt') as fobj:
        for name, age in names_ages:
            fobj.write(f'{name:40s} {age}\n')
