[Skip to content](https://dplyr.tidyverse.org/reference/make_tbl.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Create a "tbl" object
=====================

Source: [`R/tbl.R`](https://github.com/tidyverse/dplyr/blob/main/R/tbl.R)

`make_tbl.Rd`

`[tbl()](https://dplyr.tidyverse.org/reference/tbl.html) ` is the standard constructor for tbls. `[is.tbl()](https://dplyr.tidyverse.org/reference/tbl.html) ` tests.

Usage[](https://dplyr.tidyverse.org/reference/make_tbl.html#ref-usage)

-----------------------------------------------------------------------

    make_tbl(subclass, ...)

Arguments[](https://dplyr.tidyverse.org/reference/make_tbl.html#arguments)

---------------------------------------------------------------------------

subclass[](https://dplyr.tidyverse.org/reference/make_tbl.html#arg-subclass)

name of subclass. "tbl" is an abstract base class, so you must supply this value. `tbl_` is automatically prepended to the class name

...[](https://dplyr.tidyverse.org/reference/make_tbl.html#arg--)

For `[tbl()](https://dplyr.tidyverse.org/reference/tbl.html) `, other fields used by class.