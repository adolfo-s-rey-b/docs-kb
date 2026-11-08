[Skip to content](https://ggplot2.tidyverse.org/reference/max_height.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Get the maximal width/length of a list of grobs
===============================================

Source: [`R/facet-.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/facet-.R)

`max_height.Rd`

Get the maximal width/length of a list of grobs

Usage[](https://ggplot2.tidyverse.org/reference/max_height.html#ref-usage)

---------------------------------------------------------------------------

    max_height(grobs, value_only = FALSE)
    
    max_width(grobs, value_only = FALSE)

Arguments[](https://ggplot2.tidyverse.org/reference/max_height.html#arguments)

-------------------------------------------------------------------------------

grobs[](https://ggplot2.tidyverse.org/reference/max_height.html#arg-grobs)

A list of grobs

value\_only[](https://ggplot2.tidyverse.org/reference/max_height.html#arg-value-only)

Should the return value be a simple numeric vector giving the maximum in cm

Value[](https://ggplot2.tidyverse.org/reference/max_height.html#value)

-----------------------------------------------------------------------

The largest value. measured in cm as a unit object or a numeric vector depending on `value_only`