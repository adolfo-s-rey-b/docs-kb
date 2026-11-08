[Skip to content](https://purrr.tidyverse.org/reference/slowly.html#container)

![](https://purrr.tidyverse.org/logo.png)

Wrap a function to wait between executions
==========================================

Source: [`R/adverb-slowly.R`](https://github.com/tidyverse/purrr/blob/main/R/adverb-slowly.R)

`slowly.Rd`

`slowly()` takes a function and modifies it to wait a given amount of time between each call.

Usage[](https://purrr.tidyverse.org/reference/slowly.html#ref-usage)

---------------------------------------------------------------------

    slowly(f, rate = rate_delay(), quiet = TRUE)

Arguments[](https://purrr.tidyverse.org/reference/slowly.html#arguments)

-------------------------------------------------------------------------

f[](https://purrr.tidyverse.org/reference/slowly.html#arg-f)

A function to modify, specified in one of the following ways:

*   A named function, e.g. `mean`.
    
*   An anonymous function, e.g. `\(x) x + 1` or `function(x) x + 1`.
    
*   A formula, e.g. `~ .x + 1`. No longer recommended.
    

rate[](https://purrr.tidyverse.org/reference/slowly.html#arg-rate)

A [rate](https://purrr.tidyverse.org/reference/rate-helpers.html)
 object. Defaults to a constant delay.

quiet[](https://purrr.tidyverse.org/reference/slowly.html#arg-quiet)

Hide errors (`TRUE`, the default), or display them as they occur?

Value[](https://purrr.tidyverse.org/reference/slowly.html#value)

-----------------------------------------------------------------

A function that takes the same arguments as `.f`, but returns a different value, as described above.

Adverbs[](https://purrr.tidyverse.org/reference/slowly.html#adverbs)

---------------------------------------------------------------------

This function is called an adverb because it modifies the effect of a function (a verb). If you'd like to include a function created an adverb in a package, be sure to read [faq-adverbs-export](https://purrr.tidyverse.org/reference/faq-adverbs-export.html)
.

See also[](https://purrr.tidyverse.org/reference/slowly.html#see-also)

-----------------------------------------------------------------------

Other adverbs: `[auto_browse()](https://purrr.tidyverse.org/reference/auto_browse.html) `, `[compose()](https://purrr.tidyverse.org/reference/compose.html) `, `[insistently()](https://purrr.tidyverse.org/reference/insistently.html) `, `[negate()](https://purrr.tidyverse.org/reference/negate.html) `, `[partial()](https://purrr.tidyverse.org/reference/partial.html) `, `[possibly()](https://purrr.tidyverse.org/reference/possibly.html) `, `[quietly()](https://purrr.tidyverse.org/reference/quietly.html) `, `[safely()](https://purrr.tidyverse.org/reference/safely.html) `

Examples[](https://purrr.tidyverse.org/reference/slowly.html#ref-examples)

---------------------------------------------------------------------------

    # For these example, we first create a custom rate
    # with a low waiting time between attempts:
    rate <- rate_delay(0.1)
    
    # slowly() causes a function to sleep for a given time between calls:
    slow_runif <- slowly(\(x) runif(1), rate = rate, quiet = FALSE)
    out <- map(1:5, slow_runif)
    #> Retrying in 0.1 seconds.
    #> Retrying in 0.1 seconds.
    #> Retrying in 0.1 seconds.
    #> Retrying in 0.1 seconds.