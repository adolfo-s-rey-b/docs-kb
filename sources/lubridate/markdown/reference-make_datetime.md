[Skip to content](https://lubridate.tidyverse.org/reference/make_datetime.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Efficient creation of date-times from numeric representations
=============================================================

Source: [`R/instants.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/instants.r)

`make_datetime.Rd`

`make_datetime()` is a very fast drop-in replacement for `[base::ISOdate()](https://rdrr.io/r/base/ISOdatetime.html) ` and `[base::ISOdatetime()](https://rdrr.io/r/base/ISOdatetime.html) `. `make_date()` produces objects of class `Date`.

Usage[](https://lubridate.tidyverse.org/reference/make_datetime.html#ref-usage)

--------------------------------------------------------------------------------

    make_datetime(
      year = 1970L,
      month = 1L,
      day = 1L,
      hour = 0L,
      min = 0L,
      sec = 0,
      tz = "UTC"
    )
    
    make_date(year = 1970L, month = 1L, day = 1L)

Arguments[](https://lubridate.tidyverse.org/reference/make_datetime.html#arguments)

------------------------------------------------------------------------------------

year[](https://lubridate.tidyverse.org/reference/make_datetime.html#arg-year)

numeric year

month[](https://lubridate.tidyverse.org/reference/make_datetime.html#arg-month)

numeric month

day[](https://lubridate.tidyverse.org/reference/make_datetime.html#arg-day)

numeric day

hour[](https://lubridate.tidyverse.org/reference/make_datetime.html#arg-hour)

numeric hour

min[](https://lubridate.tidyverse.org/reference/make_datetime.html#arg-min)

numeric minute

sec[](https://lubridate.tidyverse.org/reference/make_datetime.html#arg-sec)

numeric second

tz[](https://lubridate.tidyverse.org/reference/make_datetime.html#arg-tz)

time zone. Defaults to UTC.

Details[](https://lubridate.tidyverse.org/reference/make_datetime.html#details)

--------------------------------------------------------------------------------

Input vectors are silently recycled. All inputs except `sec` are silently converted to integer vectors; `sec` can be either integer or double.

Examples[](https://lubridate.tidyverse.org/reference/make_datetime.html#ref-examples)

--------------------------------------------------------------------------------------

    make_datetime(year = 1999, month = 12, day = 22, sec = 10)
    #> [1] "1999-12-22 00:00:10 UTC"
    make_datetime(year = 1999, month = 12, day = 22, sec = c(10, 11))
    #> [1] "1999-12-22 00:00:10 UTC" "1999-12-22 00:00:11 UTC"