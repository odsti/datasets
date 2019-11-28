## Arbuthnot's christening data.

Data comes from [Arbuthnot's 1710
paper](https://www.york.ac.uk/depts/maths/histstat/arbuthnot.pdf).

From: Philosophical Transactions of the Royal Society of London **27** (1710),
186–190,  reprinted  in M G Kendall and R L Plackett (eds), "Studies in the
History of Statistics  and Probability" Volume II, High Wycombe: Griffin 1977,
pp. 30–34.

We extracted the text with:

```
pdftotext -layout arbuthnot.pdf arbuthnot.txt
```

then edited the result to form `arbuthnot.csv`.

We loaded the `Arbuthnot` data frame from the [HistData
R package](https://www.rdocumentation.org/packages/HistData), and checked their
values against ours.  Finally, we corrected he female values for 1646, 1689,
and 1707, and the male value for 1707, after confirming by comparison to a [PDF
of the original
pages](https://royalsocietypublishing.org/doi/pdf/10.1098/rstl.1710.0011).

The data are the number of christenings of each sex in London, for the given
years (1629-1710).

We release `arbuthnot.csv` under the [Public Domain Dedication and License][PDDL].


[PDDL]: https://www.opendatacommons.org/licenses/pddl/index.html
[CC-0 license]: https://creativecommons.org/share-your-work/public-domain/cc0/
