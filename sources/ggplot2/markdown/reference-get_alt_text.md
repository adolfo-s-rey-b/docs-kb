[Skip to content](https://ggplot2.tidyverse.org/reference/get_alt_text.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Extract alt text from a plot
============================

Source: [`R/labels.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/labels.R)

`get_alt_text.Rd`

This function returns a text that can be used as alt-text in webpages etc. Currently it will use the `alt` label, added with `+ labs(alt = <...>)`, or a return an empty string, but in the future it might try to generate an alt text from the information stored in the plot.

Usage[](https://ggplot2.tidyverse.org/reference/get_alt_text.html#ref-usage)

-----------------------------------------------------------------------------

    get_alt_text(p, ...)

Arguments[](https://ggplot2.tidyverse.org/reference/get_alt_text.html#arguments)

---------------------------------------------------------------------------------

p[](https://ggplot2.tidyverse.org/reference/get_alt_text.html#arg-p)

a ggplot object

...[](https://ggplot2.tidyverse.org/reference/get_alt_text.html#arg--)

Arguments passed to methods.

Value[](https://ggplot2.tidyverse.org/reference/get_alt_text.html#value)

-------------------------------------------------------------------------

A text string

Examples[](https://ggplot2.tidyverse.org/reference/get_alt_text.html#ref-examples)

-----------------------------------------------------------------------------------

    p <- ggplot(mpg, aes(displ, hwy)) +
      geom_point()
    
    # Returns an empty string
    get_alt_text(p)
    #> [1] ""
    
    # A user provided alt text
    p <- p + labs(
      alt = paste("A scatterplot showing the negative correlation between engine",
                  "displacement as a function of highway miles per gallon")
    )
    
    get_alt_text(p)
    #> [1] "A scatterplot showing the negative correlation between engine displacement as a function of highway miles per gallon"