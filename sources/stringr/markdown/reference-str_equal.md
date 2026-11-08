[Skip to content](https://stringr.tidyverse.org/reference/str_equal.html#container)

![](https://stringr.tidyverse.org/logo.png)

Determine if two strings are equivalent
=======================================

Source: [`R/equal.R`](https://github.com/tidyverse/stringr/blob/main/R/equal.R)

`str_equal.Rd`

This uses Unicode canonicalisation rules, and optionally ignores case.

Usage[](https://stringr.tidyverse.org/reference/str_equal.html#ref-usage)

--------------------------------------------------------------------------

    str_equal(x, y, locale = "en", ignore_case = FALSE, ...)

Arguments[](https://stringr.tidyverse.org/reference/str_equal.html#arguments)

------------------------------------------------------------------------------

x, y[](https://stringr.tidyverse.org/reference/str_equal.html#arg-x-y)

A pair of character vectors.

locale[](https://stringr.tidyverse.org/reference/str_equal.html#arg-locale)

Locale to use for comparisons. See `[stringi::stri_locale_list()](https://rdrr.io/pkg/stringi/man/stri_locale_list.html) ` for all possible options. Defaults to "en" (English) to ensure that default behaviour is consistent across platforms.

ignore\_case[](https://stringr.tidyverse.org/reference/str_equal.html#arg-ignore-case)

Ignore case when comparing strings?

...[](https://stringr.tidyverse.org/reference/str_equal.html#arg--)

Other options used to control collation. Passed on to `[stringi::stri_opts_collator()](https://rdrr.io/pkg/stringi/man/stri_opts_collator.html) `.

Value[](https://stringr.tidyverse.org/reference/str_equal.html#value)

----------------------------------------------------------------------

An logical vector the same length as `x`/`y`.

See also[](https://stringr.tidyverse.org/reference/str_equal.html#see-also)

----------------------------------------------------------------------------

`[stringi::stri_cmp_equiv()](https://rdrr.io/pkg/stringi/man/stri_compare.html) ` for the underlying implementation.

Examples[](https://stringr.tidyverse.org/reference/str_equal.html#ref-examples)

--------------------------------------------------------------------------------

    # These two strings encode "a" with an accent in two different ways
    a1 <- "\u00e1"
    a2 <- "a\u0301"
    c(a1, a2)
    #> [1] "á" "á"
    
    a1 == a2
    #> [1] FALSE
    str_equal(a1, a2)
    #> [1] TRUE
    
    # ohm and omega use different code points but should always be treated
    # as equal
    ohm <- "\u2126"
    omega <- "\u03A9"
    c(ohm, omega)
    #> [1] "Ω" "Ω"
    
    ohm == omega
    #> [1] FALSE
    str_equal(ohm, omega)
    #> [1] TRUE