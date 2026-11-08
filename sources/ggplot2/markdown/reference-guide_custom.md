[Skip to content](https://ggplot2.tidyverse.org/reference/guide_custom.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Custom guides
=============

Source: [`R/guide-custom.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/guide-custom.R)

`guide_custom.Rd`

This is a special guide that can be used to display any graphical object (grob) along with the regular guides. This guide has no associated scale.

Usage[](https://ggplot2.tidyverse.org/reference/guide_custom.html#ref-usage)

-----------------------------------------------------------------------------

    guide_custom(
      grob,
      width = grobWidth(grob),
      height = grobHeight(grob),
      title = NULL,
      theme = NULL,
      position = NULL,
      order = 0
    )

Arguments[](https://ggplot2.tidyverse.org/reference/guide_custom.html#arguments)

---------------------------------------------------------------------------------

grob[](https://ggplot2.tidyverse.org/reference/guide_custom.html#arg-grob)

A grob to display.

width, height[](https://ggplot2.tidyverse.org/reference/guide_custom.html#arg-width-height)

The allocated width and height to display the grob, given in `[grid::unit()](https://rdrr.io/r/grid/unit.html) `s.

title[](https://ggplot2.tidyverse.org/reference/guide_custom.html#arg-title)

A character string or expression indicating the title of guide. If `NULL` (default), no title is shown.

theme[](https://ggplot2.tidyverse.org/reference/guide_custom.html#arg-theme)

A `[theme](https://ggplot2.tidyverse.org/reference/theme.html) ` object to style the guide individually or differently from the plot's theme settings. The `theme` argument in the guide partially overrides, and is combined with, the plot's theme. Arguments that apply to a single legend are respected, most of which have the `legend`\-prefix. Arguments that apply to combined legends (the legend box) are ignored, including `legend.position`, `legend.justification.*`, `legend.location` and `legend.box.*`.

position[](https://ggplot2.tidyverse.org/reference/guide_custom.html#arg-position)

A character string indicating where the legend should be placed relative to the plot panels. One of "top", "right", "bottom", "left", or "inside".

order[](https://ggplot2.tidyverse.org/reference/guide_custom.html#arg-order)

positive integer less than 99 that specifies the order of this guide among multiple guides. This controls the order in which multiple guides are displayed, not the contents of the guide itself. If 0 (default), the order is determined by a secret algorithm.

Examples[](https://ggplot2.tidyverse.org/reference/guide_custom.html#ref-examples)

-----------------------------------------------------------------------------------

    # A standard plot
    p <- ggplot(mpg, aes(displ, hwy)) +
      geom_point()
    
    # Define a graphical object
    circle <- grid::circleGrob()
    
    # Rendering a grob as a guide
    p + guides(custom = guide_custom(circle, title = "My circle"))
    
    
    # Controlling the size of the grob defined in relative units
    p + guides(custom = guide_custom(
      circle, title = "My circle",
      width = unit(2, "cm"), height = unit(2, "cm"))
    )
    
    
    # Size of grobs in absolute units is taken directly without the need to
    # set these manually
    p + guides(custom = guide_custom(
      title = "My circle",
      grob = grid::circleGrob(r = unit(1, "cm"))
    ))