[Skip to content](https://lubridate.tidyverse.org/reference/leap_year.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Is a year a leap year?
======================

Source: [`R/leap-years.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/leap-years.r)

`leap_year.Rd`

If x is a recognized date-time object, leap\_year will return whether x occurs during a leap year. If x is a number, it is interpreted as a year in the Gregorian calendar and `leap_year` returns `TRUE` if it is a leap year.

Usage[](https://lubridate.tidyverse.org/reference/leap_year.html#ref-usage)

----------------------------------------------------------------------------

    leap_year(date)

Arguments[](https://lubridate.tidyverse.org/reference/leap_year.html#arguments)

--------------------------------------------------------------------------------

date[](https://lubridate.tidyverse.org/reference/leap_year.html#arg-date)

a date-time object or a year

Value[](https://lubridate.tidyverse.org/reference/leap_year.html#value)

------------------------------------------------------------------------

TRUE if x is a leap year, FALSE otherwise

Examples[](https://lubridate.tidyverse.org/reference/leap_year.html#ref-examples)

----------------------------------------------------------------------------------

    x <- as.Date("2009-08-02")
    leap_year(x) # FALSE
    #> [1] FALSE
    leap_year(2009) # FALSE
    #> [1] FALSE
    leap_year(2008) # TRUE
    #> [1] TRUE
    leap_year(1900) # FALSE
    #> [1] FALSE
    leap_year(2000) # TRUE
    #> [1] TRUE