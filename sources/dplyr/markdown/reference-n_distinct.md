[Skip to content](https://dplyr.tidyverse.org/reference/n_distinct.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Count unique combinations
=========================

Source: [`R/n-distinct.R`](https://github.com/tidyverse/dplyr/blob/main/R/n-distinct.R)

`n_distinct.Rd`

`n_distinct()` counts the number of unique/distinct combinations in a set of one or more vectors. It's a faster and more concise equivalent to `nrow(unique(data.frame(...)))`.

Usage[](https://dplyr.tidyverse.org/reference/n_distinct.html#ref-usage)

-------------------------------------------------------------------------

    n_distinct(..., na.rm = FALSE)

Arguments[](https://dplyr.tidyverse.org/reference/n_distinct.html#arguments)

-----------------------------------------------------------------------------

...[](https://dplyr.tidyverse.org/reference/n_distinct.html#arg--)

Unnamed vectors. If multiple vectors are supplied, then they should have the same length.

na.rm[](https://dplyr.tidyverse.org/reference/n_distinct.html#arg-na-rm)

If `TRUE`, exclude missing observations from the count. If there are multiple vectors in `...`, an observation will be excluded if _any_ of the values are missing.

Value[](https://dplyr.tidyverse.org/reference/n_distinct.html#value)

---------------------------------------------------------------------

A single number.

Examples[](https://dplyr.tidyverse.org/reference/n_distinct.html#ref-examples)

-------------------------------------------------------------------------------

    x <- c(1, 1, 2, 2, 2)
    n_distinct(x)
    #> [1] 2
    
    y <- c(3, 3, NA, 3, 3)
    n_distinct(y)
    #> [1] 2
    n_distinct(y, na.rm = TRUE)
    #> [1] 1
    
    # Pairs (1, 3), (2, 3), and (2, NA) are distinct
    n_distinct(x, y)
    #> [1] 3
    
    # (2, NA) is dropped, leaving 2 distinct combinations
    n_distinct(x, y, na.rm = TRUE)
    #> [1] 2
    
    # Also works with data frames
    n_distinct(data.frame(x, y))
    #> [1] 3