[Skip to content](https://stringr.tidyverse.org/reference/str_pad.html#container)

![](https://stringr.tidyverse.org/logo.png)

Pad a string to minimum width
=============================

Source: [`R/pad.R`](https://github.com/tidyverse/stringr/blob/main/R/pad.R)

`str_pad.Rd`

Pad a string to a fixed width, so that `str_length(str_pad(x, n))` is always greater than or equal to `n`.

Usage[](https://stringr.tidyverse.org/reference/str_pad.html#ref-usage)

------------------------------------------------------------------------

    str_pad(
      string,
      width,
      side = c("left", "right", "both"),
      pad = " ",
      use_width = TRUE
    )

Arguments[](https://stringr.tidyverse.org/reference/str_pad.html#arguments)

----------------------------------------------------------------------------

string[](https://stringr.tidyverse.org/reference/str_pad.html#arg-string)

Input vector. Either a character vector, or something coercible to one.

width[](https://stringr.tidyverse.org/reference/str_pad.html#arg-width)

Minimum width of padded strings.

side[](https://stringr.tidyverse.org/reference/str_pad.html#arg-side)

Side on which padding character is added (left, right or both).

pad[](https://stringr.tidyverse.org/reference/str_pad.html#arg-pad)

Single padding character (default is a space).

use\_width[](https://stringr.tidyverse.org/reference/str_pad.html#arg-use-width)

If `FALSE`, use the length of the string instead of the width; see `[str_width()](https://stringr.tidyverse.org/reference/str_length.html) `/`[str_length()](https://stringr.tidyverse.org/reference/str_length.html) ` for the difference.

Value[](https://stringr.tidyverse.org/reference/str_pad.html#value)

--------------------------------------------------------------------

A character vector the same length as `stringr`/`width`/`pad`.

See also[](https://stringr.tidyverse.org/reference/str_pad.html#see-also)

--------------------------------------------------------------------------

`[str_trim()](https://stringr.tidyverse.org/reference/str_trim.html) ` to remove whitespace; `[str_trunc()](https://stringr.tidyverse.org/reference/str_trunc.html) ` to decrease the maximum width of a string.

Examples[](https://stringr.tidyverse.org/reference/str_pad.html#ref-examples)

------------------------------------------------------------------------------

    rbind(
      str_pad("hadley", 30, "left"),
      str_pad("hadley", 30, "right"),
      str_pad("hadley", 30, "both")
    )
    #>      [,1]                            
    #> [1,] "                        hadley"
    #> [2,] "hadley                        "
    #> [3,] "            hadley            "
    
    # All arguments are vectorised except side
    str_pad(c("a", "abc", "abcdef"), 10)
    #> [1] "         a" "       abc" "    abcdef"
    str_pad("a", c(5, 10, 20))
    #> [1] "    a"                "         a"          
    #> [3] "                   a"
    str_pad("a", 10, pad = c("-", "_", " "))
    #> [1] "---------a" "_________a" "         a"
    
    # Longer strings are returned unchanged
    str_pad("hadley", 3)
    #> [1] "hadley"