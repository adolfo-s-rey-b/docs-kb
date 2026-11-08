[Skip to content](https://ggplot2.tidyverse.org/reference/gg_par.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Interpreter for graphical parameters
====================================

Source: [`R/utilities-grid.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/utilities-grid.R)

`gg_par.Rd`

This is a wrapper for `[grid::gpar()](https://rdrr.io/r/grid/gpar.html) ` that applies ggplot2's interpretation of graphical parameters.

Usage[](https://ggplot2.tidyverse.org/reference/gg_par.html#ref-usage)

-----------------------------------------------------------------------

    gg_par(..., stroke = NULL, pointsize = NULL)

Arguments[](https://ggplot2.tidyverse.org/reference/gg_par.html#arguments)

---------------------------------------------------------------------------

...[](https://ggplot2.tidyverse.org/reference/gg_par.html#arg--)

Named arguments passed on to `gpar()`.

stroke[](https://ggplot2.tidyverse.org/reference/gg_par.html#arg-stroke)

Linewidth for points. Populates the `lwd` grid parameter.

pointsize[](https://ggplot2.tidyverse.org/reference/gg_par.html#arg-pointsize)

Size for points. Populates the `fontsize` grid parameter.

Value[](https://ggplot2.tidyverse.org/reference/gg_par.html#value)

-------------------------------------------------------------------

An object of class 'gpar'.