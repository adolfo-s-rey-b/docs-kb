[Skip to content](https://stringr.tidyverse.org/reference/word.html#container)

![](https://stringr.tidyverse.org/logo.png)

Extract words from a sentence
=============================

Source: [`R/word.R`](https://github.com/tidyverse/stringr/blob/main/R/word.R)

`word.Rd`

Extract words from a sentence

Usage[](https://stringr.tidyverse.org/reference/word.html#ref-usage)

---------------------------------------------------------------------

    word(string, start = 1L, end = start, sep = fixed(" "))

Arguments[](https://stringr.tidyverse.org/reference/word.html#arguments)

-------------------------------------------------------------------------

string[](https://stringr.tidyverse.org/reference/word.html#arg-string)

Input vector. Either a character vector, or something coercible to one.

start, end[](https://stringr.tidyverse.org/reference/word.html#arg-start-end)

Pair of integer vectors giving range of words (inclusive) to extract. If negative, counts backwards from the last word.

The default value select the first word.

sep[](https://stringr.tidyverse.org/reference/word.html#arg-sep)

Separator between words. Defaults to single space.

Value[](https://stringr.tidyverse.org/reference/word.html#value)

-----------------------------------------------------------------

A character vector with the same length as `string`/`start`/`end`.

Examples[](https://stringr.tidyverse.org/reference/word.html#ref-examples)

---------------------------------------------------------------------------

    sentences <- c("Jane saw a cat", "Jane sat down")
    word(sentences, 1)
    #> [1] "Jane" "Jane"
    word(sentences, 2)
    #> [1] "saw" "sat"
    word(sentences, -1)
    #> [1] "cat"  "down"
    word(sentences, 2, -1)
    #> [1] "saw a cat" "sat down" 
    
    # Also vectorised over start and end
    word(sentences[1], 1:3, -1)
    #> [1] "Jane saw a cat" "saw a cat"      "a cat"         
    word(sentences[1], 1, 1:4)
    #> [1] "Jane"           "Jane saw"       "Jane saw a"     "Jane saw a cat"
    
    # Can define words by other separators
    str <- 'abc.def..123.4568.999'
    word(str, 1, sep = fixed('..'))
    #> [1] "abc.def"
    word(str, 2, sep = fixed('..'))
    #> [1] "123.4568.999"