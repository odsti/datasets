# Galton's data on heights

This are the `Galton` and `GaltonFamlies` data frames from the [HistData
R package](https://www.rdocumentation.org/packages/HistData).

The data are those that [Francis
Galton](https://en.wikipedia.org/wiki/Francis_Galton) used for the following
paper:

Galton, F. (1886). [Regression Towards Mediocrity in Hereditary Stature](
https://galton.org/essays/1880-1889/galton-1886-jaigi-regression-stature.pdf)
Journal of the Anthropological Institute, 15, 246-263

I believe the actual data here come from [James
Hanley's](http://www.medicine.mcgill.ca/epidemiology/hanley/) transcription of
[Galton's original
notebooks](http://www.medicine.mcgill.ca/epidemiology/hanley/galton/notebook/index.html),
with with the deliberately omitted entries filled in.

See also [Hanley's page on the same
data](http://www.medicine.mcgill.ca/epidemiology/hanley/galton).

Although the original R HistData package has a GPL license, I (Matthew Brett)
don't think any of the data here would qualify for copyright under US law, as
these are facts, and their arrangement does not seem creative. From
<https://en.wikipedia.org/wiki/Database_right>:

The `galton_combined.csv` data frame has 934 rows, with one row per child.
The children belong to 205 unique families.  All heights are in inches.

* `family`: family identifier, a string giving identifiers in Galton's
  notebook.  These are string representations of numbers from `001` through
  `204`. One family has identifier `136A`.
* `father`: father's height in inches.
* `mother`: mother's height in inches.
* `midparentHeight`: Adjusted average of parents' heights, calculated from
  formula `father + 1.08 * mother) / 2`.
* `children`: number of children in this family.
* `childNum`: identifying number of child within this family.  Boys listed
  before girls, boys then girls listed in decreasing height order.
* `gender`: gender of child, `"male"` or `"female"`.
* `childHeight`: height of child in inches.

Hanley's paper on these data says, of the Galton's notebook entries:

> The  entire  “listing”  contains  entries  for  963  children  (486, sons, 476
daughters) from 205 families ranging in size from 1 to 15 children. Some 934
children had numerical values (35 were recorded as “about x.0inches”). In 26
others (21 female, 5 male) height  was  described  verbally  (“tallish,”
“middle,”  etc.) ...

James A. Hanley (2004) ["Transmuting" Women into Men: Galton's Family Data on
Human Stature](https://www.jstor.org/stable/27643564) The American Statistician
Vol. 58, No. 3 (Aug., 2004), pp. 237-243.  There is [another copy of the paper
here]](http://www.medicine.mcgill.ca/epidemiology/hanley/Reprints/Hanley_Article_Galton_Data.pdf).

The `galton_heights.csv` data appear to be transcription of the data from Table
I of Galton's 1886 paper.  As Hanley's "Transmuting" paper discusses, it is
rather hard to work out how the 928 children from that table correspond to the
original data.

Columns in `galton_heights.csv` are:

* `parent`: mid-parent height in inches, from formula for `midparentHeight`
  above.
* `child`: child's height in inches, where female children's heights have been
  multiplied by 1.08.

The `child` height values all end in `.2` or `.7` .  For example, the first two
unique heights are `61.7` and `62.2`.  This is because of the bins that Galton
used in his Table I.  He explains in the caption:

> The reason why the headings run 62.2% 63.2% &c., instead of 62.5, 63.5, &c.,
is that the observations are unequally distributed between 62 and 63, 63 and
64, &c., there being a strong bias in favour of integral inches.

It's easiest to see what this means by looking at [Galton's Table
I](https://galton.org/essays/1880-1889/galton-1886-jaigi-regression-stature.pdf).

`galton_children.csv` contains one row per child, where the data refers only to the child (not to the parents).  The data comes from the `galton_combined.csv` data frame. Specifically, the variables are:

* `child_number`: identifying number of child within this family (see
  `childNum` above).
* `gender`: gender of child, `"male"` or `"female"`.
* `height`: height of child in inches (`childHeight` above)
* `family`: family identifier, as above.

`galton_families.csv` data also come from `galton_combined.csv` above.  The
table contains one row per family, where the data refer only to the family.

Variables:

* `family`: family identifier, as above.
* `father`: father's height in inches.
* `mother`: mother's height in inches.
