[Skip to content](https://stringr.tidyverse.org/reference/str_detect.html#container)

![](https://stringr.tidyverse.org/logo.png)

Detect the presence/absence of a match
======================================

Source: [`R/detect.R`](https://github.com/tidyverse/stringr/blob/main/R/detect.R)

`str_detect.Rd`

`str_detect()` returns a logical vector with `TRUE` for each element of `string` that matches `pattern` and `FALSE` otherwise. It's equivalent to `grepl(pattern, string)`.

Usage[](https://stringr.tidyverse.org/reference/str_detect.html#ref-usage)

---------------------------------------------------------------------------

    str_detect(string, pattern, negate = FALSE)

Arguments[](https://stringr.tidyverse.org/reference/str_detect.html#arguments)

-------------------------------------------------------------------------------

string[](https://stringr.tidyverse.org/reference/str_detect.html#arg-string)

Input vector. Either a character vector, or something coercible to one.

pattern[](https://stringr.tidyverse.org/reference/str_detect.html#arg-pattern)

Pattern to look for.

The default interpretation is a regular expression, as described in `[vignette("regular-expressions")](https://stringr.tidyverse.org/articles/regular-expressions.html) `. Use `[regex()](https://stringr.tidyverse.org/reference/modifiers.html) ` for finer control of the matching behaviour.

Match a fixed string (i.e. by comparing only bytes), using `[fixed()](https://stringr.tidyverse.org/reference/modifiers.html) `. This is fast, but approximate. Generally, for matching human text, you'll want `[coll()](https://stringr.tidyverse.org/reference/modifiers.html) ` which respects character matching rules for the specified locale.

You can not match boundaries, including `""`, with this function.

negate[](https://stringr.tidyverse.org/reference/str_detect.html#arg-negate)

If `TRUE`, inverts the resulting boolean vector.

Value[](https://stringr.tidyverse.org/reference/str_detect.html#value)

-----------------------------------------------------------------------

A logical vector the same length as `string`/`pattern`.

See also[](https://stringr.tidyverse.org/reference/str_detect.html#see-also)

-----------------------------------------------------------------------------

`[stringi::stri_detect()](https://rdrr.io/pkg/stringi/man/stri_detect.html) ` which this function wraps, `[str_subset()](https://stringr.tidyverse.org/reference/str_subset.html) ` for a convenient wrapper around `x[str_detect(x, pattern)]`

Examples[](https://stringr.tidyverse.org/reference/str_detect.html#ref-examples)

---------------------------------------------------------------------------------

    fruit <- c("apple", "banana", "pear", "pineapple")
    str_detect(fruit, "a")
    #> [1] TRUE TRUE TRUE TRUE
    str_detect(fruit, "^a")
    #> [1]  TRUE FALSE FALSE FALSE
    str_detect(fruit, "a$")
    #> [1] FALSE  TRUE FALSE FALSE
    str_detect(fruit, "b")
    #> [1] FALSE  TRUE FALSE FALSE
    str_detect(fruit, "[aeiou]")
    #> [1] TRUE TRUE TRUE TRUE
    
    # Also vectorised over pattern
    str_detect("aecfg", letters)
    #>  [1]  TRUE FALSE  TRUE FALSE  TRUE  TRUE  TRUE FALSE FALSE FALSE FALSE
    #> [12] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
    #> [23] FALSE FALSE FALSE FALSE
    
    # Returns TRUE if the pattern do NOT match
    str_detect(fruit, "^p", negate = TRUE)
    #> [1]  TRUE  TRUE FALSE FALSE