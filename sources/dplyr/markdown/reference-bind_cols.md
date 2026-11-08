[Skip to content](https://dplyr.tidyverse.org/reference/bind_cols.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Bind multiple data frames by column
===================================

Source: [`R/bind-cols.R`](https://github.com/tidyverse/dplyr/blob/main/R/bind-cols.R)

`bind_cols.Rd`

Bind any number of data frames by column, making a wider result. This is similar to `do.call(cbind, dfs)`.

Where possible prefer using a [join](https://dplyr.tidyverse.org/reference/mutate-joins.html)
 to combine multiple data frames. `bind_cols()` binds the rows in order in which they appear so it is easy to create meaningless results without realising it.

Usage[](https://dplyr.tidyverse.org/reference/bind_cols.html#ref-usage)

------------------------------------------------------------------------

    bind_cols(
      ...,
      .name_repair = c("unique", "universal", "check_unique", "minimal")
    )

Arguments[](https://dplyr.tidyverse.org/reference/bind_cols.html#arguments)

----------------------------------------------------------------------------

...[](https://dplyr.tidyverse.org/reference/bind_cols.html#arg--)

Data frames to combine. Each argument can either be a data frame, a list that could be a data frame, or a list of data frames. Inputs are [recycled](https://vctrs.r-lib.org/reference/theory-faq-recycling.html)
 to the same length, then matched by position.

.name\_repair[](https://dplyr.tidyverse.org/reference/bind_cols.html#arg--name-repair)

One of `"unique"`, `"universal"`, or `"check_unique"`. See `[vctrs::vec_as_names()](https://vctrs.r-lib.org/reference/vec_as_names.html) ` for the meaning of these options.

Value[](https://dplyr.tidyverse.org/reference/bind_cols.html#value)

--------------------------------------------------------------------

A data frame the same type as the first element of `...`.

Examples[](https://dplyr.tidyverse.org/reference/bind_cols.html#ref-examples)

------------------------------------------------------------------------------

    df1 <- tibble(x = 1:3)
    df2 <- tibble(y = 3:1)
    bind_cols(df1, df2)
    #> # A tibble: 3 × 2
    #>       x     y
    #>   <int> <int>
    #> 1     1     3
    #> 2     2     2
    #> 3     3     1
    
    # Row sizes must be compatible when column-binding
    try(bind_cols(tibble(x = 1:3), tibble(y = 1:2)))
    #> Error in bind_cols(tibble(x = 1:3), tibble(y = 1:2)) : 
    #>   Can't recycle `..1` (size 3) to match `..2` (size 2).