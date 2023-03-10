# Relationship between SAT and GPA scores

The data here from an edited automated read of the data at
<https://zeescorrelationstudy.weebly.com>, by Zuleyma Zarate.

It is a record of students [SAT test](https://en.wikipedia.org/wiki/SAT) scores and their Grade Point Average (GPA).

From that page:

> ## What is a GPA?
>
> Your GPA is the average of all your grades In order to determine your GPA
you sum up your grades of each class using points and divide that number by
how many classes you have.
>
> * A = 4
> * B = 3
> * C = 2
> * D = 1
> * F = 0

Later in that page:

> I selected a random sample of 100 students from the Spring 2013 SAT Score
reports that I acquired from my college career counselor, Ms. Van Norden.

The page then presents the data in a table, as three PNG files.  You will also
find these PNG files in the `originals` subdirectory of this directory.

In fact, the table only contain 99 rows (students).

To generate the `processed/sat_gpa.csv` file, I (MB) uploaded the PNG files to
<https://extracttable.com>, downloaded the read CSV files, and edited them by
hand to fix some formatting and one missing row.

You will see from the web page above that a regression of SAT as a function of GPA gives:

* $y = 418.54x + 144.42$
* $R^2 = 0.616$
* $R = 0.785$.

There is no license given on the page, but I believe this qualifies as data
without creative rearrangement, and thus is not subject to US copyright.
