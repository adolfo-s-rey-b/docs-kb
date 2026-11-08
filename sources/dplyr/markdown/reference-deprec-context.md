[Skip to content](https://dplyr.tidyverse.org/reference/deprec-context.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Information about the "current" group or variable
=================================================

Source: [`R/deprec-context.R`](https://github.com/tidyverse/dplyr/blob/main/R/deprec-context.R)

`deprec-context.Rd`

[![[Deprecated]](https://dplyr.tidyverse.org/reference/figures/lifecycle-deprecated.svg)](https://lifecycle.r-lib.org/articles/stages.html#deprecated)

These functions were deprecated in dplyr 1.1.0.

*   `cur_data()` is deprecated in favor of `[pick()](https://dplyr.tidyverse.org/reference/pick.html) `.
    
*   `cur_data_all()` is deprecated but does not have a direct replacement as selecting the grouping variables is not well-defined and is unlikely to ever be useful.
    

Usage[](https://dplyr.tidyverse.org/reference/deprec-context.html#ref-usage)

-----------------------------------------------------------------------------

    cur_data()
    
    cur_data_all()