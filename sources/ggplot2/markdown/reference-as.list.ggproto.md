[Skip to content](https://ggplot2.tidyverse.org/reference/as.list.ggproto.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Convert a ggproto object to a list
==================================

Source: [`R/ggproto.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/ggproto.R)

`as.list.ggproto.Rd`

This will not include the object's `super` member.

Usage[](https://ggplot2.tidyverse.org/reference/as.list.ggproto.html#ref-usage)

--------------------------------------------------------------------------------

    # S3 method for class 'ggproto'
    as.list(x, inherit = TRUE, ...)

Arguments[](https://ggplot2.tidyverse.org/reference/as.list.ggproto.html#arguments)

------------------------------------------------------------------------------------

x[](https://ggplot2.tidyverse.org/reference/as.list.ggproto.html#arg-x)

A ggproto object to convert to a list.

inherit[](https://ggplot2.tidyverse.org/reference/as.list.ggproto.html#arg-inherit)

If `TRUE` (the default), flatten all inherited items into the returned list. If `FALSE`, do not include any inherited items.

...[](https://ggplot2.tidyverse.org/reference/as.list.ggproto.html#arg--)

Arguments passed on to `[base::as.list.environment](https://rdrr.io/r/base/list.html) `

`all.names`

a logical indicating whether to copy all values or (default) only those whose names do not begin with a dot.

`sorted`

a logical indicating whether the `[names](https://rdrr.io/r/base/names.html) ` of the resulting list should be sorted (increasingly). Note that this is somewhat costly, but may be useful for comparison of environments.