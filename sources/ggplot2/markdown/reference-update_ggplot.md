[Skip to content](https://ggplot2.tidyverse.org/reference/update_ggplot.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Add custom objects to ggplot
============================

Source: [`R/plot-construction.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/plot-construction.R)

`update_ggplot.Rd`

This generic allows you to add your own methods for adding custom objects to a ggplot with [+.gg](https://ggplot2.tidyverse.org/reference/gg-add.html)
. The `ggplot_add()` function is vestigial and the `update_ggplot()` function should be used instead.

Usage[](https://ggplot2.tidyverse.org/reference/update_ggplot.html#ref-usage)

------------------------------------------------------------------------------

    update_ggplot(object, plot, ...)
    
    ggplot_add(object, plot, ...)

Arguments[](https://ggplot2.tidyverse.org/reference/update_ggplot.html#arguments)

----------------------------------------------------------------------------------

object[](https://ggplot2.tidyverse.org/reference/update_ggplot.html#arg-object)

An object to add to the plot

plot[](https://ggplot2.tidyverse.org/reference/update_ggplot.html#arg-plot)

The ggplot object to add `object` to

Value[](https://ggplot2.tidyverse.org/reference/update_ggplot.html#value)

--------------------------------------------------------------------------

A modified ggplot object

Details[](https://ggplot2.tidyverse.org/reference/update_ggplot.html#details)

------------------------------------------------------------------------------

Custom methods for `update_ggplot()` are intended to update the `plot` variable using information from a custom `object`. This can become convenient when writing extensions that don't build on the pre-existing grammar like layers, facets, coords and themes. The `update_ggplot()` function is never intended to be used directly, but it is triggered when an object is added to a plot via the `+` operator. Please note that the full `plot` object is exposed at this point, which comes with the responsibility of returning the plot intact.

Examples[](https://ggplot2.tidyverse.org/reference/update_ggplot.html#ref-examples)

------------------------------------------------------------------------------------

    # making a new method for the generic
    # in this example, we enable adding text elements
    S7::method(update_ggplot, list(element_text, class_ggplot)) <-
      function(object, plot, ...) {
        plot + theme(text = object)
      }
    
    # we can now use `+` to add our object to a plot
    ggplot(mpg, aes(displ, cty)) +
      geom_point() +
      element_text(colour = "red")
    
    
    # clean-up