""" Process diet dataset
"""

import os.path as op

import pandas as pd

orig_fname = op.join('original', 'Diet_SPSS.sav')

df = pd.read_spss(orig_fname)

simple_df = df.loc[:, ['Diet', 'weightLOST']].rename(columns={
    'Diet': 'diet',
    'weightLOST': 'weight_lost'})

# Recode diet column to strings to make clear it is categorical.
simple_df['diet'] = simple_df['diet'].replace(
    {1: 'A', 2: 'B', 3: 'C'})

proc_fname = op.join('processed', 'sheffield_diet.csv')

simple_df.to_csv(proc_fname, index=None)
