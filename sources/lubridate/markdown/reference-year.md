[Skip to content](https://lubridate.tidyverse.org/reference/year.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Get/set years component of a date-time
======================================

Source: [`R/accessors-year.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/accessors-year.r)

`year.Rd`

Date-time must be a POSIXct, POSIXlt, Date, Period or any other object convertible to POSIXlt.

`isoyear()` returns years according to the ISO 8601 week calendar.

`epiyear()` returns years according to the epidemiological week calendars.

Usage[](https://lubridate.tidyverse.org/reference/year.html#ref-usage)

-----------------------------------------------------------------------

    year(x)
    
    year(x) <- value
    
    isoyear(x)
    
    epiyear(x)

Arguments[](https://lubridate.tidyverse.org/reference/year.html#arguments)

---------------------------------------------------------------------------

x[](https://lubridate.tidyverse.org/reference/year.html#arg-x)

a date-time object

value[](https://lubridate.tidyverse.org/reference/year.html#arg-value)

a numeric object

Value[](https://lubridate.tidyverse.org/reference/year.html#value)

-------------------------------------------------------------------

the years element of x as a decimal number

Details[](https://lubridate.tidyverse.org/reference/year.html#details)

-----------------------------------------------------------------------

year does not yet support years before 0 C.E.

References[](https://lubridate.tidyverse.org/reference/year.html#references)

-----------------------------------------------------------------------------

[https://en.wikipedia.org/wiki/ISO\_week\_date](https://en.wikipedia.org/wiki/ISO_week_date)

Examples[](https://lubridate.tidyverse.org/reference/year.html#ref-examples)

-----------------------------------------------------------------------------

    x <- ymd("2012-03-26")
    year(x)
    #> [1] 2012
    year(x) <- 2001
    year(x) > 1995
    #> [1] TRUE