[Skip to content](https://stringr.tidyverse.org/reference/str_which.html#container)

![](https://stringr.tidyverse.org/logo.png)

Find matching indices
=====================

Source: [`R/subset.R`](https://github.com/tidyverse/stringr/blob/main/R/subset.R)

`str_which.Rd`

`str_which()` returns the indices of `string` where there's at least one match to `pattern`. It's a wrapper around `which(str_detect(x, pattern))`, and is equivalent to `grep(pattern, x)`.

Usage[](https://stringr.tidyverse.org/reference/str_which.html#ref-usage)

--------------------------------------------------------------------------

    str_which(string, pattern, negate = FALSE)

Arguments[](https://stringr.tidyverse.org/reference/str_which.html#arguments)

------------------------------------------------------------------------------

string[](https://stringr.tidyverse.org/reference/str_which.html#arg-string)

Input vector. Either a character vector, or something coercible to one.

pattern[](https://stringr.tidyverse.org/reference/str_which.html#arg-pattern)

Pattern to look for.

The default interpretation is a regular expression, as described in `[vignette("regular-expressions")](https://stringr.tidyverse.org/articles/regular-expressions.html) `. Use `[regex()](https://stringr.tidyverse.org/reference/modifiers.html) ` for finer control of the matching behaviour.

Match a fixed string (i.e. by comparing only bytes), using `[fixed()](https://stringr.tidyverse.org/reference/modifiers.html) `. This is fast, but approximate. Generally, for matching human text, you'll want `[coll()](https://stringr.tidyverse.org/reference/modifiers.html) ` which respects character matching rules for the specified locale.

You can not match boundaries, including `""`, with this function.

negate[](https://stringr.tidyverse.org/reference/str_which.html#arg-negate)

If `TRUE`, inverts the resulting boolean vector.

Value[](https://stringr.tidyverse.org/reference/str_which.html#value)

----------------------------------------------------------------------

An integer vector, usually smaller than `string`.

Examples[](https://stringr.tidyverse.org/reference/str_which.html#ref-examples)

--------------------------------------------------------------------------------

    fruit <- c("apple", "banana", "pear", "pineapple")
    str_which(fruit, "a")
    #> [1] 1 2 3 4
    
    # Elements that don't match
    str_which(fruit, "^p", negate = TRUE)
    #> [1] 1 2
    
    # Missings never match
    str_which(c("a", NA, "b"), ".")
    #> [1] 1 3