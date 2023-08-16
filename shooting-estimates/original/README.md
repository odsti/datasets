# Police shootings data

You can track this from the Git sub-module, but the Washington Post data is
from <https://github.com/washingtonpost/data-police-shootings>.

Please remember to do:

```bash
git submodule update --init
```

to fetch the data from the Git submodule, when you first start.

`./Mapping Police Violence.csv` comes from <https://mappingpoliceviolence.org>
as of August 16th 2023.  Their methodology is
<https://mappingpoliceviolence.org/methodology>.

The [FBI Use-Of-Force data
page](https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/le/uof) has data from
which I (MB) filled `./uof_participation.csv`, by hand.

The `cupes-007.csv` data are from [this
survey](https://www.skeptic.com/research-center/reports/Research-Report-CUPES-007.pdf).
The data table comes from an import of the [supplementary materials for the
survey](https://www.skeptic.com/research-center/reports/Supplemental-CUPES-007.pdf).
