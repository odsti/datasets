""" Scrape ratings from https://guide.doctorwhonews.net
"""

import pandas as pd

URL_TEMPLATE = \
'https://guide.doctorwhonews.net/info.php?detail=ratings&start={start}&type=rating'

# https://guide.doctorwhonews.net/info.php
# Number of episodes
N_EPISODES = 871

# Ratings given in 100 row blocks
tables = []
for start in range(0, N_EPISODES + 1, 100):
    these_tables = pd.read_html(URL_TEMPLATE.format(start=start))
    if len(these_tables) > 1:
        raise ValueError('Too many tables')
    if len(these_tables) == 0:
        break
    table = these_tables[0]
    if len(table) == 0:
        break
    tables.append(these_tables[0])

ratings = pd.concat(tables)
assert len(ratings) == N_EPISODES

ratings.to_csv('doctor_who_raw.csv', index=False)
