# Data for passengers and crew of RMS Titanic

From <https://cran.r-project.org/package=stablelearner>

Imported from R with:

```r
install.packages('stablelearner')
data("titanic", package = "stablelearner")
write.csv(titanic, 'titanic_stablelearner.csv', row.names=FALSE)
```

on 24 December 2019.

The output data is in `processed/titanic_stlearn.csv`.  It is barely processed
from the R dataset as above - see `process_titanic.py`.  The single change is
recoding the `embarked` field from "B", "C", "Q", "S" to "Belfast",
"Cherbourg", "Queenstown", "Southampton".


## Data dictionary

This description largely derives from
<https://rdrr.io/cran/stablelearner/man/titanic.html>, but applies to the
processed data in `processed/titanic_stlearn.csv`.

* `name`: a string with the name of the passenger.
* `gender`: a string with one of two labels: "male" and "female".
* `age`: a numeric value with the person's age on the day of the sinking. The
  age of babies (under 12 months) is given as a fraction of one year, rounded
  to the nearest month (2 months = 2/12 = 0.1667).
* `class`: a string specifying the class for passengers: "1st", "2nd", "3rd";
  or the type of service aboard for crew members. See below for discussion of
  passengers, crew and the crew service types.
* `embarked`: a string with the person's port of embarkation, one of:
  "Belfast", "Cherbourg", "Queenstown" or "Southampton".
* `country`: a string with the person's home country.
* `ticketno`: a numeric value specifying the persons ticket number (NA for crew
  members, also see below).
* `fare`: a numeric value with the ticket price (NA for crew members, musicians
  and employees of the shipyard company, also see below).
* `sibsp`: an integer specifying the number of siblings/spouses aboard; adopted
  from Vanderbilt data set (see below).  Always NA for crew, sometimes NA for
  passengers.
* `parch`: an ordered factor specifying the number of parents/children aboard;
  adopted from Vanderbilt data set (see below).  Always NA for crew, sometimes
  NA for passengers.
* `survived`: a string with one of two labels: "no" and "yes". It specifies
  whether the person survived the sinking.

### Source (from Stablelearner link above)

The complete list of persons on the RMS Titanic was downloaded from
<http://www.encyclopedia-titanica.org> on April 5, 2016. The information given
in `sibsp` and `parch` was adopted from a data set obtained from
<http://biostat.mc.vanderbilt.edu/DataSets>.

### Details

The main source of these data, [Encylopedia
Titanica](http://www.encyclopedia-titanica.org) (ET), contains much information
about Titanic's passengers and crew.

The [ET passenger
list](https://www.encyclopedia-titanica.org/titanic-passenger-lists) lists 324
First Class passengers, 285 Second Class and 708 Third Class, for a total of
1317 passengers. People listed as passengers include the [8
musicians](https://en.wikipedia.org/wiki/Musicians_of_the_RMS_Titanic) and the
[9 members of the Guarantee
Group](https://en.wikipedia.org/wiki/Crew_of_the_RMS_Titanic#Guarantee_group)
who stayed on the ship for the journey across the Atlantic. The Guarantee Group
were a team of employees of the shipbuilding company, [Harland and
Wolff](https://en.wikipedia.org/wiki/Harland_and_Wolff), including the ship's
designer, [Thomas Andrews](https://en.wikipedia.org/wiki/Thomas_Andrews). Their
job was to monitor the ship's performance and fix any problems that might
arise. Unfortunately, the biggest problem that did arise proved too difficult
to fix. The musicians and the Guarantee Group have missing values for their
ticket price (`fare`), as do the rest of the crew, and one other passenger.

See the [ET crew
lists](https://www.encyclopedia-titanica.org/titanic-crew-lists) for the
following numbers of crew in different categories:

* 66 deck crew (including officers).
* 325 engineers and engineering crew.
* 431 victualling crew (including - in this list - 5 postal clerks).
* 69 restaurant staff.

This gives a total of 891 crew members listed at ET.

The dataset here only has 324 engineers / engineering crew, so the total number
of crew in this data set is one less, at 890.

Also see the [table from Lord Merey's
report](https://www.titanicinquiry.org/BOTInq/BOTReport/botRepSaved.php) for
tabulations of lost and saved.  These numbers differ slightly from those you
can calculate from the dataset here.

For discussion of the `sibsp` and `parch` variables, see the [information file
on the Vanderbuilt
website](http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic3info.txt),
archived here, along with the matching `titanic3.csv` data file - see
`vanderbilt/README.md`.
