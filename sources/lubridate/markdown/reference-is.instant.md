[Skip to content](https://lubridate.tidyverse.org/reference/is.instant.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Is x a date-time object?
========================

Source: [`R/instants.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/instants.r)

`is.instant.Rd`

An instant is a specific moment in time. Most common date-time objects (e.g, POSIXct, POSIXlt, and Date objects) are instants.

Usage[](https://lubridate.tidyverse.org/reference/is.instant.html#ref-usage)

-----------------------------------------------------------------------------

    is.instant(x)
    
    is.timepoint(x)

Arguments[](https://lubridate.tidyverse.org/reference/is.instant.html#arguments)

---------------------------------------------------------------------------------

x[](https://lubridate.tidyverse.org/reference/is.instant.html#arg-x)

an R object

Value[](https://lubridate.tidyverse.org/reference/is.instant.html#value)

-------------------------------------------------------------------------

TRUE if x is a POSIXct, POSIXlt, or Date object, FALSE otherwise.

See also[](https://lubridate.tidyverse.org/reference/is.instant.html#see-also)

-------------------------------------------------------------------------------

`[is.timespan()](https://lubridate.tidyverse.org/reference/is.timespan.html) `, `[is.POSIXt()](https://lubridate.tidyverse.org/reference/posix_utils.html) `, `[is.Date()](https://lubridate.tidyverse.org/reference/date_utils.html) `

Examples[](https://lubridate.tidyverse.org/reference/is.instant.html#ref-examples)

-----------------------------------------------------------------------------------

    is.instant(as.Date("2009-08-03")) # TRUE
    #> [1] TRUE
    is.timepoint(5) # FALSE
    #> [1] FALSE