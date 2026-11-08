[Skip to content](https://ggplot2.tidyverse.org/reference/fill_alpha.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Modify fill transparency
========================

Source: [`R/utilities-patterns.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/utilities-patterns.R)

`fill_alpha.Rd`

This works much like [alpha()](https://scales.r-lib.org/reference/alpha.html)
 in that it modifies the transparency of fill colours. It differs in that `fill_alpha()` also attempts to set the transparency of `<GridPattern>` objects.

Usage[](https://ggplot2.tidyverse.org/reference/fill_alpha.html#ref-usage)

---------------------------------------------------------------------------

    fill_alpha(fill, alpha)

Arguments[](https://ggplot2.tidyverse.org/reference/fill_alpha.html#arguments)

-------------------------------------------------------------------------------

fill[](https://ggplot2.tidyverse.org/reference/fill_alpha.html#arg-fill)

A fill colour given as a `character` or `integer` vector, or as a (list of) `<GridPattern>` object(s).

alpha[](https://ggplot2.tidyverse.org/reference/fill_alpha.html#arg-alpha)

A transparency value between 0 (transparent) and 1 (opaque), parallel to `fill`.

Value[](https://ggplot2.tidyverse.org/reference/fill_alpha.html#value)

-----------------------------------------------------------------------

A `character` vector of colours, or list of `<GridPattern>` objects.

Examples[](https://ggplot2.tidyverse.org/reference/fill_alpha.html#ref-examples)

---------------------------------------------------------------------------------

    # Typical colour input
    fill_alpha("red", 0.5)
    #> [1] "#FF000080"
    
    if (utils::packageVersion("grid") > "4.2") {
      # Pattern input
      fill_alpha(list(grid::linearGradient()), 0.5)
    }
    #> [[1]]
    #> $x1
    #> [1] 0npc
    #> 
    #> $y1
    #> [1] 0npc
    #> 
    #> $x2
    #> [1] 1npc
    #> 
    #> $y2
    #> [1] 1npc
    #> 
    #> $stops
    #> [1] 0 1
    #> 
    #> $colours
    #> [1] "#00000080" "#FFFFFF80"
    #> 
    #> $extend
    #> [1] "pad"
    #> 
    #> $group
    #> [1] TRUE
    #> 
    #> attr(,"class")
    #> [1] "GridLinearGradient" "GridPattern"       
    #>