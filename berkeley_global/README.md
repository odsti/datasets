# Berkeley Earth data

The data are the global land and sea temperature data downloaded from
<https://berkeleyearth.org/data/>.  At the time I (MB) accessed the data (23
September 2023), the link to the data was under the heading "Global Monthly
Averages (1850 – Recent)".

In the same page authors assert the
[CC-By-NC](https://creativecommons.org/licenses/by-nc/4.0/) license, although
I doubt whether this could reasonably be enforced.

See the processing script for details.

The citation for the original data is:

> Rohde, R. A. and Hausfather, Z.: The Berkeley Earth Land/Ocean Temperature
Record, Earth Syst. Sci. Data, 12, 3469 — 3479,
<https://doi.org/10.5194/essd-12-3469-2020>, 2020.

The description of the original values is:

> This file contains a brief summary of the changes in Earth's global average
surface temperature estimated by combining the Berkeley Earth land-surface
temperature field with a reinterpolated version of the HadSST4 ocean
temperature field.

There are two sets of measures:

1. Using air temperature above sea ice
2. Using water temperature below sea ice

Specifically the processing pulls out "Anomaly" column for the air temperature values (1. above).

The "Anomaly" value is the temperature difference from the average from the Jan
1951-Dec 1980 global mean temperature, estimated here as 14.701 degrees C.

The processing adds back this average, to give estimated temperature values in
degrees centigrade.
