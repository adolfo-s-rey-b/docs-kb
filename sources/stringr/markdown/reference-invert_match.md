[Skip to content](https://stringr.tidyverse.org/reference/invert_match.html#container)

![](https://stringr.tidyverse.org/logo.png)

Switch location of matches to location of non-matches
=====================================================

Source: [`R/locate.R`](https://github.com/tidyverse/stringr/blob/main/R/locate.R)

`invert_match.Rd`

Invert a matrix of match locations to match the opposite of what was previously matched.

Usage[](https://stringr.tidyverse.org/reference/invert_match.html#ref-usage)

-----------------------------------------------------------------------------

    invert_match(loc)

Arguments[](https://stringr.tidyverse.org/reference/invert_match.html#arguments)

---------------------------------------------------------------------------------

loc[](https://stringr.tidyverse.org/reference/invert_match.html#arg-loc)

matrix of match locations, as from `[str_locate_all()](https://stringr.tidyverse.org/reference/str_locate.html) `

Value[](https://stringr.tidyverse.org/reference/invert_match.html#value)

-------------------------------------------------------------------------

numeric match giving locations of non-matches

Examples[](https://stringr.tidyverse.org/reference/invert_match.html#ref-examples)

-----------------------------------------------------------------------------------

    numbers <- "1 and 2 and 4 and 456"
    num_loc <- str_locate_all(numbers, "[0-9]+")[[1]]
    str_sub(numbers, num_loc[, "start"], num_loc[, "end"])
    #> [1] "1"   "2"   "4"   "456"
    
    text_loc <- invert_match(num_loc)
    str_sub(numbers, text_loc[, "start"], text_loc[, "end"])
    #> [1] ""      " and " " and " " and " ""