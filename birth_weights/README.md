# Baby weight data

Data found via <https://rpubs.com/s2003493/Birthweight-Analysis>, and thence
<https://github.com/HwaiTengTeoh/Newborns-Weight-Prediction>.  From the
description there, source was
<https://www.kaggle.com/competitions/csci-ml-s19-pa1>, and data source is:

> Overview of data
>
> The Dataset used is collected by North Carolina State Center for Health
Statistics and we acknowledge The State Center for Health Statistics (SCHS)
and the Howard W. Odum Institute for Research in Social Science at UNC at
Chapel Hill as the source of data.

The files currently at <https://www.kaggle.com/competitions/csci-ml-s19-pa1>
differ somewhat from those in
<https://github.com/HwaiTengTeoh/Newborns-Weight-Prediction> - they appear to
have been updated in the Kaggle version.  For example, birth weight in the
Kaggle dataset is in a column `BWEIGHT` and appears to be in kilograms, whereas
birth weight in the Github repo is in fields `BPOUNDS` and `BOUNCES` (pounds
and ounces).  I've chosen the Github repository version for compatibility with
the description in the Github repo.

From [description of a similar or identical
dataset](https://gist.github.com/rakeshchada/7e480b2a8fe7ff7e8f16>) (with
matching column names, and very similar data description) the original data
source was
<https://dataverse.unc.edu/dataset.xhtml?persistentId=hdl:1902.29/10446> (now
"deaccessioned").

I (Matthew Brett) will assume the data was deaccessioned because there is
considerable identifying data there, and so I've stripped the data down to:

* `sex` : Sex of the baby
* `gestation_weeks` : Completed weeks of gestation.
* `mother_daily_cig_num` : Average number of cigarettes used daily (Mother).
* `mother_daily_drink_num`: Average number of drinks used daily (mother).
* `birth_weight` :  Baby's weight at birth in kilograms.

I (Matthew Brett) don't think any of the data here would qualify for copyright
under US law, as these are facts, and their arrangement is not creative. From
<https://en.wikipedia.org/wiki/Database_right>.
