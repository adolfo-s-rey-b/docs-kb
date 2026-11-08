[Skip to content](https://dplyr.tidyverse.org/reference/group_nest.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Nest a tibble using a grouping specification
============================================

Source: [`R/group-nest.R`](https://github.com/tidyverse/dplyr/blob/main/R/group-nest.R)

`group_nest.Rd`

[![[Experimental]](https://dplyr.tidyverse.org/reference/figures/lifecycle-experimental.svg)](https://lifecycle.r-lib.org/articles/stages.html#experimental)

Nest a tibble using a grouping specification

Usage[](https://dplyr.tidyverse.org/reference/group_nest.html#ref-usage)

-------------------------------------------------------------------------

    group_nest(.tbl, ..., .key = "data", keep = FALSE)

Arguments[](https://dplyr.tidyverse.org/reference/group_nest.html#arguments)

-----------------------------------------------------------------------------

.tbl[](https://dplyr.tidyverse.org/reference/group_nest.html#arg--tbl)

A tbl

...[](https://dplyr.tidyverse.org/reference/group_nest.html#arg--)

Grouping specification, forwarded to `[group_by()](https://dplyr.tidyverse.org/reference/group_by.html) `

.key[](https://dplyr.tidyverse.org/reference/group_nest.html#arg--key)

the name of the list column

keep[](https://dplyr.tidyverse.org/reference/group_nest.html#arg-keep)

Should the grouping columns be kept in the list column.

Value[](https://dplyr.tidyverse.org/reference/group_nest.html#value)

---------------------------------------------------------------------

A tbl with one row per unique combination of the grouping variables. The first columns are the grouping variables, followed by a list column of tibbles with matching rows of the remaining columns.

Lifecycle[](https://dplyr.tidyverse.org/reference/group_nest.html#lifecycle)

-----------------------------------------------------------------------------

`group_nest()` is not stable because `[tidyr::nest(.by =)](https://tidyr.tidyverse.org/reference/nest.html) ` provides very similar behavior. It may be deprecated in the future.

Grouped data frames[](https://dplyr.tidyverse.org/reference/group_nest.html#grouped-data-frames)

-------------------------------------------------------------------------------------------------

The primary use case for `group_nest()` is with already grouped data frames, typically a result of `[group_by()](https://dplyr.tidyverse.org/reference/group_by.html) `. In this case `group_nest()` only uses the first argument, the grouped tibble, and warns when `...` is used.

Ungrouped data frames[](https://dplyr.tidyverse.org/reference/group_nest.html#ungrouped-data-frames)

-----------------------------------------------------------------------------------------------------

When used on ungrouped data frames, `group_nest()` forwards the `...` to `[group_by()](https://dplyr.tidyverse.org/reference/group_by.html) ` before nesting, therefore the `...` are subject to the data mask.

See also[](https://dplyr.tidyverse.org/reference/group_nest.html#see-also)

---------------------------------------------------------------------------

Other grouping functions: `[group_by()](https://dplyr.tidyverse.org/reference/group_by.html) `, `[group_map()](https://dplyr.tidyverse.org/reference/group_map.html) `, `[group_split()](https://dplyr.tidyverse.org/reference/group_split.html) `, `[group_trim()](https://dplyr.tidyverse.org/reference/group_trim.html) `

Examples[](https://dplyr.tidyverse.org/reference/group_nest.html#ref-examples)

-------------------------------------------------------------------------------

    
    #----- use case 1: a grouped data frame
    iris |>
      group_by(Species) |>
      group_nest()
    #> # A tibble: 3 × 2
    #>   Species                  data
    #>   <fct>      <list<tibble[,4]>>
    #> 1 setosa               [50 × 4]
    #> 2 versicolor           [50 × 4]
    #> 3 virginica            [50 × 4]
    
    # this can be useful if the grouped data has been altered before nesting
    iris |>
      group_by(Species) |>
      filter(Sepal.Length > mean(Sepal.Length)) |>
      group_nest()
    #> # A tibble: 3 × 2
    #>   Species                  data
    #>   <fct>      <list<tibble[,4]>>
    #> 1 setosa               [22 × 4]
    #> 2 versicolor           [24 × 4]
    #> 3 virginica            [22 × 4]
    
    #----- use case 2: using group_nest() on a ungrouped data frame with
    #                  a grouping specification that uses the data mask
    starwars |>
      group_nest(species, homeworld)
    #> # A tibble: 57 × 3
    #>    species  homeworld                  data
    #>    <chr>    <chr>       <list<tibble[,12]>>
    #>  1 Aleena   Aleen Minor            [1 × 12]
    #>  2 Besalisk Ojom                   [1 × 12]
    #>  3 Cerean   Cerea                  [1 × 12]
    #>  4 Chagrian Champala               [1 × 12]
    #>  5 Clawdite Zolan                  [1 × 12]
    #>  6 Droid    Naboo                  [1 × 12]
    #>  7 Droid    Tatooine               [2 × 12]
    #>  8 Droid    NA                     [3 × 12]
    #>  9 Dug      Malastare              [1 × 12]
    #> 10 Ewok     Endor                  [1 × 12]
    #> # ℹ 47 more rows