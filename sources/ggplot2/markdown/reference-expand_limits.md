[Skip to content](https://ggplot2.tidyverse.org/reference/expand_limits.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Expand the plot limits, using data
==================================

Source: [`R/limits.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/limits.R)

`expand_limits.Rd`

[![[Superseded]](https://ggplot2.tidyverse.org/reference/figures/lifecycle-superseded.svg)](https://lifecycle.r-lib.org/articles/stages.html#superseded)
: It is recommended to pass a function to the `limits` argument in scales instead. For example: `scale_x_continuous(limits = ~range(.x, 0))` to include zero.  
  
Sometimes you may want to ensure limits include a single value, for all panels or all plots. This function is a thin wrapper around `[geom_blank()](https://ggplot2.tidyverse.org/reference/geom_blank.html) ` that makes it easy to add such values.

Usage[](https://ggplot2.tidyverse.org/reference/expand_limits.html#ref-usage)

------------------------------------------------------------------------------

    expand_limits(...)

Arguments[](https://ggplot2.tidyverse.org/reference/expand_limits.html#arguments)

----------------------------------------------------------------------------------

...[](https://ggplot2.tidyverse.org/reference/expand_limits.html#arg--)

named list of aesthetics specifying the value (or values) that should be included in each scale.

Examples[](https://ggplot2.tidyverse.org/reference/expand_limits.html#ref-examples)

------------------------------------------------------------------------------------

    p <- ggplot(mtcars, aes(mpg, wt)) + geom_point()
    p + expand_limits(x = 0)
    
    p + expand_limits(y = c(1, 9))
    
    p + expand_limits(x = 0, y = 0)
    
    
    ggplot(mtcars, aes(mpg, wt)) +
      geom_point(aes(colour = cyl)) +
      expand_limits(colour = seq(2, 10, by = 2))
    
    ggplot(mtcars, aes(mpg, wt)) +
      geom_point(aes(colour = factor(cyl))) +
      expand_limits(colour = factor(seq(2, 10, by = 2)))