[Skip to content](https://stringr.tidyverse.org/reference/str_split.html#container)

![](https://stringr.tidyverse.org/logo.png)

Split up a string into pieces
=============================

Source: [`R/split.R`](https://github.com/tidyverse/stringr/blob/main/R/split.R)

`str_split.Rd`

This family of functions provides various ways of splitting a string up into pieces. These two functions return a character vector:

*   `str_split_1()` takes a single string and splits it into pieces, returning a single character vector.
    
*   `str_split_i()` splits each string in a character vector into pieces and extracts the `i`th value, returning a character vector.
    

These two functions return a more complex object:

*   `str_split()` splits each string in a character vector into a varying number of pieces, returning a list of character vectors.
    
*   `str_split_fixed()` splits each string in a character vector into a fixed number of pieces, returning a character matrix.
    

Usage[](https://stringr.tidyverse.org/reference/str_split.html#ref-usage)

--------------------------------------------------------------------------

    str_split(string, pattern, n = Inf, simplify = FALSE)
    
    str_split_1(string, pattern)
    
    str_split_fixed(string, pattern, n)
    
    str_split_i(string, pattern, i)

Arguments[](https://stringr.tidyverse.org/reference/str_split.html#arguments)

------------------------------------------------------------------------------

string[](https://stringr.tidyverse.org/reference/str_split.html#arg-string)

Input vector. Either a character vector, or something coercible to one.

pattern[](https://stringr.tidyverse.org/reference/str_split.html#arg-pattern)

Pattern to look for.

The default interpretation is a regular expression, as described in `[vignette("regular-expressions")](https://stringr.tidyverse.org/articles/regular-expressions.html) `. Use `[regex()](https://stringr.tidyverse.org/reference/modifiers.html) ` for finer control of the matching behaviour.

Match a fixed string (i.e. by comparing only bytes), using `[fixed()](https://stringr.tidyverse.org/reference/modifiers.html) `. This is fast, but approximate. Generally, for matching human text, you'll want `[coll()](https://stringr.tidyverse.org/reference/modifiers.html) ` which respects character matching rules for the specified locale.

Match character, word, line and sentence boundaries with `[boundary()](https://stringr.tidyverse.org/reference/modifiers.html) `. The empty string, `""``, is equivalent to` boundary("character")\`.

n[](https://stringr.tidyverse.org/reference/str_split.html#arg-n)

Maximum number of pieces to return. Default (Inf) uses all possible split positions.

For `str_split()`, this determines the maximum length of each element of the output. For `str_split_fixed()`, this determines the number of columns in the output; if an input is too short, the result will be padded with `""`.

simplify[](https://stringr.tidyverse.org/reference/str_split.html#arg-simplify)

A boolean.

*   `FALSE` (the default): returns a list of character vectors.
    
*   `TRUE`: returns a character matrix.
    

i[](https://stringr.tidyverse.org/reference/str_split.html#arg-i)

Element to return. Use a negative value to count from the right hand side.

Value[](https://stringr.tidyverse.org/reference/str_split.html#value)

----------------------------------------------------------------------

*   `str_split_1()`: a character vector.
    
*   `str_split()`: a list the same length as `string`/`pattern` containing character vectors.
    
*   `str_split_fixed()`: a character matrix with `n` columns and the same number of rows as the length of `string`/`pattern`.
    
*   `str_split_i()`: a character vector the same length as `string`/`pattern`.
    

See also[](https://stringr.tidyverse.org/reference/str_split.html#see-also)

----------------------------------------------------------------------------

`[stringi::stri_split()](https://rdrr.io/pkg/stringi/man/stri_split.html) ` for the underlying implementation.

Examples[](https://stringr.tidyverse.org/reference/str_split.html#ref-examples)

--------------------------------------------------------------------------------

    fruits <- c(
      "apples and oranges and pears and bananas",
      "pineapples and mangos and guavas"
    )
    
    str_split(fruits, " and ")
    #> [[1]]
    #> [1] "apples"  "oranges" "pears"   "bananas"
    #> 
    #> [[2]]
    #> [1] "pineapples" "mangos"     "guavas"    
    #> 
    str_split(fruits, " and ", simplify = TRUE)
    #>      [,1]         [,2]      [,3]     [,4]     
    #> [1,] "apples"     "oranges" "pears"  "bananas"
    #> [2,] "pineapples" "mangos"  "guavas" ""       
    
    # If you want to split a single string, use `str_split_1`
    str_split_1(fruits[[1]], " and ")
    #> [1] "apples"  "oranges" "pears"   "bananas"
    
    # Specify n to restrict the number of possible matches
    str_split(fruits, " and ", n = 3)
    #> [[1]]
    #> [1] "apples"            "oranges"           "pears and bananas"
    #> 
    #> [[2]]
    #> [1] "pineapples" "mangos"     "guavas"    
    #> 
    str_split(fruits, " and ", n = 2)
    #> [[1]]
    #> [1] "apples"                        "oranges and pears and bananas"
    #> 
    #> [[2]]
    #> [1] "pineapples"        "mangos and guavas"
    #> 
    # If n greater than number of pieces, no padding occurs
    str_split(fruits, " and ", n = 5)
    #> [[1]]
    #> [1] "apples"  "oranges" "pears"   "bananas"
    #> 
    #> [[2]]
    #> [1] "pineapples" "mangos"     "guavas"    
    #> 
    
    # Use fixed to return a character matrix
    str_split_fixed(fruits, " and ", 3)
    #>      [,1]         [,2]      [,3]               
    #> [1,] "apples"     "oranges" "pears and bananas"
    #> [2,] "pineapples" "mangos"  "guavas"           
    str_split_fixed(fruits, " and ", 4)
    #>      [,1]         [,2]      [,3]     [,4]     
    #> [1,] "apples"     "oranges" "pears"  "bananas"
    #> [2,] "pineapples" "mangos"  "guavas" ""       
    
    # str_split_i extracts only a single piece from a string
    str_split_i(fruits, " and ", 1)
    #> [1] "apples"     "pineapples"
    str_split_i(fruits, " and ", 4)
    #> [1] "bananas" NA       
    # use a negative number to select from the end
    str_split_i(fruits, " and ", -1)
    #> [1] "bananas" "guavas"