[Skip to content](https://stringr.tidyverse.org/reference/str_conv.html#container)

![](https://stringr.tidyverse.org/logo.png)

Specify the encoding of a string
================================

Source: [`R/conv.R`](https://github.com/tidyverse/stringr/blob/main/R/conv.R)

`str_conv.Rd`

This is a convenient way to override the current encoding of a string.

Usage[](https://stringr.tidyverse.org/reference/str_conv.html#ref-usage)

-------------------------------------------------------------------------

    str_conv(string, encoding)

Arguments[](https://stringr.tidyverse.org/reference/str_conv.html#arguments)

-----------------------------------------------------------------------------

string[](https://stringr.tidyverse.org/reference/str_conv.html#arg-string)

Input vector. Either a character vector, or something coercible to one.

encoding[](https://stringr.tidyverse.org/reference/str_conv.html#arg-encoding)

Name of encoding. See `[stringi::stri_enc_list()](https://rdrr.io/pkg/stringi/man/stri_enc_list.html) ` for a complete list.

Examples[](https://stringr.tidyverse.org/reference/str_conv.html#ref-examples)

-------------------------------------------------------------------------------

    # Example from encoding?stringi::stringi
    x <- rawToChar(as.raw(177))
    x
    #> [1] "\xb1"
    str_conv(x, "ISO-8859-2") # Polish "a with ogonek"
    #> [1] "ą"
    str_conv(x, "ISO-8859-1") # Plus-minus
    #> [1] "±"