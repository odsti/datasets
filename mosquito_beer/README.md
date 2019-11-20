# Mosquitoes and beer data

These are the data from [Beer Consumption Increases Human Attractiveness to Malaria Mosquitoes](https://doi.org/10.1371/journal.pone.0009546).

The first author, Dr [Thierry Lefèvre](https://sites.google.com/site/thierryelefevre), kindly sent the original data.

He released the data and derivatives under the [CC-BY](https://creativecommons.org/licenses/by/4.0) license.  Specifically, you should attribute any copies of these data to Dr Thierry Lefèvre, and reference the paper above.

The processed data are in `processed/mosquito_beer.csv`.

Variables in that file are:

* `volunteer`: 43 levels corresponding to the id of the 43
  volunteers.
* `group`: 2 levels "beer" or "water" (= volunteers were
  assigned to either the beer (volunteer 1 to 25) or the water
  treatment (volunteer 26 to 43).
* `test`: 2 levels "after" or "before"  (the attractiveness of
  each volunteer was tested twice: before drinking and 15 min
  after drinking either water or beer).
* `nb_relased`: nb of released mosquitoes (n=50 for each test
  and group).
* `no_odour`: nb of caught mosquitoes in the "no_odour control
  trap".
* `volunt_odour`: nb of caught mosquitoes in the volunteer odour
  trap.
* `activated`: number of trapped mosquitoes (= `no_odour` +
  `volunt_odour`).
* `co2no`: CO2 concentration in the no odour trap.
* `co2od`: CO2 concentration in the volunteer odour trap.
* `temp`: body temperature of the volunteer.
* `trapside`: 2 levels (A or B) this is the side of the
  volunteer odour treatment in the Y-olfactometer (volunteer
  odour on the right side: A or on the left side: B)
* `datetime`: date / time of the corresponding test run.
