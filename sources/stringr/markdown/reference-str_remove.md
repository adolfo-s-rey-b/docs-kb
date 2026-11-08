[Skip to content](https://stringr.tidyverse.org/reference/str_remove.html#container)

![](https://stringr.tidyverse.org/logo.png)

Remove matched patterns
=======================

Source: [`R/remove.R`](https://github.com/tidyverse/stringr/blob/main/R/remove.R)

`str_remove.Rd`

Remove matches, i.e. replace them with `""`.

Usage[](https://stringr.tidyverse.org/reference/str_remove.html#ref-usage)

---------------------------------------------------------------------------

    str_remove(string, pattern)
    
    str_remove_all(string, pattern)

Arguments[](https://stringr.tidyverse.org/reference/str_remove.html#arguments)

-------------------------------------------------------------------------------

string[](https://stringr.tidyverse.org/reference/str_remove.html#arg-string)

Input vector. Either a character vector, or something coercible to one.

pattern[](https://stringr.tidyverse.org/reference/str_remove.html#arg-pattern)

Pattern to look for.

The default interpretation is a regular expression, as described in `[vignette("regular-expressions")](https://stringr.tidyverse.org/articles/regular-expressions.html) `. Use `[regex()](https://stringr.tidyverse.org/reference/modifiers.html) ` for finer control of the matching behaviour.

Match a fixed string (i.e. by comparing only bytes), using `[fixed()](https://stringr.tidyverse.org/reference/modifiers.html) `. This is fast, but approximate. Generally, for matching human text, you'll want `[coll()](https://stringr.tidyverse.org/reference/modifiers.html) ` which respects character matching rules for the specified locale.

You can not match boundaries, including `""`, with this function.

Value[](https://stringr.tidyverse.org/reference/str_remove.html#value)

-----------------------------------------------------------------------

A character vector the same length as `string`/`pattern`.

See also[](https://stringr.tidyverse.org/reference/str_remove.html#see-also)

-----------------------------------------------------------------------------

`[str_replace()](https://stringr.tidyverse.org/reference/str_replace.html) ` for the underlying implementation.

Examples[](https://stringr.tidyverse.org/reference/str_remove.html#ref-examples)

---------------------------------------------------------------------------------

    fruits <- c("one apple", "two pears", "three bananas")
    str_remove(fruits, "[aeiou]")
    #> [1] "ne apple"     "tw pears"     "thre bananas"
    str_remove_all(fruits, "[aeiou]")
    #> [1] "n ppl"    "tw prs"   "thr bnns"