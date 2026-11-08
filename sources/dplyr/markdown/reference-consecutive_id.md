[Skip to content](https://dplyr.tidyverse.org/reference/consecutive_id.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Generate a unique identifier for consecutive combinations
=========================================================

Source: [`R/consecutive-id.R`](https://github.com/tidyverse/dplyr/blob/main/R/consecutive-id.R)

`consecutive_id.Rd`

`consecutive_id()` generates a unique identifier that increments every time a variable (or combination of variables) changes. Inspired by `data.table::rleid()`.

Usage[](https://dplyr.tidyverse.org/reference/consecutive_id.html#ref-usage)

-----------------------------------------------------------------------------

    consecutive_id(...)

Arguments[](https://dplyr.tidyverse.org/reference/consecutive_id.html#arguments)

---------------------------------------------------------------------------------

...[](https://dplyr.tidyverse.org/reference/consecutive_id.html#arg--)

Unnamed vectors. If multiple vectors are supplied, then they should have the same length.

Value[](https://dplyr.tidyverse.org/reference/consecutive_id.html#value)

-------------------------------------------------------------------------

A numeric vector the same length as the longest element of `...`.

Examples[](https://dplyr.tidyverse.org/reference/consecutive_id.html#ref-examples)

-----------------------------------------------------------------------------------

    consecutive_id(c(TRUE, TRUE, FALSE, FALSE, TRUE, FALSE, NA, NA))
    #> [1] 1 1 2 2 3 4 5 5
    consecutive_id(c(1, 1, 1, 2, 1, 1, 2, 2))
    #> [1] 1 1 1 2 3 3 4 4
    
    df <- data.frame(x = c(0, 0, 1, 0), y = c(2, 2, 2, 2))
    df |> group_by(x, y) |> summarise(n = n())
    #> `summarise()` has regrouped the output.
    #> ℹ Summaries were computed grouped by x and y.
    #> ℹ Output is grouped by x.
    #> ℹ Use `summarise(.groups = "drop_last")` to silence this message.
    #> ℹ Use `summarise(.by = c(x, y))` for per-operation grouping
    #>   (`?dplyr::dplyr_by`) instead.
    #> # A tibble: 2 × 3
    #> # Groups:   x [2]
    #>       x     y     n
    #>   <dbl> <dbl> <int>
    #> 1     0     2     3
    #> 2     1     2     1
    df |> group_by(id = consecutive_id(x, y), x, y) |> summarise(n = n())
    #> `summarise()` has regrouped the output.
    #> ℹ Summaries were computed grouped by id, x, and y.
    #> ℹ Output is grouped by id and x.
    #> ℹ Use `summarise(.groups = "drop_last")` to silence this message.
    #> ℹ Use `summarise(.by = c(id, x, y))` for per-operation grouping
    #>   (`?dplyr::dplyr_by`) instead.
    #> # A tibble: 3 × 4
    #> # Groups:   id, x [3]
    #>      id     x     y     n
    #>   <int> <dbl> <dbl> <int>
    #> 1     1     0     2     2
    #> 2     2     1     2     1
    #> 3     3     0     2     1