[Skip to content](https://purrr.tidyverse.org/reference/negate.html#container)

![](https://purrr.tidyverse.org/logo.png)

Negate a predicate function so it selects what it previously rejected
=====================================================================

Source: [`R/adverb-negate.R`](https://github.com/tidyverse/purrr/blob/main/R/adverb-negate.R)

`negate.Rd`

Negating a function changes `TRUE` to `FALSE` and `FALSE` to `TRUE`.

Usage[](https://purrr.tidyverse.org/reference/negate.html#ref-usage)

---------------------------------------------------------------------

    negate(.p)

Arguments[](https://purrr.tidyverse.org/reference/negate.html#arguments)

-------------------------------------------------------------------------

.p[](https://purrr.tidyverse.org/reference/negate.html#arg--p)

A predicate function (i.e. a function that returns either `TRUE` or `FALSE`) specified in one of the following ways:

*   A named function, e.g. `is.character`.
    
*   An anonymous function, e.g. `\(x) all(x < 0)` or `function(x) all(x < 0)`.
    
*   A formula, e.g. `~ all(.x < 0)`. Use `.x` to refer to the first argument. No longer recommended.
    

Value[](https://purrr.tidyverse.org/reference/negate.html#value)

-----------------------------------------------------------------

A new predicate function.

Adverbs[](https://purrr.tidyverse.org/reference/negate.html#adverbs)

---------------------------------------------------------------------

This function is called an adverb because it modifies the effect of a function (a verb). If you'd like to include a function created an adverb in a package, be sure to read [faq-adverbs-export](https://purrr.tidyverse.org/reference/faq-adverbs-export.html)
.

See also[](https://purrr.tidyverse.org/reference/negate.html#see-also)

-----------------------------------------------------------------------

Other adverbs: `[auto_browse()](https://purrr.tidyverse.org/reference/auto_browse.html) `, `[compose()](https://purrr.tidyverse.org/reference/compose.html) `, `[insistently()](https://purrr.tidyverse.org/reference/insistently.html) `, `[partial()](https://purrr.tidyverse.org/reference/partial.html) `, `[possibly()](https://purrr.tidyverse.org/reference/possibly.html) `, `[quietly()](https://purrr.tidyverse.org/reference/quietly.html) `, `[safely()](https://purrr.tidyverse.org/reference/safely.html) `, `[slowly()](https://purrr.tidyverse.org/reference/slowly.html) `

Examples[](https://purrr.tidyverse.org/reference/negate.html#ref-examples)

---------------------------------------------------------------------------

    x <- list(x = 1:10, y = rbernoulli(10), z = letters)
    x |> keep(is.numeric) |> names()
    #> [1] "x"
    x |> keep(negate(is.numeric)) |> names()
    #> [1] "y" "z"
    # Same as
    x |> discard(is.numeric)
    #> $y
    #>  [1]  TRUE  TRUE  TRUE FALSE FALSE FALSE  TRUE FALSE FALSE  TRUE
    #> 
    #> $z
    #>  [1] "a" "b" "c" "d" "e" "f" "g" "h" "i" "j" "k" "l" "m" "n" "o" "p"
    #> [17] "q" "r" "s" "t" "u" "v" "w" "x" "y" "z"
    #>