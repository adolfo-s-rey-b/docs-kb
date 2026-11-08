[Skip to content](https://purrr.tidyverse.org/reference/rate-helpers.html#container)

![](https://purrr.tidyverse.org/logo.png)

Create delaying rate settings
=============================

Source: [`R/rate.R`](https://github.com/tidyverse/purrr/blob/main/R/rate.R)

`rate-helpers.Rd`

These helpers create rate settings that you can pass to `[insistently()](https://purrr.tidyverse.org/reference/insistently.html) ` and `[slowly()](https://purrr.tidyverse.org/reference/slowly.html) `. You can also use them in your own functions with `[rate_sleep()](https://purrr.tidyverse.org/reference/rate_sleep.html) `.

Usage[](https://purrr.tidyverse.org/reference/rate-helpers.html#ref-usage)

---------------------------------------------------------------------------

    rate_delay(pause = 1, max_times = Inf)
    
    rate_backoff(
      pause_base = 1,
      pause_cap = 60,
      pause_min = 1,
      max_times = 3,
      jitter = TRUE
    )
    
    is_rate(x)

Arguments[](https://purrr.tidyverse.org/reference/rate-helpers.html#arguments)

-------------------------------------------------------------------------------

pause[](https://purrr.tidyverse.org/reference/rate-helpers.html#arg-pause)

Delay between attempts in seconds.

max\_times[](https://purrr.tidyverse.org/reference/rate-helpers.html#arg-max-times)

Maximum number of requests to attempt.

pause\_base, pause\_cap[](https://purrr.tidyverse.org/reference/rate-helpers.html#arg-pause-base-pause-cap)

`rate_backoff()` uses an exponential back-off so that each request waits `pause_base * 2^i` seconds, up to a maximum of `pause_cap` seconds.

pause\_min[](https://purrr.tidyverse.org/reference/rate-helpers.html#arg-pause-min)

Minimum time to wait in the backoff; generally only necessary if you need pauses less than one second (which may not be kind to the server, use with caution!).

jitter[](https://purrr.tidyverse.org/reference/rate-helpers.html#arg-jitter)

Whether to introduce a random jitter in the waiting time.

x[](https://purrr.tidyverse.org/reference/rate-helpers.html#arg-x)

An object to test.

Examples[](https://purrr.tidyverse.org/reference/rate-helpers.html#ref-examples)

---------------------------------------------------------------------------------

    # A delay rate waits the same amount of time:
    rate <- rate_delay(0.02)
    for (i in 1:3) rate_sleep(rate, quiet = FALSE)
    #> Retrying in 0.02 seconds.
    #> Retrying in 0.02 seconds.
    
    # A backoff rate waits exponentially longer each time, with random
    # jitter by default:
    rate <- rate_backoff(pause_base = 0.2, pause_min = 0.005)
    for (i in 1:3) rate_sleep(rate, quiet = FALSE)
    #> Retrying in 0.047 seconds.
    #> Retrying in 0.29 seconds.