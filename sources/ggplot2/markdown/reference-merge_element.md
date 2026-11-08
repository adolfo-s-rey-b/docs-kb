[Skip to content](https://ggplot2.tidyverse.org/reference/merge_element.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Merge a parent element into a child element
===========================================

Source: [`R/theme.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/theme.R)

`merge_element.Rd`

This is a generic and element classes must provide an implementation of this method

Usage[](https://ggplot2.tidyverse.org/reference/merge_element.html#ref-usage)

------------------------------------------------------------------------------

    merge_element(new, old, ...)

Arguments[](https://ggplot2.tidyverse.org/reference/merge_element.html#arguments)

----------------------------------------------------------------------------------

new[](https://ggplot2.tidyverse.org/reference/merge_element.html#arg-new)

The child element in the theme hierarchy

old[](https://ggplot2.tidyverse.org/reference/merge_element.html#arg-old)

The parent element in the theme hierarchy

Value[](https://ggplot2.tidyverse.org/reference/merge_element.html#value)

--------------------------------------------------------------------------

A modified version of `new` updated with the properties of `old`

Examples[](https://ggplot2.tidyverse.org/reference/merge_element.html#ref-examples)

------------------------------------------------------------------------------------

    new <- element_text(colour = "red")
    old <- element_text(colour = "blue", size = 10)
    
    # Adopt size but ignore colour
    merge_element(new, old)
    #> <ggplot2::element_text>
    #>  @ family       : NULL
    #>  @ face         : NULL
    #>  @ italic       : chr NA
    #>  @ fontweight   : num NA
    #>  @ fontwidth    : num NA
    #>  @ colour       : chr "red"
    #>  @ size         : num 10
    #>  @ hjust        : NULL
    #>  @ vjust        : NULL
    #>  @ angle        : NULL
    #>  @ lineheight   : NULL
    #>  @ margin       : NULL
    #>  @ debug        : NULL
    #>  @ inherit.blank: logi FALSE