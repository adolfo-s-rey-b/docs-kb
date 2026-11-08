[Skip to content](https://ggplot2.tidyverse.org/reference/print.ggplot.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Explicitly draw plot
====================

Source: [`R/plot.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/plot.R)

`print.ggplot.Rd`

Generally, you do not need to print or plot a ggplot2 plot explicitly: the default top-level print method will do it for you. You will, however, need to call `[print()](https://rdrr.io/r/base/print.html) ` explicitly if you want to draw a plot inside a function or for loop.

Arguments[](https://ggplot2.tidyverse.org/reference/print.ggplot.html#arguments)

---------------------------------------------------------------------------------

x[](https://ggplot2.tidyverse.org/reference/print.ggplot.html#arg-x)

plot to display

newpage[](https://ggplot2.tidyverse.org/reference/print.ggplot.html#arg-newpage)

draw new (empty) page first?

vp[](https://ggplot2.tidyverse.org/reference/print.ggplot.html#arg-vp)

viewport to draw plot in

...[](https://ggplot2.tidyverse.org/reference/print.ggplot.html#arg--)

other arguments not used by this method

Value[](https://ggplot2.tidyverse.org/reference/print.ggplot.html#value)

-------------------------------------------------------------------------

Invisibly returns the original plot.

Examples[](https://ggplot2.tidyverse.org/reference/print.ggplot.html#ref-examples)

-----------------------------------------------------------------------------------

    colours <- c("class", "drv", "fl")
    
    # Doesn't seem to do anything!
    for (colour in colours) {
      ggplot(mpg, aes(displ, hwy, colour = .data[[colour]])) +
        geom_point()
    }
    
    for (colour in colours) {
      print(ggplot(mpg, aes(displ, hwy, colour = .data[[colour]])) +
              geom_point())
    }