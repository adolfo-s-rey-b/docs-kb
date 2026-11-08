[Skip to content](https://stringr.tidyverse.org/reference/str_starts.html#container)

![](https://stringr.tidyverse.org/logo.png)

Detect the presence/absence of a match at the start/end
=======================================================

Source: [`R/detect.R`](https://github.com/tidyverse/stringr/blob/main/R/detect.R)

`str_starts.Rd`

`str_starts()` and `str_ends()` are special cases of `[str_detect()](https://stringr.tidyverse.org/reference/str_detect.html) ` that only match at the beginning or end of a string, respectively.

Usage[](https://stringr.tidyverse.org/reference/str_starts.html#ref-usage)

---------------------------------------------------------------------------

    str_starts(string, pattern, negate = FALSE)
    
    str_ends(string, pattern, negate = FALSE)

Arguments[](https://stringr.tidyverse.org/reference/str_starts.html#arguments)

-------------------------------------------------------------------------------

string[](https://stringr.tidyverse.org/reference/str_starts.html#arg-string)

Input vector. Either a character vector, or something coercible to one.

pattern[](https://stringr.tidyverse.org/reference/str_starts.html#arg-pattern)

Pattern with which the string starts or ends.

The default interpretation is a regular expression, as described in [stringi::about\_search\_regex](https://rdrr.io/pkg/stringi/man/about_search_regex.html)
. Control options with `[regex()](https://stringr.tidyverse.org/reference/modifiers.html) `.

Match a fixed string (i.e. by comparing only bytes), using `[fixed()](https://stringr.tidyverse.org/reference/modifiers.html) `. This is fast, but approximate. Generally, for matching human text, you'll want `[coll()](https://stringr.tidyverse.org/reference/modifiers.html) ` which respects character matching rules for the specified locale.

negate[](https://stringr.tidyverse.org/reference/str_starts.html#arg-negate)

If `TRUE`, inverts the resulting boolean vector.

Value[](https://stringr.tidyverse.org/reference/str_starts.html#value)

-----------------------------------------------------------------------

A logical vector.

Examples[](https://stringr.tidyverse.org/reference/str_starts.html#ref-examples)

---------------------------------------------------------------------------------

    fruit <- c("apple", "banana", "pear", "pineapple")
    str_starts(fruit, "p")
    #> [1] FALSE FALSE  TRUE  TRUE
    str_starts(fruit, "p", negate = TRUE)
    #> [1]  TRUE  TRUE FALSE FALSE
    str_ends(fruit, "e")
    #> [1]  TRUE FALSE FALSE  TRUE
    str_ends(fruit, "e", negate = TRUE)
    #> [1] FALSE  TRUE  TRUE FALSE