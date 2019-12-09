""" Process Oliner table data
"""

import os.path as op

import numpy as np
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


def check_pcts(fname):
    df = pd.read_csv(fname)
    pcts = df.iloc[1:, 1:]
    n = len(pcts)
    assert np.all(np.abs(pcts.sum() - 100) <= n * 0.05)

check_pcts('oliner_tab6_5mother.csv')
proc_n_table('oliner_tab6_5mother.csv', 'level')
check_pcts('oliner_tab6_5father.csv')
proc_n_table('oliner_tab6_5father.csv', 'level')
check_pcts('oliner_tab6_6.csv')
proc_n_table('oliner_tab6_6.csv', 'level')
proc_n_table('oliner_tab6_7.csv', 'value')
proc_n_table('oliner_tab6_8a_1.csv', 'party_yn')
proc_n_table('oliner_tab6_8a_2.csv', 'party_type')
