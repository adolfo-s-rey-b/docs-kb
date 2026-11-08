[Skip to content](https://lubridate.tidyverse.org/reference/minute.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Get/set minutes component of a date-time
========================================

Source: [`R/accessors-minute.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/accessors-minute.r)

`minute.Rd`

Date-time must be a POSIXct, POSIXlt, Date, Period, chron, yearmon, yearqtr, zoo, zooreg, timeDate, xts, its, ti, jul, timeSeries, and fts objects.

Usage[](https://lubridate.tidyverse.org/reference/minute.html#ref-usage)

-------------------------------------------------------------------------

    minute(x)
    
    minute(x) <- value

Arguments[](https://lubridate.tidyverse.org/reference/minute.html#arguments)

-----------------------------------------------------------------------------

x[](https://lubridate.tidyverse.org/reference/minute.html#arg-x)

a date-time object

value[](https://lubridate.tidyverse.org/reference/minute.html#arg-value)

numeric value to be assigned

Value[](https://lubridate.tidyverse.org/reference/minute.html#value)

---------------------------------------------------------------------

the minutes element of x as a decimal number

Examples[](https://lubridate.tidyverse.org/reference/minute.html#ref-examples)

-------------------------------------------------------------------------------

    x <- ymd("2012-03-26")
    minute(x)
    #> [1] 0
    minute(x) <- 1
    minute(x) <- 61
    minute(x) > 2
    #> [1] FALSE