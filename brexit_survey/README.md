# The Brexit survey

These data are from the 2016 Hansard Survey.  The survey was soon after the
Brexit referendum.

Every year, the [Hansard
Society](https://www.hansardsociety.org.uk/research/audit-of-political-engagement)
sponsors a survey on political engagement in the UK.

They put topical questions in each survey.  For the 2016 / 7 survey, they asked
about how people voted in the Brexit referendum.

Luckily, they make the data freely available online for us to analyze.

You can get the original data for yourself from the [UK Data Service, dataset
8183](https://discover.ukdataservice.ac.uk/catalogue/?sn=8183).

The main (details) page there records the data as "open":

> Open data – Researchers can access open datasets without any registration.
Some may be subject to an Open Government Licence (OGL) or a Creative Commons
Licence (CC).

The [citation
page](https://doc.ukdataservice.ac.uk/doc/8183/mrdoc/UKDA/UKDA_Study_8183_Information.htm) has:

> All works which use or refer to these materials should acknowledge these
sources by means of data citation. To ensure that such source attributions are
captured for citation indexes, citations must appear in footnotes or in the
reference section of publications. The citation for this data collection is:
>
> Hansard Society. Parliament and Government Programme. (2017). Audit of
Political Engagement 14, 2017. [data collection]. UK Data Service. SN: 8183,
http://doi.org/10.5255/UKDA-SN-8183-1

The UK Data Service has data files in various formats, including:

* SPSS format (for the SPSS statistical package);
* Stata format (for the Stata statistical package);
* tab-delimited (a general data format, that can be used with Pandas, Excel,
  and other packages).

The data is in a standard form, with one row per respondent, and one column
per question.

The `original` directory has an unchanged copy of the tab-delimited version of
the data file. The directory also has a copy of the document describing the
questions they ask and the way that they have recorded the answers in the data
file.  This is often called the “data dictionary”.  It was originally in Rich
Text Format, but we have converted to PDF for convenience.  It is otherwise
identical to the file you will find at the UK Data Service.

The `./process_brexit.py` file converts the file to `.csv` format, restricts
to two columns, with more memorable names, and cleans up some invalid values.

In particular the processed dataset has the following columns:

*   `brexit_vote`: respondents' report of their vote in the Brexit referendum.
     Result is categorical with any of these values:
    *  "Remain"
    *  "Leave"
    *  "Did not vote"
    *  "Too young"
    *  "Can't remember"
    *  "Refused"
*   `age`: age in years.
