[Skip to content](https://lubridate.tidyverse.org/reference/date_decimal.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Converts a decimal to a date
============================

Source: [`R/decimal-dates.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/decimal-dates.r)

`date_decimal.Rd`

Converts a decimal to a date

Usage[](https://lubridate.tidyverse.org/reference/date_decimal.html#ref-usage)

-------------------------------------------------------------------------------

    date_decimal(decimal, tz = "UTC")

Arguments[](https://lubridate.tidyverse.org/reference/date_decimal.html#arguments)

-----------------------------------------------------------------------------------

decimal[](https://lubridate.tidyverse.org/reference/date_decimal.html#arg-decimal)

a numeric object

tz[](https://lubridate.tidyverse.org/reference/date_decimal.html#arg-tz)

the time zone required

Value[](https://lubridate.tidyverse.org/reference/date_decimal.html#value)

---------------------------------------------------------------------------

a POSIXct object, whose year corresponds to the integer part of decimal. The months, days, hours, minutes and seconds elements are picked so the date-time will accurately represent the fraction of the year expressed by decimal.

Examples[](https://lubridate.tidyverse.org/reference/date_decimal.html#ref-examples)

-------------------------------------------------------------------------------------

    date <- ymd("2009-02-10")
    decimal <- decimal_date(date) # 2009.11
    date_decimal(decimal) # "2009-02-10 UTC"
    #> [1] "2009-02-10 UTC"