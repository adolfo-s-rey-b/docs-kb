[Skip to content](https://dplyr.tidyverse.org/reference/group_by_drop_default.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Default value for .drop argument of group\_by
=============================================

Source: [`R/group-by.R`](https://github.com/tidyverse/dplyr/blob/main/R/group-by.R)

`group_by_drop_default.Rd`

Default value for .drop argument of group\_by

Usage[](https://dplyr.tidyverse.org/reference/group_by_drop_default.html#ref-usage)

------------------------------------------------------------------------------------

    group_by_drop_default(.tbl)

Arguments[](https://dplyr.tidyverse.org/reference/group_by_drop_default.html#arguments)

----------------------------------------------------------------------------------------

.tbl[](https://dplyr.tidyverse.org/reference/group_by_drop_default.html#arg--tbl)

A data frame

Value[](https://dplyr.tidyverse.org/reference/group_by_drop_default.html#value)

--------------------------------------------------------------------------------

`TRUE` unless `.tbl` is a grouped data frame that was previously obtained by `group_by(.drop = FALSE)`

Examples[](https://dplyr.tidyverse.org/reference/group_by_drop_default.html#ref-examples)

------------------------------------------------------------------------------------------

    group_by_drop_default(iris)
    #> [1] TRUE
    
    iris |>
      group_by(Species) |>
      group_by_drop_default()
    #> [1] TRUE
    
    iris |>
      group_by(Species, .drop = FALSE) |>
      group_by_drop_default()
    #> [1] FALSE