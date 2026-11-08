[Skip to content](https://dplyr.tidyverse.org/reference/group_trim.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Trim grouping structure
=======================

Source: [`R/group-trim.R`](https://github.com/tidyverse/dplyr/blob/main/R/group-trim.R)

`group_trim.Rd`

[![[Experimental]](https://dplyr.tidyverse.org/reference/figures/lifecycle-experimental.svg)](https://lifecycle.r-lib.org/articles/stages.html#experimental)
 Drop unused levels of all factors that are used as grouping variables, then recalculates the grouping structure.

`group_trim()` is particularly useful after a `[filter()](https://dplyr.tidyverse.org/reference/filter.html) ` that is intended to select a subset of groups.

Usage[](https://dplyr.tidyverse.org/reference/group_trim.html#ref-usage)

-------------------------------------------------------------------------

    group_trim(.tbl, .drop = group_by_drop_default(.tbl))

Arguments[](https://dplyr.tidyverse.org/reference/group_trim.html#arguments)

-----------------------------------------------------------------------------

.tbl[](https://dplyr.tidyverse.org/reference/group_trim.html#arg--tbl)

A [grouped data frame](https://dplyr.tidyverse.org/reference/grouped_df.html)

.drop[](https://dplyr.tidyverse.org/reference/group_trim.html#arg--drop)

See `[group_by()](https://dplyr.tidyverse.org/reference/group_by.html) `

Value[](https://dplyr.tidyverse.org/reference/group_trim.html#value)

---------------------------------------------------------------------

A [grouped data frame](https://dplyr.tidyverse.org/reference/grouped_df.html)

See also[](https://dplyr.tidyverse.org/reference/group_trim.html#see-also)

---------------------------------------------------------------------------

Other grouping functions: `[group_by()](https://dplyr.tidyverse.org/reference/group_by.html) `, `[group_map()](https://dplyr.tidyverse.org/reference/group_map.html) `, `[group_nest()](https://dplyr.tidyverse.org/reference/group_nest.html) `, `[group_split()](https://dplyr.tidyverse.org/reference/group_split.html) `

Examples[](https://dplyr.tidyverse.org/reference/group_trim.html#ref-examples)

-------------------------------------------------------------------------------

    iris |>
      group_by(Species) |>
      filter(Species == "setosa", .preserve = TRUE) |>
      group_trim()
    #> # A tibble: 50 × 5
    #> # Groups:   Species [1]
    #>    Sepal.Length Sepal.Width Petal.Length Petal.Width Species
    #>           <dbl>       <dbl>        <dbl>       <dbl> <fct>  
    #>  1          5.1         3.5          1.4         0.2 setosa 
    #>  2          4.9         3            1.4         0.2 setosa 
    #>  3          4.7         3.2          1.3         0.2 setosa 
    #>  4          4.6         3.1          1.5         0.2 setosa 
    #>  5          5           3.6          1.4         0.2 setosa 
    #>  6          5.4         3.9          1.7         0.4 setosa 
    #>  7          4.6         3.4          1.4         0.3 setosa 
    #>  8          5           3.4          1.5         0.2 setosa 
    #>  9          4.4         2.9          1.4         0.2 setosa 
    #> 10          4.9         3.1          1.5         0.1 setosa 
    #> # ℹ 40 more rows