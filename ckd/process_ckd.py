""" Process CKD file to CSV
"""

import os.path as op
from io import StringIO

import numpy as np
import pandas as pd
from scipy.io import arff

# Patch input file to remove extra missing value.
# The original file appears to be mal-formed, and therefore causes errors when
# reading with Scipy.  Specifically, the value in line 399, starting `75,70`,
# has an extra missing field specified with double commas: `,,`.
with open('chronic_kidney_disease_full.arff', 'rt') as fobj:
    data_txt = fobj.read()
data_txt = data_txt.replace(',,', ',')

# Load modified data as Numpy record arrays.
data, meta = arff.loadarff(StringIO(data_txt))

# To pandas data frame
df = pd.DataFrame.from_records(data)

# Rename columns to full names given in header of ARFF file.
renames = {
    'age': 'Age',
    'bp': 'Blood Pressure',
    'sg': 'Specific Gravity',
    'al': 'Albumin',
    'su': 'Sugar',
    'rbc': 'Red Blood Cells',
    'pc': 'Pus Cell',
    'pcc': 'Pus Cell clumps',
    'ba': 'Bacteria',
    'bgr': 'Blood Glucose Random',
    'bu': 'Blood Urea',
    'sc': 'Serum Creatinine',
    'sod': 'Sodium',
    'pot': 'Potassium',
    'hemo': 'Hemoglobin',
    'pcv': 'Packed Cell Volume',
    'wbcc': 'White Blood Cell Count',
    'rbcc': 'Red Blood Cell Count',
    'htn': 'Hypertension',
    'dm': 'Diabetes Mellitus',
    'cad': 'Coronary Artery Disease',
    'appet': 'Appetite',
    'pe': 'Pedal Edema',
    'ane': 'Anemia',
    'class': 'Class'
}

df = df.rename(renames, axis='columns')


def recode_bytes(val):
    """ Recode columns with byte strings to strings

    Replace ? with NA
    """
    out = val.decode('latin1')
    if out == '?':
        out = np.nan
    return out


for col_name, col_dtype in df.dtypes.items():
    if col_dtype != np.dtype(object):
        continue
    # Recode object column with recoder.
    new_col = df[col_name].apply(recode_bytes)
    # Convert to float if possible.
    try:
        new_col = new_col.astype(float)
    except ValueError:
        pass
    df[col_name] = new_col

out_fname = op.join('processed', 'ckd_full.csv')
df.to_csv(out_fname, index=False)


# Processing to match (almost) the file from Berkeley Foundations of Data
# Science: https://www.inferentialthinking.com
# See README
clean = df.dropna(how='any')
clean = clean.replace({'Class': dict(ckd=1, notckd=0)})
out_fname_clean = op.join('processed', 'ckd_clean.csv')
clean.to_csv(out_fname_clean, index=False)
