[Skip to content](https://dplyr.tidyverse.org/reference/all_equal.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Flexible equality comparison for data frames
============================================

Source: [`R/all-equal.R`](https://github.com/tidyverse/dplyr/blob/main/R/all-equal.R)

`all_equal.Rd`

[![[Deprecated]](https://dplyr.tidyverse.org/reference/figures/lifecycle-deprecated.svg)](https://lifecycle.r-lib.org/articles/stages.html#deprecated)

`all_equal()` allows you to compare data frames, optionally ignoring row and column names. It is deprecated as of dplyr 1.1.0, because it makes it too easy to ignore important differences.

Usage[](https://dplyr.tidyverse.org/reference/all_equal.html#ref-usage)

------------------------------------------------------------------------

    all_equal(
      target,
      current,
      ignore_col_order = TRUE,
      ignore_row_order = TRUE,
      convert = FALSE,
      ...
    )

Arguments[](https://dplyr.tidyverse.org/reference/all_equal.html#arguments)

----------------------------------------------------------------------------

target, current[](https://dplyr.tidyverse.org/reference/all_equal.html#arg-target-current)

Two data frames to compare.

ignore\_col\_order[](https://dplyr.tidyverse.org/reference/all_equal.html#arg-ignore-col-order)

Should order of columns be ignored?

ignore\_row\_order[](https://dplyr.tidyverse.org/reference/all_equal.html#arg-ignore-row-order)

Should order of rows be ignored?

convert[](https://dplyr.tidyverse.org/reference/all_equal.html#arg-convert)

Should similar classes be converted? Currently this will convert factor to character and integer to double.

...[](https://dplyr.tidyverse.org/reference/all_equal.html#arg--)

Ignored. Needed for compatibility with `[all.equal()](https://rdrr.io/r/base/all.equal.html) `.

Value[](https://dplyr.tidyverse.org/reference/all_equal.html#value)

--------------------------------------------------------------------

`TRUE` if equal, otherwise a character vector describing the reasons why they're not equal. Use `[isTRUE()](https://rdrr.io/r/base/Logic.html) ` if using the result in an `if` expression.

Examples[](https://dplyr.tidyverse.org/reference/all_equal.html#ref-examples)

------------------------------------------------------------------------------

    scramble <- function(x) x[sample(nrow(x)), sample(ncol(x))]
    
    # `all_equal()` ignored row and column ordering by default,
    # but we now feel that that makes it too easy to make mistakes
    mtcars2 <- scramble(mtcars)
    all_equal(mtcars, mtcars2)
    #> Warning: `all_equal()` was deprecated in dplyr 1.1.0.
    #> ℹ Please use `all.equal()` instead.
    #> ℹ And manually order the rows/cols as needed
    #> [1] TRUE
    
    # Instead, be explicit about the row and column ordering
    all.equal(
      mtcars,
      mtcars2[rownames(mtcars), names(mtcars)]
    )
    #> [1] TRUE