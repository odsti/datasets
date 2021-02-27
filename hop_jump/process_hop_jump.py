""" Process hop jump values from digitized plot
"""

import os.path as op

import numpy as np
import pandas as pd


from_plot = pd.read_csv(op.join('original', 'hop_jump.csv'))
data = np.array(from_plot)

# Vertical jump measures were originally in whole inches.
# Round to nearest inch, then back to cm.
cm2inch = 0.39370
data[:, 1] = np.round(data[:, 1] * cm2inch) / cm2inch

# Round values into final data frame.
out_df = pd.DataFrame(np.round(data, 2),
                      columns=['triple', 'vertical'])

out_fname = op.join('processed', 'hop_jump.csv')
out_df.to_csv(out_fname, index=False)
