[Skip to content](https://lubridate.tidyverse.org/reference/decimal_date.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Converts a date to a decimal of its year
========================================

Source: [`R/decimal-dates.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/decimal-dates.r)

`decimal_date.Rd`

Converts a date to a decimal of its year

Usage[](https://lubridate.tidyverse.org/reference/decimal_date.html#ref-usage)

-------------------------------------------------------------------------------

    decimal_date(date)

Arguments[](https://lubridate.tidyverse.org/reference/decimal_date.html#arguments)

-----------------------------------------------------------------------------------

date[](https://lubridate.tidyverse.org/reference/decimal_date.html#arg-date)

a POSIXt or Date object

Value[](https://lubridate.tidyverse.org/reference/decimal_date.html#value)

---------------------------------------------------------------------------

a numeric object where the date is expressed as a fraction of its year

Examples[](https://lubridate.tidyverse.org/reference/decimal_date.html#ref-examples)

-------------------------------------------------------------------------------------

    date <- ymd("2009-02-10")
    decimal_date(date) # 2009.11
    #> [1] 2009.11