[Skip to content](https://purrr.tidyverse.org/reference/auto_browse.html#container)

![](https://purrr.tidyverse.org/logo.png)

Wrap a function so it will automatically `browse()` on error
============================================================

Source: [`R/adverb-auto-browse.R`](https://github.com/tidyverse/purrr/blob/main/R/adverb-auto-browse.R)

`auto_browse.Rd`

A function wrapped with `auto_browse()` will automatically enter an interactive debugger using `[browser()](https://rdrr.io/r/base/browser.html) ` when ever it encounters an error.

Usage[](https://purrr.tidyverse.org/reference/auto_browse.html#ref-usage)

--------------------------------------------------------------------------

    auto_browse(.f)

Arguments[](https://purrr.tidyverse.org/reference/auto_browse.html#arguments)

------------------------------------------------------------------------------

.f[](https://purrr.tidyverse.org/reference/auto_browse.html#arg--f)

A function to modify, specified in one of the following ways:

*   A named function, e.g. `mean`.
    
*   An anonymous function, e.g. `\(x) x + 1` or `function(x) x + 1`.
    
*   A formula, e.g. `~ .x + 1`. No longer recommended.
    

Value[](https://purrr.tidyverse.org/reference/auto_browse.html#value)

----------------------------------------------------------------------

A function that takes the same arguments as `.f`, but returns a different value, as described above.

Adverbs[](https://purrr.tidyverse.org/reference/auto_browse.html#adverbs)

--------------------------------------------------------------------------

This function is called an adverb because it modifies the effect of a function (a verb). If you'd like to include a function created an adverb in a package, be sure to read [faq-adverbs-export](https://purrr.tidyverse.org/reference/faq-adverbs-export.html)
.

See also[](https://purrr.tidyverse.org/reference/auto_browse.html#see-also)

----------------------------------------------------------------------------

Other adverbs: `[compose()](https://purrr.tidyverse.org/reference/compose.html) `, `[insistently()](https://purrr.tidyverse.org/reference/insistently.html) `, `[negate()](https://purrr.tidyverse.org/reference/negate.html) `, `[partial()](https://purrr.tidyverse.org/reference/partial.html) `, `[possibly()](https://purrr.tidyverse.org/reference/possibly.html) `, `[quietly()](https://purrr.tidyverse.org/reference/quietly.html) `, `[safely()](https://purrr.tidyverse.org/reference/safely.html) `, `[slowly()](https://purrr.tidyverse.org/reference/slowly.html) `

Examples[](https://purrr.tidyverse.org/reference/auto_browse.html#ref-examples)

--------------------------------------------------------------------------------

    # For interactive usage, auto_browse() is useful because it automatically
    # starts a browser() in the right place.
    f <- function(x) {
      y <- 20
      if (x > 5) {
        stop("!")
      } else {
        x
      }
    }
    if (interactive()) {
      map(1:6, auto_browse(f))
    }