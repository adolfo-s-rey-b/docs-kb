[Skip to content](https://dplyr.tidyverse.org/reference/with_groups.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Perform an operation with temporary groups
==========================================

Source: [`R/groups-with.R`](https://github.com/tidyverse/dplyr/blob/main/R/groups-with.R)

`with_groups.Rd`

[![[Superseded]](https://dplyr.tidyverse.org/reference/figures/lifecycle-superseded.svg)](https://lifecycle.r-lib.org/articles/stages.html#superseded)

This was an experimental function that allows you to modify the grouping variables for a single operation; it is superseded in favour of using the `.by` argument to individual verbs.

Usage[](https://dplyr.tidyverse.org/reference/with_groups.html#ref-usage)

--------------------------------------------------------------------------

    with_groups(.data, .groups, .f, ...)

Arguments[](https://dplyr.tidyverse.org/reference/with_groups.html#arguments)

------------------------------------------------------------------------------

.data[](https://dplyr.tidyverse.org/reference/with_groups.html#arg--data)

A data frame

.groups[](https://dplyr.tidyverse.org/reference/with_groups.html#arg--groups)

<`[tidy-select](https://dplyr.tidyverse.org/reference/dplyr_tidy_select.html) `\> One or more variables to group by. Unlike `[group_by()](https://dplyr.tidyverse.org/reference/group_by.html) `, you can only group by existing variables, and you can use tidy-select syntax like `c(x, y, z)` to select multiple variables.

Use `NULL` to temporarily **un**group.

.f[](https://dplyr.tidyverse.org/reference/with_groups.html#arg--f)

Function to apply to regrouped data. Supports purrr-style `~` syntax

...[](https://dplyr.tidyverse.org/reference/with_groups.html#arg--)

Additional arguments passed on to `...`.

Examples[](https://dplyr.tidyverse.org/reference/with_groups.html#ref-examples)

--------------------------------------------------------------------------------

    df <- tibble(g = c(1, 1, 2, 2, 3), x = runif(5))
    
    # Old
    df |>
      with_groups(g, mutate, x_mean = mean(x))
    #> # A tibble: 5 × 3
    #>       g     x x_mean
    #>   <dbl> <dbl>  <dbl>
    #> 1     1 0.185  0.472
    #> 2     1 0.758  0.472
    #> 3     2 0.567  0.749
    #> 4     2 0.932  0.749
    #> 5     3 0.639  0.639
    # New
    df |> mutate(x_mean = mean(x), .by = g)
    #> # A tibble: 5 × 3
    #>       g     x x_mean
    #>   <dbl> <dbl>  <dbl>
    #> 1     1 0.185  0.472
    #> 2     1 0.758  0.472
    #> 3     2 0.567  0.749
    #> 4     2 0.932  0.749
    #> 5     3 0.639  0.639