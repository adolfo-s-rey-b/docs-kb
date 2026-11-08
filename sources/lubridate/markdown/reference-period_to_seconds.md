[Skip to content](https://lubridate.tidyverse.org/reference/period_to_seconds.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Contrive a period to/from a given number of seconds
===================================================

Source: [`R/periods.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/periods.r)

`period_to_seconds.Rd`

`period_to_seconds()` approximately converts a period to seconds assuming there are 365.25 days in a calendar year and 365.25/12 days in a month.

`seconds_to_period()` create a period that has the maximum number of non-zero elements (days, hours, minutes, seconds). This computation is exact because it doesn't involve years or months.

Usage[](https://lubridate.tidyverse.org/reference/period_to_seconds.html#ref-usage)

------------------------------------------------------------------------------------

    period_to_seconds(x)
    
    seconds_to_period(x)

Arguments[](https://lubridate.tidyverse.org/reference/period_to_seconds.html#arguments)

----------------------------------------------------------------------------------------

x[](https://lubridate.tidyverse.org/reference/period_to_seconds.html#arg-x)

A numeric object. The number of seconds to coerce into a period.

Value[](https://lubridate.tidyverse.org/reference/period_to_seconds.html#value)

--------------------------------------------------------------------------------

A number (period) that roughly equates to the period (seconds) given.