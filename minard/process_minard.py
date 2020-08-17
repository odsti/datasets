""" Process Minard data
"""

import os.path as op

import numpy as np
import pandas as pd

cities = pd.read_csv(op.join('original', 'minard_cities.csv'))
troops = pd.read_csv(op.join('original', 'minard_troops.csv'))


def lookup_city(row):
    d_longs = cities['Longditude'] - row['Longditude']
    d_lats = cities['Latitude'] - row['Latitude']
    dists = np.sqrt(d_longs ** 2 + d_lats ** 2)
    good_cities = cities.loc[dists < 0.1, 'City']
    n_good = len(good_cities)
    if n_good == 0:
        return np.nan
    if n_good > 1:
        raise RuntimeError('Too many matching cities ' +
                           ', '.join(good_cities))
    return good_cities.iloc[0]


troop_cities = troops.assign(City=troops.apply(lookup_city, axis='columns'))
troop_cities = troop_cities.dropna()
