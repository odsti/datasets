# Sheffield diet data set

Sheffield University has a nice website with example
datasets at
<https://www.sheffield.ac.uk/mash/statistics/datasets>

The links appear to be down as of 1 July 2023, but you
can find some of them via <https://web.archive.org>,
and you can find the data files in the `./original`
subdirectory.

This is their diet dataset, from
<https://www.sheffield.ac.uk/polopoly_fs/1.937196!/file/Diet_SPSS.sav>.

The only information we have is from the dataset webpage, duplicated in the
data dictionary document (below):

> This data set contains information on 78 people using one of three diets.

We process the SPSS version of the file because it the data differs from the
R / csv version of the file via the same page, and the SPSS version corresponds
to the given [data
dictionary](https://www.sheffield.ac.uk/polopoly_fs/1.937194!/file/Diet_data_description.docx).

Here is the data dictionary from that link above:

| Variable       |  Explanation                          |
| -------------- | ------------------------------------- |
| Person         |  Participant number                   |
| gender         |  Gender, 1 = male, 0 = female         |
| Age            |  Age (years)                          |
| Height         |  Height (cm)                          |
| preweight      |  Weight before the diet (kg)          |
| Diet           |  Diet                                 |
| weight10weeks  |  Weight after 10 weeks (kg)           |
| weightLOST     |  Weight lost after 10 weeks (kg)      |

The LICENSE attached to the data dictionary document is CC-by-NC-SA. I can't
see a version there, but say [CC-by-NC-SA
3](https://creativecommons.org/licenses/by-nc-sa/3.0).  The document records
the data as:

> contributed by Ellen Marshall, University of Sheffield
