[Skip to content](https://ggplot2.tidyverse.org/reference/aes_all.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Given a character vector, create a set of identity mappings
===========================================================

Source: [`R/aes.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/aes.R)

`aes_all.Rd`

Given a character vector, create a set of identity mappings

Usage[](https://ggplot2.tidyverse.org/reference/aes_all.html#ref-usage)

------------------------------------------------------------------------

    aes_all(vars)

Arguments[](https://ggplot2.tidyverse.org/reference/aes_all.html#arguments)

----------------------------------------------------------------------------

vars[](https://ggplot2.tidyverse.org/reference/aes_all.html#arg-vars)

vector of variable names

Examples[](https://ggplot2.tidyverse.org/reference/aes_all.html#ref-examples)

------------------------------------------------------------------------------

    aes_all(names(mtcars))
    #> Aesthetic mapping: 
    #> * `mpg`  -> `mpg`
    #> * `cyl`  -> `cyl`
    #> * `disp` -> `disp`
    #> * `hp`   -> `hp`
    #> * `drat` -> `drat`
    #> * `wt`   -> `wt`
    #> * `qsec` -> `qsec`
    #> * `vs`   -> `vs`
    #> * `am`   -> `am`
    #> * `gear` -> `gear`
    #> * `carb` -> `carb`
    aes_all(c("x", "y", "col", "pch"))
    #> Aesthetic mapping: 
    #> * `x`      -> `x`
    #> * `y`      -> `y`
    #> * `colour` -> `col`
    #> * `shape`  -> `pch`