# Data for Machiavellianism test

Data from <https://openpsychometrics.org/_rawdata>, and specifically
<http://openpsychometrics.org/_rawdata/MACH_data.zip>, as of 3rd June 2020.

See the files in `original` for the raw data.

Thanks to the "mach4" team from one of my courses for pointing me to this
interesting dataset.

## Data dictionary

I modified the text starting at the next sentence, to the end of this page,
from the original `original/codebook.txt`.

This data was collected using an online version of the MACH-IV developed by
Richard Christie and Florence L. Geis. See Christie, R. & Geis, F. (1970)
"Studies in Machiavellianism". NY: Academic Press.

Data collection took place July 2017 - March 2019.

The main body of the consisted of 20 questions. The text of those questions is
below.

* Q1 : "Never tell anyone the real reason you did something unless it is useful
  to do so."
* Q2 : "The best way to handle people is to tell them what they want to hear."
* Q3 : "One should take action only when sure it is morally right."
* Q4 : "Most people are basically good and kind."
* Q5 : "It is safest to assume that all people have a vicious streak and it
  will come out when they are given a chance."
* Q6 : "Honesty is the best policy in all cases."
* Q7 : "There is no excuse for lying to someone else."
* Q8 : "Generally speaking, people won't work hard unless they're forced to do
  so."
* Q9 : "All in all, it is better to be humble and honest than to be important
  and dishonest."
* Q10 : "When you ask someone to do something for you, it is best to give the
  real reasons for wanting it rather than giving reasons which carry more
  weight."
* Q11 : "Most people who get ahead in the world lead clean, moral lives."
* Q12 : "Anyone who completely trusts anyone else is asking for trouble."
* Q13 : "The biggest difference between most criminals and other people is that
  the criminals are stupid enough to get caught."
* Q14 : "Most people are brave."
* Q15 : "It is wise to flatter important people."
* Q16 : "It is possible to be good in all respects."
* Q17 : "P.T. Barnum was wrong when he said that there's a sucker born every
  minute."
* Q18 : "It is hard to get ahead without cutting corners here and there."
* Q19 : "People suffering from incurable diseases should have the choice of
  being put painlessly to death."
* Q20 : "Most people forget more easily the death of their parents than the
  loss of their property."

The questions were presented one at a time in a random order. Users responded
to each item on a five point scale: 1=Disagree, 2=Slightly disagree, 3=Neutral,
4=Slightly agree, 5=Agree.

Three values are recorded for each question. e.g.

* Q1A - the user's Answer.
* Q1I - the position (Index) of that item in the survey, where 1 means item
  presented first. These questions always start the survey, so the index
  numbers range from 1 to 20.
* Q1E - the time spent (Elapsed) on that question in milliseconds.

After the test body, users were asked if they would be willing to complete an
additional research survey. This data only includes those who agreed to.

The optional survey included a variety of questions:

The Ten Item Personality Inventory was administered (see Gosling, S. D.,
Rentfrow, P. J., & Swann, W. B., Jr. (2003). A Very Brief Measure of the Big
Five Personality Domains. Journal of Research in Personality, 37, 504-528.):

* TIPI1 - Extraverted, enthusiastic.
* TIPI2 - Critical, quarrelsome.
* TIPI3 - Dependable, self-disciplined.
* TIPI4 - Anxious, easily upset.
* TIPI5 - Open to new experiences, complex.
* TIPI6 - Reserved, quiet.
* TIPI7 - Sympathetic, warm.
* TIPI8 - Disorganized, careless.
* TIPI9 - Calm, emotionally stable.
* TIPI10 - Conventional, uncreative.

The TIPI items were rated "I see myself as:" `_____` such that

* 1 = Disagree strongly
* 2 = Disagree moderately
* 3 = Disagree a little
* 4 = Neither agree nor disagree
* 5 = Agree a little
* 6 = Agree moderately
* 7 = Agree strongly


The following items were presented as a check-list and subjects were instructed
"In the grid below, check all the words whose definitions you are sure you
know":

* VCL1 - boat
* VCL2 - incoherent
* VCL3 - pallid
* VCL4 - robot
* VCL5 - audible
* VCL6 - cuivocal
* VCL7 - paucity
* VCL8 - epistemology
* VCL9 - florted
* VCL10 - decide
* VCL11 - pastiche
* VCL12 - verdid
* VCL13 - abysmal
* VCL14 - lucid
* VCL15 - betray
* VCL16 - funny

A value of 1 is checked, 0 means unchecked. The words at VCL6, VCL9, and VCL12
are not real words and can be used as a validity check.

A bunch more questions were then asked.

In the following, unless otherwise specified, I have recoded an original value
of 0 as missing in the processed table.

* education - "How much education have you completed?", 1=Less than high
  school, 2=High school, 3=University degree, 4=Graduate degree.
* urban - "What type of area did you live when you were a child?", "Rural"
  (countryside), "Suburban", "Urban" (town, city).
* gender - "What is your gender?", "Male", "Female", "Other".
* engnat - "Is English your native language?", "Yes", "No"
* age - "How many years old are you?".  In processing, answers > 110 set to
  missing.
* hand - "What hand do you use to write with?", "Right", "Left", "Both".
* religion - "What is your religion?"", "Agnostic", "Atheist", "Buddhist,
  "Christian (Catholic)", "Christian (Mormon)", "Christian (Protestant),
  "Christian (Other)", "Hindu", "Jewish", "Muslim", "Sikh", "Other".
* orientation - "What is your sexual orientation?"", "Heterosexual", "Bisexual,
  "Homosexual", "Asexual", "Other".
* race - "What is your race?"", "Asian", "Arab", "Black", "Indigenous
  Australian", "Native American", "White", "Other".
* voted - "Have you voted in a national election in the past year?"", "Yes,
  "No".
* married - "What is your marital status?"", "Never married", "Currently
  married", "Previously married".
* familysize - "Including you, how many children did your mother have?".  In
  processing, values of 0 or > 40 set to missing.
* major - "If you attended a university, what was your major (e.g.
  "psychology", "English", "civil engineering")?"

The following values were calculated by the server:

* country - the user's network location
* screenw - width of user's device in pixels
* screenh - width of user's device in pixels

The time spent on each page was recorded in seconds:

* introelapse
* testelapse
* surveyelapse
