[Skip to content](https://purrr.tidyverse.org/reference/prepend.html#container)

![](https://purrr.tidyverse.org/logo.png)

Prepend a vector
================

Source: [`R/deprec-prepend.R`](https://github.com/tidyverse/purrr/blob/main/R/deprec-prepend.R)

`prepend.Rd`

[![[Deprecated]](https://purrr.tidyverse.org/reference/figures/lifecycle-deprecated.svg)](https://lifecycle.r-lib.org/articles/stages.html#deprecated)

This function was deprecated in purrr 1.0.0 because it's not related to the core purpose of purrr.

This is a companion to `[append()](https://rdrr.io/r/base/append.html) ` to help merging two lists or atomic vectors. `prepend()` is a clearer semantic signal than `[c()](https://rdrr.io/r/base/c.html) ` that a vector is to be merged at the beginning of another, especially in a pipe chain.

Usage[](https://purrr.tidyverse.org/reference/prepend.html#ref-usage)

----------------------------------------------------------------------

    prepend(x, values, before = NULL)

Arguments[](https://purrr.tidyverse.org/reference/prepend.html#arguments)

--------------------------------------------------------------------------

x[](https://purrr.tidyverse.org/reference/prepend.html#arg-x)

the vector to be modified.

values[](https://purrr.tidyverse.org/reference/prepend.html#arg-values)

to be included in the modified vector.

before[](https://purrr.tidyverse.org/reference/prepend.html#arg-before)

a subscript, before which the values are to be appended. If `NULL`, values will be appended at the beginning even for `x` of length 0.

Value[](https://purrr.tidyverse.org/reference/prepend.html#value)

------------------------------------------------------------------

A merged vector.

Examples[](https://purrr.tidyverse.org/reference/prepend.html#ref-examples)

----------------------------------------------------------------------------

    x <- as.list(1:3)
    
    x |> append("a")
    #> [[1]]
    #> [1] 1
    #> 
    #> [[2]]
    #> [1] 2
    #> 
    #> [[3]]
    #> [1] 3
    #> 
    #> [[4]]
    #> [1] "a"
    #> 
    x |> prepend("a")
    #> Warning: `prepend()` was deprecated in purrr 1.0.0.
    #> ℹ Please use append(after = 0) instead.
    #> [[1]]
    #> [1] "a"
    #> 
    #> [[2]]
    #> [1] 1
    #> 
    #> [[3]]
    #> [1] 2
    #> 
    #> [[4]]
    #> [1] 3
    #> 
    x |> prepend(list("a", "b"), before = 3)
    #> [[1]]
    #> [1] 1
    #> 
    #> [[2]]
    #> [1] 2
    #> 
    #> [[3]]
    #> [1] "a"
    #> 
    #> [[4]]
    #> [1] "b"
    #> 
    #> [[5]]
    #> [1] 3
    #> 
    prepend(list(), x)
    #> [[1]]
    #> [1] 1
    #> 
    #> [[2]]
    #> [1] 2
    #> 
    #> [[3]]
    #> [1] 3
    #>