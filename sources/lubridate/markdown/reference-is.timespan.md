[Skip to content](https://lubridate.tidyverse.org/reference/is.timespan.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Is x a length of time?
======================

Source: [`R/timespans.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/timespans.r)

`is.timespan.Rd`

Is x a length of time?

Usage[](https://lubridate.tidyverse.org/reference/is.timespan.html#ref-usage)

------------------------------------------------------------------------------

    is.timespan(x)

Arguments[](https://lubridate.tidyverse.org/reference/is.timespan.html#arguments)

----------------------------------------------------------------------------------

x[](https://lubridate.tidyverse.org/reference/is.timespan.html#arg-x)

an R object

Value[](https://lubridate.tidyverse.org/reference/is.timespan.html#value)

--------------------------------------------------------------------------

TRUE if x is a period, interval, duration, or difftime object, FALSE otherwise.

See also[](https://lubridate.tidyverse.org/reference/is.timespan.html#see-also)

--------------------------------------------------------------------------------

`[is.instant()](https://lubridate.tidyverse.org/reference/is.instant.html) `, `[is.duration()](https://lubridate.tidyverse.org/reference/duration.html) `, `[is.difftime()](https://lubridate.tidyverse.org/reference/is.difftime.html) `, `[is.period()](https://lubridate.tidyverse.org/reference/period.html) `, `[is.interval()](https://lubridate.tidyverse.org/reference/interval.html) `

Examples[](https://lubridate.tidyverse.org/reference/is.timespan.html#ref-examples)

------------------------------------------------------------------------------------

    is.timespan(as.Date("2009-08-03")) # FALSE
    #> [1] FALSE
    is.timespan(duration(second = 1)) # TRUE
    #> [1] TRUE