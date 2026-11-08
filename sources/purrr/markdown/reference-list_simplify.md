[Skip to content](https://purrr.tidyverse.org/reference/list_simplify.html#container)

![](https://purrr.tidyverse.org/logo.png)

Simplify a list to an atomic or S3 vector
=========================================

Source: [`R/list-simplify.R`](https://github.com/tidyverse/purrr/blob/main/R/list-simplify.R)

`list_simplify.Rd`

Simplification maintains a one-to-one correspondence between the input and output, implying that each element of `x` must contain a one element vector or a one-row data frame. If you don't want to maintain this correspondence, then you probably want either `[list_c()](https://purrr.tidyverse.org/reference/list_c.html) `/`[list_rbind()](https://purrr.tidyverse.org/reference/list_c.html) ` or `[list_flatten()](https://purrr.tidyverse.org/reference/list_flatten.html) `.

Usage[](https://purrr.tidyverse.org/reference/list_simplify.html#ref-usage)

----------------------------------------------------------------------------

    list_simplify(x, ..., strict = TRUE, ptype = NULL)

Arguments[](https://purrr.tidyverse.org/reference/list_simplify.html#arguments)

--------------------------------------------------------------------------------

x[](https://purrr.tidyverse.org/reference/list_simplify.html#arg-x)

A list.

...[](https://purrr.tidyverse.org/reference/list_simplify.html#arg--)

These dots are for future extensions and must be empty.

strict[](https://purrr.tidyverse.org/reference/list_simplify.html#arg-strict)

What should happen if simplification fails? If `TRUE` (the default) it will error. If `FALSE` and `ptype` is not supplied, it will return `x` unchanged.

ptype[](https://purrr.tidyverse.org/reference/list_simplify.html#arg-ptype)

An optional prototype to ensure that the output type is always the same.

Value[](https://purrr.tidyverse.org/reference/list_simplify.html#value)

------------------------------------------------------------------------

A vector the same length as `x`.

Examples[](https://purrr.tidyverse.org/reference/list_simplify.html#ref-examples)

----------------------------------------------------------------------------------

    list_simplify(list(1, 2, 3))
    #> [1] 1 2 3
    
    # Only works when vectors are length one and have compatible types:
    try(list_simplify(list(1, 2, 1:3)))
    #> Error in list_simplify(list(1, 2, 1:3)) : 
    #>   `x[[3]]` must have size 1, not size 3.
    try(list_simplify(list(1, 2, "x")))
    #> Error in list_simplify(list(1, 2, "x")) : 
    #>   Can't combine `<list>[[1]]` <double> and `<list>[[3]]` <character>.
    
    # Unless you strict = FALSE, in which case you get the input back:
    list_simplify(list(1, 2, 1:3), strict = FALSE)
    #> [[1]]
    #> [1] 1
    #> 
    #> [[2]]
    #> [1] 2
    #> 
    #> [[3]]
    #> [1] 1 2 3
    #> 
    list_simplify(list(1, 2, "x"), strict = FALSE)
    #> [[1]]
    #> [1] 1
    #> 
    #> [[2]]
    #> [1] 2
    #> 
    #> [[3]]
    #> [1] "x"
    #>