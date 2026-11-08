[Skip to content](https://lubridate.tidyverse.org/reference/week.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Get/set weeks component of a date-time
======================================

Source: [`R/accessors-week.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/accessors-week.r)

`week.Rd`

`week()` returns the number of complete seven day periods that have occurred between the date and January 1st, plus one.

`isoweek()` returns the week as it would appear in the ISO 8601 system, which uses a reoccurring leap week.

`epiweek()` is the US CDC version of epidemiological week. It follows same rules as `isoweek()` but starts on Sunday. In other parts of the world the convention is to start epidemiological weeks on Monday, which is the same as `isoweek`.

Usage[](https://lubridate.tidyverse.org/reference/week.html#ref-usage)

-----------------------------------------------------------------------

    week(x)
    
    week(x) <- value
    
    isoweek(x)
    
    epiweek(x)

Arguments[](https://lubridate.tidyverse.org/reference/week.html#arguments)

---------------------------------------------------------------------------

x[](https://lubridate.tidyverse.org/reference/week.html#arg-x)

a date-time object. Must be a POSIXct, POSIXlt, Date, chron, yearmon, yearqtr, zoo, zooreg, timeDate, xts, its, ti, jul, timeSeries, or fts object.

value[](https://lubridate.tidyverse.org/reference/week.html#arg-value)

a numeric object

Value[](https://lubridate.tidyverse.org/reference/week.html#value)

-------------------------------------------------------------------

the weeks element of x as an integer number

References[](https://lubridate.tidyverse.org/reference/week.html#references)

-----------------------------------------------------------------------------

[https://en.wikipedia.org/wiki/ISO\_week\_date](https://en.wikipedia.org/wiki/ISO_week_date)

See also[](https://lubridate.tidyverse.org/reference/week.html#see-also)

-------------------------------------------------------------------------

`[isoyear()](https://lubridate.tidyverse.org/reference/year.html) `

Examples[](https://lubridate.tidyverse.org/reference/week.html#ref-examples)

-----------------------------------------------------------------------------

    x <- ymd("2012-03-26")
    week(x)
    #> [1] 13
    week(x) <- 1
    week(x) <- 54
    week(x) > 3
    #> [1] FALSE