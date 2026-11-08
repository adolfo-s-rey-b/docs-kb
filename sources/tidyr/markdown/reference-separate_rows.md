[Skip to content](https://tidyr.tidyverse.org/reference/separate_rows.html#container)

![](https://tidyr.tidyverse.org/logo.png)

Separate a collapsed column into multiple rows
==============================================

Source: [`R/separate-rows.R`](https://github.com/tidyverse/tidyr/blob/main/R/separate-rows.R)

`separate_rows.Rd`

[![[Superseded]](https://tidyr.tidyverse.org/reference/figures/lifecycle-superseded.svg)](https://lifecycle.r-lib.org/articles/stages.html#superseded)

`separate_rows()` has been superseded in favour of `[separate_longer_delim()](https://tidyr.tidyverse.org/reference/separate_longer_delim.html) ` because it has a more consistent API with other separate functions. Superseded functions will not go away, but will only receive critical bug fixes.

If a variable contains observations with multiple delimited values, `separate_rows()` separates the values and places each one in its own row.

Usage[](https://tidyr.tidyverse.org/reference/separate_rows.html#ref-usage)

----------------------------------------------------------------------------

    separate_rows(data, ..., sep = "[^[:alnum:].]+", convert = FALSE)

Arguments[](https://tidyr.tidyverse.org/reference/separate_rows.html#arguments)

--------------------------------------------------------------------------------

data[](https://tidyr.tidyverse.org/reference/separate_rows.html#arg-data)

A data frame.

...[](https://tidyr.tidyverse.org/reference/separate_rows.html#arg--)

<`[tidy-select](https://tidyr.tidyverse.org/reference/tidyr_tidy_select.html) `\> Columns to separate across multiple rows

sep[](https://tidyr.tidyverse.org/reference/separate_rows.html#arg-sep)

Separator delimiting collapsed values.

convert[](https://tidyr.tidyverse.org/reference/separate_rows.html#arg-convert)

If `TRUE` will automatically run `[type.convert()](https://rdrr.io/r/utils/type.convert.html) ` on the key column. This is useful if the column types are actually numeric, integer, or logical.

Examples[](https://tidyr.tidyverse.org/reference/separate_rows.html#ref-examples)

----------------------------------------------------------------------------------

    df <- tibble(
      x = 1:3,
      y = c("a", "d,e,f", "g,h"),
      z = c("1", "2,3,4", "5,6")
    )
    separate_rows(df, y, z, convert = TRUE)
    #> # A tibble: 6 × 3
    #>       x y         z
    #>   <int> <chr> <int>
    #> 1     1 a         1
    #> 2     2 d         2
    #> 3     2 e         3
    #> 4     2 f         4
    #> 5     3 g         5
    #> 6     3 h         6
    
    # Now recommended
    df |>
      separate_longer_delim(c(y, z), delim = ",")
    #> # A tibble: 6 × 3
    #>       x y     z    
    #>   <int> <chr> <chr>
    #> 1     1 a     1    
    #> 2     2 d     2    
    #> 3     2 e     3    
    #> 4     2 f     4    
    #> 5     3 g     5    
    #> 6     3 h     6