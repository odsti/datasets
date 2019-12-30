# Analysis of current ET engineer listing vs dataset

* `et_engineering_crew.html` (not in repository) was an HTML-only download of
  <https://www.encyclopedia-titanica.org/titanic-engineering-crew> with "All"
  listed on one page.
* `check_engineers.py` analyzes the HTML in the page above, and extracts names,
  ages for all the engineers listed.  It writes out a text file of each name
  and age from the page. It then reads the processed data in
  ``../processed/titanic_stlearn.csv`` dataset and writes out the name and age
  of all "engineering crew" from those data.
* `et_stlearn_diff.csv` is a table harmonizing the names in the dataset and the
  names in the HTML page.  In 3 cases, the dataset has an alternative name for
  the same person.  For one person on the HTML page -- [Mr William John
  Murdock](https://www.encyclopedia-titanica.org/titanic-biography/william-murdock.html)
  -- there is no matching entry in the dataset.
* There are many other small variations of names and ages between the page and
  the dataset.
