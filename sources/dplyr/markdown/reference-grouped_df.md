[Skip to content](https://dplyr.tidyverse.org/reference/grouped_df.html#container)

![](https://dplyr.tidyverse.org/logo.png)

A grouped data frame.
=====================

Source: [`R/grouped-df.R`](https://github.com/tidyverse/dplyr/blob/main/R/grouped-df.R)

`grouped_df.Rd`

The easiest way to create a grouped data frame is to call the `[group_by()](https://dplyr.tidyverse.org/reference/group_by.html) ` method on a data frame or tbl: this will take care of capturing the unevaluated expressions for you.

These functions are designed for programmatic use. For data analysis purposes see `[group_data()](https://dplyr.tidyverse.org/reference/group_data.html) ` for the accessor functions that retrieve various metadata from a grouped data frames.

Usage[](https://dplyr.tidyverse.org/reference/grouped_df.html#ref-usage)

-------------------------------------------------------------------------

    grouped_df(data, vars, drop = group_by_drop_default(data))
    
    is.grouped_df(x)
    
    is_grouped_df(x)

Arguments[](https://dplyr.tidyverse.org/reference/grouped_df.html#arguments)

-----------------------------------------------------------------------------

data[](https://dplyr.tidyverse.org/reference/grouped_df.html#arg-data)

a tbl or data frame.

vars[](https://dplyr.tidyverse.org/reference/grouped_df.html#arg-vars)

A character vector.

drop[](https://dplyr.tidyverse.org/reference/grouped_df.html#arg-drop)

When `.drop = TRUE`, empty groups are dropped.