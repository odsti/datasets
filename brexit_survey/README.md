# The Brexit survey

These data are from the 2016 Hansard Survey.  The survey was soon after the
Brexit referendum.

Every year, the [Hansard
Society](https://www.hansardsociety.org.uk/research/audit-of-political-engagement)
sponsors a survey on political engagement in the UK.

They put topical questions in each survey.  For the 2016 / 7 survey, they asked
about how people voted in the Brexit referendum.

Luckily, they make the data freely available online for us to analyze.

You can get the data for yourself from the UK Data Service:
[https://discover.ukdataservice.ac.uk/catalogue/?sn=8183](https://discover.ukdataservice.ac.uk/catalogue/?sn=8183).
There are data files in various formats, including:

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
to same columns, with more memorable names, and cleans up some invalid values.
