# Boston house prices - corrected

Here is a summary of the background for the dataset
<http://lib.stat.cmu.edu/datasets/boston>.

> The Boston house-price data of Harrison, D. and Rubinfeld, D.L. 'Hedonic
> prices and the demand for clean air', J. Environ. Economics & Management,
> vol.5, 81-102, 1978.   Used in Belsley, Kuh & Welsch, 'Regression
> diagnostics ...', Wiley, 1980.   N.B. Various transformations are used in
> the table on pages 244-261 of the latter.

Pages 244-261 of the Belsley *et al* book above are typscript listings of the
values in dataset.  From page page 245:

> The following are the data used for the analysis of Harrison and Rubinfield
(1978) Housing-Price equation treated in section 4.4 ...  We are grateful to
David Harrison and Daniel L. Rubinfield for making these data available.

The rows in the dataset are each "towns", or, more accurately, *census tracts*,
within the Boston [Standard Metropolitan Statistical
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
  (`B` above) but the result of the given, rather obscure calculation on `B`.  See below for more discussion.
* `lower_stat_pct`: Percentage of population that is lower status: 1/2
  * (proportion of adults without some high school education and proportion of
    male workers classified as laborers).

## The `black_index` variable is odd, and probably wrong.

See [this commentary on data for the "black_index"
variable](https://medium.com/@docintangible/racist-data-destruction-113e3eff54a8)
for more detail, and links to the original 1970 census data.  The formula
$1000(B - 0.63)^2$  is not in the column descriptions of original paper, which
records the column as being "Black proportion of population", although their
suggested model does use $(B - 0.63)^2$ as a transformation.   The formula does
appear as the explanation for the variable in the column descriptions of the
Belsley *et al* book cited above (p. 231).

It may be possible to reconstruct the actual *proportions* `B` from the
[original census
data](https://www2.census.gov/library/publications/decennial/1970/phc-1/39204513p3ch05.pdf),
combined with the `census_tract` values here.  But, a quick check from those
figures does not match what we have here.  Consider the first row, for
"Nahant", census tract number 2011.  The 1970 census document above lists 0.3
"Percent Negro" (sic). The formula above gives 393.129 for 0.3, but the table
(and the Belsley original) has 396.90.  Likewise for the two following rows for
"Swampscott", census tract numbers 2021, 2022; 1970 census "Percent negro"
values are 0.1, 0.5; calculated `black_index` values are: 395.641, 390.625;
recorded values are 396.90, 392.83.  The Belsley *et al* book lists the
correspondence of observation numbers to town name (Exhibit 4.21 p. 230), and
these match the names in the original Belsley listing, and the data here.  The
recorded census tracts of 2011, 2021, 2022 are [still
correct](http://www2.census.gov/geo/maps/dc10map/tract/st25_ma/c25009_essex/DC10CT_C25009_003.pdf)
for Nahant and Swampscott.  It seems that the data in the original Belsley *et
al* table and stored in the data frame here, do not correspond to the values in
the 1970 census.
