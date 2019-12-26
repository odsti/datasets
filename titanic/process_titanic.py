#!/usr/bin/env python
# coding: utf-8

# Read, check and process the Stablelearner Titanic data set.
#
# See `README` and <https://rdrr.io/cran/stablelearner/man/titanic.html> for
# details.

import os.path as op

import numpy as np
import pandas as pd

# Read the data frame.
titanic = pd.read_csv('titanic_stablelearner.csv')

# Recode embarked field to full names of ports.
titanic['embarked'] = titanic['embarked'].replace(
    dict(S='Southampton', C='Cherbourg', B='Belfast', Q='Queenstown'))


# Check there are 890 crew members, 1317 passengers, as reported at
# https://rdrr.io/cran/stablelearner/man/titanic.html
is_crew = titanic['class'].str.contains('crew') | titanic['class'].str.contains('staff')
print('Number of crew', np.count_nonzero(is_crew))
print('Number of passengers', np.count_nonzero(~is_crew))

# Save
out_fname = op.join('processed', 'titanic_stlearn.csv')
titanic.to_csv(out_fname, index=None)

# Check that data frame loads correctly.
print(pd.read_csv(out_fname).head())
