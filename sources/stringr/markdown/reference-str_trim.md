[Skip to content](https://stringr.tidyverse.org/reference/str_trim.html#container)

![](https://stringr.tidyverse.org/logo.png)

Remove whitespace
=================

Source: [`R/trim.R`](https://github.com/tidyverse/stringr/blob/main/R/trim.R)

`str_trim.Rd`

`str_trim()` removes whitespace from start and end of string; `str_squish()` removes whitespace at the start and end, and replaces all internal whitespace with a single space.

Usage[](https://stringr.tidyverse.org/reference/str_trim.html#ref-usage)

-------------------------------------------------------------------------

    str_trim(string, side = c("both", "left", "right"))
    
    str_squish(string)

Arguments[](https://stringr.tidyverse.org/reference/str_trim.html#arguments)

-----------------------------------------------------------------------------

string[](https://stringr.tidyverse.org/reference/str_trim.html#arg-string)

Input vector. Either a character vector, or something coercible to one.

side[](https://stringr.tidyverse.org/reference/str_trim.html#arg-side)

Side on which to remove whitespace: "left", "right", or "both", the default.

Value[](https://stringr.tidyverse.org/reference/str_trim.html#value)

---------------------------------------------------------------------

A character vector the same length as `string`.

See also[](https://stringr.tidyverse.org/reference/str_trim.html#see-also)

---------------------------------------------------------------------------

`[str_pad()](https://stringr.tidyverse.org/reference/str_pad.html) ` to add whitespace

Examples[](https://stringr.tidyverse.org/reference/str_trim.html#ref-examples)

-------------------------------------------------------------------------------

    str_trim("  String with trailing and leading white space\t")
    #> [1] "String with trailing and leading white space"
    str_trim("\n\nString with trailing and leading white space\n\n")
    #> [1] "String with trailing and leading white space"
    
    str_squish("  String with trailing,  middle, and leading white space\t")
    #> [1] "String with trailing, middle, and leading white space"
    str_squish("\n\nString with excess,  trailing and leading white   space\n\n")
    #> [1] "String with excess, trailing and leading white space"