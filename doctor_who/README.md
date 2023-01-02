# Doctor Who episode statistics

See the `process_dr_who.Rmd` file for details.

In summary, these are the scraped and processed data from the scraped from
<https://guide.doctorwhonews.net>.

The `processed/doctor_who_stats.csv` file has the following columns:

*   `Episode Title`
*   `Weekday`: day of week of first broadcast.
*   `Length`: run time.
*   `Share`: audience share relative to other programmes broadcast at same time.
*   `AI`: [Audience Appreciation Index](https://tardis.fandom.com/wiki/Appreciation_Index)
*   `Chart`: Ranking in terms of number of viewers (see below) compared to all
    other programmes broadcast that week.
*   `Broadcast datetime`: Date and time of first broadcast.
*   `viewers_in_millions`: Viewers in millions.  These appear to be viewers
    within 7 days of the original broadcast, initially on TV only, and later
    including Tablets and PCs, and later still, tablets, PCs and smartphones.
    See the notebook above for more discussion.
