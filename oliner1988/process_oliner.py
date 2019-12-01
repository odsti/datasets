""" Process Oliner table data
"""

import os.path as op

import pandas as pd

def proc_n_table(fname, label_col):
    in_tab = pd.read_csv(fname)

    n_rows = in_tab[label_col] == 'n'
    ns = in_tab[n_rows].iloc[0, 1:].astype(int)

    # Multiply proportions by n
    tab = in_tab[~n_rows].copy()
    tab.iloc[:, 1:] = (tab.iloc[:, 1:] * ns / 100).round().astype(int)

    # Subtract bystanders to get actives
    tab = tab.rename(columns={'nonrescuers': 'actives'})
    tab['actives'] = tab['actives'] - tab['bystanders']
    ns['nonrescuers'] -= ns['bystanders']

    # add n at end of table
    tab.loc[tab.index.max() + 1] = ['out of'] + list(ns)

    # Save
    tab_fname = op.join('processed', fname)
    tab.to_csv(tab_fname, index=None)

# Table 6.7
proc_n_table('oliner_tab6_7.csv', 'value')
proc_n_table('oliner_tab6_8a_1.csv', 'party_yn')
proc_n_table('oliner_tab6_8a_2.csv', 'party_type')
