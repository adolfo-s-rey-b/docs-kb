[Skip to content](https://dplyr.tidyverse.org/reference/sql.html#container)

![](https://dplyr.tidyverse.org/logo.png)

SQL escaping.
=============

Source: [`R/compat-dbplyr.R`](https://github.com/tidyverse/dplyr/blob/main/R/compat-dbplyr.R)

`sql.Rd`

These functions are critical when writing functions that translate R functions to sql functions. Typically a conversion function should escape all its inputs and return an sql object.

Usage[](https://dplyr.tidyverse.org/reference/sql.html#ref-usage)

------------------------------------------------------------------

    sql(...)

Arguments[](https://dplyr.tidyverse.org/reference/sql.html#arguments)

----------------------------------------------------------------------

...[](https://dplyr.tidyverse.org/reference/sql.html#arg--)

Character vectors that will be combined into a single SQL expression.