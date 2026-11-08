[Skip to content](https://ggplot2.tidyverse.org/reference/pattern_alpha.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Modify transparency for patterns
================================

Source: [`R/utilities-patterns.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/utilities-patterns.R)

`pattern_alpha.Rd`

This generic allows you to add your own methods for adding transparency to pattern-like objects.

Usage[](https://ggplot2.tidyverse.org/reference/pattern_alpha.html#ref-usage)

------------------------------------------------------------------------------

    pattern_alpha(x, alpha)

Arguments[](https://ggplot2.tidyverse.org/reference/pattern_alpha.html#arguments)

----------------------------------------------------------------------------------

x[](https://ggplot2.tidyverse.org/reference/pattern_alpha.html#arg-x)

Object to be interpreted as pattern.

alpha[](https://ggplot2.tidyverse.org/reference/pattern_alpha.html#arg-alpha)

A `numeric` vector between 0 and 1. If `NA`, alpha values are preserved.

Value[](https://ggplot2.tidyverse.org/reference/pattern_alpha.html#value)

--------------------------------------------------------------------------

`x` with modified transparency