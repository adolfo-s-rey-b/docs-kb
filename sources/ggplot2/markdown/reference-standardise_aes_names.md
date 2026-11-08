[Skip to content](https://ggplot2.tidyverse.org/reference/standardise_aes_names.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Standardise aesthetic names
===========================

Source: [`R/aes.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/aes.R)

`standardise_aes_names.Rd`

This function standardises aesthetic names by converting `color` to `colour` (also in substrings, e.g. `point_color` to `point_colour`) and translating old style R names to ggplot names (eg. `pch` to `shape`, `cex` to `size`).

Usage[](https://ggplot2.tidyverse.org/reference/standardise_aes_names.html#ref-usage)

--------------------------------------------------------------------------------------

    standardise_aes_names(x)

Arguments[](https://ggplot2.tidyverse.org/reference/standardise_aes_names.html#arguments)

------------------------------------------------------------------------------------------

x[](https://ggplot2.tidyverse.org/reference/standardise_aes_names.html#arg-x)

Character vector of aesthetics names, such as `c("colour", "size", "shape")`.

Value[](https://ggplot2.tidyverse.org/reference/standardise_aes_names.html#value)

----------------------------------------------------------------------------------

Character vector of standardised names.