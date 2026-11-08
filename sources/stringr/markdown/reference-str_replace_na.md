[Skip to content](https://stringr.tidyverse.org/reference/str_replace_na.html#container)

![](https://stringr.tidyverse.org/logo.png)

Turn NA into "NA"
=================

Source: [`R/replace.R`](https://github.com/tidyverse/stringr/blob/main/R/replace.R)

`str_replace_na.Rd`

Turn NA into "NA"

Usage[](https://stringr.tidyverse.org/reference/str_replace_na.html#ref-usage)

-------------------------------------------------------------------------------

    str_replace_na(string, replacement = "NA")

Arguments[](https://stringr.tidyverse.org/reference/str_replace_na.html#arguments)

-----------------------------------------------------------------------------------

string[](https://stringr.tidyverse.org/reference/str_replace_na.html#arg-string)

Input vector. Either a character vector, or something coercible to one.

replacement[](https://stringr.tidyverse.org/reference/str_replace_na.html#arg-replacement)

A single string.

Examples[](https://stringr.tidyverse.org/reference/str_replace_na.html#ref-examples)

-------------------------------------------------------------------------------------

    str_replace_na(c(NA, "abc", "def"))
    #> [1] "NA"  "abc" "def"