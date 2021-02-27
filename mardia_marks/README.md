# Students scores from Mardia 1979

Data from R package <https://www.rdocumentation.org/packages/bnlearn>, and
specifically, <https://www.rdocumentation.org/packages/bnlearn/topics/marks>.

Noted as being from "Mardia (1979)":

> Mardia, Kantilal Vardichand, Kent, John. T., Bibby, John M. (1979).
> *Multivariate Analysis*. United Kingdom: Academic Press.

You can find some previews at
<https://www.google.co.uk/books/edition/_/bxjvAAAAMAAJ>.  A search for
`mechanics` gives a preview with the top three rows of these data listed on
page 1.

It wasn't clear to me what the suggested data license was.  The R package is
under the usual GPL (>= 2).

At the time of writing, someone has a copy of the book at
<https://statisticalsupportandresearch.files.wordpress.com/2017/06/k-v-mardia-j-t-kent-j-m-bibby-multivariate-analysis-probability-and-mathematical-statistics-academic-press-inc-1979.pdf>.

The data come from table 1.2.1 of the book.  There is little information about
the data except for:

> ... performance on different papers taken by the same students.

The table heading for the table 1.2.1 has:

> Marks in open-book and closed-book examinations out of 100

"O" and "C" below refer to Open-book and Closed-book respectively.

The variable headings for the table are:

1. "Mechanics (C)" - `MECH` in the data file.
2. "Vectors (C)" - `VECT`
3. "Algebra (O)" - `ALG`
4. "Analysis (O)" - `ANL` (mercifully)
5. "Statistics (O)" - `STAT`.
