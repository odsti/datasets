# Duncan data for occupations and prestige

See `./original/README.md` for the original data source.  It's tutorial data from John Fox's textbook [Applied Regression Analysis and Generalized Linear Models](https://us.sagepub.com/en-us/nam/applied-regression-analysis-and-generalized-linear-models/book237254).

The dataset combines information from the 1950 U.S. Census with data collected
by the National Opinion Research Centre (NORC). The Census data contained
information about different occupations, such as the percentage of people
working in that occupation who earned over a certain amount per year. The NORC
data was from a survey which asked participants to rate how prestigious they
considered each occupation. Here are the descriptions of the variables in the
dataset, which covers 45 occupations (adapted from [here](https://rdrr.io/cran/carData/man/Duncan.html)):

* `name` - the name of the occupation, from the 1950 US Census
* `type`- type of occupation, with the following categories ``prof``,
  professional and managerial; ``wc``, white-collar; ``bc``, blue-collar. (E.g.
  how the occupation was classified in the 1950 US Census)
* `income` - percentage of census respondents within the occupation who earned
  3,500 dollars or more per year (about 36,000 US dollars in 2017)
* `education` - percentage of census respondents within the occupation who were
  high school graduates 
* `prestige` - percentage of respondents in the NORC survey who rated the
  occupation as “good” or better in prestige.
