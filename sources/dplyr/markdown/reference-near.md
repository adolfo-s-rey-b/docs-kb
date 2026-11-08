[Skip to content](https://dplyr.tidyverse.org/reference/near.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Compare two numeric vectors
===========================

Source: [`R/near.R`](https://github.com/tidyverse/dplyr/blob/main/R/near.R)

`near.Rd`

This is a safe way of comparing if two vectors of floating point numbers are (pairwise) equal. This is safer than using `==`, because it has a built in tolerance

Usage[](https://dplyr.tidyverse.org/reference/near.html#ref-usage)

-------------------------------------------------------------------

    near(x, y, tol = .Machine$double.eps^0.5)

Arguments[](https://dplyr.tidyverse.org/reference/near.html#arguments)

-----------------------------------------------------------------------

x, y[](https://dplyr.tidyverse.org/reference/near.html#arg-x-y)

Numeric vectors to compare

tol[](https://dplyr.tidyverse.org/reference/near.html#arg-tol)

Tolerance of comparison.

Examples[](https://dplyr.tidyverse.org/reference/near.html#ref-examples)

-------------------------------------------------------------------------

    sqrt(2) ^ 2 == 2
    #> [1] FALSE
    near(sqrt(2) ^ 2, 2)
    #> [1] TRUE