[Skip to content](https://lubridate.tidyverse.org/reference/now.html#container)

![](https://lubridate.tidyverse.org/logo.png)

The current day and time
========================

Source: [`R/instants.r`](https://github.com/tidyverse/lubridate/blob/v1.9.5/R/instants.r)

`now.Rd`

The current day and time

Usage[](https://lubridate.tidyverse.org/reference/now.html#ref-usage)

----------------------------------------------------------------------

    now(tzone = "")
    
    today(tzone = "")

Arguments[](https://lubridate.tidyverse.org/reference/now.html#arguments)

--------------------------------------------------------------------------

tzone[](https://lubridate.tidyverse.org/reference/now.html#arg-tzone)

a character vector specifying which time zone you would like the current time in. tzone defaults to your computer's system timezone. You can retrieve the current time in the Universal Coordinated Time (UTC) with now("UTC").

Value[](https://lubridate.tidyverse.org/reference/now.html#value)

------------------------------------------------------------------

`now` - the current datetime as a `POSIXct` object

Examples[](https://lubridate.tidyverse.org/reference/now.html#ref-examples)

----------------------------------------------------------------------------

    now()
    #> [1] "2026-02-09 09:41:38 UTC"
    now("GMT")
    #> [1] "2026-02-09 09:41:38 GMT"
    now("")
    #> [1] "2026-02-09 09:41:38 UTC"
    now() == now() # would be TRUE if computer processed both at the same instant
    #> [1] FALSE
    now() < now() # TRUE
    #> [1] TRUE
    now() > now() # FALSE
    #> [1] FALSE
    today()
    #> [1] "2026-02-09"
    today("GMT")
    #> [1] "2026-02-09"
    today() == today("GMT") # not always true
    #> [1] TRUE
    today() < as.Date("2999-01-01") # TRUE  (so far)
    #> [1] TRUE