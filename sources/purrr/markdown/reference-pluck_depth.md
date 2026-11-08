[Skip to content](https://purrr.tidyverse.org/reference/pluck_depth.html#container)

![](https://purrr.tidyverse.org/logo.png)

Compute the depth of a vector
=============================

Source: [`R/pluck-depth.R`](https://github.com/tidyverse/purrr/blob/main/R/pluck-depth.R)

`pluck_depth.Rd`

The depth of a vector is how many levels that you can index/pluck into it. `pluck_depth()` was previously called `vec_depth()`.

Usage[](https://purrr.tidyverse.org/reference/pluck_depth.html#ref-usage)

--------------------------------------------------------------------------

    pluck_depth(x, is_node = NULL)

Arguments[](https://purrr.tidyverse.org/reference/pluck_depth.html#arguments)

------------------------------------------------------------------------------

x[](https://purrr.tidyverse.org/reference/pluck_depth.html#arg-x)

A vector

is\_node[](https://purrr.tidyverse.org/reference/pluck_depth.html#arg-is-node)

Optionally override the default criteria for determine an element can be recursed within. The default matches the behaviour of `[pluck()](https://purrr.tidyverse.org/reference/pluck.html) ` which can recurse into lists and expressions.

Value[](https://purrr.tidyverse.org/reference/pluck_depth.html#value)

----------------------------------------------------------------------

An integer.

Examples[](https://purrr.tidyverse.org/reference/pluck_depth.html#ref-examples)

--------------------------------------------------------------------------------

    x <- list(
      list(),
      list(list()),
      list(list(list(1)))
    )
    pluck_depth(x)
    #> [1] 5
    x |> map_int(pluck_depth)
    #> [1] 1 2 4