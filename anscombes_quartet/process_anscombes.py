""" Process Anscombe's quartet data

https://en.wikipedia.org/wiki/Anscombe%27s_quartet

"""

import os.path as op

import numpy as np

import pandas as pd

""" From:
https://en.wikipedia.org/wiki/Anscombe%27s_quartet
"""

data = """\
10.0 	8.04 	10.0 	9.14 	10.0 	7.46 	8.0 	6.58
8.0 	6.95 	8.0 	8.14 	8.0 	6.77 	8.0 	5.76
13.0 	7.58 	13.0 	8.74 	13.0 	12.74 	8.0 	7.71
9.0 	8.81 	9.0 	8.77 	9.0 	7.11 	8.0 	8.84
11.0 	8.33 	11.0 	9.26 	11.0 	7.81 	8.0 	8.47
14.0 	9.96 	14.0 	8.10 	14.0 	8.84 	8.0 	7.04
6.0 	7.24 	6.0 	6.13 	6.0 	6.08 	8.0 	5.25
4.0 	4.26 	4.0 	3.10 	4.0 	5.39 	19.0 	12.50
12.0 	10.84 	12.0 	9.13 	12.0 	8.15 	8.0 	5.56
7.0 	4.82 	7.0 	7.26 	7.0 	6.42 	8.0 	7.91
5.0 	5.68 	5.0 	4.74 	5.0 	5.73 	8.0 	6.89"""

data_lines = [[float(v) for v in L.split()] for L in data.splitlines()]
data_arr = np.array(data_lines)

# This one's a bit confusing. It rearranges the data into quartets, item.
in_data = data_arr.reshape((-1, 2, 4), order='F').transpose(
    2, 0, 1).reshape((-1, 2))
quartet_labels = np.repeat(['I', 'II', 'III', 'IV'], 11)

df = pd.DataFrame({'quartet': quartet_labels,
                   'x': in_data[:, 0],
                   'y': in_data[:, 1]})

out_fname = op.join('processed', 'anscombes_quartet.csv')
df.to_csv(out_fname, index=None)

# Show the various summary stats.
quartet_gs = df.groupby('quartet')
print('Means\n', quartet_gs.mean())
print('\nSTDs\n', quartet_gs.std())
print('\nrs\n', quartet_gs.apply(lambda d : np.corrcoef(d['x'], d['y'])[0, 1]))
