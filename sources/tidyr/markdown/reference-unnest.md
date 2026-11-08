[Skip to content](https://tidyr.tidyverse.org/reference/unnest.html#container)

![](https://tidyr.tidyverse.org/logo.png)

Unnest a list-column of data frames into rows and columns
=========================================================

Source: [`R/unnest.R`](https://github.com/tidyverse/tidyr/blob/main/R/unnest.R)

`unnest.Rd`

Unnest expands a list-column containing data frames into rows and columns.

Usage[](https://tidyr.tidyverse.org/reference/unnest.html#ref-usage)

---------------------------------------------------------------------

    unnest(
      data,
      cols,
      ...,
      keep_empty = FALSE,
      ptype = NULL,
      names_sep = NULL,
      names_repair = "check_unique",
      .drop = deprecated(),
      .id = deprecated(),
      .sep = deprecated(),
      .preserve = deprecated()
    )

Arguments[](https://tidyr.tidyverse.org/reference/unnest.html#arguments)

-------------------------------------------------------------------------

data[](https://tidyr.tidyverse.org/reference/unnest.html#arg-data)

A data frame.

cols[](https://tidyr.tidyverse.org/reference/unnest.html#arg-cols)

<`[tidy-select](https://tidyr.tidyverse.org/reference/tidyr_tidy_select.html) `\> List-columns to unnest.

When selecting multiple columns, values from the same row will be recycled to their common size.

...[](https://tidyr.tidyverse.org/reference/unnest.html#arg--)

[![[Deprecated]](https://tidyr.tidyverse.org/reference/figures/lifecycle-deprecated.svg)](https://lifecycle.r-lib.org/articles/stages.html#deprecated)
: previously you could write `df |> unnest(x, y, z)`. Convert to `df |> unnest(c(x, y, z))`. If you previously created a new variable in `unnest()` you'll now need to do it explicitly with `mutate()`. Convert `df |> unnest(y = fun(x, y, z))` to `df |> mutate(y = fun(x, y, z)) |> unnest(y)`.

keep\_empty[](https://tidyr.tidyverse.org/reference/unnest.html#arg-keep-empty)

By default, you get one row of output for each element of the list that you are unchopping/unnesting. This means that if there's a size-0 element (like `NULL` or an empty data frame or vector), then that entire row will be dropped from the output. If you want to preserve all rows, use `keep_empty = TRUE` to replace size-0 elements with a single row of missing values.

ptype[](https://tidyr.tidyverse.org/reference/unnest.html#arg-ptype)

Optionally, a named list of column name-prototype pairs to coerce `cols` to, overriding the default that will be guessed from combining the individual values. Alternatively, a single empty ptype can be supplied, which will be applied to all `cols`.

names\_sep[](https://tidyr.tidyverse.org/reference/unnest.html#arg-names-sep)

If `NULL`, the default, the outer names will come from the inner names. If a string, the outer names will be formed by pasting together the outer and the inner column names, separated by `names_sep`.

names\_repair[](https://tidyr.tidyverse.org/reference/unnest.html#arg-names-repair)

Used to check that output data frame has valid names. Must be one of the following options:

*   `"minimal`": no name repair or checks, beyond basic existence,
    
*   `"unique`": make sure names are unique and not empty,
    
*   `"check_unique`": (the default), no name repair, but check they are unique,
    
*   `"universal`": make the names unique and syntactic
    
*   a function: apply custom name repair.
    
*   [tidyr\_legacy](https://tidyr.tidyverse.org/reference/tidyr_legacy.html)
    : use the name repair from tidyr 0.8.
    
*   a formula: a purrr-style anonymous function (see `[rlang::as_function()](https://rlang.r-lib.org/reference/as_function.html) `)
    

See `[vctrs::vec_as_names()](https://vctrs.r-lib.org/reference/vec_as_names.html) ` for more details on these terms and the strategies used to enforce them.

.drop, .preserve[](https://tidyr.tidyverse.org/reference/unnest.html#arg--drop-preserve)

[![[Deprecated]](https://tidyr.tidyverse.org/reference/figures/lifecycle-deprecated.svg)](https://lifecycle.r-lib.org/articles/stages.html#deprecated)
: all list-columns are now preserved; If there are any that you don't want in the output use `select()` to remove them prior to unnesting.

.id[](https://tidyr.tidyverse.org/reference/unnest.html#arg--id)

[![[Deprecated]](https://tidyr.tidyverse.org/reference/figures/lifecycle-deprecated.svg)](https://lifecycle.r-lib.org/articles/stages.html#deprecated)
: convert `df |> unnest(x, .id = "id")` to `df |> mutate(id = names(x)) |> unnest(x))`.

.sep[](https://tidyr.tidyverse.org/reference/unnest.html#arg--sep)

[![[Deprecated]](https://tidyr.tidyverse.org/reference/figures/lifecycle-deprecated.svg)](https://lifecycle.r-lib.org/articles/stages.html#deprecated)
: use `names_sep` instead.

New syntax[](https://tidyr.tidyverse.org/reference/unnest.html#new-syntax)

---------------------------------------------------------------------------

tidyr 1.0.0 introduced a new syntax for `[nest()](https://tidyr.tidyverse.org/reference/nest.html) ` and `unnest()` that's designed to be more similar to other functions. Converting to the new syntax should be straightforward (guided by the message you'll receive) but if you just need to run an old analysis, you can easily revert to the previous behaviour using `[nest_legacy()](https://tidyr.tidyverse.org/reference/nest_legacy.html) ` and `[unnest_legacy()](https://tidyr.tidyverse.org/reference/nest_legacy.html) ` as follows:

    library(tidyr)
    nest <- nest_legacy
    unnest <- unnest_legacy

See also[](https://tidyr.tidyverse.org/reference/unnest.html#see-also)

-----------------------------------------------------------------------

Other rectangling: `[hoist()](https://tidyr.tidyverse.org/reference/hoist.html) `, `[unnest_longer()](https://tidyr.tidyverse.org/reference/unnest_longer.html) `, `[unnest_wider()](https://tidyr.tidyverse.org/reference/unnest_wider.html) `

Examples[](https://tidyr.tidyverse.org/reference/unnest.html#ref-examples)

---------------------------------------------------------------------------

    # unnest() is designed to work with lists of data frames
    df <- tibble(
      x = 1:3,
      y = list(
        NULL,
        tibble(a = 1, b = 2),
        tibble(a = 1:3, b = 3:1, c = 4)
      )
    )
    # unnest() recycles input rows for each row of the list-column
    # and adds a column for each column
    df |> unnest(y)
    #> # A tibble: 4 × 4
    #>       x     a     b     c
    #>   <int> <dbl> <dbl> <dbl>
    #> 1     2     1     2    NA
    #> 2     3     1     3     4
    #> 3     3     2     2     4
    #> 4     3     3     1     4
    
    # input rows with 0 rows in the list-column will usually disappear,
    # but you can keep them (generating NAs) with keep_empty = TRUE:
    df |> unnest(y, keep_empty = TRUE)
    #> # A tibble: 5 × 4
    #>       x     a     b     c
    #>   <int> <dbl> <dbl> <dbl>
    #> 1     1    NA    NA    NA
    #> 2     2     1     2    NA
    #> 3     3     1     3     4
    #> 4     3     2     2     4
    #> 5     3     3     1     4
    
    # Multiple columns ----------------------------------------------------------
    # You can unnest multiple columns simultaneously
    df <- tibble(
      x = 1:2,
      y = list(
        tibble(a = 1, b = 2),
        tibble(a = 3:4, b = 5:6)
      ),
      z = list(
        tibble(c = 1, d = 2),
        tibble(c = 3:4, d = 5:6)
      )
    )
    df |> unnest(c(y, z))
    #> # A tibble: 3 × 5
    #>       x     a     b     c     d
    #>   <int> <dbl> <dbl> <dbl> <dbl>
    #> 1     1     1     2     1     2
    #> 2     2     3     5     3     5
    #> 3     2     4     6     4     6
    
    # Compare with unnesting one column at a time, which generates
    # the Cartesian product
    df |>
      unnest(y) |>
      unnest(z)
    #> # A tibble: 5 × 5
    #>       x     a     b     c     d
    #>   <int> <dbl> <dbl> <dbl> <dbl>
    #> 1     1     1     2     1     2
    #> 2     2     3     5     3     5
    #> 3     2     3     5     4     6
    #> 4     2     4     6     3     5
    #> 5     2     4     6     4     6