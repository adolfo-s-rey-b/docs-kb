[Skip to content](https://purrr.tidyverse.org/reference/as_vector.html#container)

![](https://purrr.tidyverse.org/logo.png)

Coerce a list to a vector
=========================

Source: [`R/superseded-simplify.R`](https://github.com/tidyverse/purrr/blob/main/R/superseded-simplify.R)

`as_vector.Rd`

[![[Superseded]](https://purrr.tidyverse.org/reference/figures/lifecycle-superseded.svg)](https://lifecycle.r-lib.org/articles/stages.html#superseded)

These functions were superseded in purrr 1.0.0 in favour of `[list_simplify()](https://purrr.tidyverse.org/reference/list_simplify.html) ` which has more consistent semantics based on vctrs principles:

*   `as_vector(x)` is now `list_simplify(x)`
    
*   `simplify(x)` is now `list_simplify(x, strict = FALSE)`
    
*   `simplify_all(x)` is `map(x, list_simplify, strict = FALSE)`
    

Superseded functions will not go away, but will only receive critical bug fixes.

Usage[](https://purrr.tidyverse.org/reference/as_vector.html#ref-usage)

------------------------------------------------------------------------

    as_vector(.x, .type = NULL)
    
    simplify(.x, .type = NULL)
    
    simplify_all(.x, .type = NULL)

Arguments[](https://purrr.tidyverse.org/reference/as_vector.html#arguments)

----------------------------------------------------------------------------

.x[](https://purrr.tidyverse.org/reference/as_vector.html#arg--x)

A list of vectors

.type[](https://purrr.tidyverse.org/reference/as_vector.html#arg--type)

Can be a vector mold specifying both the type and the length of the vectors to be concatenated, such as `numeric(1)` or `integer(4)`. Alternatively, it can be a string describing the type, one of: "logical", "integer", "double", "complex", "character" or "raw".

Examples[](https://purrr.tidyverse.org/reference/as_vector.html#ref-examples)

------------------------------------------------------------------------------

    # was
    as.list(letters) |> as_vector("character")
    #>  [1] "a" "b" "c" "d" "e" "f" "g" "h" "i" "j" "k" "l" "m" "n" "o" "p"
    #> [17] "q" "r" "s" "t" "u" "v" "w" "x" "y" "z"
    # now
    as.list(letters) |> list_simplify(ptype = character())
    #>  [1] "a" "b" "c" "d" "e" "f" "g" "h" "i" "j" "k" "l" "m" "n" "o" "p"
    #> [17] "q" "r" "s" "t" "u" "v" "w" "x" "y" "z"
    
    # was:
    list(1:2, 3:4, 5:6) |> as_vector(integer(2))
    #> [1] 1 2 3 4 5 6
    # now:
    list(1:2, 3:4, 5:6) |> list_c(ptype = integer())
    #> [1] 1 2 3 4 5 6