[Skip to content](https://stringr.tidyverse.org/reference/case.html#container)

![](https://stringr.tidyverse.org/logo.png)

Convert string to upper case, lower case, title case, or sentence case
======================================================================

Source: [`R/case.R`](https://github.com/tidyverse/stringr/blob/main/R/case.R)

`case.Rd`

*   `str_to_upper()` converts to upper case.
    
*   `str_to_lower()` converts to lower case.
    
*   `str_to_title()` converts to title case, where only the first letter of each word is capitalized.
    
*   `str_to_sentence()` convert to sentence case, where only the first letter of sentence is capitalized.
    

Usage[](https://stringr.tidyverse.org/reference/case.html#ref-usage)

---------------------------------------------------------------------

    str_to_upper(string, locale = "en")
    
    str_to_lower(string, locale = "en")
    
    str_to_title(string, locale = "en")
    
    str_to_sentence(string, locale = "en")

Arguments[](https://stringr.tidyverse.org/reference/case.html#arguments)

-------------------------------------------------------------------------

string[](https://stringr.tidyverse.org/reference/case.html#arg-string)

Input vector. Either a character vector, or something coercible to one.

locale[](https://stringr.tidyverse.org/reference/case.html#arg-locale)

Locale to use for comparisons. See `[stringi::stri_locale_list()](https://rdrr.io/pkg/stringi/man/stri_locale_list.html) ` for all possible options. Defaults to "en" (English) to ensure that default behaviour is consistent across platforms.

Value[](https://stringr.tidyverse.org/reference/case.html#value)

-----------------------------------------------------------------

A character vector the same length as `string`.

Examples[](https://stringr.tidyverse.org/reference/case.html#ref-examples)

---------------------------------------------------------------------------

    dog <- "The quick brown dog"
    str_to_upper(dog)
    #> [1] "THE QUICK BROWN DOG"
    str_to_lower(dog)
    #> [1] "the quick brown dog"
    str_to_title(dog)
    #> [1] "The Quick Brown Dog"
    str_to_sentence("the quick brown dog")
    #> [1] "The quick brown dog"
    
    # Locale matters!
    str_to_upper("i") # English
    #> [1] "I"
    str_to_upper("i", "tr") # Turkish
    #> [1] "İ"