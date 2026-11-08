[Skip to content](https://stringr.tidyverse.org/reference/str_like.html#container)

![](https://stringr.tidyverse.org/logo.png)

Detect a pattern in the same way as `SQL`'s `LIKE` and `ILIKE` operators
========================================================================

Source: [`R/detect.R`](https://github.com/tidyverse/stringr/blob/main/R/detect.R)

`str_like.Rd`

`str_like()` and `str_like()` follow the conventions of the SQL `LIKE` and `ILIKE` operators, namely:

*   Must match the entire string.
    
*   `_` matches a single character (like `.`).
    
*   `%` matches any number of characters (like `.*`).
    
*   `\%` and `\_` match literal `%` and `_`.
    

The difference between the two functions is their case-sensitivity: `str_like()` is case sensitive and `str_ilike()` is not.

Usage[](https://stringr.tidyverse.org/reference/str_like.html#ref-usage)

-------------------------------------------------------------------------

    str_like(string, pattern, ignore_case = deprecated())
    
    str_ilike(string, pattern)

Arguments[](https://stringr.tidyverse.org/reference/str_like.html#arguments)

-----------------------------------------------------------------------------

string[](https://stringr.tidyverse.org/reference/str_like.html#arg-string)

Input vector. Either a character vector, or something coercible to one.

pattern[](https://stringr.tidyverse.org/reference/str_like.html#arg-pattern)

A character vector containing a SQL "like" pattern. See above for details.

ignore\_case[](https://stringr.tidyverse.org/reference/str_like.html#arg-ignore-case)

[![[Deprecated]](https://stringr.tidyverse.org/reference/figures/lifecycle-deprecated.svg)](https://lifecycle.r-lib.org/articles/stages.html#deprecated)

Value[](https://stringr.tidyverse.org/reference/str_like.html#value)

---------------------------------------------------------------------

A logical vector the same length as `string`.

Note[](https://stringr.tidyverse.org/reference/str_like.html#note)

-------------------------------------------------------------------

Prior to stringr 1.6.0, `str_like()` was incorrectly case-insensitive.

Examples[](https://stringr.tidyverse.org/reference/str_like.html#ref-examples)

-------------------------------------------------------------------------------

    fruit <- c("apple", "banana", "pear", "pineapple")
    str_like(fruit, "app")
    #> [1] FALSE FALSE FALSE FALSE
    str_like(fruit, "app%")
    #> [1]  TRUE FALSE FALSE FALSE
    str_like(fruit, "APP%")
    #> [1] FALSE FALSE FALSE FALSE
    str_like(fruit, "ba_ana")
    #> [1] FALSE  TRUE FALSE FALSE
    str_like(fruit, "%apple")
    #> [1]  TRUE FALSE FALSE  TRUE
    
    str_ilike(fruit, "app")
    #> [1] FALSE FALSE FALSE FALSE
    str_ilike(fruit, "app%")
    #> [1]  TRUE FALSE FALSE FALSE
    str_ilike(fruit, "APP%")
    #> [1]  TRUE FALSE FALSE FALSE
    str_ilike(fruit, "ba_ana")
    #> [1] FALSE  TRUE FALSE FALSE
    str_ilike(fruit, "%apple")
    #> [1]  TRUE FALSE FALSE  TRUE