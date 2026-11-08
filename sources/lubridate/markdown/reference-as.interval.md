[Skip to content](https://lubridate.tidyverse.org/reference/as.interval.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Change an object to an `interval`
=================================

Source: [`R/coercion.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/coercion.r)

`as.interval.Rd`

as.interval changes difftime, Duration, Period and numeric class objects to intervals that begin at the specified date-time. Numeric objects are first coerced to timespans equal to the numeric value in seconds.

Usage[](https://lubridate.tidyverse.org/reference/as.interval.html#ref-usage)

------------------------------------------------------------------------------

    as.interval(x, start, ...)

Arguments[](https://lubridate.tidyverse.org/reference/as.interval.html#arguments)

----------------------------------------------------------------------------------

x[](https://lubridate.tidyverse.org/reference/as.interval.html#arg-x)

a duration, difftime, period, or numeric object that describes the length of the interval

start[](https://lubridate.tidyverse.org/reference/as.interval.html#arg-start)

a POSIXt or Date object that describes when the interval begins

...[](https://lubridate.tidyverse.org/reference/as.interval.html#arg--)

additional arguments to pass to as.interval

Value[](https://lubridate.tidyverse.org/reference/as.interval.html#value)

--------------------------------------------------------------------------

an interval object

Details[](https://lubridate.tidyverse.org/reference/as.interval.html#details)

------------------------------------------------------------------------------

as.interval can be used to create accurate transformations between Period objects, which measure time spans in variable length units, and Duration objects, which measure timespans as an exact number of seconds. A start date- time must be supplied to make the conversion. Lubridate uses this start date to look up how many seconds each variable length unit (e.g. month, year) lasted for during the time span described. See `[as.duration()](https://lubridate.tidyverse.org/reference/as.duration.html) `, `[as.period()](https://lubridate.tidyverse.org/reference/as.period.html) `.

See also[](https://lubridate.tidyverse.org/reference/as.interval.html#see-also)

--------------------------------------------------------------------------------

`[interval()](https://lubridate.tidyverse.org/reference/interval.html) `

Examples[](https://lubridate.tidyverse.org/reference/as.interval.html#ref-examples)

------------------------------------------------------------------------------------

    diff <- make_difftime(days = 31) # difftime
    as.interval(diff, ymd("2009-01-01"))
    #> [1] 2009-01-01 UTC--2009-02-01 UTC
    as.interval(diff, ymd("2009-02-01"))
    #> [1] 2009-02-01 UTC--2009-03-04 UTC
    
    dur <- duration(days = 31) # duration
    as.interval(dur, ymd("2009-01-01"))
    #> [1] 2009-01-01 UTC--2009-02-01 UTC
    as.interval(dur, ymd("2009-02-01"))
    #> [1] 2009-02-01 UTC--2009-03-04 UTC
    
    per <- period(months = 1) # period
    as.interval(per, ymd("2009-01-01"))
    #> [1] 2009-01-01 UTC--2009-02-01 UTC
    as.interval(per, ymd("2009-02-01"))
    #> [1] 2009-02-01 UTC--2009-03-01 UTC
    
    as.interval(3600, ymd("2009-01-01")) # numeric
    #> [1] 2009-01-01 UTC--2018-11-10 UTC