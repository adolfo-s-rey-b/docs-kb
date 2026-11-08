[Skip to content](https://lubridate.tidyverse.org/reference/mplus.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Add and subtract months to a date without exceeding the last day of the new month
=================================================================================

Source: [`R/ops-m+.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/ops-m+.r)

`mplus.Rd`

Adding months frustrates basic arithmetic because consecutive months have different lengths. With other elements, it is helpful for arithmetic to perform automatic roll over. For example, 12:00:00 + 61 seconds becomes 12:01:01. However, people often prefer that this behavior NOT occur with months. For example, we sometimes want January 31 + 1 month = February 28 and not March 3. `%m+%` performs this type of arithmetic. Date `%m+%` months(n) always returns a date in the nth month after Date. If the new date would usually spill over into the n + 1th month, `%m+%` will return the last day of the nth month (`[rollback()](https://lubridate.tidyverse.org/reference/rollbackward.html) `). Date `%m-%` months(n) always returns a date in the nth month before Date.

Usage[](https://lubridate.tidyverse.org/reference/mplus.html#ref-usage)

------------------------------------------------------------------------

    e1 %m+% e2
    
    add_with_rollback(e1, e2, roll_to_first = FALSE, preserve_hms = TRUE)

Arguments[](https://lubridate.tidyverse.org/reference/mplus.html#arguments)

----------------------------------------------------------------------------

e1[](https://lubridate.tidyverse.org/reference/mplus.html#arg-e-)

A period or a date-time object of class [POSIXlt](https://rdrr.io/r/base/DateTimeClasses.html)
, [POSIXct](https://lubridate.tidyverse.org/reference/posix_utils.html)
 or [Date](https://lubridate.tidyverse.org/reference/date_utils.html)
.

e2[](https://lubridate.tidyverse.org/reference/mplus.html#arg-e-)

A period or a date-time object of class [POSIXlt](https://rdrr.io/r/base/DateTimeClasses.html)
, [POSIXct](https://lubridate.tidyverse.org/reference/posix_utils.html)
 or [Date](https://lubridate.tidyverse.org/reference/date_utils.html)
. Note that one of e1 and e2 must be a period and the other a date-time object.

roll\_to\_first[](https://lubridate.tidyverse.org/reference/mplus.html#arg-roll-to-first)

rollback to the first day of the month instead of the last day of the previous month (passed to `[rollback()](https://lubridate.tidyverse.org/reference/rollbackward.html) `)

preserve\_hms[](https://lubridate.tidyverse.org/reference/mplus.html#arg-preserve-hms)

retains the same hour, minute, and second information? If FALSE, the new date will be at 00:00:00 (passed to `[rollback()](https://lubridate.tidyverse.org/reference/rollbackward.html) `)

Value[](https://lubridate.tidyverse.org/reference/mplus.html#value)

--------------------------------------------------------------------

A date-time object of class POSIXlt, POSIXct or Date

Details[](https://lubridate.tidyverse.org/reference/mplus.html#details)

------------------------------------------------------------------------

`%m+%` and `%m-%` handle periods with components less than a month by first adding/subtracting months and then performing usual arithmetic with smaller units.

`%m+%` and `%m-%` should be used with caution as they are not one-to-one operations and results for either will be sensitive to the order of operations.

Examples[](https://lubridate.tidyverse.org/reference/mplus.html#ref-examples)

------------------------------------------------------------------------------

    jan <- ymd_hms("2010-01-31 03:04:05")
    jan + months(1:3) # Feb 31 and April 31 returned as NA
    #> [1] NA                        "2010-03-31 03:04:05 UTC"
    #> [3] NA                       
    # NA "2010-03-31 03:04:05 UTC" NA
    jan %m+% months(1:3) # No rollover
    #> [1] "2010-02-28 03:04:05 UTC" "2010-03-31 03:04:05 UTC"
    #> [3] "2010-04-30 03:04:05 UTC"
    
    leap <- ymd("2012-02-29")
    "2012-02-29 UTC"
    #> [1] "2012-02-29 UTC"
    leap %m+% years(1)
    #> [1] "2013-02-28"
    leap %m+% years(-1)
    #> [1] "2011-02-28"
    leap %m-% years(1)
    #> [1] "2011-02-28"
    
    x <- ymd_hms("2019-01-29 01:02:03")
    add_with_rollback(x, months(1))
    #> [1] "2019-02-28 01:02:03 UTC"
    add_with_rollback(x, months(1), preserve_hms = FALSE)
    #> [1] "2019-02-28 UTC"
    add_with_rollback(x, months(1), roll_to_first = TRUE)
    #> [1] "2019-03-01 01:02:03 UTC"
    add_with_rollback(x, months(1), roll_to_first = TRUE, preserve_hms = FALSE)
    #> [1] "2019-03-01 UTC"