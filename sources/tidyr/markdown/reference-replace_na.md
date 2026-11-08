[Skip to content](https://tidyr.tidyverse.org/reference/replace_na.html#container)

![](https://tidyr.tidyverse.org/logo.png)

Replace NAs with specified values
=================================

Source: [`R/replace_na.R`](https://github.com/tidyverse/tidyr/blob/main/R/replace_na.R)

`replace_na.Rd`

Replace NAs with specified values

Usage[](https://tidyr.tidyverse.org/reference/replace_na.html#ref-usage)

-------------------------------------------------------------------------

    replace_na(data, replace, ...)

Arguments[](https://tidyr.tidyverse.org/reference/replace_na.html#arguments)

-----------------------------------------------------------------------------

data[](https://tidyr.tidyverse.org/reference/replace_na.html#arg-data)

A data frame or vector.

replace[](https://tidyr.tidyverse.org/reference/replace_na.html#arg-replace)

If `data` is a data frame, `replace` takes a named list of values, with one value for each column that has missing values to be replaced. Each value in `replace` will be cast to the type of the column in `data` that it being used as a replacement in.

If `data` is a vector, `replace` takes a single value. This single value replaces all of the missing values in the vector. `replace` will be cast to the type of `data`.

...[](https://tidyr.tidyverse.org/reference/replace_na.html#arg--)

Additional arguments for methods. Currently unused.

Value[](https://tidyr.tidyverse.org/reference/replace_na.html#value)

---------------------------------------------------------------------

`replace_na()` returns an object with the same type as `data`.

See also[](https://tidyr.tidyverse.org/reference/replace_na.html#see-also)

---------------------------------------------------------------------------

`[dplyr::na_if()](https://dplyr.tidyverse.org/reference/na_if.html) ` to replace specified values with `NA`s; `[dplyr::coalesce()](https://dplyr.tidyverse.org/reference/coalesce.html) ` to replaces `NA`s with values from other vectors.

Examples[](https://tidyr.tidyverse.org/reference/replace_na.html#ref-examples)

-------------------------------------------------------------------------------

    # Replace NAs in a data frame
    df <- tibble(x = c(1, 2, NA), y = c("a", NA, "b"))
    df |> replace_na(list(x = 0, y = "unknown"))
    #> # A tibble: 3 × 2
    #>       x y      
    #>   <dbl> <chr>  
    #> 1     1 a      
    #> 2     2 unknown
    #> 3     0 b      
    
    # Replace NAs in a vector
    df |> dplyr::mutate(x = replace_na(x, 0))
    #> # A tibble: 3 × 2
    #>       x y    
    #>   <dbl> <chr>
    #> 1     1 a    
    #> 2     2 NA   
    #> 3     0 b    
    # OR
    df$x |> replace_na(0)
    #> [1] 1 2 0
    df$y |> replace_na("unknown")
    #> [1] "a"       "unknown" "b"      
    
    # Replace NULLs in a list: NULLs are the list-col equivalent of NAs
    df_list <- tibble(z = list(1:5, NULL, 10:20))
    df_list |> replace_na(list(z = list(5)))
    #> # A tibble: 3 × 1
    #>   z         
    #>   <list>    
    #> 1 <int [5]> 
    #> 2 <dbl [1]> 
    #> 3 <int [11]>