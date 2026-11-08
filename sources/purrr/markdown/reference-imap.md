[Skip to content](https://purrr.tidyverse.org/reference/imap.html#container)

![](https://purrr.tidyverse.org/logo.png)

Apply a function to each element of a vector, and its index
===========================================================

Source: [`R/imap.R`](https://github.com/tidyverse/purrr/blob/main/R/imap.R)

`imap.Rd`

`imap(x, ...)`, an indexed map, is short hand for `map2(x, names(x), ...)` if `x` has names, or `map2(x, seq_along(x), ...)` if it does not. This is useful if you need to compute on both the value and the position of an element.

Usage[](https://purrr.tidyverse.org/reference/imap.html#ref-usage)

-------------------------------------------------------------------

    imap(.x, .f, ...)
    
    imap_lgl(.x, .f, ...)
    
    imap_chr(.x, .f, ...)
    
    imap_int(.x, .f, ...)
    
    imap_dbl(.x, .f, ...)
    
    imap_vec(.x, .f, ...)
    
    iwalk(.x, .f, ...)

Arguments[](https://purrr.tidyverse.org/reference/imap.html#arguments)

-----------------------------------------------------------------------

.x[](https://purrr.tidyverse.org/reference/imap.html#arg--x)

A list or atomic vector.

.f[](https://purrr.tidyverse.org/reference/imap.html#arg--f)

A function, specified in one of the following ways:

*   A named function, e.g. `paste`.
    
*   An anonymous function, e.g. `\(x, idx) x + idx` or `function(x, idx) x + idx`.
    
*   A formula, e.g. `~ .x + .y`. Use `.x` to refer to the current element and `.y` to refer to the current index. No longer recommended.
    

[![[Experimental]](https://purrr.tidyverse.org/reference/figures/lifecycle-experimental.svg)](https://lifecycle.r-lib.org/articles/stages.html#experimental)

Wrap a function with `[in_parallel()](https://purrr.tidyverse.org/reference/in_parallel.html) ` to declare that it should be performed in parallel. See `[in_parallel()](https://purrr.tidyverse.org/reference/in_parallel.html) ` for more details. Use of `...` is not permitted in this context.

...[](https://purrr.tidyverse.org/reference/imap.html#arg--)

Additional arguments passed on to the mapped function.

We now generally recommend against using `...` to pass additional (constant) arguments to `.f`. Instead use a shorthand anonymous function:

    # Instead of
    x |> map(f, 1, 2, collapse = ",")
    # do:
    x |> map(\(x) f(x, 1, 2, collapse = ","))

This makes it easier to understand which arguments belong to which function and will tend to yield better error messages.

Value[](https://purrr.tidyverse.org/reference/imap.html#value)

---------------------------------------------------------------

A vector the same length as `.x`.

See also[](https://purrr.tidyverse.org/reference/imap.html#see-also)

---------------------------------------------------------------------

Other map variants: `[lmap()](https://purrr.tidyverse.org/reference/lmap.html) `, `[map()](https://purrr.tidyverse.org/reference/map.html) `, `[map2()](https://purrr.tidyverse.org/reference/map2.html) `, `[map_depth()](https://purrr.tidyverse.org/reference/map_depth.html) `, `[map_if()](https://purrr.tidyverse.org/reference/map_if.html) `, `[modify()](https://purrr.tidyverse.org/reference/modify.html) `, `[pmap()](https://purrr.tidyverse.org/reference/pmap.html) `

Examples[](https://purrr.tidyverse.org/reference/imap.html#ref-examples)

-------------------------------------------------------------------------

    imap_chr(sample(10), paste)
    #>  [1] "4 1"   "2 2"   "3 3"   "1 4"   "6 5"   "8 6"   "5 7"   "7 8"  
    #>  [9] "9 9"   "10 10"
    
    imap_chr(sample(10), \(x, idx) paste0(idx, ": ", x))
    #>  [1] "1: 6"  "2: 5"  "3: 2"  "4: 1"  "5: 4"  "6: 7"  "7: 8"  "8: 10"
    #>  [9] "9: 9"  "10: 3"
    
    iwalk(mtcars, \(x, idx) cat(idx, ": ", median(x), "\n", sep = ""))
    #> mpg: 19.2
    #> cyl: 6
    #> disp: 196.3
    #> hp: 123
    #> drat: 3.695
    #> wt: 3.325
    #> qsec: 17.71
    #> vs: 0
    #> am: 0
    #> gear: 4
    #> carb: 2