[Skip to content](https://tidyr.tidyverse.org/reference/unite.html#container)

![](https://tidyr.tidyverse.org/logo.png)

Unite multiple columns into one by pasting strings together
===========================================================

Source: [`R/unite.R`](https://github.com/tidyverse/tidyr/blob/main/R/unite.R)

`unite.Rd`

Convenience function to paste together multiple columns into one.

Usage[](https://tidyr.tidyverse.org/reference/unite.html#ref-usage)

--------------------------------------------------------------------

    unite(data, col, ..., sep = "_", remove = TRUE, na.rm = FALSE)

Arguments[](https://tidyr.tidyverse.org/reference/unite.html#arguments)

------------------------------------------------------------------------

data[](https://tidyr.tidyverse.org/reference/unite.html#arg-data)

A data frame.

col[](https://tidyr.tidyverse.org/reference/unite.html#arg-col)

The name of the new column, as a string or symbol.

This argument is passed by expression and supports [quasiquotation](https://rlang.r-lib.org/reference/topic-inject.html)
 (you can unquote strings and symbols). The name is captured from the expression with `[rlang::ensym()](https://rlang.r-lib.org/reference/defusing-advanced.html) ` (note that this kind of interface where symbols do not represent actual objects is now discouraged in the tidyverse; we support it here for backward compatibility).

...[](https://tidyr.tidyverse.org/reference/unite.html#arg--)

<`[tidy-select](https://tidyr.tidyverse.org/reference/tidyr_tidy_select.html) `\> Columns to unite

sep[](https://tidyr.tidyverse.org/reference/unite.html#arg-sep)

Separator to use between values.

remove[](https://tidyr.tidyverse.org/reference/unite.html#arg-remove)

If `TRUE`, remove input columns from output data frame.

na.rm[](https://tidyr.tidyverse.org/reference/unite.html#arg-na-rm)

If `TRUE`, missing values will be removed prior to uniting each value.

See also[](https://tidyr.tidyverse.org/reference/unite.html#see-also)

----------------------------------------------------------------------

`[separate()](https://tidyr.tidyverse.org/reference/separate.html) `, the complement.

Examples[](https://tidyr.tidyverse.org/reference/unite.html#ref-examples)

--------------------------------------------------------------------------

    df <- expand_grid(x = c("a", NA), y = c("b", NA))
    df
    #> # A tibble: 4 × 2
    #>   x     y    
    #>   <chr> <chr>
    #> 1 a     b    
    #> 2 a     NA   
    #> 3 NA    b    
    #> 4 NA    NA   
    
    df |> unite("z", x:y, remove = FALSE)
    #> # A tibble: 4 × 3
    #>   z     x     y    
    #>   <chr> <chr> <chr>
    #> 1 a_b   a     b    
    #> 2 a_NA  a     NA   
    #> 3 NA_b  NA    b    
    #> 4 NA_NA NA    NA   
    # To remove missing values:
    df |> unite("z", x:y, na.rm = TRUE, remove = FALSE)
    #> # A tibble: 4 × 3
    #>   z     x     y    
    #>   <chr> <chr> <chr>
    #> 1 "a_b" a     b    
    #> 2 "a"   a     NA   
    #> 3 "b"   NA    b    
    #> 4 ""    NA    NA   
    
    # Separate is almost the complement of unite
    df |>
      unite("xy", x:y) |>
      separate(xy, c("x", "y"))
    #> # A tibble: 4 × 2
    #>   x     y    
    #>   <chr> <chr>
    #> 1 a     b    
    #> 2 a     NA   
    #> 3 NA    b    
    #> 4 NA    NA   
    # (but note `x` and `y` contain now "NA" not NA)