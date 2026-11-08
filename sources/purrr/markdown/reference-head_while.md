[Skip to content](https://purrr.tidyverse.org/reference/head_while.html#container)

![](https://purrr.tidyverse.org/logo.png)

Find head/tail that all satisfies a predicate.
==============================================

Source: [`R/head-tail.R`](https://github.com/tidyverse/purrr/blob/main/R/head-tail.R)

`head_while.Rd`

Find head/tail that all satisfies a predicate.

Usage[](https://purrr.tidyverse.org/reference/head_while.html#ref-usage)

-------------------------------------------------------------------------

    head_while(.x, .p, ...)
    
    tail_while(.x, .p, ...)

Arguments[](https://purrr.tidyverse.org/reference/head_while.html#arguments)

-----------------------------------------------------------------------------

.x[](https://purrr.tidyverse.org/reference/head_while.html#arg--x)

A list or atomic vector.

.p[](https://purrr.tidyverse.org/reference/head_while.html#arg--p)

A single predicate function, a formula describing such a predicate function, or a logical vector of the same length as `.x`. Alternatively, if the elements of `.x` are themselves lists of objects, a string indicating the name of a logical element in the inner lists. Only those elements where `.p` evaluates to `TRUE` will be modified.

...[](https://purrr.tidyverse.org/reference/head_while.html#arg--)

Additional arguments passed on to the mapped function.

We now generally recommend against using `...` to pass additional (constant) arguments to `.f`. Instead use a shorthand anonymous function:

    # Instead of
    x |> map(f, 1, 2, collapse = ",")
    # do:
    x |> map(\(x) f(x, 1, 2, collapse = ","))

This makes it easier to understand which arguments belong to which function and will tend to yield better error messages.

Value[](https://purrr.tidyverse.org/reference/head_while.html#value)

---------------------------------------------------------------------

A vector the same type as `.x`.

Examples[](https://purrr.tidyverse.org/reference/head_while.html#ref-examples)

-------------------------------------------------------------------------------

    pos <- function(x) x >= 0
    head_while(5:-5, pos)
    #> [1] 5 4 3 2 1 0
    tail_while(5:-5, negate(pos))
    #> [1] -1 -2 -3 -4 -5
    
    big <- function(x) x > 100
    head_while(0:10, big)
    #> integer(0)
    tail_while(0:10, big)
    #> integer(0)