[Skip to content](https://lubridate.tidyverse.org/reference/rollbackward.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Roll backward or forward a date the previous, current or next month
===================================================================

Source: [`R/ops-m+.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/ops-m+.r)

`rollbackward.Rd`

`rollbackward()` changes a date to the last day of the previous month or to the first day of the month. `rollforward()` rolls to the last day of the current month or to the first day of the next month. Optionally, the new date can retain the same hour, minute, and second information. `rollback()` is a synonym for `rollbackward()`.

Usage[](https://lubridate.tidyverse.org/reference/rollbackward.html#ref-usage)

-------------------------------------------------------------------------------

    rollbackward(dates, roll_to_first = FALSE, preserve_hms = TRUE)
    
    rollback(dates, roll_to_first = FALSE, preserve_hms = TRUE)
    
    rollforward(dates, roll_to_first = FALSE, preserve_hms = TRUE)

Arguments[](https://lubridate.tidyverse.org/reference/rollbackward.html#arguments)

-----------------------------------------------------------------------------------

dates[](https://lubridate.tidyverse.org/reference/rollbackward.html#arg-dates)

A POSIXct, POSIXlt or Date class object.

roll\_to\_first[](https://lubridate.tidyverse.org/reference/rollbackward.html#arg-roll-to-first)

Rollback to the first day of the month instead of the last day of the month

preserve\_hms[](https://lubridate.tidyverse.org/reference/rollbackward.html#arg-preserve-hms)

Retains the same hour, minute, and second information? If FALSE, the new date will be at 00:00:00.

Value[](https://lubridate.tidyverse.org/reference/rollbackward.html#value)

---------------------------------------------------------------------------

A date-time object of class POSIXlt, POSIXct or Date, whose day has been adjusted to the last day of the previous month, or to the first day of the month.

Examples[](https://lubridate.tidyverse.org/reference/rollbackward.html#ref-examples)

-------------------------------------------------------------------------------------

    date <- ymd("2010-03-03")
    rollbackward(date)
    #> [1] "2010-02-28"
    
    dates <- date + months(0:2)
    rollbackward(dates)
    #> [1] "2010-02-28" "2010-03-31" "2010-04-30"
    
    date <- ymd_hms("2010-03-03 12:44:22")
    rollbackward(date)
    #> [1] "2010-02-28 12:44:22 UTC"
    rollbackward(date, roll_to_first = TRUE)
    #> [1] "2010-03-01 12:44:22 UTC"
    rollbackward(date, preserve_hms = FALSE)
    #> [1] "2010-02-28 UTC"
    rollbackward(date, roll_to_first = TRUE, preserve_hms = FALSE)
    #> [1] "2010-03-01 UTC"