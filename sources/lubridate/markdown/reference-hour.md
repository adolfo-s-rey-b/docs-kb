[Skip to content](https://lubridate.tidyverse.org/reference/hour.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Get/set hours component of a date-time
======================================

Source: [`R/accessors-hour.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/accessors-hour.r)

`hour.Rd`

Date-time must be a POSIXct, POSIXlt, Date, Period, chron, yearmon, yearqtr, zoo, zooreg, timeDate, xts, its, ti, jul, timeSeries, and fts objects.

Usage[](https://lubridate.tidyverse.org/reference/hour.html#ref-usage)

-----------------------------------------------------------------------

    hour(x)
    
    hour(x) <- value

Arguments[](https://lubridate.tidyverse.org/reference/hour.html#arguments)

---------------------------------------------------------------------------

x[](https://lubridate.tidyverse.org/reference/hour.html#arg-x)

a date-time object

value[](https://lubridate.tidyverse.org/reference/hour.html#arg-value)

numeric value to be assigned to the `hour` component

Value[](https://lubridate.tidyverse.org/reference/hour.html#value)

-------------------------------------------------------------------

the hours element of x as a decimal number

Examples[](https://lubridate.tidyverse.org/reference/hour.html#ref-examples)

-----------------------------------------------------------------------------

    x <- ymd("2012-03-26")
    hour(x)
    #> [1] 0
    hour(x) <- 1
    hour(x) <- 25
    hour(x) > 2
    #> [1] FALSE