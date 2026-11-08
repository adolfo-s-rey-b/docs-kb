[Skip to content](https://tidyr.tidyverse.org/reference/drop_na.html#container)

![](https://tidyr.tidyverse.org/logo.png)

Drop rows containing missing values
===================================

Source: [`R/drop-na.R`](https://github.com/tidyverse/tidyr/blob/main/R/drop-na.R)

`drop_na.Rd`

`drop_na()` drops rows where any column specified by `...` contains a missing value.

Usage[](https://tidyr.tidyverse.org/reference/drop_na.html#ref-usage)

----------------------------------------------------------------------

    drop_na(data, ...)

Arguments[](https://tidyr.tidyverse.org/reference/drop_na.html#arguments)

--------------------------------------------------------------------------

data[](https://tidyr.tidyverse.org/reference/drop_na.html#arg-data)

A data frame.

...[](https://tidyr.tidyverse.org/reference/drop_na.html#arg--)

<`[tidy-select](https://tidyr.tidyverse.org/reference/tidyr_tidy_select.html) `\> Columns to inspect for missing values. If empty, all columns are used.

Details[](https://tidyr.tidyverse.org/reference/drop_na.html#details)

----------------------------------------------------------------------

Another way to interpret `drop_na()` is that it only keeps the "complete" rows (where no rows contain missing values). Internally, this completeness is computed through `[vctrs::vec_detect_complete()](https://vctrs.r-lib.org/reference/vec_detect_complete.html) `.

Examples[](https://tidyr.tidyverse.org/reference/drop_na.html#ref-examples)

----------------------------------------------------------------------------

    df <- tibble(x = c(1, 2, NA), y = c("a", NA, "b"))
    df |> drop_na()
    #> # A tibble: 1 × 2
    #>       x y    
    #>   <dbl> <chr>
    #> 1     1 a    
    df |> drop_na(x)
    #> # A tibble: 2 × 2
    #>       x y    
    #>   <dbl> <chr>
    #> 1     1 a    
    #> 2     2 NA   
    
    vars <- "y"
    df |> drop_na(x, any_of(vars))
    #> # A tibble: 1 × 2
    #>       x y    
    #>   <dbl> <chr>
    #> 1     1 a