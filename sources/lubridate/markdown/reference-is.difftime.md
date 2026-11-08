[Skip to content](https://lubridate.tidyverse.org/reference/is.difftime.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Is x a difftime object?
=======================

Source: [`R/difftimes.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/difftimes.r)

`is.difftime.Rd`

Is x a difftime object?

Usage[](https://lubridate.tidyverse.org/reference/is.difftime.html#ref-usage)

------------------------------------------------------------------------------

    is.difftime(x)

Arguments[](https://lubridate.tidyverse.org/reference/is.difftime.html#arguments)

----------------------------------------------------------------------------------

x[](https://lubridate.tidyverse.org/reference/is.difftime.html#arg-x)

an R object

Value[](https://lubridate.tidyverse.org/reference/is.difftime.html#value)

--------------------------------------------------------------------------

TRUE if x is a difftime object, FALSE otherwise.

See also[](https://lubridate.tidyverse.org/reference/is.difftime.html#see-also)

--------------------------------------------------------------------------------

`[is.instant()](https://lubridate.tidyverse.org/reference/is.instant.html) `, `[is.timespan()](https://lubridate.tidyverse.org/reference/is.timespan.html) `, `[is.interval()](https://lubridate.tidyverse.org/reference/interval.html) `, `[is.period()](https://lubridate.tidyverse.org/reference/period.html) `.

Examples[](https://lubridate.tidyverse.org/reference/is.difftime.html#ref-examples)

------------------------------------------------------------------------------------

    is.difftime(as.Date("2009-08-03")) # FALSE
    #> [1] FALSE
    is.difftime(make_difftime(days = 12.4)) # TRUE
    #> [1] TRUE