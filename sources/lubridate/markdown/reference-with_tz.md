[Skip to content](https://lubridate.tidyverse.org/reference/with_tz.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Get date-time in a different time zone
======================================

Source: [`R/time-zones.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/time-zones.r)

`with_tz.Rd`

with\_tz returns a date-time as it would appear in a different time zone. The actual moment of time measured does not change, just the time zone it is measured in. with\_tz defaults to the Universal Coordinated time zone (UTC) when an unrecognized time zone is inputted. See `[Sys.timezone()](https://rdrr.io/r/base/timezones.html) ` for more information on how R recognizes time zones.

Usage[](https://lubridate.tidyverse.org/reference/with_tz.html#ref-usage)

--------------------------------------------------------------------------

    with_tz(time, tzone = "", ...)
    
    # Default S3 method
    with_tz(time, tzone = "", ...)

Arguments[](https://lubridate.tidyverse.org/reference/with_tz.html#arguments)

------------------------------------------------------------------------------

time[](https://lubridate.tidyverse.org/reference/with_tz.html#arg-time)

a POSIXct, POSIXlt, Date, chron date-time object or a data.frame object. When a data.frame all POSIXt elements of a data.frame are processed with `with_tz()` and new data.frame is returned.

tzone[](https://lubridate.tidyverse.org/reference/with_tz.html#arg-tzone)

a character string containing the time zone to convert to. R must recognize the name contained in the string as a time zone on your system.

...[](https://lubridate.tidyverse.org/reference/with_tz.html#arg--)

Parameters passed to other methods.

Value[](https://lubridate.tidyverse.org/reference/with_tz.html#value)

----------------------------------------------------------------------

a POSIXct object in the updated time zone

See also[](https://lubridate.tidyverse.org/reference/with_tz.html#see-also)

----------------------------------------------------------------------------

`[force_tz()](https://lubridate.tidyverse.org/reference/force_tz.html) `

Examples[](https://lubridate.tidyverse.org/reference/with_tz.html#ref-examples)

--------------------------------------------------------------------------------

    x <- ymd_hms("2009-08-07 00:00:01", tz = "America/New_York")
    with_tz(x, "GMT")
    #> [1] "2009-08-07 04:00:01 GMT"