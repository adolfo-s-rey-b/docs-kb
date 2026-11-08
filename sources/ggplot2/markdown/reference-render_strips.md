[Skip to content](https://ggplot2.tidyverse.org/reference/render_strips.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Render panel strips
===================

Source: [`R/facet-.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/facet-.R)

`render_strips.Rd`

All positions are rendered and it is up to the facet to decide which to use

Usage[](https://ggplot2.tidyverse.org/reference/render_strips.html#ref-usage)

------------------------------------------------------------------------------

    render_strips(x = NULL, y = NULL, labeller = identity, theme)

Arguments[](https://ggplot2.tidyverse.org/reference/render_strips.html#arguments)

----------------------------------------------------------------------------------

x, y[](https://ggplot2.tidyverse.org/reference/render_strips.html#arg-x-y)

A data.frame with a column for each variable and a row for each combination to draw

labeller[](https://ggplot2.tidyverse.org/reference/render_strips.html#arg-labeller)

A labeller function

theme[](https://ggplot2.tidyverse.org/reference/render_strips.html#arg-theme)

a `theme` object

Value[](https://ggplot2.tidyverse.org/reference/render_strips.html#value)

--------------------------------------------------------------------------

A list with an "x" and a "y" element, each containing a "top" and "bottom" or "left" and "right" element respectively. These contains a list of rendered strips as gtables.