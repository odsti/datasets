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
