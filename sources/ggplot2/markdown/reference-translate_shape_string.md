[Skip to content](https://ggplot2.tidyverse.org/reference/translate_shape_string.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Translating shape strings
=========================

Source: [`R/geom-point.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/geom-point.R)

`translate_shape_string.Rd`

`translate_shape_string()` is a helper function for translating point shapes given as a character vector into integers that are interpreted by the grid system.

Usage[](https://ggplot2.tidyverse.org/reference/translate_shape_string.html#ref-usage)

---------------------------------------------------------------------------------------

    translate_shape_string(shape_string)

Arguments[](https://ggplot2.tidyverse.org/reference/translate_shape_string.html#arguments)

-------------------------------------------------------------------------------------------

shape\_string[](https://ggplot2.tidyverse.org/reference/translate_shape_string.html#arg-shape-string)

A character vector giving point shapes. Non-character input will be returned.

Value[](https://ggplot2.tidyverse.org/reference/translate_shape_string.html#value)

-----------------------------------------------------------------------------------

An integer vector with translated shapes.

Examples[](https://ggplot2.tidyverse.org/reference/translate_shape_string.html#ref-examples)

---------------------------------------------------------------------------------------------

    translate_shape_string(c("circle", "square", "triangle"))
    #> [1] 19 15 17
    
    # Strings with 1 or less characters are interpreted as symbols
    translate_shape_string(c("a", "b", "?"))
    #> [1] "a" "b" "?"