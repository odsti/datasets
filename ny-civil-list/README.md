# New York civil list police exam scores

The files here from the New York City Civil List active Civil list.

See [the NYC open data
page](https://data.cityofnewyork.us/City-Government/Civil-Service-List-Active-/vx8i-nprf) for details.

From that page:

> A Civil Service List consists of all candidates who passed an exam,
> ranked in score order. An established list is considered active for
> no less than one year and no more than four years from the date of
> establishment. For more information visit DCAS’ "Work for the City"
> webpage at:
> https://www1.nyc.gov/site/dcas/employment/take-an-exam.page

These data are as I retrieved them on 10 April 2020.  To preserve their exact state, I put the files on Figshare:

* [data file on
  Figshare](https://figshare.com/articles/NYC_Civil_List_Active_as_of_2020-04-10/12115383)
* [metadata on
  Figshare](https://figshare.com/articles/NYC_Civil_List_Active_metadata_as_of_2020-04-10/12115548)

The `proc_nyc_list` notebook fetches the files from Figshare.

The notebook selects the exam scores for all candidates taking the
open [Police Officer written
exam](https://www1.nyc.gov/site/nypd/careers/police-officers/po-exam.page),
for two iterations of the exam:

* Exam number 7323, for which results were published on
  27th September 2017.  There are 10987 people with marks recorded for
  this exam.
* Exam 8339, results published on 27th February 2019;  13819 people.

There is one processed file for each these two exams, with columns:

* `First Name`: A candidate’s first name as it appears on their
  application.
* `MI`: A candidate’s middle initial (MI) as it appears on their
  application.
* `Last Name`: A candidate’s last name as it appears on their
  application.
* `Adj. FA`: The Adjusted Final Average (“Adj. FA” or “AFA”) is an
  eligible candidate’s test score in addition to any additional
  credits granted.
