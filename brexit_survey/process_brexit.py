""" Process Brexit survey results
"""

from pathlib import Path

# Data frame library.
import pandas as pd
pd.set_option('mode.copy_on_write', True)

original_dir = Path('original')
processed_dir = Path('processed')

# Load the data frame, and put it in the variable "audit_data".
# The values are separated by tab characters, written as "\t" in Python
# strings.
audit_data = pd.read_csv(
    original_dir / 'audit_of_political_engagement_14_2017.tab',
    sep='\t')

"""
For the moment, we will focus on two questions labeled ``cut15``
and ``numage``.  ``cut15`` is the question about Brexit. The data dictionary
has the *variable label* "CUT15 - How did you vote on the question 'Should the
United Kingdom remain a member of the European Union or leave the European
Union'?".  The recorded values run from 1 through 6 and have the following
labels:

    Value label information for cut15
    Value = 1.0    Label = Remain a member of the European Union
    Value = 2.0    Label = Leave the European Union
    Value = 3.0    Label = Did not vote
    Value = 4.0    Label = Too young
    Value = 5.0    Label = Can't remember
    Value = 6.0    Label = Refused

We also want the variable ``numage``; this is the age of the respondent in
years.
"""

vote_recode = {
    1.0 : 'Remain',
    2.0 : 'Leave',
    3.0 : 'Did not vote',
    4.0 : 'Too young',
    5.0 : "Can't remember",
    6.0 : "Refused"}

df = pd.DataFrame()
df['brexit_vote'] = audit_data['cut15'].replace(vote_recode)
df['age'] = audit_data['numage']

# Drop rows where age is 0
good_data = df[df['age'] != 0]
# We lose 14 rows.
assert len(good_data) == len(df) - 14

out_csv = processed_dir / 'brexit_survey.csv'
good_data.to_csv(out_csv, index=None)

print(pd.read_csv(out_csv).head())
