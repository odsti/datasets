""" Process movie_metadata.csv
"""

import os.path as op

import numpy as np
import pandas as pd

tmdb_fname = op.join('original', 'tmdb_5000_movies.csv')

tmdb_df = pd.read_csv(tmdb_fname)

cols = ['title',
        'budget',
        'runtime',
        'revenue',
        'vote_average',
        'vote_count']

col2dtype = {'year': int,
             'budget': int}

# Remove films with few votes (highly variable average scores).
n_vote_threshold = 100

tmdb_trim = tmdb_df.loc[tmdb_df['vote_count'] > n_vote_threshold, cols]

def proc_rd(rd):
    if pd.isnull(rd):
        return rd
    parts = rd.split('-')
    assert len(parts) == 3
    return parts[0]


def proc_pc(pc_s):
    if pd.isnull(pc_s):
        return pc_s
    pc = eval(pc_s)
    if len(pc) == 0:
        return np.nan
    return pc[0]["iso_3166_1"]


# Calculate year and country
tmdb_trim['year'] = tmdb_df['release_date'].apply(proc_rd)
tmdb_trim['country'] = tmdb_df['production_countries'].apply(proc_pc)

# Drop missing values
tmdb_trim = tmdb_trim.dropna()

# Some columns can now be ints
for name, dt in col2dtype.items():
    tmdb_trim[name] = tmdb_trim[name].astype(dt)

# Sort by average score.
tmdb_by_score = tmdb_trim.sort_values('vote_average', ascending=False)

# Write full processed dataset.
out_fname = op.join('processed', 'tmdb_movies.csv')
tmdb_by_score.to_csv(out_fname, index=None)
