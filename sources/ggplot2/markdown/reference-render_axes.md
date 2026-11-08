[Skip to content](https://ggplot2.tidyverse.org/reference/render_axes.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Render panel axes
=================

Source: [`R/facet-.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/facet-.R)

`render_axes.Rd`

These helpers facilitates generating theme compliant axes when building up the plot.

Usage[](https://ggplot2.tidyverse.org/reference/render_axes.html#ref-usage)

----------------------------------------------------------------------------

    render_axes(x = NULL, y = NULL, coord, theme, transpose = FALSE)

Arguments[](https://ggplot2.tidyverse.org/reference/render_axes.html#arguments)

--------------------------------------------------------------------------------

x, y[](https://ggplot2.tidyverse.org/reference/render_axes.html#arg-x-y)

A list of ranges as available to the draw\_panel method in `Facet` subclasses.

coord[](https://ggplot2.tidyverse.org/reference/render_axes.html#arg-coord)

A `Coord` object

theme[](https://ggplot2.tidyverse.org/reference/render_axes.html#arg-theme)

A `theme` object

transpose[](https://ggplot2.tidyverse.org/reference/render_axes.html#arg-transpose)

Should the output be transposed?

Value[](https://ggplot2.tidyverse.org/reference/render_axes.html#value)

------------------------------------------------------------------------

A list with the element "x" and "y" each containing axis specifications for the ranges passed in. Each axis specification is a list with a "top" and "bottom" element for x-axes and "left" and "right" element for y-axis, holding the respective axis grobs. Depending on the content of x and y some of the grobs might be zeroGrobs. If `transpose=TRUE` the content of the x and y elements will be transposed so e.g. all left-axes are collected in a left element as a list of grobs.