""" Scrape HTML output from ET engineer list, check against data.
"""
import os.path as op

import numpy as np
import pandas as pd

from bs4 import BeautifulSoup


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
    p_dict['role'] = category.text.strip()
    low_family = p_dict['familyName'].lower()
    where_title = title.lower().find(low_family)
    assert where_title != -1
    p_dict['familyName'] = title[where_title:where_title+len(low_family)]
    return p_dict


def dict2name(d):
    return '{familyName}, {honorificPrefix}. {givenName}'.format(**d)


data = pd.read_csv(op.join(HERE, '..', 'processed', 'titanic_stlearn.csv'))
engineers = data[data['class'] == 'engineering crew'].sort_values('name')
page = read_page(op.join(HERE, 'et_engineering_crew.html'))
people = page2people(page)
names_ages = [(dict2name(d), d['age']) for d in people]


def s1(e):
    return e[0]


names_ages = sorted(names_ages, key=s1)
enames_ages = sorted(zip(engineers['name'], engineers['age']), key=s1)

with open('et_names.txt', 'wt') as fobj:
    for name, age in names_ages:
        fobj.write(f'{name:40s} {age}\n')

with open('st_names.txt', 'wt') as fobj:
    for name, age in enames_ages:
        fobj.write(f'{name:40s} {age}\n')
