[Skip to content](https://dplyr.tidyverse.org/reference/tbl_vars.html#container)

![](https://dplyr.tidyverse.org/logo.png)

List variables provided by a tbl.
=================================

Source: [`R/tbl.R`](https://github.com/tidyverse/dplyr/blob/main/R/tbl.R)

`tbl_vars.Rd`

`tbl_vars()` returns all variables while `tbl_nongroup_vars()` returns only non-grouping variables. The `groups` attribute of the object returned by `tbl_vars()` is a character vector of the grouping columns.

Usage[](https://dplyr.tidyverse.org/reference/tbl_vars.html#ref-usage)

-----------------------------------------------------------------------

    tbl_vars(x)
    
    tbl_nongroup_vars(x)

Arguments[](https://dplyr.tidyverse.org/reference/tbl_vars.html#arguments)

---------------------------------------------------------------------------

x[](https://dplyr.tidyverse.org/reference/tbl_vars.html#arg-x)

A tbl object

See also[](https://dplyr.tidyverse.org/reference/tbl_vars.html#see-also)

-------------------------------------------------------------------------

`[group_vars()](https://dplyr.tidyverse.org/reference/group_data.html) ` for a function that returns grouping variables.