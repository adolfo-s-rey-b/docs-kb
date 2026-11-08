[Skip to content](https://dplyr.tidyverse.org/reference/tbl_ptype.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Return a prototype of a tbl
===========================

Source: [`R/colwise.R`](https://github.com/tidyverse/dplyr/blob/main/R/colwise.R)

`tbl_ptype.Rd`

Used in `_if` functions to enable type-based selection even when the data is lazily generated. Should either return the complete tibble, or if that can not be computed quickly, a 0-row tibble where the columns are of the correct type.

Usage[](https://dplyr.tidyverse.org/reference/tbl_ptype.html#ref-usage)

------------------------------------------------------------------------

    tbl_ptype(.data)