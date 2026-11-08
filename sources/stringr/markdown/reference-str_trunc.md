[Skip to content](https://stringr.tidyverse.org/reference/str_trunc.html#container)

![](https://stringr.tidyverse.org/logo.png)

Truncate a string to maximum width
==================================

Source: [`R/trunc.R`](https://github.com/tidyverse/stringr/blob/main/R/trunc.R)

`str_trunc.Rd`

Truncate a string to a fixed of characters, so that `str_length(str_trunc(x, n))` is always less than or equal to `n`.

Usage[](https://stringr.tidyverse.org/reference/str_trunc.html#ref-usage)

--------------------------------------------------------------------------

    str_trunc(string, width, side = c("right", "left", "center"), ellipsis = "...")

Arguments[](https://stringr.tidyverse.org/reference/str_trunc.html#arguments)

------------------------------------------------------------------------------

string[](https://stringr.tidyverse.org/reference/str_trunc.html#arg-string)

Input vector. Either a character vector, or something coercible to one.

width[](https://stringr.tidyverse.org/reference/str_trunc.html#arg-width)

Maximum width of string.

side, ellipsis[](https://stringr.tidyverse.org/reference/str_trunc.html#arg-side-ellipsis)

Location and content of ellipsis that indicates content has been removed.

Value[](https://stringr.tidyverse.org/reference/str_trunc.html#value)

----------------------------------------------------------------------

A character vector the same length as `string`.

See also[](https://stringr.tidyverse.org/reference/str_trunc.html#see-also)

----------------------------------------------------------------------------

`[str_pad()](https://stringr.tidyverse.org/reference/str_pad.html) ` to increase the minimum width of a string.

Examples[](https://stringr.tidyverse.org/reference/str_trunc.html#ref-examples)

--------------------------------------------------------------------------------

    x <- "This string is moderately long"
    rbind(
      str_trunc(x, 20, "right"),
      str_trunc(x, 20, "left"),
      str_trunc(x, 20, "center")
    )
    #>      [,1]                  
    #> [1,] "This string is mo..."
    #> [2,] "...s moderately long"
    #> [3,] "This stri...ely long"