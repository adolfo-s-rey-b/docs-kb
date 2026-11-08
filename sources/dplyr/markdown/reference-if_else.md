[Skip to content](https://dplyr.tidyverse.org/reference/if_else.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Vectorised if-else
==================

Source: [`R/if-else.R`](https://github.com/tidyverse/dplyr/blob/main/R/if-else.R)

`if_else.Rd`

`if_else()` is a vectorized [if-else](https://rdrr.io/r/base/Control.html)
. Compared to the base R equivalent, `[ifelse()](https://rdrr.io/r/base/ifelse.html) `, this function allows you to handle missing values in the `condition` with `missing` and always takes `true`, `false`, and `missing` into account when determining what the output type should be.

Usage[](https://dplyr.tidyverse.org/reference/if_else.html#ref-usage)

----------------------------------------------------------------------

    if_else(
      condition,
      true,
      false,
      missing = NULL,
      ...,
      ptype = NULL,
      size = deprecated()
    )

Arguments[](https://dplyr.tidyverse.org/reference/if_else.html#arguments)

--------------------------------------------------------------------------

condition[](https://dplyr.tidyverse.org/reference/if_else.html#arg-condition)

A logical vector

true, false[](https://dplyr.tidyverse.org/reference/if_else.html#arg-true-false)

Vectors to use for `TRUE` and `FALSE` values of `condition`.

Both `true` and `false` will be [recycled](https://vctrs.r-lib.org/reference/theory-faq-recycling.html)
 to the size of `condition`.

`true`, `false`, and `missing` (if used) will be cast to their common type.

missing[](https://dplyr.tidyverse.org/reference/if_else.html#arg-missing)

If not `NULL`, will be used as the value for `NA` values of `condition`. Follows the same size and type rules as `true` and `false`.

...[](https://dplyr.tidyverse.org/reference/if_else.html#arg--)

These dots are for future extensions and must be empty.

ptype[](https://dplyr.tidyverse.org/reference/if_else.html#arg-ptype)

An optional prototype declaring the desired output type. If supplied, this overrides the common type of `true`, `false`, and `missing`.

size[](https://dplyr.tidyverse.org/reference/if_else.html#arg-size)

[![[Deprecated]](https://dplyr.tidyverse.org/reference/figures/lifecycle-deprecated.svg)](https://lifecycle.r-lib.org/articles/stages.html#deprecated)

Output size is always taken from `condition`.

Value[](https://dplyr.tidyverse.org/reference/if_else.html#value)

------------------------------------------------------------------

A vector with the same size as `condition` and the same type as the common type of `true`, `false`, and `missing`.

Where `condition` is `TRUE`, the matching values from `true`, where it is `FALSE`, the matching values from `false`, and where it is `NA`, the matching values from `missing`, if provided, otherwise a missing value will be used.

See also[](https://dplyr.tidyverse.org/reference/if_else.html#see-also)

------------------------------------------------------------------------

`[vctrs::vec_if_else()](https://vctrs.r-lib.org/reference/vec_if_else.html) `

Examples[](https://dplyr.tidyverse.org/reference/if_else.html#ref-examples)

----------------------------------------------------------------------------

    x <- c(-5:5, NA)
    if_else(x < 0, NA, x)
    #>  [1] NA NA NA NA NA  0  1  2  3  4  5 NA
    
    # Explicitly handle `NA` values in the `condition` with `missing`
    if_else(x < 0, "negative", "positive", missing = "missing")
    #>  [1] "negative" "negative" "negative" "negative" "negative" "positive"
    #>  [7] "positive" "positive" "positive" "positive" "positive" "missing" 
    
    # Unlike `ifelse()`, `if_else()` preserves types
    x <- factor(sample(letters[1:5], 10, replace = TRUE))
    ifelse(x %in% c("a", "b", "c"), x, NA)
    #>  [1]  2 NA NA  2 NA  1  2 NA  2 NA
    if_else(x %in% c("a", "b", "c"), x, NA)
    #>  [1] c    <NA> <NA> c    <NA> b    c    <NA> c    <NA>
    #> Levels: b c d
    
    # `if_else()` is often useful for creating new columns inside of `mutate()`
    starwars |>
      mutate(category = if_else(height < 100, "short", "tall"), .keep = "used")
    #> # A tibble: 87 × 2
    #>    height category
    #>     <int> <chr>   
    #>  1    172 tall    
    #>  2    167 tall    
    #>  3     96 short   
    #>  4    202 tall    
    #>  5    150 tall    
    #>  6    178 tall    
    #>  7    165 tall    
    #>  8     97 short   
    #>  9    183 tall    
    #> 10    182 tall    
    #> # ℹ 77 more rows