[Skip to content](https://ggplot2.tidyverse.org/reference/as_labeller.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Coerce to labeller function
===========================

Source: [`R/labeller.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/labeller.R)

`as_labeller.Rd`

This transforms objects to labeller functions. Used internally by `[labeller()](https://ggplot2.tidyverse.org/reference/labeller.html) `.

Usage[](https://ggplot2.tidyverse.org/reference/as_labeller.html#ref-usage)

----------------------------------------------------------------------------

    as_labeller(x, default = label_value, multi_line = TRUE)

Arguments[](https://ggplot2.tidyverse.org/reference/as_labeller.html#arguments)

--------------------------------------------------------------------------------

x[](https://ggplot2.tidyverse.org/reference/as_labeller.html#arg-x)

Object to coerce to a labeller function. If a named character vector, it is used as a lookup table before being passed on to `default`. If a non-labeller function, it is assumed it takes and returns character vectors and is applied to the labels. If a labeller, it is simply applied to the labels.

default[](https://ggplot2.tidyverse.org/reference/as_labeller.html#arg-default)

Default labeller to process the labels produced by lookup tables or modified by non-labeller functions.

multi\_line[](https://ggplot2.tidyverse.org/reference/as_labeller.html#arg-multi-line)

Whether to display the labels of multiple factors on separate lines. This is passed to the labeller function.

See also[](https://ggplot2.tidyverse.org/reference/as_labeller.html#see-also)

------------------------------------------------------------------------------

`[labeller()](https://ggplot2.tidyverse.org/reference/labeller.html) `, [labellers](https://ggplot2.tidyverse.org/reference/labellers.html)

Examples[](https://ggplot2.tidyverse.org/reference/as_labeller.html#ref-examples)

----------------------------------------------------------------------------------

    p <- ggplot(mtcars, aes(disp, drat)) + geom_point()
    p + facet_wrap(~am)
    
    
    # Rename labels on the fly with a lookup character vector
    to_string <- as_labeller(c(`0` = "Zero", `1` = "One"))
    p + facet_wrap(~am, labeller = to_string)
    
    
    # Quickly transform a function operating on character vectors to a
    # labeller function:
    appender <- function(string, suffix = "-foo") paste0(string, suffix)
    p + facet_wrap(~am, labeller = as_labeller(appender))
    
    
    # If you have more than one faceting variable, be sure to dispatch
    # your labeller to the right variable with labeller()
    p + facet_grid(cyl ~ am, labeller = labeller(am = to_string))