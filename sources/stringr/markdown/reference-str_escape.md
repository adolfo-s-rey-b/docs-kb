[Skip to content](https://stringr.tidyverse.org/reference/str_escape.html#container)

![](https://stringr.tidyverse.org/logo.png)

Escape regular expression metacharacters
========================================

Source: [`R/escape.R`](https://github.com/tidyverse/stringr/blob/main/R/escape.R)

`str_escape.Rd`

This function escapes metacharacter, the characters that have special meaning to the regular expression engine. In most cases you are better off using `[fixed()](https://stringr.tidyverse.org/reference/modifiers.html) ` since it is faster, but `str_escape()` is useful if you are composing user provided strings into a pattern.

Usage[](https://stringr.tidyverse.org/reference/str_escape.html#ref-usage)

---------------------------------------------------------------------------

    str_escape(string)

Arguments[](https://stringr.tidyverse.org/reference/str_escape.html#arguments)

-------------------------------------------------------------------------------

string[](https://stringr.tidyverse.org/reference/str_escape.html#arg-string)

Input vector. Either a character vector, or something coercible to one.

Value[](https://stringr.tidyverse.org/reference/str_escape.html#value)

-----------------------------------------------------------------------

A character vector the same length as `string`.

Examples[](https://stringr.tidyverse.org/reference/str_escape.html#ref-examples)

---------------------------------------------------------------------------------

    str_detect(c("a", "."), ".")
    #> [1] TRUE TRUE
    str_detect(c("a", "."), str_escape("."))
    #> [1] FALSE  TRUE