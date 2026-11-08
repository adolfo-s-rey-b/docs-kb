[Skip to content](https://ggplot2.tidyverse.org/reference/resolution.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Compute the "resolution" of a numeric vector
============================================

Source: [`R/utilities-resolution.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/utilities-resolution.R)

`resolution.Rd`

The resolution is the smallest non-zero distance between adjacent values. If there is only one unique value, then the resolution is defined to be one. If x is an integer vector, then it is assumed to represent a discrete variable, and the resolution is 1. If the differences are all smaller than the tolerance, set resolution to 1.

Usage[](https://ggplot2.tidyverse.org/reference/resolution.html#ref-usage)

---------------------------------------------------------------------------

    resolution(x, zero = TRUE, discrete = FALSE)

Arguments[](https://ggplot2.tidyverse.org/reference/resolution.html#arguments)

-------------------------------------------------------------------------------

x[](https://ggplot2.tidyverse.org/reference/resolution.html#arg-x)

numeric vector

zero[](https://ggplot2.tidyverse.org/reference/resolution.html#arg-zero)

should a zero value be automatically included in the computation of resolution

discrete[](https://ggplot2.tidyverse.org/reference/resolution.html#arg-discrete)

should vectors mapped with a discrete scale be treated as having a resolution of 1?

Examples[](https://ggplot2.tidyverse.org/reference/resolution.html#ref-examples)

---------------------------------------------------------------------------------

    resolution(1:10)
    #> [1] 1
    resolution((1:10) - 0.5)
    #> [1] 0.5
    resolution((1:10) - 0.5, FALSE)
    #> [1] 1
    
    # Note the difference between numeric and integer vectors
    resolution(c(2, 10, 20, 50))
    #> [1] 2
    resolution(c(2L, 10L, 20L, 50L))
    #> [1] 1