[Skip to content](https://purrr.tidyverse.org/reference/update_list.html#container)

![](https://purrr.tidyverse.org/logo.png)

Update a list with formulas
===========================

Source: [`R/list-modify.R`](https://github.com/tidyverse/purrr/blob/main/R/list-modify.R)

`update_list.Rd`

[![[Deprecated]](https://purrr.tidyverse.org/reference/figures/lifecycle-deprecated.svg)](https://lifecycle.r-lib.org/articles/stages.html#deprecated)

`update_list()` was deprecated in purrr 1.0.0, because we no longer believe that functions that use NSE are a good fit for purrr.

`update_list()` handles formulas and quosures that can refer to values existing within the input list. This function is deprecated because we no longer believe that functions that use tidy evaluation are a good fit for purrr.

Usage[](https://purrr.tidyverse.org/reference/update_list.html#ref-usage)

--------------------------------------------------------------------------

    update_list(.x, ...)

Arguments[](https://purrr.tidyverse.org/reference/update_list.html#arguments)

------------------------------------------------------------------------------

.x[](https://purrr.tidyverse.org/reference/update_list.html#arg--x)

List to modify.

...[](https://purrr.tidyverse.org/reference/update_list.html#arg--)

New values of a list. Use `[zap()](https://rlang.r-lib.org/reference/zap.html) ` to remove values.

These values should be either all named or all unnamed. When inputs are all named, they are matched to `.x` by name. When they are all unnamed, they are matched by position.

[Dynamic dots](https://rlang.r-lib.org/reference/dyn-dots.html)
 are supported. In particular, if your replacement values are stored in a list, you can splice that in with `!!!`.