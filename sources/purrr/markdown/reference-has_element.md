[Skip to content](https://purrr.tidyverse.org/reference/has_element.html#container)

![](https://purrr.tidyverse.org/logo.png)

Does a list contain an object?
==============================

Source: [`R/detect.R`](https://github.com/tidyverse/purrr/blob/main/R/detect.R)

`has_element.Rd`

Does a list contain an object?

Usage[](https://purrr.tidyverse.org/reference/has_element.html#ref-usage)

--------------------------------------------------------------------------

    has_element(.x, .y)

Arguments[](https://purrr.tidyverse.org/reference/has_element.html#arguments)

------------------------------------------------------------------------------

.x[](https://purrr.tidyverse.org/reference/has_element.html#arg--x)

A list or atomic vector.

.y[](https://purrr.tidyverse.org/reference/has_element.html#arg--y)

Object to test for

Examples[](https://purrr.tidyverse.org/reference/has_element.html#ref-examples)

--------------------------------------------------------------------------------

    x <- list(1:10, 5, 9.9)
    x |> has_element(1:10)
    #> [1] TRUE
    x |> has_element(3)
    #> [1] FALSE