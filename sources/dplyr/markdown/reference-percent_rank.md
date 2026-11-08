[Skip to content](https://dplyr.tidyverse.org/reference/percent_rank.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Proportional ranking functions
==============================

Source: [`R/rank.R`](https://github.com/tidyverse/dplyr/blob/main/R/rank.R)

`percent_rank.Rd`

These two ranking functions implement two slightly different ways to compute a percentile. For each `x_i` in `x`:

*   `cume_dist(x)` counts the total number of values less than or equal to `x_i`, and divides it by the number of observations.
    
*   `percent_rank(x)` counts the total number of values less than `x_i`, and divides it by the number of observations minus 1.
    

In both cases, missing values are ignored when counting the number of observations.

Usage[](https://dplyr.tidyverse.org/reference/percent_rank.html#ref-usage)

---------------------------------------------------------------------------

    percent_rank(x)
    
    cume_dist(x)

Arguments[](https://dplyr.tidyverse.org/reference/percent_rank.html#arguments)

-------------------------------------------------------------------------------

x[](https://dplyr.tidyverse.org/reference/percent_rank.html#arg-x)

A vector to rank

By default, the smallest values will get the smallest ranks. Use `[desc()](https://dplyr.tidyverse.org/reference/desc.html) ` to reverse the direction so the largest values get the smallest ranks.

Missing values will be given rank `NA`. Use `coalesce(x, Inf)` or `coalesce(x, -Inf)` if you want to treat them as the largest or smallest values respectively.

To rank by multiple columns at once, supply a data frame.

Value[](https://dplyr.tidyverse.org/reference/percent_rank.html#value)

-----------------------------------------------------------------------

A numeric vector containing a proportion.

See also[](https://dplyr.tidyverse.org/reference/percent_rank.html#see-also)

-----------------------------------------------------------------------------

Other ranking functions: `[ntile()](https://dplyr.tidyverse.org/reference/ntile.html) `, `[row_number()](https://dplyr.tidyverse.org/reference/row_number.html) `

Examples[](https://dplyr.tidyverse.org/reference/percent_rank.html#ref-examples)

---------------------------------------------------------------------------------

    x <- c(5, 1, 3, 2, 2)
    
    cume_dist(x)
    #> [1] 1.0 0.2 0.8 0.6 0.6
    percent_rank(x)
    #> [1] 1.00 0.00 0.75 0.25 0.25
    
    # You can understand what's going on by computing it by hand
    sapply(x, function(xi) sum(x <= xi) / length(x))
    #> [1] 1.0 0.2 0.8 0.6 0.6
    sapply(x, function(xi) sum(x < xi)  / (length(x) - 1))
    #> [1] 1.00 0.00 0.75 0.25 0.25
    # The real computations are a little more complex in order to
    # correctly deal with missing values