# Boston house prices - corrected

Here is a summary of the background for the dataset
<http://lib.stat.cmu.edu/datasets/boston>.

> The Boston house-price data of Harrison, D. and Rubinfeld, D.L. 'Hedonic
> prices and the demand for clean air', J. Environ. Economics & Management,
> vol.5, 81-102, 1978.   Used in Belsley, Kuh & Welsch, 'Regression
> diagnostics ...', Wiley, 1980.   N.B. Various transformations are used in
> the table on pages 244-261 of the latter.

The rows are each "towns", or, more accurately, census tracts, within the
Boston [Standard Metropolitan Statistical
Area](https://en.wikipedia.org/wiki/Metropolitan_statistical_area) (SMSA) in
Massachusetts.  The "towns" are therefore districts within the greater Boston
area.

For each town there are a series of average measurements and estimates for
housing and other environmental factors.  The measurements and estimates are
from 1970.

Controversially, there is also a measure relating to the proportion of Black
residents in each town.

The original file in `original/boston_corrected.txt` comes from
<http://lib.stat.cmu.edu/datasets/boston_corrected.txt>.

As noted in that file:

> This file contains the Harrison and Rubinfeld (1978) data corrected for
> a few minor errors and augmented with the latitude and longitude of the
> observations.

The file gives these references for the corrections:

> Gilley, O.W., and R. Kelley Pace, "On the Harrison and Rubinfeld Data",
Journal of Environmental Economics and Management, 31 (1996), 403-405.
Provided corrections and examined censoring.
>
> Pace, R. Kelley, and O.W. Gilley, "Using the Spatial Configuration of the
Data to Improve Estimation",  Journal of the Real Estate Finance and Economics
14 (1997), 333-340. Added georeferencing and spatial estimation.

[Gilley and Kelley (1996)](http://www.spatial-statistics.com/pace_manuscripts/jeem_ms_dir/pdf/fin_jeem.pdf) give details of the corrections.

The variables in the `processed/boston_corrected.csv` file are:

* `town`: Town name
* `town_no`: Town number (appears to be arbitrary)
* `census_tract`: census tract number.
* `longitude`
* `latitude`
* `median_home_value`:  Corrected estimated median value of owner-occupied
  homes in units of 1K USD.
* `crime_rate`: per capita crime rate by town
* `zoned_25k_p`: Proportion of a town's residential land zoned for lots
  greater than 25,000 square feet.
* `indust_p`: proportion of non-retail business acres per town
* `borders_charles`: Charles River dummy variable (= 1 if tract bounds river;
  0 otherwise)
* `NOx`: nitric oxides concentration (parts per 10 million)
* `n_rooms_avg`: average number of rooms in owner units.
* `before_1940_p`: proportion of owner-occupied units built prior to 1940
* `employ_dist`: weighted distances to five Boston employment centres
* `radial_access`: index of accessibility to radial highways
* `tax_rate`: full-value property-tax rate per \$10,000
* `pupil_teacher_ratio`: pupil-teacher ratio by town
* `black_index`: $1000(B - 0.63)^2$ where `B` is the proportion of Black
  residents by town.  Notice this is *not* the proportion of Black residents,
  (`B` above) but the result of the given, rather obscure calculation on `B`.
  See [this commentary on data for the "black_index"
  variable](https://medium.com/@docintangible/racist-data-destruction-113e3eff54a8)
  for more detail, and links to the original 1970 census data.
* `lower_stat_pct`: Percentage of population that is lower status: 1/2
  * (proportion of adults without some high school education and proportion of
  male workers classified as laborers).

See [this commentary on data for the "black_index"
variable](https://medium.com/@docintangible/racist-data-destruction-113e3eff54a8)
for more detail on the rather obscure meaning of this column.
