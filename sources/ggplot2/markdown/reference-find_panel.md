[Skip to content](https://ggplot2.tidyverse.org/reference/find_panel.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Find panels in a gtable
=======================

Source: [`R/facet-.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/facet-.R)

`find_panel.Rd`

These functions help detect the placement of panels in a gtable, if they are named with "panel" in the beginning. `find_panel()` returns the extend of the panel area, while `panel_cols()` and `panel_rows()` returns the columns and rows that contains panels respectively.

Usage[](https://ggplot2.tidyverse.org/reference/find_panel.html#ref-usage)

---------------------------------------------------------------------------

    find_panel(table)
    
    panel_cols(table)
    
    panel_rows(table)

Arguments[](https://ggplot2.tidyverse.org/reference/find_panel.html#arguments)

-------------------------------------------------------------------------------

table[](https://ggplot2.tidyverse.org/reference/find_panel.html#arg-table)

A gtable

Value[](https://ggplot2.tidyverse.org/reference/find_panel.html#value)

-----------------------------------------------------------------------

A data.frame with some or all of the columns t(op), r(ight), b(ottom), and l(eft)