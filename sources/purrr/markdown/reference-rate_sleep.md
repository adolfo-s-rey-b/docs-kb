[Skip to content](https://purrr.tidyverse.org/reference/rate_sleep.html#container)

![](https://purrr.tidyverse.org/logo.png)

Wait for a given time
=====================

Source: [`R/rate.R`](https://github.com/tidyverse/purrr/blob/main/R/rate.R)

`rate_sleep.Rd`

If the rate's internal counter exceeds the maximum number of times it is allowed to sleep, `rate_sleep()` throws an error of class `purrr_error_rate_excess`.

Usage[](https://purrr.tidyverse.org/reference/rate_sleep.html#ref-usage)

-------------------------------------------------------------------------

    rate_sleep(rate, quiet = TRUE)
    
    rate_reset(rate)

Arguments[](https://purrr.tidyverse.org/reference/rate_sleep.html#arguments)

-----------------------------------------------------------------------------

rate[](https://purrr.tidyverse.org/reference/rate_sleep.html#arg-rate)

A [rate](https://purrr.tidyverse.org/reference/rate-helpers.html)
 object determining the waiting time.

quiet[](https://purrr.tidyverse.org/reference/rate_sleep.html#arg-quiet)

If `FALSE`, prints a message displaying how long until the next request.

Details[](https://purrr.tidyverse.org/reference/rate_sleep.html#details)

-------------------------------------------------------------------------

Call `rate_reset()` to reset the internal rate counter to 0.

See also[](https://purrr.tidyverse.org/reference/rate_sleep.html#see-also)

---------------------------------------------------------------------------

`[rate_backoff()](https://purrr.tidyverse.org/reference/rate-helpers.html) `, `[insistently()](https://purrr.tidyverse.org/reference/insistently.html) `