[Skip to content](https://tidyr.tidyverse.org/reference/full_seq.html#container)

![](https://tidyr.tidyverse.org/logo.png)

Create the full sequence of values in a vector
==============================================

Source: [`R/seq.R`](https://github.com/tidyverse/tidyr/blob/main/R/seq.R)

`full_seq.Rd`

This is useful if you want to fill in missing values that should have been observed but weren't. For example, `full_seq(c(1, 2, 4, 6), 1)` will return `1:6`.

Usage[](https://tidyr.tidyverse.org/reference/full_seq.html#ref-usage)

-----------------------------------------------------------------------

    full_seq(x, period, tol = 1e-06)

Arguments[](https://tidyr.tidyverse.org/reference/full_seq.html#arguments)

---------------------------------------------------------------------------

x[](https://tidyr.tidyverse.org/reference/full_seq.html#arg-x)

A numeric vector.

period[](https://tidyr.tidyverse.org/reference/full_seq.html#arg-period)

Gap between each observation. The existing data will be checked to ensure that it is actually of this periodicity.

tol[](https://tidyr.tidyverse.org/reference/full_seq.html#arg-tol)

Numerical tolerance for checking periodicity.

Examples[](https://tidyr.tidyverse.org/reference/full_seq.html#ref-examples)

-----------------------------------------------------------------------------

    full_seq(c(1, 2, 4, 5, 10), 1)
    #>  [1]  1  2  3  4  5  6  7  8  9 10