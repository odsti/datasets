# GET AND CLEAN THE DUNCAN OCCUPATIONAL PRESTIGE DATASET

import pandas as pd

# read in the data
df = pd.read_fwf("original/Duncan.txt")

# clean the column names
df = df[['type income education', 'Unnamed: 2', 'Unnamed: 3',
       'Unnamed: 4', 'Unnamed: 5']]
df.columns = ["name", "type", "income", "education", "prestige"]

# save the data
df.to_csv("processed/Duncan_Occupational_Prestige.csv", index=False)
