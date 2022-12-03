# Belief and serology in long Covid

The data here are from the paper:

Matta J, Wiernik E, Robineau O, et al. *Association of Self-reported COVID-19
Infection and SARS-CoV-2 Serology Test Results With Persistent Physical
Symptoms Among French Adults During the COVID-19 Pandemic*. JAMA Intern Med.
2022;182(1):19–25. doi:10.1001/jamainternmed.2021.6454

Here is the [link to the Matta et al
article](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2785832)
in JAMA.

There is no associated dataset, but I (MB) have copy-pasted data from the end
of eTable 4 in the supplementary material, to give the file
`original/matta_table_e4.csv`.

## About the study

The paper is an analysis of volunteers from the French CONSTANCES
population-based cohort study that:

> received ethical approval and included approximately 200 000 volunteers who
were aged 18 to 69 years between 2012 and 2019 and who consented to be followed
up through annual questionnaires and linked administrative databases.

Of these 200K volunteers, the authors invited a subset of 35,852 to participate
in the current study.  They first tried to get blood antibody data to find
which of the participants had had Covid.

> Between May and November 2020, self-sampling dried-blood spot kits were
mailed to each participant.

Notice that:

> The participants received their serology test results by mail or email.

The results of these tests are given in the output dataset in the "serology"
column, with "yes" for a positive Covid antibody test, and "no" otherwise.

They also asked the participants to say whether they *believed* that they had
been infected with Covid, and when.

> Between December 2020 and January 2021, the participants answered this
question from the fourth SAPRIS questionnaire: “Since March, do you think you
have been infected by the coronavirus (whether or not confirmed by a physician
or a test)?”.  Participants answered “Yes,” “No,” or “I don’t know.” At the
time they answered this question, the participants were aware of their serology
test results

The answers to this question are in the output dataset as the "belief" column,
with "yes" if they thought they had been infected, and "no" otherwise.

In the same December / January set of questionnaires, the researchers asked
about persistent symptoms associated with long-Covid, with the following
question:

> “Since March 2020, have you had any of the following symptoms that you did
not usually have before?”

Among the symptoms they asked about were sore muscles, fatigue, poor attention, and anosmia.

About 75% of the original invited cohort had data complete enough for further
analysis.

> Of 35,852 volunteers invited to participate in this cross-sectional analysis, a cohort of 26,823 (74.8%) with complete data for serologic testing and self-reported infection were included.

The authors also looked at the following information:

> Age, sex, educational level, income, and self-rated health in 2019 were
obtained from the inclusion questionnaire and the 2019 CONSTANCES
questionnaire.

As noted in the footnotes to eTable 4:

> Lower scores indicate better self-rated health.

The `health_2019` column in the output data table is the reconstructed 1-8
rating each participant gave for their health, as of 2019.  I (MB)
reconstructed this from eTable 4.  See `./process_long_covid.Rmd` for details.

26,620 of these 26,823 respondents had valid data for `health_2019`; I have
only included these participants in the output table.
