[Skip to content](https://purrr.tidyverse.org/reference/compose.html#container)

![](https://purrr.tidyverse.org/logo.png)

Compose multiple functions together to create a new function
============================================================

Source: [`R/adverb-compose.R`](https://github.com/tidyverse/purrr/blob/main/R/adverb-compose.R)

`compose.Rd`

Create a new function that is the composition of multiple functions, i.e. `compose(f, g)` is equivalent to `function(...) f(g(...))`.

Usage[](https://purrr.tidyverse.org/reference/compose.html#ref-usage)

----------------------------------------------------------------------

    compose(..., .dir = c("backward", "forward"))

Arguments[](https://purrr.tidyverse.org/reference/compose.html#arguments)

--------------------------------------------------------------------------

...[](https://purrr.tidyverse.org/reference/compose.html#arg--)

Functions to apply in order (from right to left by default). Formulas are converted to functions in the usual way.

[Dynamic dots](https://rlang.r-lib.org/reference/dyn-dots.html)
 are supported. In particular, if your functions are stored in a list, you can splice that in with `!!!`.

.dir[](https://purrr.tidyverse.org/reference/compose.html#arg--dir)

If `"backward"` (the default), the functions are called in the reverse order, from right to left, as is conventional in mathematics. If `"forward"`, they are called from left to right.

Value[](https://purrr.tidyverse.org/reference/compose.html#value)

------------------------------------------------------------------

A function

Adverbs[](https://purrr.tidyverse.org/reference/compose.html#adverbs)

----------------------------------------------------------------------

This function is called an adverb because it modifies the effect of a function (a verb). If you'd like to include a function created an adverb in a package, be sure to read [faq-adverbs-export](https://purrr.tidyverse.org/reference/faq-adverbs-export.html)
.

See also[](https://purrr.tidyverse.org/reference/compose.html#see-also)

------------------------------------------------------------------------

Other adverbs: `[auto_browse()](https://purrr.tidyverse.org/reference/auto_browse.html) `, `[insistently()](https://purrr.tidyverse.org/reference/insistently.html) `, `[negate()](https://purrr.tidyverse.org/reference/negate.html) `, `[partial()](https://purrr.tidyverse.org/reference/partial.html) `, `[possibly()](https://purrr.tidyverse.org/reference/possibly.html) `, `[quietly()](https://purrr.tidyverse.org/reference/quietly.html) `, `[safely()](https://purrr.tidyverse.org/reference/safely.html) `, `[slowly()](https://purrr.tidyverse.org/reference/slowly.html) `

Examples[](https://purrr.tidyverse.org/reference/compose.html#ref-examples)

----------------------------------------------------------------------------

    not_null <- compose(`!`, is.null)
    not_null(4)
    #> [1] TRUE
    not_null(NULL)
    #> [1] FALSE
    
    add1 <- function(x) x + 1
    compose(add1, add1)(8)
    #> [1] 10
    
    fn <- compose(\(x) paste(x, "foo"), \(x) paste(x, "bar"))
    fn("input")
    #> [1] "input bar foo"
    
    # Lists of functions can be spliced with !!!
    fns <- list(
      function(x) paste(x, "foo"),
      \(x) paste(x, "bar")
    )
    fn <- compose(!!!fns)
    fn("input")
    #> [1] "input bar foo"