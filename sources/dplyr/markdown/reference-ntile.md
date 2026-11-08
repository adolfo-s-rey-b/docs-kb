[Skip to content](https://dplyr.tidyverse.org/reference/ntile.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Bucket a numeric vector into `n` groups
=======================================

Source: [`R/rank.R`](https://github.com/tidyverse/dplyr/blob/main/R/rank.R)

`ntile.Rd`

`ntile()` is a sort of very rough rank, which breaks the input vector into `n` buckets. If `length(x)` is not an integer multiple of `n`, the size of the buckets will differ by up to one, with larger buckets coming first.

Unlike other ranking functions, `ntile()` ignores ties: it will create evenly sized buckets even if the same value of `x` ends up in different buckets.

Usage[](https://dplyr.tidyverse.org/reference/ntile.html#ref-usage)

--------------------------------------------------------------------

    ntile(x = row_number(), n)

Arguments[](https://dplyr.tidyverse.org/reference/ntile.html#arguments)

------------------------------------------------------------------------

x[](https://dplyr.tidyverse.org/reference/ntile.html#arg-x)

A vector to rank

By default, the smallest values will get the smallest ranks. Use `[desc()](https://dplyr.tidyverse.org/reference/desc.html) ` to reverse the direction so the largest values get the smallest ranks.

Missing values will be given rank `NA`. Use `coalesce(x, Inf)` or `coalesce(x, -Inf)` if you want to treat them as the largest or smallest values respectively.

To rank by multiple columns at once, supply a data frame.

n[](https://dplyr.tidyverse.org/reference/ntile.html#arg-n)

Number of groups to bucket into

See also[](https://dplyr.tidyverse.org/reference/ntile.html#see-also)

----------------------------------------------------------------------

Other ranking functions: `[percent_rank()](https://dplyr.tidyverse.org/reference/percent_rank.html) `, `[row_number()](https://dplyr.tidyverse.org/reference/row_number.html) `

Examples[](https://dplyr.tidyverse.org/reference/ntile.html#ref-examples)

--------------------------------------------------------------------------

    x <- c(5, 1, 3, 2, 2, NA)
    ntile(x, 2)
    #> [1]  2  1  2  1  1 NA
    ntile(x, 4)
    #> [1]  4  1  3  1  2 NA
    
    # If the bucket sizes are uneven, the larger buckets come first
    ntile(1:8, 3)
    #> [1] 1 1 1 2 2 2 3 3
    
    # Ties are ignored
    ntile(rep(1, 8), 3)
    #> [1] 1 1 1 2 2 2 3 3