[Skip to content](https://purrr.tidyverse.org/reference/along.html#container)

![](https://purrr.tidyverse.org/logo.png)

Create a list of given length
=============================

Source: [`R/deprec-along.R`](https://github.com/tidyverse/purrr/blob/main/R/deprec-along.R)

`along.Rd`

[![[Deprecated]](https://purrr.tidyverse.org/reference/figures/lifecycle-deprecated.svg)](https://lifecycle.r-lib.org/articles/stages.html#deprecated)

This function was deprecated in purrr 1.0.0 since it's not related to the core purpose of purrr.

It can be useful to create an empty list that you plan to fill later. This is similar to the idea of `[seq_along()](https://rdrr.io/r/base/seq.html) `, which creates a vector of the same length as its input.

Usage[](https://purrr.tidyverse.org/reference/along.html#ref-usage)

--------------------------------------------------------------------

    list_along(x)

Arguments[](https://purrr.tidyverse.org/reference/along.html#arguments)

------------------------------------------------------------------------

x[](https://purrr.tidyverse.org/reference/along.html#arg-x)

A vector.

Value[](https://purrr.tidyverse.org/reference/along.html#value)

----------------------------------------------------------------

A list of the same length as `x`.

Examples[](https://purrr.tidyverse.org/reference/along.html#ref-examples)

--------------------------------------------------------------------------

    x <- 1:5
    seq_along(x)
    #> [1] 1 2 3 4 5
    list_along(x)
    #> Warning: `list_along()` was deprecated in purrr 1.0.0.
    #> ℹ Please use rep_along(x, list()) instead.
    #> [[1]]
    #> NULL
    #> 
    #> [[2]]
    #> NULL
    #> 
    #> [[3]]
    #> NULL
    #> 
    #> [[4]]
    #> NULL
    #> 
    #> [[5]]
    #> NULL
    #>