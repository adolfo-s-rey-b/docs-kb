[Skip to content](https://lubridate.tidyverse.org/reference/second.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Get/set seconds component of a date-time
========================================

Source: [`R/accessors-second.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/accessors-second.r)

`second.Rd`

Date-time must be a POSIXct, POSIXlt, Date, Period, chron, yearmon, yearqtr, zoo, zooreg, timeDate, xts, its, ti, jul, timeSeries, and fts objects.

Usage[](https://lubridate.tidyverse.org/reference/second.html#ref-usage)

-------------------------------------------------------------------------

    second(x)
    
    second(x) <- value

Arguments[](https://lubridate.tidyverse.org/reference/second.html#arguments)

-----------------------------------------------------------------------------

x[](https://lubridate.tidyverse.org/reference/second.html#arg-x)

a date-time object

value[](https://lubridate.tidyverse.org/reference/second.html#arg-value)

numeric value to be assigned

Value[](https://lubridate.tidyverse.org/reference/second.html#value)

---------------------------------------------------------------------

the seconds element of x as a decimal number

Examples[](https://lubridate.tidyverse.org/reference/second.html#ref-examples)

-------------------------------------------------------------------------------

    x <- ymd("2012-03-26")
    second(x)
    #> [1] 0
    second(x) <- 1
    second(x) <- 61
    second(x) > 2
    #> [1] FALSE