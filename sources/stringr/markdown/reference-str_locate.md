[Skip to content](https://stringr.tidyverse.org/reference/str_locate.html#container)

![](https://stringr.tidyverse.org/logo.png)

Find location of match
======================

Source: [`R/locate.R`](https://github.com/tidyverse/stringr/blob/main/R/locate.R)

`str_locate.Rd`

`str_locate()` returns the `start` and `end` position of the first match; `str_locate_all()` returns the `start` and `end` position of each match.

Because the `start` and `end` values are inclusive, zero-length matches (e.g. `$`, `^`, `\\b`) will have an `end` that is smaller than `start`.

Usage[](https://stringr.tidyverse.org/reference/str_locate.html#ref-usage)

---------------------------------------------------------------------------

    str_locate(string, pattern)
    
    str_locate_all(string, pattern)

Arguments[](https://stringr.tidyverse.org/reference/str_locate.html#arguments)

-------------------------------------------------------------------------------

string[](https://stringr.tidyverse.org/reference/str_locate.html#arg-string)

Input vector. Either a character vector, or something coercible to one.

pattern[](https://stringr.tidyverse.org/reference/str_locate.html#arg-pattern)

Pattern to look for.

The default interpretation is a regular expression, as described in `[vignette("regular-expressions")](https://stringr.tidyverse.org/articles/regular-expressions.html) `. Use `[regex()](https://stringr.tidyverse.org/reference/modifiers.html) ` for finer control of the matching behaviour.

Match a fixed string (i.e. by comparing only bytes), using `[fixed()](https://stringr.tidyverse.org/reference/modifiers.html) `. This is fast, but approximate. Generally, for matching human text, you'll want `[coll()](https://stringr.tidyverse.org/reference/modifiers.html) ` which respects character matching rules for the specified locale.

Match character, word, line and sentence boundaries with `[boundary()](https://stringr.tidyverse.org/reference/modifiers.html) `. The empty string, `""``, is equivalent to` boundary("character")\`.

Value[](https://stringr.tidyverse.org/reference/str_locate.html#value)

-----------------------------------------------------------------------

*   `str_locate()` returns an integer matrix with two columns and one row for each element of `string`. The first column, `start`, gives the position at the start of the match, and the second column, `end`, gives the position of the end.
    
*   `str_locate_all()` returns a list of integer matrices with the same length as `string`/`pattern`. The matrices have columns `start` and `end` as above, and one row for each match.
    

See also[](https://stringr.tidyverse.org/reference/str_locate.html#see-also)

-----------------------------------------------------------------------------

`[str_extract()](https://stringr.tidyverse.org/reference/str_extract.html) ` for a convenient way of extracting matches, `[stringi::stri_locate()](https://rdrr.io/pkg/stringi/man/stri_locate.html) ` for the underlying implementation.

Examples[](https://stringr.tidyverse.org/reference/str_locate.html#ref-examples)

---------------------------------------------------------------------------------

    fruit <- c("apple", "banana", "pear", "pineapple")
    str_locate(fruit, "$")
    #>      start end
    #> [1,]     6   5
    #> [2,]     7   6
    #> [3,]     5   4
    #> [4,]    10   9
    str_locate(fruit, "a")
    #>      start end
    #> [1,]     1   1
    #> [2,]     2   2
    #> [3,]     3   3
    #> [4,]     5   5
    str_locate(fruit, "e")
    #>      start end
    #> [1,]     5   5
    #> [2,]    NA  NA
    #> [3,]     2   2
    #> [4,]     4   4
    str_locate(fruit, c("a", "b", "p", "p"))
    #>      start end
    #> [1,]     1   1
    #> [2,]     1   1
    #> [3,]     1   1
    #> [4,]     1   1
    
    str_locate_all(fruit, "a")
    #> [[1]]
    #>      start end
    #> [1,]     1   1
    #> 
    #> [[2]]
    #>      start end
    #> [1,]     2   2
    #> [2,]     4   4
    #> [3,]     6   6
    #> 
    #> [[3]]
    #>      start end
    #> [1,]     3   3
    #> 
    #> [[4]]
    #>      start end
    #> [1,]     5   5
    #> 
    str_locate_all(fruit, "e")
    #> [[1]]
    #>      start end
    #> [1,]     5   5
    #> 
    #> [[2]]
    #>      start end
    #> 
    #> [[3]]
    #>      start end
    #> [1,]     2   2
    #> 
    #> [[4]]
    #>      start end
    #> [1,]     4   4
    #> [2,]     9   9
    #> 
    str_locate_all(fruit, c("a", "b", "p", "p"))
    #> [[1]]
    #>      start end
    #> [1,]     1   1
    #> 
    #> [[2]]
    #>      start end
    #> [1,]     1   1
    #> 
    #> [[3]]
    #>      start end
    #> [1,]     1   1
    #> 
    #> [[4]]
    #>      start end
    #> [1,]     1   1
    #> [2,]     6   6
    #> [3,]     7   7
    #> 
    
    # Find location of every character
    str_locate_all(fruit, "")
    #> [[1]]
    #>      start end
    #> [1,]     1   1
    #> [2,]     2   2
    #> [3,]     3   3
    #> [4,]     4   4
    #> [5,]     5   5
    #> 
    #> [[2]]
    #>      start end
    #> [1,]     1   1
    #> [2,]     2   2
    #> [3,]     3   3
    #> [4,]     4   4
    #> [5,]     5   5
    #> [6,]     6   6
    #> 
    #> [[3]]
    #>      start end
    #> [1,]     1   1
    #> [2,]     2   2
    #> [3,]     3   3
    #> [4,]     4   4
    #> 
    #> [[4]]
    #>       start end
    #>  [1,]     1   1
    #>  [2,]     2   2
    #>  [3,]     3   3
    #>  [4,]     4   4
    #>  [5,]     5   5
    #>  [6,]     6   6
    #>  [7,]     7   7
    #>  [8,]     8   8
    #>  [9,]     9   9
    #>