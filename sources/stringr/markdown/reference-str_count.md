[Skip to content](https://stringr.tidyverse.org/reference/str_count.html#container)

![](https://stringr.tidyverse.org/logo.png)

Count number of matches
=======================

Source: [`R/count.R`](https://github.com/tidyverse/stringr/blob/main/R/count.R)

`str_count.Rd`

Counts the number of times `pattern` is found within each element of `string.`

Usage[](https://stringr.tidyverse.org/reference/str_count.html#ref-usage)

--------------------------------------------------------------------------

    str_count(string, pattern = "")

Arguments[](https://stringr.tidyverse.org/reference/str_count.html#arguments)

------------------------------------------------------------------------------

string[](https://stringr.tidyverse.org/reference/str_count.html#arg-string)

Input vector. Either a character vector, or something coercible to one.

pattern[](https://stringr.tidyverse.org/reference/str_count.html#arg-pattern)

Pattern to look for.

The default interpretation is a regular expression, as described in `[vignette("regular-expressions")](https://stringr.tidyverse.org/articles/regular-expressions.html) `. Use `[regex()](https://stringr.tidyverse.org/reference/modifiers.html) ` for finer control of the matching behaviour.

Match a fixed string (i.e. by comparing only bytes), using `[fixed()](https://stringr.tidyverse.org/reference/modifiers.html) `. This is fast, but approximate. Generally, for matching human text, you'll want `[coll()](https://stringr.tidyverse.org/reference/modifiers.html) ` which respects character matching rules for the specified locale.

Match character, word, line and sentence boundaries with `[boundary()](https://stringr.tidyverse.org/reference/modifiers.html) `. The empty string, `""``, is equivalent to` boundary("character")\`.

Value[](https://stringr.tidyverse.org/reference/str_count.html#value)

----------------------------------------------------------------------

An integer vector the same length as `string`/`pattern`.

See also[](https://stringr.tidyverse.org/reference/str_count.html#see-also)

----------------------------------------------------------------------------

`[stringi::stri_count()](https://rdrr.io/pkg/stringi/man/stri_count.html) ` which this function wraps.

`[str_locate()](https://stringr.tidyverse.org/reference/str_locate.html) `/`[str_locate_all()](https://stringr.tidyverse.org/reference/str_locate.html) ` to locate position of matches

Examples[](https://stringr.tidyverse.org/reference/str_count.html#ref-examples)

--------------------------------------------------------------------------------

    fruit <- c("apple", "banana", "pear", "pineapple")
    str_count(fruit, "a")
    #> [1] 1 3 1 1
    str_count(fruit, "p")
    #> [1] 2 0 1 3
    str_count(fruit, "e")
    #> [1] 1 0 1 2
    str_count(fruit, c("a", "b", "p", "p"))
    #> [1] 1 1 1 3
    
    str_count(c("a.", "...", ".a.a"), ".")
    #> [1] 2 3 4
    str_count(c("a.", "...", ".a.a"), fixed("."))
    #> [1] 1 3 2