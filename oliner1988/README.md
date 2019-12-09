# Data tables from Oliner and Oliner 1988

This dataset is a series of tables from the book:

Samuel P. Oliner and Pearl M. Oliner (1992) "The Altruistic Personality:
Rescuers of Jews in Nazi Europe". Free Press, New York. ISBN 0-02923829-3.

[Google books preview of Oliner
1988](https://books.google.co.uk/books?id=UctNcoCtxrIC).

The book has many analyses of interview and questionnaire data from a group of "rescuers" and a control "non-rescuer" group.

"Rescuers" were people for whom there was strong documentary evidence that they
had sheltered Jews in Europe during the Second World War.   Their primary
source in finding rescuers was the [Yad Vashem list of Righteous
Gentiles](https://www.yadvashem.org/righteous.html).  [Criteria for being added to this list are](https://www.yadvashem.org/righteous/faq.html):

> #. Active involvement of the rescuer in saving one or several Jews from the
>    threat of death or deportation to death camps
> #. Risk to the rescuer’s life, liberty or position
> #. The initial motivation being the intention to help persecuted Jews: i.e.
>    not for payment or any other reward such as religious conversion of the saved
>    person, adoption of a child, etc.
> #. The existence of testimony of those who were helped or at least
>    unequivocal documentation establishing the nature of the rescue and its
>    circumstances.

At the time of writing the book, Yad Vashem's list had around 6000 rescuers.
The authors made a selection from this list with the criteria that rescuers
were "geographically accessible and that they come from a number of different
countries" (p. 263). 95% of their rescuers came from this list, but a further
5% "consists of persons whose names we obtained rescued survivors also
interviewed by our project.  In selecting the latter group we were also guided
by the same criteria that characterize the Yad Vashem rescuers ..." (p. 262).

This procedure found 406 rescuers, of which they identified 175 before the main
project began, leaving 231 rescuers with detailed data from coded interviews
using a standard questionnaire. The statistical tables here only refer to the
231 rescuers with detailed coded questionnaire data.

The "non-rescuer" control group were 126 persons "neither on Yad Vashem's list
nor verified by our project as an authenticated rescuer living in Nazi-occupied
Europe during the war.  Ideally, this group ... should have been a random
sample from the universe of non-rescuers --- practical reality made this
impossible.  We chose instead to try and obtain a matched sample of nonrescuers
-- matched with rescuers on age, sex, education, and geographic location during
the years of the war. We were successful in matching our sample in the sense
that there are no statistically significant differences between rescuers and
nonrescuers in relations to all the above variables with the exception of age.
The mean average age of rescuers is four years older than that of nonrescuers.
We addressed this issue by holding age constant in our statistical analysis
through a process called analysis of covariance." (pp. 263-4).  The
non-rescuers had interviews using the same questionnaire as the 231 rescuers
above.

One of the questions for the non-rescuers was "Did you do anything out of the
ordinary during the war to help other people or resist the Nazis" (Q E9a, p.
343).

It turned out that 53 of the 126 non-rescuers claimed to have been members of
general resistance groups, or to have helped Jews, or both.  The authors
classed these 53 non-rescuers as "actives".  They termed the remaining 73
non-rescuers as "bystanders".

Many of the tables compare rescuers to non-rescuers.  The non-rescuers in these
tables include the "actives".  There are usually matching tables comparing
rescuers to the "bystanders"; this is the non-rescuer group but not including
the "actives".  Thus the "non-rescuer" and "bystander" groups both include the
"bystanders".

The file `oliner1988tables.pdf` contains scans of a subset of the data tables
at the end of the book.   `oliner1988chap6footnote11.pdf` has a scan of
footnote 11 for chapter 6, referred to in footnote *a* of Table 6.8.

All tables in this directory have values transcribed from the tables in the
PDF.  These are in percentages of each category "rescuers", "nonrescuers", "bystanders", with the first row being the total number in each category.

`process_oliner.py` converts these values into counts in each category
"rescuers", "actives", "bystanders", with the last row having overall counts in
each category.  The resulting tables are in the `processed` directory.

Output tables are:

* `oliner_tab6_5mother.csv`: answers to question B19 "Was your mother very
  religious, somewhat religious, not very religious or not at all religious?".
* `oliner_tab6_5father.csv`: answers to question B29 "Was your father very
  religious, somewhat religious, not very religious or not religious at all?" (slight difference in phrasing between B19 and B29 in original).
* `oliner_tab6_6.csv`: answers to question D14 "Before the war, were you very
  religious, somewhat religious, not very religious or not at all religious?".
* `oliner_tab6_7.csv`: values conveyed by person's most influential role-model.
  Respondents first answered question B1 (p. 333): "... who was the *one*
  person who had the *most influence* on you when you were growing up?   That
  is, who taught you the most about life?".  Question B12 was "What were the
  most important things you learned about life from [this role model]?".  The
  row labels in table 6.7 of Oliner (1988), and here, are responses to B12,
  recoded into categories.  Respondents could name more than one value, and
  therefore, score on more than one category.
* `oliner_tab_6_8a_1.csv` records the answers to question D15 "Did you belong
  to a political party before the war?".
* `oliner_tab_6_8a_2.csv` has coded answers to the free-form question D15a
  "What party did you belong to?".  The interviewer asked this question only if
  the respondent answered "yes" to question D15.  Of course, the available
  political parties differed for each nationality, such as German, Dutch,
  Polish.  The authors recoded the party names into categories "economic left"
  vs not, "democratic" vs not, "tolerant of minorities" vs not, and "tolerant
  of Jews" or not, based on the authors' historical assessment of these
  parties.  See `oliner1988chap6footnote11.pdf` for the names of parties
  classified as "economic left" and "democratic". Five of eight "economic left"
  parties also qualified as "democratic".
