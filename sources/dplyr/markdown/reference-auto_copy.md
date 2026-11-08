[Skip to content](https://dplyr.tidyverse.org/reference/auto_copy.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Copy tables to same source, if necessary
========================================

Source: [`R/copy-to.R`](https://github.com/tidyverse/dplyr/blob/main/R/copy-to.R)

`auto_copy.Rd`

Copy tables to same source, if necessary

Usage[](https://dplyr.tidyverse.org/reference/auto_copy.html#ref-usage)

------------------------------------------------------------------------

    auto_copy(x, y, copy = FALSE, ...)

Arguments[](https://dplyr.tidyverse.org/reference/auto_copy.html#arguments)

----------------------------------------------------------------------------

x, y[](https://dplyr.tidyverse.org/reference/auto_copy.html#arg-x-y)

`y` will be copied to `x`, if necessary.

copy[](https://dplyr.tidyverse.org/reference/auto_copy.html#arg-copy)

If `x` and `y` are not from the same data source, and `copy` is `TRUE`, then `y` will be copied into the same src as `x`. This allows you to join tables across srcs, but it is a potentially expensive operation so you must opt into it.

...[](https://dplyr.tidyverse.org/reference/auto_copy.html#arg--)

Other arguments passed on to methods.