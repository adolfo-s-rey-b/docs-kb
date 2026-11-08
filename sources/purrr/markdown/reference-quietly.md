[Skip to content](https://purrr.tidyverse.org/reference/quietly.html#container)

![](https://purrr.tidyverse.org/logo.png)

Wrap a function to capture side-effects
=======================================

Source: [`R/adverb-quietly.R`](https://github.com/tidyverse/purrr/blob/main/R/adverb-quietly.R)

`quietly.Rd`

Create a modified version of `.f` that captures side-effects along with the return value of the function and returns a list containing the `result`, `output`, `messages` and `warnings`.

Usage[](https://purrr.tidyverse.org/reference/quietly.html#ref-usage)

----------------------------------------------------------------------

    quietly(.f)

Arguments[](https://purrr.tidyverse.org/reference/quietly.html#arguments)

--------------------------------------------------------------------------

.f[](https://purrr.tidyverse.org/reference/quietly.html#arg--f)

A function to modify, specified in one of the following ways:

*   A named function, e.g. `mean`.
    
*   An anonymous function, e.g. `\(x) x + 1` or `function(x) x + 1`.
    
*   A formula, e.g. `~ .x + 1`. No longer recommended.
    

Value[](https://purrr.tidyverse.org/reference/quietly.html#value)

------------------------------------------------------------------

A function that takes the same arguments as `.f`, but returns a different value, as described above.

Adverbs[](https://purrr.tidyverse.org/reference/quietly.html#adverbs)

----------------------------------------------------------------------

This function is called an adverb because it modifies the effect of a function (a verb). If you'd like to include a function created an adverb in a package, be sure to read [faq-adverbs-export](https://purrr.tidyverse.org/reference/faq-adverbs-export.html)
.

See also[](https://purrr.tidyverse.org/reference/quietly.html#see-also)

------------------------------------------------------------------------

Other adverbs: `[auto_browse()](https://purrr.tidyverse.org/reference/auto_browse.html) `, `[compose()](https://purrr.tidyverse.org/reference/compose.html) `, `[insistently()](https://purrr.tidyverse.org/reference/insistently.html) `, `[negate()](https://purrr.tidyverse.org/reference/negate.html) `, `[partial()](https://purrr.tidyverse.org/reference/partial.html) `, `[possibly()](https://purrr.tidyverse.org/reference/possibly.html) `, `[safely()](https://purrr.tidyverse.org/reference/safely.html) `, `[slowly()](https://purrr.tidyverse.org/reference/slowly.html) `

Examples[](https://purrr.tidyverse.org/reference/quietly.html#ref-examples)

----------------------------------------------------------------------------

    f <- function() {
      print("Hi!")
      message("Hello")
      warning("How are ya?")
      "Gidday"
    }
    f()
    #> [1] "Hi!"
    #> Hello
    #> Warning: How are ya?
    #> [1] "Gidday"
    
    f_quiet <- quietly(f)
    str(f_quiet())
    #> List of 4
    #>  $ result  : chr "Gidday"
    #>  $ output  : chr "[1] \"Hi!\""
    #>  $ warnings: chr "How are ya?"
    #>  $ messages: chr "Hello\n"