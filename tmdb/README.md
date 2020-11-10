# Movie data from TMDB

Original data file from <https://www.kaggle.com/tmdb/tmdb-movie-metadata>

License recorded in description there is for the [TMDB
API](https://www.themoviedb.org/documentation/api/terms-of-use).  Kaggle used
the API to fetch the data, but we are not using the API here.  Most relevant
license for the content appears to be
<https://www.themoviedb.org/terms-of-use>.

I (Matthew Brett) don't think any of the data here would qualify for copyright
under US law, as these are facts, and their arrangement does not seem
creative. From <https://en.wikipedia.org/wiki/Database_right>:

> The TRIPS Agreement requires that copyright protection extends to databases
> and other compilations if they constitute intellectual creation by virtue of
> the selection or arrangement of their contents, even if some or all of the
> contents do not themselves constitute materials protected by copyright.

But - as might be obvious - I am not a lawyer.

Nevertheless - as per the API terms of use above - here is a link to the TMDB logo, to remind y'all that TMDB is the data source:

![](https://www.themoviedb.org/assets/2/v4/logos/v2/blue_square_1-5bdc75aaebeb75dc7ae79426ddd9be3b2be1e342510f8202baf6bffa71d7f5c4.svg)

See <https://www.themoviedb.org/about/logos-attribution>.

The [Movie Bible page](https://www.themoviedb.org/bible/movie) explains the
meaning of the fields in the data.

I believe the fields in the processed data are:

* title: translated title.
* budget: budget in US dollars, not adjusted for inflation.
* runtime: in minutes, including end credits.
* revenue: in US dollars.  May include only US box-office.
* vote_average: appears to be TMDB audience vote average.
* vote_count: number of votes.
* year: year of `release_date`.
* country: [ISO3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) code for
  first-listed country in `production_countries`.
