# Race and wages

This directory contains a data set derived from the paper:

Neal, D. A., & Johnson, W. R. (1996). [The role of premarket factors in
black-white wage
differences](https://www.ssc.wisc.edu/~gwallace/Papers/Neal%20and%20Johnson%20%281996%29.pdf).
Journal of political Economy, 104(5), 869-895.

Many thanks to Professor Derek Neal, who was very helpful in providing the Stata script to recreate the data and analysis, and an original data file to compare against.

See `./process_rage_wages.Rmd` for a notebook replicating the data analysis,
from data downloaded from the source, the [National Longditudinal Survey
site](https://www.nlsinfo.org/content/access-data-investigator).

The [data is public domain](https://www.bls.gov/bls/linksite.htm):

> Copyright
>
> The Bureau of Labor Statistics (BLS) is a Federal government agency and everything that we publish, both in hard copy and electronically, is in the public domain, except for previously copyrighted photographs and illustrations. You are free to use our public domain material without specific permission, although we do ask that you cite the Bureau of Labor Statistics as the source.

The Python notebook is copyright Matthew Brett; I (MB) release that code as
[CC-0](https://creativecommons.org/share-your-work/public-domain/cc0/).
Professor Derek Neal is the author of the `RECREATE.DO` file in `original`; he
releases the file into the public domain.

The `race_wages.do` file replicates the analyses in `RECREATE.DO` using the
processed `processed/race_wages.csv` file and Stata.  It is based on
`RECREATE.DO` and is also public domain.
