[Skip to content](https://purrr.tidyverse.org/reference/rbernoulli.html#container)

![](https://purrr.tidyverse.org/logo.png)

Generate random sample from a Bernoulli distribution
====================================================

Source: [`R/deprec-utils.R`](https://github.com/tidyverse/purrr/blob/main/R/deprec-utils.R)

`rbernoulli.Rd`

[![[Deprecated]](https://purrr.tidyverse.org/reference/figures/lifecycle-deprecated.svg)](https://lifecycle.r-lib.org/articles/stages.html#deprecated)

This function was deprecated in purrr 1.0.0 because it's not related to the core purpose of purrr.

Usage[](https://purrr.tidyverse.org/reference/rbernoulli.html#ref-usage)

-------------------------------------------------------------------------

    rbernoulli(n, p = 0.5)

Arguments[](https://purrr.tidyverse.org/reference/rbernoulli.html#arguments)

-----------------------------------------------------------------------------

n[](https://purrr.tidyverse.org/reference/rbernoulli.html#arg-n)

Number of samples

p[](https://purrr.tidyverse.org/reference/rbernoulli.html#arg-p)

Probability of getting `TRUE`

Value[](https://purrr.tidyverse.org/reference/rbernoulli.html#value)

---------------------------------------------------------------------

A logical vector

Examples[](https://purrr.tidyverse.org/reference/rbernoulli.html#ref-examples)

-------------------------------------------------------------------------------

    rbernoulli(10)
    #>  [1]  TRUE  TRUE FALSE  TRUE FALSE FALSE  TRUE FALSE  TRUE  TRUE
    rbernoulli(100, 0.1)
    #>   [1] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
    #>  [12] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE  TRUE FALSE
    #>  [23] FALSE FALSE FALSE  TRUE FALSE FALSE FALSE FALSE FALSE  TRUE FALSE
    #>  [34] FALSE FALSE FALSE  TRUE FALSE FALSE FALSE FALSE  TRUE FALSE FALSE
    #>  [45] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE  TRUE
    #>  [56]  TRUE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
    #>  [67] FALSE FALSE  TRUE  TRUE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
    #>  [78] FALSE FALSE FALSE FALSE FALSE  TRUE FALSE FALSE FALSE FALSE FALSE
    #>  [89] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
    #> [100] FALSE