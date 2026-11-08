[Skip to content](https://dplyr.tidyverse.org/reference/dim_desc.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Describing dimensions
=====================

Source: [`R/utils-format.R`](https://github.com/tidyverse/dplyr/blob/main/R/utils-format.R)

`dim_desc.Rd`

Prints the dimensions of an array-like object in a user-friendly manner, substituting `NA` with ?? (for SQL queries).

Usage[](https://dplyr.tidyverse.org/reference/dim_desc.html#ref-usage)

-----------------------------------------------------------------------

    dim_desc(x)

Arguments[](https://dplyr.tidyverse.org/reference/dim_desc.html#arguments)

---------------------------------------------------------------------------

x[](https://dplyr.tidyverse.org/reference/dim_desc.html#arg-x)

Object to show dimensions for.

Examples[](https://dplyr.tidyverse.org/reference/dim_desc.html#ref-examples)

-----------------------------------------------------------------------------

    dim_desc(mtcars)
    #> [1] "[32 x 11]"