""" Process movie_metadata.csv
"""

import os.path as op

import pandas as pd

mmd_fname = op.join('original', 'movie_metadata.csv')

mmd_df = pd.read_csv(mmd_fname)

cols = {'movie_title': 'title',
        'title_year': 'year',
        'budget': 'budget',
        'gross': 'gross',
        'country': 'country',
        'imdb_score': 'imdb_score',
        'movie_facebook_likes': 'facebook_likes'}

col2dtype = {'year': int,
             'budget': int,
             'gross': int}

mmd_trim = mmd_df.loc[:, list(cols)].rename(columns=cols).dropna()

for name, dt in col2dtype.items():
    mmd_trim[name] = mmd_trim[name].astype(dt)

mmd_by_score = mmd_trim.sort_values('imdb_score', ascending=False)

# Write full processed dataset.
out_fname = op.join('processed', 'movies.csv')
mmd_by_score.to_csv(out_fname, index=None)
