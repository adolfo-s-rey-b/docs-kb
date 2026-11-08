[Skip to content](https://ggplot2.tidyverse.org/reference/guide_axis.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Axis guide
==========

Source: [`R/guide-axis.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/guide-axis.R)

`guide_axis.Rd`

Axis guides are the visual representation of position scales like those created with [scale\_(x|y)\_continuous()](https://ggplot2.tidyverse.org/reference/scale_continuous.html)
 and [scale\_(x|y)\_discrete()](https://ggplot2.tidyverse.org/reference/scale_discrete.html)
.

Usage[](https://ggplot2.tidyverse.org/reference/guide_axis.html#ref-usage)

---------------------------------------------------------------------------

    guide_axis(
      title = waiver(),
      theme = NULL,
      check.overlap = FALSE,
      angle = waiver(),
      n.dodge = 1,
      minor.ticks = FALSE,
      cap = "none",
      order = 0,
      position = waiver()
    )

Arguments[](https://ggplot2.tidyverse.org/reference/guide_axis.html#arguments)

-------------------------------------------------------------------------------

title[](https://ggplot2.tidyverse.org/reference/guide_axis.html#arg-title)

A character string or expression indicating a title of guide. If `NULL`, the title is not shown. By default (`[waiver()](https://ggplot2.tidyverse.org/reference/waiver.html) `), the name of the scale object or the name specified in `[labs()](https://ggplot2.tidyverse.org/reference/labs.html) ` is used for the title.

theme[](https://ggplot2.tidyverse.org/reference/guide_axis.html#arg-theme)

A `[theme](https://ggplot2.tidyverse.org/reference/theme.html) ` object to style the guide individually or differently from the plot's theme settings. The `theme` argument in the guide partially overrides, and is combined with, the plot's theme.

check.overlap[](https://ggplot2.tidyverse.org/reference/guide_axis.html#arg-check-overlap)

silently remove overlapping labels, (recursively) prioritizing the first, last, and middle labels.

angle[](https://ggplot2.tidyverse.org/reference/guide_axis.html#arg-angle)

Compared to setting the angle in `[theme()](https://ggplot2.tidyverse.org/reference/theme.html) ` / `[element_text()](https://ggplot2.tidyverse.org/reference/element.html) `, this also uses some heuristics to automatically pick the `hjust` and `vjust` that you probably want. Can be one of the following:

*   `NULL` to take the angles and `hjust`/`vjust` directly from the theme.
    
*   `[waiver()](https://ggplot2.tidyverse.org/reference/waiver.html) ` to allow reasonable defaults in special cases.
    
*   A number representing the text angle in degrees.
    

n.dodge[](https://ggplot2.tidyverse.org/reference/guide_axis.html#arg-n-dodge)

The number of rows (for vertical axes) or columns (for horizontal axes) that should be used to render the labels. This is useful for displaying labels that would otherwise overlap.

minor.ticks[](https://ggplot2.tidyverse.org/reference/guide_axis.html#arg-minor-ticks)

Whether to draw the minor ticks (`TRUE`) or not draw minor ticks (`FALSE`, default).

cap[](https://ggplot2.tidyverse.org/reference/guide_axis.html#arg-cap)

A `character` to cut the axis line back to the last breaks. Can be `"none"` (default) to draw the axis line along the whole panel, or `"upper"` and `"lower"` to draw the axis to the upper or lower break, or `"both"` to only draw the line in between the most extreme breaks. `TRUE` and `FALSE` are shorthand for `"both"` and `"none"` respectively.

order[](https://ggplot2.tidyverse.org/reference/guide_axis.html#arg-order)

A positive `integer` of length 1 that specifies the order of this guide among multiple guides. This controls in which order guides are merged if there are multiple guides for the same position. If 0 (default), the order is determined by a secret algorithm.

position[](https://ggplot2.tidyverse.org/reference/guide_axis.html#arg-position)

Where this guide should be drawn: one of top, bottom, left, or right.

Examples[](https://ggplot2.tidyverse.org/reference/guide_axis.html#ref-examples)

---------------------------------------------------------------------------------

    # plot with overlapping text
    p <- ggplot(mpg, aes(cty * 100, hwy * 100)) +
      geom_point() +
      facet_wrap(vars(class))
    
    # axis guides can be customized in the scale_* functions or
    # using guides()
    p + scale_x_continuous(guide = guide_axis(n.dodge = 2))
    
    p + guides(x = guide_axis(angle = 90))
    
    
    # can also be used to add a duplicate guide
    p + guides(x = guide_axis(n.dodge = 2), y.sec = guide_axis())