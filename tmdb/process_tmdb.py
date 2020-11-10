""" Process movie_metadata.csv
"""

import os.path as op

import pandas as pd

tmdb_fname = op.join('original', 'tmdb_5000_movies.csv')

tmdb_df = pd.read_csv(tmdb_fname)

cols = {'title': 'title',
        'title_year': 'year',
        'budget': 'budget',
        'revenue': 'revenue',
        'country': 'country',
        'imdb_score': 'imdb_score',
        'movie_facebook_likes': 'facebook_likes'}

col2dtype = {'year': int,
             'budget': int,
             'gross': int}

tmdb_trim = tmdb_df.loc[:, list(cols)].rename(columns=cols).dropna()

for name, dt in col2dtype.items():
    tmdb_trim[name] = tmdb_trim[name].astype(dt)

tmdb_by_score = tmdb_trim.sort_values('imdb_score', ascending=False)

# Write full processed dataset.
out_fname = op.join('processed', 'movies.csv')
tmdb_by_score.to_csv(out_fname, index=None)
