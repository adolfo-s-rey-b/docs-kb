[Skip to content](https://dplyr.tidyverse.org/reference/rowwise.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Group input by rows
===================

Source: [`R/rowwise.R`](https://github.com/tidyverse/dplyr/blob/main/R/rowwise.R)

`rowwise.Rd`

`rowwise()` allows you to compute on a data frame a row-at-a-time. This is most useful when a vectorised function doesn't exist.

Most dplyr verbs preserve row-wise grouping. The exception is `[summarise()](https://dplyr.tidyverse.org/reference/summarise.html) `, which return a [grouped\_df](https://dplyr.tidyverse.org/reference/grouped_df.html)
. You can explicitly ungroup with `[ungroup()](https://dplyr.tidyverse.org/reference/group_by.html) ` or `[as_tibble()](https://tibble.tidyverse.org/reference/as_tibble.html) `, or convert to a [grouped\_df](https://dplyr.tidyverse.org/reference/grouped_df.html)
 with `[group_by()](https://dplyr.tidyverse.org/reference/group_by.html) `.

Usage[](https://dplyr.tidyverse.org/reference/rowwise.html#ref-usage)

----------------------------------------------------------------------

    rowwise(data, ...)

Arguments[](https://dplyr.tidyverse.org/reference/rowwise.html#arguments)

--------------------------------------------------------------------------

data[](https://dplyr.tidyverse.org/reference/rowwise.html#arg-data)

Input data frame.

...[](https://dplyr.tidyverse.org/reference/rowwise.html#arg--)

<`[tidy-select](https://dplyr.tidyverse.org/reference/dplyr_tidy_select.html) `\> Variables to be preserved when calling `[summarise()](https://dplyr.tidyverse.org/reference/summarise.html) `. This is typically a set of variables whose combination uniquely identify each row.

**NB**: unlike `[group_by()](https://dplyr.tidyverse.org/reference/group_by.html) ` you can not create new variables here but instead you can select multiple variables with (e.g.) `[everything()](https://tidyselect.r-lib.org/reference/everything.html) `.

Value[](https://dplyr.tidyverse.org/reference/rowwise.html#value)

------------------------------------------------------------------

A row-wise data frame with class `rowwise_df`. Note that a `rowwise_df` is implicitly grouped by row, but is not a `grouped_df`.

List-columns[](https://dplyr.tidyverse.org/reference/rowwise.html#list-columns)

--------------------------------------------------------------------------------

Because a rowwise has exactly one row per group it offers a small convenience for working with list-columns. Normally, `[summarise()](https://dplyr.tidyverse.org/reference/summarise.html) ` and `[mutate()](https://dplyr.tidyverse.org/reference/mutate.html) ` extract a groups worth of data with `[`. But when you index a list in this way, you get back another list. When you're working with a `rowwise` tibble, then dplyr will use `[[` instead of `[` to make your life a little easier.\
\
See also[](https://dplyr.tidyverse.org/reference/rowwise.html#see-also)\
\
------------------------------------------------------------------------\
\
`[nest_by()](https://dplyr.tidyverse.org/reference/nest_by.html) ` for a convenient way of creating rowwise data frames with nested data.\
\
Examples[](https://dplyr.tidyverse.org/reference/rowwise.html#ref-examples)\
\
----------------------------------------------------------------------------\
\
    df <- tibble(x = runif(6), y = runif(6), z = runif(6))\
    # Compute the mean of x, y, z in each row\
    df |> rowwise() |> mutate(m = mean(c(x, y, z)))\
    #> # A tibble: 6 × 4\
    #> # Rowwise: \
    #>       x      y      z     m\
    #>   <dbl>  <dbl>  <dbl> <dbl>\
    #> 1 0.837 0.303  0.915  0.685\
    #> 2 0.286 0.159  0.831  0.426\
    #> 3 0.267 0.0400 0.0458 0.118\
    #> 4 0.187 0.219  0.456  0.287\
    #> 5 0.232 0.811  0.265  0.436\
    #> 6 0.317 0.526  0.305  0.382\
    # use c_across() to more easily select many variables\
    df |> rowwise() |> mutate(m = mean(c_across(x:z)))\
    #> # A tibble: 6 × 4\
    #> # Rowwise: \
    #>       x      y      z     m\
    #>   <dbl>  <dbl>  <dbl> <dbl>\
    #> 1 0.837 0.303  0.915  0.685\
    #> 2 0.286 0.159  0.831  0.426\
    #> 3 0.267 0.0400 0.0458 0.118\
    #> 4 0.187 0.219  0.456  0.287\
    #> 5 0.232 0.811  0.265  0.436\
    #> 6 0.317 0.526  0.305  0.382\
    \
    # Compute the minimum of x and y in each row\
    df |> rowwise() |> mutate(m = min(c(x, y, z)))\
    #> # A tibble: 6 × 4\
    #> # Rowwise: \
    #>       x      y      z      m\
    #>   <dbl>  <dbl>  <dbl>  <dbl>\
    #> 1 0.837 0.303  0.915  0.303 \
    #> 2 0.286 0.159  0.831  0.159 \
    #> 3 0.267 0.0400 0.0458 0.0400\
    #> 4 0.187 0.219  0.456  0.187 \
    #> 5 0.232 0.811  0.265  0.232 \
    #> 6 0.317 0.526  0.305  0.305 \
    # In this case you can use an existing vectorised function:\
    df |> mutate(m = pmin(x, y, z))\
    #> # A tibble: 6 × 4\
    #>       x      y      z      m\
    #>   <dbl>  <dbl>  <dbl>  <dbl>\
    #> 1 0.837 0.303  0.915  0.303 \
    #> 2 0.286 0.159  0.831  0.159 \
    #> 3 0.267 0.0400 0.0458 0.0400\
    #> 4 0.187 0.219  0.456  0.187 \
    #> 5 0.232 0.811  0.265  0.232 \
    #> 6 0.317 0.526  0.305  0.305 \
    # Where these functions exist they'll be much faster than rowwise\
    # so be on the lookout for them.\
    \
    # rowwise() is also useful when doing simulations\
    params <- tribble(\
     ~sim, ~n, ~mean, ~sd,\
        1,  1,     1,   1,\
        2,  2,     2,   4,\
        3,  3,    -1,   2\
    )\
    # Here I supply variables to preserve after the computation\
    params |>\
      rowwise(sim) |>\
      reframe(z = rnorm(n, mean, sd))\
    #> # A tibble: 6 × 2\
    #>     sim      z\
    #>   <dbl>  <dbl>\
    #> 1     1  1.02 \
    #> 2     2  4.82 \
    #> 3     2 -0.588\
    #> 4     3  0.736\
    #> 5     3 -0.249\
    #> 6     3 -0.379\
    \
    # If you want one row per simulation, put the results in a list()\
    params |>\
      rowwise(sim) |>\
      summarise(z = list(rnorm(n, mean, sd)), .groups = "keep")\
    #> # A tibble: 3 × 2\
    #> # Groups:   sim [3]\
    #>     sim z        \
    #>   <dbl> <list>   \
    #> 1     1 <dbl [1]>\
    #> 2     2 <dbl [2]>\
    #> 3     3 <dbl [3]>