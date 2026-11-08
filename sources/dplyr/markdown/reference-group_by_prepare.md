[Skip to content](https://dplyr.tidyverse.org/reference/group_by_prepare.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Prepare for grouping and other operations
=========================================

Source: [`R/distinct.R`](https://github.com/tidyverse/dplyr/blob/main/R/distinct.R)
, [`R/group-by.R`](https://github.com/tidyverse/dplyr/blob/main/R/group-by.R)

`group_by_prepare.Rd`

`*_prepare()` performs standard manipulation that is needed prior to actual data processing. They are only be needed by packages that implement dplyr backends.

Usage[](https://dplyr.tidyverse.org/reference/group_by_prepare.html#ref-usage)

-------------------------------------------------------------------------------

    distinct_prepare(
      .data,
      vars,
      group_vars = character(),
      .keep_all = FALSE,
      caller_env = caller_env(2),
      error_call = caller_env()
    )
    
    group_by_prepare(
      .data,
      ...,
      .add = FALSE,
      .dots = deprecated(),
      add = deprecated(),
      error_call = caller_env()
    )

Value[](https://dplyr.tidyverse.org/reference/group_by_prepare.html#value)

---------------------------------------------------------------------------

A list

data

Modified tbl

groups

Modified groups