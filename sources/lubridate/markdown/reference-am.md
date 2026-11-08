[Skip to content](https://lubridate.tidyverse.org/reference/am.html#container)

![](https://lubridate.tidyverse.org/logo.png)

Does date time occur in the am or pm?
=====================================

Source: [`R/am-pm.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/am-pm.r)

`am.Rd`

Does date time occur in the am or pm?

Usage[](https://lubridate.tidyverse.org/reference/am.html#ref-usage)

---------------------------------------------------------------------

    am(x)
    
    pm(x)

Arguments[](https://lubridate.tidyverse.org/reference/am.html#arguments)

-------------------------------------------------------------------------

x[](https://lubridate.tidyverse.org/reference/am.html#arg-x)

a date-time object

Value[](https://lubridate.tidyverse.org/reference/am.html#value)

-----------------------------------------------------------------

TRUE or FALSE depending on whether x occurs in the am or pm

Examples[](https://lubridate.tidyverse.org/reference/am.html#ref-examples)

---------------------------------------------------------------------------

    x <- ymd("2012-03-26")
    am(x)
    #> [1] TRUE
    pm(x)
    #> [1] FALSE