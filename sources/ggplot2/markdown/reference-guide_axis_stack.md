[Skip to content](https://ggplot2.tidyverse.org/reference/guide_axis_stack.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Stacked axis guides
===================

Source: [`R/guide-axis-stack.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/guide-axis-stack.R)

`guide_axis_stack.Rd`

This guide can stack other position guides that represent position scales, like those created with [scale\_(x|y)\_continuous()](https://ggplot2.tidyverse.org/reference/scale_continuous.html)
 and [scale\_(x|y)\_discrete()](https://ggplot2.tidyverse.org/reference/scale_discrete.html)
.

Usage[](https://ggplot2.tidyverse.org/reference/guide_axis_stack.html#ref-usage)

---------------------------------------------------------------------------------

    guide_axis_stack(
      first = "axis",
      ...,
      title = waiver(),
      theme = NULL,
      spacing = NULL,
      order = 0,
      position = waiver()
    )

Arguments[](https://ggplot2.tidyverse.org/reference/guide_axis_stack.html#arguments)

-------------------------------------------------------------------------------------

first[](https://ggplot2.tidyverse.org/reference/guide_axis_stack.html#arg-first)

A position guide given as one of the following:

*   A string, for example `"axis"`.
    
*   A call to a guide function, for example `[guide_axis()](https://ggplot2.tidyverse.org/reference/guide_axis.html) `.
    

...[](https://ggplot2.tidyverse.org/reference/guide_axis_stack.html#arg--)

Additional guides to stack given in the same manner as `first`.

title[](https://ggplot2.tidyverse.org/reference/guide_axis_stack.html#arg-title)

A character string or expression indicating a title of guide. If `NULL`, the title is not shown. By default (`[waiver()](https://ggplot2.tidyverse.org/reference/waiver.html) `), the name of the scale object or the name specified in `[labs()](https://ggplot2.tidyverse.org/reference/labs.html) ` is used for the title.

theme[](https://ggplot2.tidyverse.org/reference/guide_axis_stack.html#arg-theme)

A `[theme](https://ggplot2.tidyverse.org/reference/theme.html) ` object to style the guide individually or differently from the plot's theme settings. The `theme` argument in the guide partially overrides, and is combined with, the plot's theme.

spacing[](https://ggplot2.tidyverse.org/reference/guide_axis_stack.html#arg-spacing)

A `[unit()](https://rdrr.io/r/grid/unit.html) ` objects that determines how far separate guides are spaced apart.

order[](https://ggplot2.tidyverse.org/reference/guide_axis_stack.html#arg-order)

A positive `integer` of length 1 that specifies the order of this guide among multiple guides. This controls in which order guides are merged if there are multiple guides for the same position. If 0 (default), the order is determined by a secret algorithm.

position[](https://ggplot2.tidyverse.org/reference/guide_axis_stack.html#arg-position)

Where this guide should be drawn: one of top, bottom, left, or right.

Details[](https://ggplot2.tidyverse.org/reference/guide_axis_stack.html#details)

---------------------------------------------------------------------------------

The `first` guide will be placed closest to the panel and any subsequent guides provided through `...` will follow in the given order.

Examples[](https://ggplot2.tidyverse.org/reference/guide_axis_stack.html#ref-examples)

---------------------------------------------------------------------------------------

    # A standard plot
    p <- ggplot(mpg, aes(displ, hwy)) +
      geom_point() +
      theme(axis.line = element_line())
    
    # A normal axis first, then a capped axis
    p + guides(x = guide_axis_stack("axis", guide_axis(cap = "both")))