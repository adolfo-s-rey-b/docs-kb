[Skip to content](https://purrr.tidyverse.org/reference/safely.html#container)

![](https://purrr.tidyverse.org/logo.png)

Wrap a function to capture errors
=================================

Source: [`R/adverb-safely.R`](https://github.com/tidyverse/purrr/blob/main/R/adverb-safely.R)

`safely.Rd`

Creates a modified version of `.f` that always succeeds. It returns a list with components `result` and `error`. If the function succeeds, `result` contains the returned value and `error` is `NULL`. If an error occurred, `error` is an `error` object and `result` is either `NULL` or `otherwise`.

Usage[](https://purrr.tidyverse.org/reference/safely.html#ref-usage)

---------------------------------------------------------------------

    safely(.f, otherwise = NULL, quiet = TRUE)

Arguments[](https://purrr.tidyverse.org/reference/safely.html#arguments)

-------------------------------------------------------------------------

.f[](https://purrr.tidyverse.org/reference/safely.html#arg--f)

A function to modify, specified in one of the following ways:

*   A named function, e.g. `mean`.
    
*   An anonymous function, e.g. `\(x) x + 1` or `function(x) x + 1`.
    
*   A formula, e.g. `~ .x + 1`. No longer recommended.
    

otherwise[](https://purrr.tidyverse.org/reference/safely.html#arg-otherwise)

Default value to use when an error occurs.

quiet[](https://purrr.tidyverse.org/reference/safely.html#arg-quiet)

Hide errors (`TRUE`, the default), or display them as they occur?

Value[](https://purrr.tidyverse.org/reference/safely.html#value)

-----------------------------------------------------------------

A function that takes the same arguments as `.f`, but returns a different value, as described above.

Adverbs[](https://purrr.tidyverse.org/reference/safely.html#adverbs)

---------------------------------------------------------------------

This function is called an adverb because it modifies the effect of a function (a verb). If you'd like to include a function created an adverb in a package, be sure to read [faq-adverbs-export](https://purrr.tidyverse.org/reference/faq-adverbs-export.html)
.

See also[](https://purrr.tidyverse.org/reference/safely.html#see-also)

-----------------------------------------------------------------------

Other adverbs: `[auto_browse()](https://purrr.tidyverse.org/reference/auto_browse.html) `, `[compose()](https://purrr.tidyverse.org/reference/compose.html) `, `[insistently()](https://purrr.tidyverse.org/reference/insistently.html) `, `[negate()](https://purrr.tidyverse.org/reference/negate.html) `, `[partial()](https://purrr.tidyverse.org/reference/partial.html) `, `[possibly()](https://purrr.tidyverse.org/reference/possibly.html) `, `[quietly()](https://purrr.tidyverse.org/reference/quietly.html) `, `[slowly()](https://purrr.tidyverse.org/reference/slowly.html) `

Examples[](https://purrr.tidyverse.org/reference/safely.html#ref-examples)

---------------------------------------------------------------------------

    safe_log <- safely(log)
    safe_log(10)
    #> $result
    #> [1] 2.302585
    #> 
    #> $error
    #> NULL
    #> 
    safe_log("a")
    #> $result
    #> NULL
    #> 
    #> $error
    #> <simpleError in .f(...): non-numeric argument to mathematical function>
    #> 
    
    list("a", 10, 100) |>
      map(safe_log) |>
      transpose()
    #> $result
    #> $result[[1]]
    #> NULL
    #> 
    #> $result[[2]]
    #> [1] 2.302585
    #> 
    #> $result[[3]]
    #> [1] 4.60517
    #> 
    #> 
    #> $error
    #> $error[[1]]
    #> <simpleError in .f(...): non-numeric argument to mathematical function>
    #> 
    #> $error[[2]]
    #> NULL
    #> 
    #> $error[[3]]
    #> NULL
    #> 
    #> 
    
    # This is a bit easier to work with if you supply a default value
    # of the same type and use the simplify argument to transpose():
    safe_log <- safely(log, otherwise = NA_real_)
    list("a", 10, 100) |>
      map(safe_log) |>
      transpose() |>
      simplify_all()
    #> $result
    #> [1]       NA 2.302585 4.605170
    #> 
    #> $error
    #> $error[[1]]
    #> <simpleError in .f(...): non-numeric argument to mathematical function>
    #> 
    #> $error[[2]]
    #> NULL
    #> 
    #> $error[[3]]
    #> NULL
    #> 
    #>