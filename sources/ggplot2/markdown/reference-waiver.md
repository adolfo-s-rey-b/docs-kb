[Skip to content](https://ggplot2.tidyverse.org/reference/waiver.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

A waiver object.
================

Source: [`R/utilities.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/utilities.R)

`waiver.Rd`

A waiver is a "flag" object, similar to `NULL`, that indicates the calling function should just use the default value. It is used in certain functions to distinguish between displaying nothing (`NULL`) and displaying a default value calculated elsewhere (`waiver()`). `is_waiver()` reports whether an object is a waiver.

Usage[](https://ggplot2.tidyverse.org/reference/waiver.html#ref-usage)

-----------------------------------------------------------------------

    waiver()
    
    is_waiver(x)

Arguments[](https://ggplot2.tidyverse.org/reference/waiver.html#arguments)

---------------------------------------------------------------------------

x[](https://ggplot2.tidyverse.org/reference/waiver.html#arg-x)

An object to test