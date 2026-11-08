[Skip to content](https://stringr.tidyverse.org/reference/str_flatten.html#container)

![](https://stringr.tidyverse.org/logo.png)

Flatten a string
================

Source: [`R/flatten.R`](https://github.com/tidyverse/stringr/blob/main/R/flatten.R)

`str_flatten.Rd`

`str_flatten()` reduces a character vector to a single string. This is a summary function because regardless of the length of the input `x`, it always returns a single string.

`str_flatten_comma()` is a variation designed specifically for flattening with commas. It automatically recognises if `last` uses the Oxford comma and handles the special case of 2 elements.

Usage[](https://stringr.tidyverse.org/reference/str_flatten.html#ref-usage)

----------------------------------------------------------------------------

    str_flatten(string, collapse = "", last = NULL, na.rm = FALSE)
    
    str_flatten_comma(string, last = NULL, na.rm = FALSE)

Arguments[](https://stringr.tidyverse.org/reference/str_flatten.html#arguments)

--------------------------------------------------------------------------------

string[](https://stringr.tidyverse.org/reference/str_flatten.html#arg-string)

Input vector. Either a character vector, or something coercible to one.

collapse[](https://stringr.tidyverse.org/reference/str_flatten.html#arg-collapse)

String to insert between each piece. Defaults to `""`.

last[](https://stringr.tidyverse.org/reference/str_flatten.html#arg-last)

Optional string to use in place of the final separator.

na.rm[](https://stringr.tidyverse.org/reference/str_flatten.html#arg-na-rm)

Remove missing values? If `FALSE` (the default), the result will be `NA` if any element of `string` is `NA`.

Value[](https://stringr.tidyverse.org/reference/str_flatten.html#value)

------------------------------------------------------------------------

A string, i.e. a character vector of length 1.

Examples[](https://stringr.tidyverse.org/reference/str_flatten.html#ref-examples)

----------------------------------------------------------------------------------

    str_flatten(letters)
    #> [1] "abcdefghijklmnopqrstuvwxyz"
    str_flatten(letters, "-")
    #> [1] "a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z"
    
    str_flatten(letters[1:3], ", ")
    #> [1] "a, b, c"
    
    # Use last to customise the last component
    str_flatten(letters[1:3], ", ", " and ")
    #> [1] "a, b and c"
    
    # this almost works if you want an Oxford (aka serial) comma
    str_flatten(letters[1:3], ", ", ", and ")
    #> [1] "a, b, and c"
    
    # but it will always add a comma, even when not necessary
    str_flatten(letters[1:2], ", ", ", and ")
    #> [1] "a, and b"
    
    # str_flatten_comma knows how to handle the Oxford comma
    str_flatten_comma(letters[1:3], ", and ")
    #> [1] "a, b, and c"
    str_flatten_comma(letters[1:2], ", and ")
    #> [1] "a and b"