[Skip to content](https://stringr.tidyverse.org/reference/str_dup.html#container)

![](https://stringr.tidyverse.org/logo.png)

Duplicate a string
==================

Source: [`R/dup.R`](https://github.com/tidyverse/stringr/blob/main/R/dup.R)

`str_dup.Rd`

`str_dup()` duplicates the characters within a string, e.g. `str_dup("xy", 3)` returns `"xyxyxy"`.

Usage[](https://stringr.tidyverse.org/reference/str_dup.html#ref-usage)

------------------------------------------------------------------------

    str_dup(string, times, sep = NULL)

Arguments[](https://stringr.tidyverse.org/reference/str_dup.html#arguments)

----------------------------------------------------------------------------

string[](https://stringr.tidyverse.org/reference/str_dup.html#arg-string)

Input vector. Either a character vector, or something coercible to one.

times[](https://stringr.tidyverse.org/reference/str_dup.html#arg-times)

Number of times to duplicate each string.

sep[](https://stringr.tidyverse.org/reference/str_dup.html#arg-sep)

String to insert between each duplicate.

Value[](https://stringr.tidyverse.org/reference/str_dup.html#value)

--------------------------------------------------------------------

A character vector the same length as `string`/`times`.

Examples[](https://stringr.tidyverse.org/reference/str_dup.html#ref-examples)

------------------------------------------------------------------------------

    fruit <- c("apple", "pear", "banana")
    str_dup(fruit, 2)
    #> [1] "appleapple"   "pearpear"     "bananabanana"
    str_dup(fruit, 2, sep = " ")
    #> [1] "apple apple"   "pear pear"     "banana banana"
    str_dup(fruit, 1:3)
    #> [1] "apple"              "pearpear"           "bananabananabanana"
    str_c("ba", str_dup("na", 0:5))
    #> [1] "ba"           "bana"         "banana"       "bananana"    
    #> [5] "banananana"   "bananananana"