[Skip to content](https://lubridate.tidyverse.org/reference/posix_utils.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Various POSIX utilities
=======================

Source: [`R/POSIXt.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/POSIXt.r)

`posix_utils.Rd`

`POSIXct()` mirrors primitive constructors in base R (`[double()](https://rdrr.io/r/base/double.html) `, `[character()](https://rdrr.io/r/base/character.html) ` etc.)

Usage[](https://lubridate.tidyverse.org/reference/posix_utils.html#ref-usage)

------------------------------------------------------------------------------

    is.POSIXt(x)
    
    is.POSIXlt(x)
    
    is.POSIXct(x)
    
    POSIXct(length = 0L, tz = "UTC")
    
    NA_POSIXct_

Format[](https://lubridate.tidyverse.org/reference/posix_utils.html#format)

----------------------------------------------------------------------------

An object of class `POSIXct` (inherits from `POSIXt`) of length 1.

Arguments[](https://lubridate.tidyverse.org/reference/posix_utils.html#arguments)

----------------------------------------------------------------------------------

x[](https://lubridate.tidyverse.org/reference/posix_utils.html#arg-x)

an R object

length[](https://lubridate.tidyverse.org/reference/posix_utils.html#arg-length)

A non-negative number specifying the desired length. Supplying an argument of length other than one is an error.

tz[](https://lubridate.tidyverse.org/reference/posix_utils.html#arg-tz)

a timezone (defaults to "utc")

Value[](https://lubridate.tidyverse.org/reference/posix_utils.html#value)

--------------------------------------------------------------------------

TRUE if x is a POSIXct or POSIXlt object, FALSE otherwise.

See also[](https://lubridate.tidyverse.org/reference/posix_utils.html#see-also)

--------------------------------------------------------------------------------

`[is.instant()](https://lubridate.tidyverse.org/reference/is.instant.html) `, `[is.timespan()](https://lubridate.tidyverse.org/reference/is.timespan.html) `, `[is.Date()](https://lubridate.tidyverse.org/reference/date_utils.html) `

Examples[](https://lubridate.tidyverse.org/reference/posix_utils.html#ref-examples)

------------------------------------------------------------------------------------

    is.POSIXt(as.Date("2009-08-03"))
    #> [1] FALSE
    is.POSIXt(as.POSIXct("2009-08-03"))
    #> [1] TRUE