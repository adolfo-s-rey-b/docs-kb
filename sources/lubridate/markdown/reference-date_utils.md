[Skip to content](https://lubridate.tidyverse.org/reference/date_utils.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Various date utilities
======================

Source: [`R/Dates.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/Dates.r)

`date_utils.Rd`

`Date()` mirrors primitive constructors in base R (`[double()](https://rdrr.io/r/base/double.html) `, `[character()](https://rdrr.io/r/base/character.html) ` etc.)

Usage[](https://lubridate.tidyverse.org/reference/date_utils.html#ref-usage)

-----------------------------------------------------------------------------

    is.Date(x)
    
    Date(length = 0L)
    
    NA_Date_

Format[](https://lubridate.tidyverse.org/reference/date_utils.html#format)

---------------------------------------------------------------------------

An object of class `Date` of length 1.

Arguments[](https://lubridate.tidyverse.org/reference/date_utils.html#arguments)

---------------------------------------------------------------------------------

x[](https://lubridate.tidyverse.org/reference/date_utils.html#arg-x)

an R object

length[](https://lubridate.tidyverse.org/reference/date_utils.html#arg-length)

A non-negative number specifying the desired length. Supplying an argument of length other than one is an error.

See also[](https://lubridate.tidyverse.org/reference/date_utils.html#see-also)

-------------------------------------------------------------------------------

`[is.instant()](https://lubridate.tidyverse.org/reference/is.instant.html) `, `[is.timespan()](https://lubridate.tidyverse.org/reference/is.timespan.html) `, `[is.POSIXt()](https://lubridate.tidyverse.org/reference/posix_utils.html) `, `[POSIXct()](https://lubridate.tidyverse.org/reference/posix_utils.html) `

Examples[](https://lubridate.tidyverse.org/reference/date_utils.html#ref-examples)

-----------------------------------------------------------------------------------

    is.Date(as.Date("2009-08-03")) # TRUE
    #> [1] TRUE
    is.Date(difftime(now() + 5, now())) # FALSE
    #> [1] FALSE