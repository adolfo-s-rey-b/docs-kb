[Skip to content](https://ggplot2.tidyverse.org/reference/ignoring_data.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Ignoring and exposing data
==========================

Source: [`R/utilities.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/utilities.R)

`ignoring_data.Rd`

The `.ignore_data()` function is used to hide `<AsIs>` columns during scale interactions in `[ggplot_build()](https://ggplot2.tidyverse.org/reference/ggplot_build.html) `. The `.expose_data()` function is used to restore hidden columns.

Usage[](https://ggplot2.tidyverse.org/reference/ignoring_data.html#ref-usage)

------------------------------------------------------------------------------

    .ignore_data(data)
    
    .expose_data(data)

Arguments[](https://ggplot2.tidyverse.org/reference/ignoring_data.html#arguments)

----------------------------------------------------------------------------------

data[](https://ggplot2.tidyverse.org/reference/ignoring_data.html#arg-data)

A list of `<data.frame>`s.

Value[](https://ggplot2.tidyverse.org/reference/ignoring_data.html#value)

--------------------------------------------------------------------------

A modified list of `<data.frame>s`

Examples[](https://ggplot2.tidyverse.org/reference/ignoring_data.html#ref-examples)

------------------------------------------------------------------------------------

    data <- list(
      data.frame(x = 1:3, y = I(1:3)),
      data.frame(w = I(1:3), z = 1:3)
    )
    
    ignored <- .ignore_data(data)
    str(ignored)
    #> List of 2
    #>  $ :'data.frame':	3 obs. of  2 variables:
    #>   ..$ x       : int [1:3] 1 2 3
    #>   ..$ .ignored:'data.frame':	3 obs. of  1 variable:
    #>   .. ..$ y: 'AsIs' int [1:3] 1 2 3
    #>  $ :'data.frame':	3 obs. of  2 variables:
    #>   ..$ z       : int [1:3] 1 2 3
    #>   ..$ .ignored:'data.frame':	3 obs. of  1 variable:
    #>   .. ..$ w: 'AsIs' int [1:3] 1 2 3
    
    .expose_data(ignored)
    #> [[1]]
    #>   x y
    #> 1 1 1
    #> 2 2 2
    #> 3 3 3
    #> 
    #> [[2]]
    #>   z w
    #> 1 1 1
    #> 2 2 2
    #> 3 3 3
    #>