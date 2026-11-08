[Skip to content](https://dplyr.tidyverse.org/reference/all_vars.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Apply predicate to all variables
================================

Source: [`R/colwise.R`](https://github.com/tidyverse/dplyr/blob/main/R/colwise.R)

`all_vars.Rd`

[![[Superseded]](https://dplyr.tidyverse.org/reference/figures/lifecycle-superseded.svg)](https://lifecycle.r-lib.org/articles/stages.html#superseded)

`all_vars()` and `any_vars()` were only needed for the scoped verbs, which have been superseded by the use of `[across()](https://dplyr.tidyverse.org/reference/across.html) ` in an existing verb. See `[vignette("colwise")](https://dplyr.tidyverse.org/articles/colwise.html) ` for details.

These quoting functions signal to scoped filtering verbs (e.g. `[filter_if()](https://dplyr.tidyverse.org/reference/filter_all.html) ` or `[filter_all()](https://dplyr.tidyverse.org/reference/filter_all.html) `) that a predicate expression should be applied to all relevant variables. The `all_vars()` variant takes the intersection of the predicate expressions with `&` while the `any_vars()` variant takes the union with `|`.

Usage[](https://dplyr.tidyverse.org/reference/all_vars.html#ref-usage)

-----------------------------------------------------------------------

    all_vars(expr)
    
    any_vars(expr)

Arguments[](https://dplyr.tidyverse.org/reference/all_vars.html#arguments)

---------------------------------------------------------------------------

expr[](https://dplyr.tidyverse.org/reference/all_vars.html#arg-expr)

<`[data-masking](https://rlang.r-lib.org/reference/args_data_masking.html) `\> An expression that returns a logical vector, using `.` to refer to the "current" variable.

See also[](https://dplyr.tidyverse.org/reference/all_vars.html#see-also)

-------------------------------------------------------------------------

`[vars()](https://dplyr.tidyverse.org/reference/vars.html) ` for other quoting functions that you can use with scoped verbs.