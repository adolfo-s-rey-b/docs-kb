[Skip to content](https://stringr.tidyverse.org/reference/str_to_camel.html#container)

![](https://stringr.tidyverse.org/logo.png)

Convert between different types of programming case
===================================================

Source: [`R/case.R`](https://github.com/tidyverse/stringr/blob/main/R/case.R)

`str_to_camel.Rd`

*   `str_to_camel()` converts to camel case, where the first letter of each word is capitalized, with no separation between words. By default the first letter of the first word is not capitalized.
    
*   `str_to_kebab()` converts to kebab case, where words are converted to lower case and separated by dashes (`-`).
    
*   `str_to_snake()` converts to snake case, where words are converted to lower case and separated by underscores (`_`).
    

Usage[](https://stringr.tidyverse.org/reference/str_to_camel.html#ref-usage)

-----------------------------------------------------------------------------

    str_to_camel(string, first_upper = FALSE)
    
    str_to_snake(string)
    
    str_to_kebab(string)

Arguments[](https://stringr.tidyverse.org/reference/str_to_camel.html#arguments)

---------------------------------------------------------------------------------

string[](https://stringr.tidyverse.org/reference/str_to_camel.html#arg-string)

Input vector. Either a character vector, or something coercible to one.

first\_upper[](https://stringr.tidyverse.org/reference/str_to_camel.html#arg-first-upper)

Logical. Should the first letter be capitalized?

Examples[](https://stringr.tidyverse.org/reference/str_to_camel.html#ref-examples)

-----------------------------------------------------------------------------------

    str_to_camel("my-variable")
    #> [1] "myVariable"
    str_to_camel("my-variable", first_upper = TRUE)
    #> [1] "MyVariable"
    
    str_to_snake("MyVariable")
    #> [1] "my_variable"
    str_to_kebab("MyVariable")
    #> [1] "my-variable"