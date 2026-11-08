[Skip to content](https://lubridate.tidyverse.org/reference/date.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Get/set date component of a date-time
=====================================

Source: [`R/accessors-date.R`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/accessors-date.R)

`date.Rd`

Date-time must be a POSIXct, POSIXlt, Date, chron, yearmon, yearqtr, zoo, zooreg, timeDate, xts, its, ti, jul, timeSeries, and fts objects.

Usage[](https://lubridate.tidyverse.org/reference/date.html#ref-usage)

-----------------------------------------------------------------------

    date(x)
    
    date(x) <- value

Arguments[](https://lubridate.tidyverse.org/reference/date.html#arguments)

---------------------------------------------------------------------------

x[](https://lubridate.tidyverse.org/reference/date.html#arg-x)

a date-time object

value[](https://lubridate.tidyverse.org/reference/date.html#arg-value)

an object for which the `date()` function is defined

Value[](https://lubridate.tidyverse.org/reference/date.html#value)

-------------------------------------------------------------------

the date of x as a Date

Details[](https://lubridate.tidyverse.org/reference/date.html#details)

-----------------------------------------------------------------------

`date()` does not yet support years before 0 C.E. Also `date()` is not defined for Period objects.

Base compatibility[](https://lubridate.tidyverse.org/reference/date.html#base-compatibility)

---------------------------------------------------------------------------------------------

`date()` can be called without any arguments to return a string representing the current date-time. This provides compatibility with `base:date()` which it overrides.

Examples[](https://lubridate.tidyverse.org/reference/date.html#ref-examples)

-----------------------------------------------------------------------------

    x <- ymd_hms("2012-03-26 23:12:13", tz = "America/New_York")
    date(x)
    #> [1] "2012-03-26"
    as.Date(x) # by default as.Date assumes you want to know the date in UTC
    #> [1] "2012-03-27"
    as.Date(x, tz = "America/New_York")
    #> [1] "2012-03-26"
    date(x) <- as.Date("2000-01-02")
    x
    #> [1] "2000-01-02 23:12:13 EST"