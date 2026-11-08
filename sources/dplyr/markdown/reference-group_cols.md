[Skip to content](https://dplyr.tidyverse.org/reference/group_cols.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Select grouping variables
=========================

Source: [`R/select-helpers.R`](https://github.com/tidyverse/dplyr/blob/main/R/select-helpers.R)

`group_cols.Rd`

This selection helpers matches grouping variables. It can be used in `[select()](https://dplyr.tidyverse.org/reference/select.html) ` or `[vars()](https://dplyr.tidyverse.org/reference/vars.html) ` selections.

Usage[](https://dplyr.tidyverse.org/reference/group_cols.html#ref-usage)

-------------------------------------------------------------------------

    group_cols(vars = NULL, data = NULL)

Arguments[](https://dplyr.tidyverse.org/reference/group_cols.html#arguments)

-----------------------------------------------------------------------------

vars[](https://dplyr.tidyverse.org/reference/group_cols.html#arg-vars)

[![[Defunct]](https://dplyr.tidyverse.org/reference/figures/lifecycle-defunct.svg)](https://lifecycle.r-lib.org/articles/stages.html#defunct)

data[](https://dplyr.tidyverse.org/reference/group_cols.html#arg-data)

For advanced use only. The default `NULL` automatically finds the "current" data frames.

See also[](https://dplyr.tidyverse.org/reference/group_cols.html#see-also)

---------------------------------------------------------------------------

`[groups()](https://dplyr.tidyverse.org/reference/group_data.html) ` and `[group_vars()](https://dplyr.tidyverse.org/reference/group_data.html) ` for retrieving the grouping variables outside selection contexts.

Examples[](https://dplyr.tidyverse.org/reference/group_cols.html#ref-examples)

-------------------------------------------------------------------------------

    gdf <- iris |> group_by(Species)
    gdf |> select(group_cols())
    #> # A tibble: 150 × 1
    #> # Groups:   Species [3]
    #>    Species
    #>    <fct>  
    #>  1 setosa 
    #>  2 setosa 
    #>  3 setosa 
    #>  4 setosa 
    #>  5 setosa 
    #>  6 setosa 
    #>  7 setosa 
    #>  8 setosa 
    #>  9 setosa 
    #> 10 setosa 
    #> # ℹ 140 more rows
    
    # Remove the grouping variables from mutate selections:
    gdf |> mutate_at(vars(-group_cols()), `/`, 100)
    #> # A tibble: 150 × 5
    #> # Groups:   Species [3]
    #>    Sepal.Length Sepal.Width Petal.Length Petal.Width Species
    #>           <dbl>       <dbl>        <dbl>       <dbl> <fct>  
    #>  1        0.051       0.035        0.014       0.002 setosa 
    #>  2        0.049       0.03         0.014       0.002 setosa 
    #>  3        0.047       0.032        0.013       0.002 setosa 
    #>  4        0.046       0.031        0.015       0.002 setosa 
    #>  5        0.05        0.036        0.014       0.002 setosa 
    #>  6        0.054       0.039        0.017       0.004 setosa 
    #>  7        0.046       0.034        0.014       0.003 setosa 
    #>  8        0.05        0.034        0.015       0.002 setosa 
    #>  9        0.044       0.029        0.014       0.002 setosa 
    #> 10        0.049       0.031        0.015       0.001 setosa 
    #> # ℹ 140 more rows
    # -> No longer necessary with across()
    gdf |> mutate(across(everything(), ~ . / 100))
    #> # A tibble: 150 × 5
    #> # Groups:   Species [3]
    #>    Sepal.Length Sepal.Width Petal.Length Petal.Width Species
    #>           <dbl>       <dbl>        <dbl>       <dbl> <fct>  
    #>  1        0.051       0.035        0.014       0.002 setosa 
    #>  2        0.049       0.03         0.014       0.002 setosa 
    #>  3        0.047       0.032        0.013       0.002 setosa 
    #>  4        0.046       0.031        0.015       0.002 setosa 
    #>  5        0.05        0.036        0.014       0.002 setosa 
    #>  6        0.054       0.039        0.017       0.004 setosa 
    #>  7        0.046       0.034        0.014       0.003 setosa 
    #>  8        0.05        0.034        0.015       0.002 setosa 
    #>  9        0.044       0.029        0.014       0.002 setosa 
    #> 10        0.049       0.031        0.015       0.001 setosa 
    #> # ℹ 140 more rows