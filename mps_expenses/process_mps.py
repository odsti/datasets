""" Process MPs expense details
"""

import os.path as op
import re

import numpy as np
import pandas as pd


contact = pd.read_csv(op.join('original', 'mp_contact_11_2020.csv'))
expenses = pd.read_csv(op.join('original', 'mp_expenses_2020_21.csv')).dropna(
    how='all')


def drop_salutation(name):
    salutation, rest = name.split(' ', 1)
    if salutation in ('Ms', 'Mrs', 'Miss', 'Mr', 'Dr', 'Dame', 'Sir'):
        return rest
    return name


RENAMES = {  # Contact name, desired name to match expenses
           "Angus Brendan MacNeil": "Angus MacNeil",
           "Anne Marie Morris": "Anne Morris",
           "William Cash": "Bill Cash",
           "Robert Neill": "Bob Neill",
           "Chi Onwurah": "Chinyelu Onwurah",
           "Christian Matheson": "Chris Matheson",
           "Christopher Pincher": "Chris Pincher",
           "Chris Elmore": "Christopher Elmore",
           "Dan Poulter": "Daniel Poulter",
           "David T C Davies": "David Davies",
           "Ed Davey": "Edward Davey",
           "Imran Ahmad Khan": "Imran Ahmad-Khan",
           "Jeffrey M Donaldson": "Jeffrey Donaldson",
           "Liz Saville Roberts": "Liz Saville-Roberts",
           "Mary Kelly Foy": "Mary Foy",
           'Matt Hancock': 'Matthew Hancock',
           'Naz Shah': 'Naseem Shah',
           'Preet Kaur Gill': 'Preet Gill',
           'Steve Barclay': 'Stephen Barclay',
           'Steve McCabe': 'Stephen McCabe',
           'Stuart C McDonald': 'Stuart McDonald',
           'Stewart Malcolm McDonald': 'Stewart McDonald',
           'Thérèse Coffey': 'Therese Coffey',
}


def process_name(name):
    name = drop_salutation(name)
    return RENAMES.get(name, name)


contact['MP name'] = contact['Name (Display as)'].apply(process_name)

# Expenses missing a contact.
emissing_contact = expenses[~expenses['MP name'].isin(contact['MP name'])]


def debug_names(contact, expenses):
    """ Print suggestions for matching names
    """
    # Go through each, looking for last name
    con_copy = contact.copy()
    con_copy['last'] = contact['MP name'].apply(lambda n : n.split()[-1])

    for idx, values in emissing_contact.iterrows():
        name = values['MP name']
        last = re.split('[ -]', name)[-1]
        print(name)
        maybes = con_copy[contact['MP name'].str.contains(last)]
        if len(maybes) == 0:
            print('No suggestions')
        else:
            print("Possible contact rows")
            print(maybes)


details = contact.loc[:, ['MP name', 'Party']]

def proc_pounds(v):
    return float(v.replace('£', '').replace(',', ''))

column_renames = {
    'Office spend': 'Office',
    'Staffing spend': 'Staffing',
    'Windup spend': 'Windup',
    'Accommodation spend': 'Accommodation',
    'Travel/subs spend': 'Travel',
    'Other spend': 'Other',
    'Overall total spend for this financial year': 'Total',
}

total_spend = expenses.loc[:, ['MP name']]
total_spend = total_spend.assign(
    **{new: expenses[old].apply(proc_pounds)
       for old, new in column_renames.items()})

both = details.merge(total_spend, on='MP name')

# Check we have the correct number of MPs
assert len(both) == 650

# Check we got everything
calc_totals = both.loc[:, 'Office':'Other'].sum(axis=1)
assert np.allclose(calc_totals, both['Total'])

out_fname = op.join('processed', 'uk_mp_expenses_2020_21.csv')
both.to_csv(out_fname, index=None)

# Show first few rows from processed file.
print(pd.read_csv(out_fname).head())
