[Skip to content](https://lubridate.tidyverse.org/reference/local_time.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Get local time from a date-time vector.
=======================================

Source: [`R/time-zones.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/time-zones.r)

`local_time.Rd`

`local_time` retrieves day clock time in specified time zones. Computation is vectorized over both `dt` and `tz` arguments, the shortest is recycled in accordance with standard R rules.

Usage[](https://lubridate.tidyverse.org/reference/local_time.html#ref-usage)

-----------------------------------------------------------------------------

    local_time(dt, tz = NULL, units = "secs")

Arguments[](https://lubridate.tidyverse.org/reference/local_time.html#arguments)

---------------------------------------------------------------------------------

dt[](https://lubridate.tidyverse.org/reference/local_time.html#arg-dt)

a date-time object.

tz[](https://lubridate.tidyverse.org/reference/local_time.html#arg-tz)

a character vector of timezones for which to compute the local time.

units[](https://lubridate.tidyverse.org/reference/local_time.html#arg-units)

passed directly to `[as.difftime()](https://generics.r-lib.org/reference/coercion-time-difference.html) `.

Examples[](https://lubridate.tidyverse.org/reference/local_time.html#ref-examples)

-----------------------------------------------------------------------------------

    
    x <- ymd_hms(c("2009-08-07 01:02:03", "2009-08-07 10:20:30"))
    local_time(x, units = "secs")
    #> Time differences in secs
    #> [1]  3723 37230
    local_time(x, units = "hours")
    #> Time differences in hours
    #> [1]  1.034167 10.341667
    local_time(x, "Europe/Amsterdam")
    #> Time differences in secs
    #> [1] 10923 44430
    local_time(x, "Europe/Amsterdam") == local_time(with_tz(x, "Europe/Amsterdam"))
    #> [1] TRUE TRUE
    
    x <- ymd_hms("2009-08-07 01:02:03")
    local_time(x, c("America/New_York", "Europe/Amsterdam", "Asia/Shanghai"), unit = "hours")
    #> Time differences in hours
    #> [1] 21.034167  3.034167  9.034167