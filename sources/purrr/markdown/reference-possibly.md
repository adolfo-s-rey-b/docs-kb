[Skip to content](https://purrr.tidyverse.org/reference/possibly.html#container)

![](https://purrr.tidyverse.org/logo.png)

Wrap a function to return a value instead of an error
=====================================================

Source: [`R/adverb-possibly.R`](https://github.com/tidyverse/purrr/blob/main/R/adverb-possibly.R)

`possibly.Rd`

Create a modified version of `.f` that return a default value (`otherwise`) whenever an error occurs.

Usage[](https://purrr.tidyverse.org/reference/possibly.html#ref-usage)

-----------------------------------------------------------------------

    possibly(.f, otherwise = NULL, quiet = TRUE)

Arguments[](https://purrr.tidyverse.org/reference/possibly.html#arguments)

---------------------------------------------------------------------------

.f[](https://purrr.tidyverse.org/reference/possibly.html#arg--f)

A function to modify, specified in one of the following ways:

*   A named function, e.g. `mean`.
    
*   An anonymous function, e.g. `\(x) x + 1` or `function(x) x + 1`.
    
*   A formula, e.g. `~ .x + 1`. No longer recommended.
    

otherwise[](https://purrr.tidyverse.org/reference/possibly.html#arg-otherwise)

Default value to use when an error occurs.

quiet[](https://purrr.tidyverse.org/reference/possibly.html#arg-quiet)

Hide errors (`TRUE`, the default), or display them as they occur?

Value[](https://purrr.tidyverse.org/reference/possibly.html#value)

-------------------------------------------------------------------

A function that takes the same arguments as `.f`, but returns a different value, as described above.

Adverbs[](https://purrr.tidyverse.org/reference/possibly.html#adverbs)

-----------------------------------------------------------------------

This function is called an adverb because it modifies the effect of a function (a verb). If you'd like to include a function created an adverb in a package, be sure to read [faq-adverbs-export](https://purrr.tidyverse.org/reference/faq-adverbs-export.html)
.

See also[](https://purrr.tidyverse.org/reference/possibly.html#see-also)

-------------------------------------------------------------------------

Other adverbs: `[auto_browse()](https://purrr.tidyverse.org/reference/auto_browse.html) `, `[compose()](https://purrr.tidyverse.org/reference/compose.html) `, `[insistently()](https://purrr.tidyverse.org/reference/insistently.html) `, `[negate()](https://purrr.tidyverse.org/reference/negate.html) `, `[partial()](https://purrr.tidyverse.org/reference/partial.html) `, `[quietly()](https://purrr.tidyverse.org/reference/quietly.html) `, `[safely()](https://purrr.tidyverse.org/reference/safely.html) `, `[slowly()](https://purrr.tidyverse.org/reference/slowly.html) `

Examples[](https://purrr.tidyverse.org/reference/possibly.html#ref-examples)

-----------------------------------------------------------------------------

    # To replace errors with a default value, use possibly().
    list("a", 10, 100) |>
      map_dbl(possibly(log, NA_real_))
    #> [1]       NA 2.302585 4.605170
    
    # The default, NULL, will be discarded with `list_c()`
    list("a", 10, 100) |>
      map(possibly(log)) |>
      list_c()
    #> [1] 2.302585 4.605170