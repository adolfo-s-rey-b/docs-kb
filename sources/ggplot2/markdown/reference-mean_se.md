[Skip to content](https://ggplot2.tidyverse.org/reference/mean_se.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Calculate mean and standard error of the mean
=============================================

Source: [`R/stat-summary.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/stat-summary.R)

`mean_se.Rd`

For use with `[stat_summary()](https://ggplot2.tidyverse.org/reference/stat_summary.html) `

Usage[](https://ggplot2.tidyverse.org/reference/mean_se.html#ref-usage)

------------------------------------------------------------------------

    mean_se(x, mult = 1)

Arguments[](https://ggplot2.tidyverse.org/reference/mean_se.html#arguments)

----------------------------------------------------------------------------

x[](https://ggplot2.tidyverse.org/reference/mean_se.html#arg-x)

numeric vector.

mult[](https://ggplot2.tidyverse.org/reference/mean_se.html#arg-mult)

number of multiples of standard error.

Value[](https://ggplot2.tidyverse.org/reference/mean_se.html#value)

--------------------------------------------------------------------

A data frame with three columns:

`y`

The mean.

`ymin`

The mean minus the multiples of the standard error.

`ymax`

The mean plus the multiples of the standard error.

Examples[](https://ggplot2.tidyverse.org/reference/mean_se.html#ref-examples)

------------------------------------------------------------------------------

    set.seed(1)
    x <- rnorm(100)
    mean_se(x)
    #>           y       ymin      ymax
    #> 1 0.1088874 0.01906743 0.1987073