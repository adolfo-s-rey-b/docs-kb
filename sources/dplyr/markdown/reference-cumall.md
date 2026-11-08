[Skip to content](https://dplyr.tidyverse.org/reference/cumall.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Cumulative versions of any, all, and mean
=========================================

Source: [`R/funs.R`](https://github.com/tidyverse/dplyr/blob/main/R/funs.R)

`cumall.Rd`

dplyr provides `cumall()`, `cumany()`, and `cummean()` to complete R's set of cumulative functions.

Usage[](https://dplyr.tidyverse.org/reference/cumall.html#ref-usage)

---------------------------------------------------------------------

    cumall(x)
    
    cumany(x)
    
    cummean(x)

Arguments[](https://dplyr.tidyverse.org/reference/cumall.html#arguments)

-------------------------------------------------------------------------

x[](https://dplyr.tidyverse.org/reference/cumall.html#arg-x)

For `cumall()` and `cumany()`, a logical vector; for `cummean()` an integer or numeric vector.

Value[](https://dplyr.tidyverse.org/reference/cumall.html#value)

-----------------------------------------------------------------

A vector the same length as `x`.

Cumulative logical functions[](https://dplyr.tidyverse.org/reference/cumall.html#cumulative-logical-functions)

---------------------------------------------------------------------------------------------------------------

These are particularly useful in conjunction with `[filter()](https://dplyr.tidyverse.org/reference/filter.html) `:

*   `cumall(x)`: all cases until the first `FALSE`.
    
*   `cumall(!x)`: all cases until the first `TRUE`.
    
*   `cumany(x)`: all cases after the first `TRUE`.
    
*   `cumany(!x)`: all cases after the first `FALSE`.
    

Examples[](https://dplyr.tidyverse.org/reference/cumall.html#ref-examples)

---------------------------------------------------------------------------

    # `cummean()` returns a numeric/integer vector of the same length
    # as the input vector.
    x <- c(1, 3, 5, 2, 2)
    cummean(x)
    #> [1] 1.00 2.00 3.00 2.75 2.60
    cumsum(x) / seq_along(x)
    #> [1] 1.00 2.00 3.00 2.75 2.60
    
    # `cumall()` and `cumany()` return logicals
    cumall(x < 5)
    #> [1]  TRUE  TRUE FALSE FALSE FALSE
    cumany(x == 3)
    #> [1] FALSE  TRUE  TRUE  TRUE  TRUE
    
    # `cumall()` vs. `cumany()`
    df <- data.frame(
      date = as.Date("2020-01-01") + 0:6,
      balance = c(100, 50, 25, -25, -50, 30, 120)
    )
    # all rows after first overdraft
    df |> filter(cumany(balance < 0))
    #>         date balance
    #> 1 2020-01-04     -25
    #> 2 2020-01-05     -50
    #> 3 2020-01-06      30
    #> 4 2020-01-07     120
    # all rows until first overdraft
    df |> filter(cumall(!(balance < 0)))
    #>         date balance
    #> 1 2020-01-01     100
    #> 2 2020-01-02      50
    #> 3 2020-01-03      25