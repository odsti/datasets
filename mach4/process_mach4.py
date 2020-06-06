""" Process Mach4 data
"""

import os.path as op
import re

import numpy as np
import pandas as pd

TAB_SPLITTER = re.compile(r'\t+')
COMMA_SPLITTER = re.compile(r',\s*')

# From codebook
Q_DEFS = {
"Q1" : "Never tell anyone the real reason you did something unless it is useful to do so.",
"Q2" : "The best way to handle people is to tell them what they want to hear.",
"Q3" : "One should take action only when sure it is morally right.",
"Q4" : "Most people are basically good and kind.",
"Q5" : "It is safest to assume that all people have a vicious streak and it will come out when they are given a chance.",
"Q6" : "Honesty is the best policy in all cases.",
"Q7" : "There is no excuse for lying to someone else.",
"Q8" : "Generally speaking, people won't work hard unless they're forced to do so.",
"Q9" : "All in all, it is better to be humble and honest than to be important and dishonest.",
"Q10" : "When you ask someone to do something for you, it is best to give the real reasons for wanting it rather than giving reasons which carry more weight.",
"Q11" : "Most people who get ahead in the world lead clean, moral lives.",
"Q12" : "Anyone who completely trusts anyone else is asking for trouble.",
"Q13" : "The biggest difference between most criminals and other people is that the criminals are stupid enough to get caught.",
"Q14" : "Most people are brave.",
"Q15" : "It is wise to flatter important people.",
"Q16" : "It is possible to be good in all respects.",
"Q17" : "P.T. Barnum was wrong when he said that there's a sucker born every minute.",
"Q18" : "It is hard to get ahead without cutting corners here and there.",
"Q19" : "People suffering from incurable diseases should have the choice of being put painlessly to death.",
"Q20" : "Most people forget more easily the death of their parents than the loss of their property."
}
# Answer column for each question.
# Answer columns have suffix A, Index columns have suffix I, duration (Elapsed)
# columns have suffix E.
ALL_QA = [q + 'A' for q in Q_DEFS]

# Questions for which 1 means more Machiavellian.
# For the remaining questions, 5 means more Maciavellian.
TO_REVERSE = ("Q3", "Q4", "Q6", "Q7" , "Q9" , "Q10", "Q11", "Q14", "Q16",
              "Q17")
TO_REVERSE_QA = [q + 'A' for q in TO_REVERSE]

# Example answers to questions, where questions presented in random order.
# We use these to get a calculated score from a couple of websites (see below),
# and then test we get the same calculated score.
TEST_DATA = {
    "Q19A": 3,
    "Q10A": 5,
    "Q2A": 1,
    "Q16A": 5,
    "Q11A": 2,
    "Q13A": 1,
    "Q15A": 3,
    "Q9A": 5,
    "Q7A": 4,
    "Q8A": 1,
    "Q12A": 3,
    "Q5A": 3,
    "Q4A": 3,
    "Q18A": 4,
    "Q17A": 2,
    "Q6A": 4,
    "Q14A": 2,
    "Q20A": 2,
    "Q1A": 1,
    "Q3A": 4,
}


# Sort test data by question numbers.
def qno(q):
    return int(q[1:-1])

TEST_DATA = {q: TEST_DATA[q] for q in sorted(TEST_DATA, key=qno)}

# Recoding dictionary that replaces 1 with 5, 2 with 4, etc.
REV_DICT = dict(zip(range(1, 6), range(5, 0, -1)))

# Recoding dictionary for use with data frame "replace" method.
# Keys are column names, values are recoding dictionary to apply to give
# column.
NEG_RECODERS = {q: REV_DICT for q in TO_REVERSE_QA}

def machIV_score(df):
    """ Calculate overall MACH IV score for data frame `df`.

    Sum all scores, after reversing negative columns.
    """
    recoded = df.loc[:, ALL_QA].replace(NEG_RECODERS)
    return recoded.sum(axis='columns')

# Make test data frame with answers for which score is known.
test_df = pd.DataFrame(TEST_DATA, index=(0,))

# Check input data against returned score of 46 from:
#   https://www.aconsciousrethink.com/6299/machiavellian-scale-test
#   https://openpsychometrics.org/tests/MACH-IV
assert float(machIV_score(test_df)) == 46

# Rename some columns - from codebook
TIPI_DEFS = '''\
TIPI1	Extraverted, enthusiastic.
TIPI2	Critical, quarrelsome.
TIPI3	Dependable, self-disciplined.
TIPI4	Anxious, easily upset.
TIPI5	Open to new experiences, complex.
TIPI6	Reserved, quiet.
TIPI7	Sympathetic, warm.
TIPI8	Disorganized, careless.
TIPI9	Calm, emotionally stable.
TIPI10	Conventional, uncreative.
'''

VCL_DEFS ='''\
VCL1	boat
VCL2	incoherent
VCL3	pallid
VCL4	robot
VCL5	audible
VCL6	cuivocal
VCL7	paucity
VCL8	epistemology
VCL9	florted
VCL10	decide
VCL11	pastiche
VCL12	verdid
VCL13	abysmal
VCL14	lucid
VCL15	betray
VCL16	funny
'''

def defs2renames(defs):
    """ Column renaming dictionary given multiline `defs` string
    """
    renames = {}
    for line in defs.splitlines():
        name, rest = TAB_SPLITTER.split(line)
        first, *_ = rest.lower().split(',')
        first_first = first.split()[0]
        renames[name] = f'{name}_{first_first}'
    return renames


TIPI_RENAMES = defs2renames(TIPI_DEFS)
VCL_RENAMES = defs2renames(VCL_DEFS)
# Merge the dictionaries for renaming columns.
RENAMES = {**TIPI_RENAMES, **VCL_RENAMES}

# Value recoding dictionary for various demographic questions.
# See codebook.
DEM_RECODERS = {
    'urban': {1: 'Rural', 2: "Suburban", 3: "Urban"},
    'gender': {1: 'Male', 2: 'Female', 3: 'Other'},
    'engnat': {1: 'Yes', 2: 'No'},
    'hand': {1: 'Right', 2: 'Left', 3: 'Both'},
    'religion': {1: 'Agnostic',
                 2: 'Atheist',
                 3: 'Buddhist',
                 4: 'Christian (Catholic)',
                 5: 'Christian (Mormon)',
                 6: 'Christian (Protestant)',
                 7: 'Christian (Other)',
                 8: 'Hindu',
                 9: 'Jewish',
                 10: 'Muslim',
                 11: 'Sikh',
                 12: 'Other'},
    'orientation': {1: 'Heterosexual', 2: 'Bisexual', 3: 'Homosexual', 4:
                    'Asexual', 5: 'Other'},
    'race': {10: 'Asian', 20: 'Arab', 30: 'Black', 40: 'Indigenous Australian',
             50: 'Native American', 60: 'White', 70: 'Other'},
    'voted': {1: 'Yes', 2: 'No'},
    'married': {1: 'Never married',
                2: 'Currently married',
                3: 'Previously married'},
}
# Add interpretation of 0 as missing value to demographic value coders.
for name, recoder in DEM_RECODERS.items():
    recoder[0] = np.nan

# Recode missing value marker -> nan for some other demographic variables
DEM_RECODERS['education'] = {0: np.nan}

# Family size has some values > 40
def recode_familysize(v):
    if v > 40 or v == 0:
        return np.nan
    return v

# Age has some values > 150
def recode_age(v):
    if v > 150:
        return np.nan
    return v

# Read original data. Values are separated by tabs not commas.
in_fname = op.join('original', 'data.csv')
df = pd.read_csv(in_fname, sep='\t')

# Apply column renaming.
renamed = df.rename(columns=RENAMES)
# Apply value recoding dictionaries.
replaced = renamed.replace(DEM_RECODERS)
# Apply family size and age recoding functions.
recoded = replaced.assign(
    age=replaced['age'].apply(recode_age),
    familysize=replaced['familysize'].apply(recode_familysize)
)
# Calculate total score.
recoded['machIV_score'] = machIV_score(df)

# Write full processed dataset.
out_fname = op.join('processed', 'mach_iv.csv')
recoded.to_csv(out_fname, index=None)

# Write stripped down version, without individual questions or the word /
# personality questions.
auto_dems = recoded.loc[:, 'country':'surveyelapse']
rest = recoded.loc[:, 'education':]
thinner = pd.concat([auto_dems, rest], axis='columns')
out_fname_thin = op.join('processed', 'mach_iv_thin.csv')
thinner.to_csv(out_fname_thin, index=None)
