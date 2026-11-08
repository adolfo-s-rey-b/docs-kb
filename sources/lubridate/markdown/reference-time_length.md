[Skip to content](https://lubridate.tidyverse.org/reference/time_length.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Compute the exact length of a time span
=======================================

Source: [`R/timespans.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/timespans.r)
, [`R/intervals.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/intervals.r)

`time_length.Rd`

Compute the exact length of a time span

Usage[](https://lubridate.tidyverse.org/reference/time_length.html#ref-usage)

------------------------------------------------------------------------------

    time_length(x, unit = "second")
    
    # S4 method for class 'Interval'
    time_length(x, unit = "second")

Arguments[](https://lubridate.tidyverse.org/reference/time_length.html#arguments)

----------------------------------------------------------------------------------

x[](https://lubridate.tidyverse.org/reference/time_length.html#arg-x)

a duration, period, difftime or interval

unit[](https://lubridate.tidyverse.org/reference/time_length.html#arg-unit)

a character string that specifies with time units to use

Value[](https://lubridate.tidyverse.org/reference/time_length.html#value)

--------------------------------------------------------------------------

the length of the interval in the specified unit. A negative number connotes a negative interval or duration

Details[](https://lubridate.tidyverse.org/reference/time_length.html#details)

------------------------------------------------------------------------------

When `x` is an [Interval](https://lubridate.tidyverse.org/reference/Interval-class.html)
 object and `unit` are years or months, `time_length()` takes into account the fact that all months and years don't have the same number of days.

When `x` is a [Duration](https://lubridate.tidyverse.org/reference/Duration-class.html)
, [Period](https://lubridate.tidyverse.org/reference/Period-class.html)
 or `[difftime()](https://rdrr.io/r/base/difftime.html) ` object, length in months or years is based on their most common lengths in seconds (see `[timespan()](https://lubridate.tidyverse.org/reference/timespan.html) `).

See also[](https://lubridate.tidyverse.org/reference/time_length.html#see-also)

--------------------------------------------------------------------------------

`[timespan()](https://lubridate.tidyverse.org/reference/timespan.html) `

Examples[](https://lubridate.tidyverse.org/reference/time_length.html#ref-examples)

------------------------------------------------------------------------------------

    int <- interval(ymd("1980-01-01"), ymd("2014-09-18"))
    time_length(int, "week")
    #> [1] 1811.286
    
    # Exact age
    time_length(int, "year")
    #> [1] 34.71233
    
    # Age at last anniversary
    trunc(time_length(int, "year"))
    #> [1] 34
    
    # Example of difference between intervals and durations
    int <- interval(ymd("1900-01-01"), ymd("1999-12-31"))
    time_length(int, "year")
    #> [1] 99.99726
    time_length(as.duration(int), "year")
    #> [1] 99.99452