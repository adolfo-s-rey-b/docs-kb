[Skip to content](https://dplyr.tidyverse.org/reference/vars.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Select variables
================

Source: [`R/colwise.R`](https://github.com/tidyverse/dplyr/blob/main/R/colwise.R)

`vars.Rd`

[![[Superseded]](https://dplyr.tidyverse.org/reference/figures/lifecycle-superseded.svg)](https://lifecycle.r-lib.org/articles/stages.html#superseded)

`vars()` is superseded because it is only needed for the scoped verbs (i.e. `[mutate_at()](https://dplyr.tidyverse.org/reference/mutate_all.html) `, `[summarise_at()](https://dplyr.tidyverse.org/reference/summarise_all.html) `, and friends), which have been been superseded in favour of `[across()](https://dplyr.tidyverse.org/reference/across.html) `. See `[vignette("colwise")](https://dplyr.tidyverse.org/articles/colwise.html) ` for details.

This helper is intended to provide tidy-select semantics for scoped verbs like `[mutate_at()](https://dplyr.tidyverse.org/reference/mutate_all.html) ` and `[summarise_at()](https://dplyr.tidyverse.org/reference/summarise_all.html) `. Note that anywhere you can supply `vars()` specification, you can also supply a numeric vector of column positions or a character vector of column names.

Usage[](https://dplyr.tidyverse.org/reference/vars.html#ref-usage)

-------------------------------------------------------------------

    vars(...)

Arguments[](https://dplyr.tidyverse.org/reference/vars.html#arguments)

-----------------------------------------------------------------------

...[](https://dplyr.tidyverse.org/reference/vars.html#arg--)

<`[tidy-select](https://dplyr.tidyverse.org/reference/dplyr_tidy_select.html) `\> Variables to operate on.

See also[](https://dplyr.tidyverse.org/reference/vars.html#see-also)

---------------------------------------------------------------------

`[all_vars()](https://dplyr.tidyverse.org/reference/all_vars.html) ` and `[any_vars()](https://dplyr.tidyverse.org/reference/all_vars.html) ` for other quoting functions that you can use with scoped verbs.