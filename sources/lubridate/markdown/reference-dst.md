[Skip to content](https://lubridate.tidyverse.org/reference/dst.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Get **d**aylight **s**avings **t**ime indicator of a date-time
==============================================================

Source: [`R/accessors-dst.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/accessors-dst.r)

`dst.Rd`

Date-time must be a POSIXct, POSIXlt, Date, chron, yearmon, yearqtr, zoo, zooreg, timeDate, xts, its, ti, jul, timeSeries, and fts objects.

Usage[](https://lubridate.tidyverse.org/reference/dst.html#ref-usage)

----------------------------------------------------------------------

    dst(x)

Arguments[](https://lubridate.tidyverse.org/reference/dst.html#arguments)

--------------------------------------------------------------------------

x[](https://lubridate.tidyverse.org/reference/dst.html#arg-x)

a date-time object

Value[](https://lubridate.tidyverse.org/reference/dst.html#value)

------------------------------------------------------------------

A logical. TRUE if DST is in force, FALSE if not, NA if unknown.

Details[](https://lubridate.tidyverse.org/reference/dst.html#details)

----------------------------------------------------------------------

A date-time's daylight savings flag can not be set because it depends on the date-time's year, month, day, and hour values.

Examples[](https://lubridate.tidyverse.org/reference/dst.html#ref-examples)

----------------------------------------------------------------------------

    x <- ymd("2012-03-26")
    dst(x)
    #> [1] FALSE