[Skip to content](https://ggplot2.tidyverse.org/reference/guide_axis_logticks.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Axis with logarithmic tick marks
================================

Source: [`R/guide-axis-logticks.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/guide-axis-logticks.R)

`guide_axis_logticks.Rd`

This axis guide replaces the placement of ticks marks at intervals in log10 space.

Usage[](https://ggplot2.tidyverse.org/reference/guide_axis_logticks.html#ref-usage)

------------------------------------------------------------------------------------

    guide_axis_logticks(
      long = 2.25,
      mid = 1.5,
      short = 0.75,
      prescale.base = NULL,
      negative.small = NULL,
      short.theme = element_line(),
      expanded = TRUE,
      cap = "none",
      theme = NULL,
      prescale_base = deprecated(),
      negative_small = deprecated(),
      short_theme = deprecated(),
      ...
    )

Arguments[](https://ggplot2.tidyverse.org/reference/guide_axis_logticks.html#arguments)

----------------------------------------------------------------------------------------

long, mid, short[](https://ggplot2.tidyverse.org/reference/guide_axis_logticks.html#arg-long-mid-short)

A `[grid::unit()](https://rdrr.io/r/grid/unit.html) ` object or `[rel()](https://ggplot2.tidyverse.org/reference/element.html) ` object setting the (relative) length of the long, middle and short ticks. Numeric values are interpreted as `[rel()](https://ggplot2.tidyverse.org/reference/element.html) ` objects. The `[rel()](https://ggplot2.tidyverse.org/reference/element.html) ` values are used to multiply values of the `axis.ticks.length` theme setting.

prescale.base[](https://ggplot2.tidyverse.org/reference/guide_axis_logticks.html#arg-prescale-base)

Base of logarithm used to transform data manually. The default, `NULL`, will use the scale transformation to calculate positions. Only set `prescale.base` if the data has already been log-transformed. When using a log-transform in the position scale or in `[coord_transform()](https://ggplot2.tidyverse.org/reference/coord_transform.html) `, keep the default `NULL` argument.

negative.small[](https://ggplot2.tidyverse.org/reference/guide_axis_logticks.html#arg-negative-small)

When the scale limits include 0 or negative numbers, what should be the smallest absolute value that is marked with a tick? If `NULL` (default), will be the smallest of 0.1 or 0.1 times the absolute scale maximum.

short.theme[](https://ggplot2.tidyverse.org/reference/guide_axis_logticks.html#arg-short-theme)

A theme [element](https://ggplot2.tidyverse.org/reference/element.html)
 for customising the display of the shortest ticks. Must be a line or blank element, and it inherits from the `axis.minor.ticks` setting for the relevant position.

expanded[](https://ggplot2.tidyverse.org/reference/guide_axis_logticks.html#arg-expanded)

Whether the ticks should cover the range after scale expansion (`TRUE`, default), or be restricted to the scale limits (`FALSE`).

cap[](https://ggplot2.tidyverse.org/reference/guide_axis_logticks.html#arg-cap)

A `character` to cut the axis line back to the last breaks. Can be `"none"` (default) to draw the axis line along the whole panel, or `"upper"` and `"lower"` to draw the axis to the upper or lower break, or `"both"` to only draw the line in between the most extreme breaks. `TRUE` and `FALSE` are shorthand for `"both"` and `"none"` respectively.

theme[](https://ggplot2.tidyverse.org/reference/guide_axis_logticks.html#arg-theme)

A `[theme](https://ggplot2.tidyverse.org/reference/theme.html) ` object to style the guide individually or differently from the plot's theme settings. The `theme` argument in the guide partially overrides, and is combined with, the plot's theme.

prescale\_base, negative\_small, short\_theme[](https://ggplot2.tidyverse.org/reference/guide_axis_logticks.html#arg-prescale-base-negative-small-short-theme)

[![[Deprecated]](https://ggplot2.tidyverse.org/reference/figures/lifecycle-deprecated.svg)](https://lifecycle.r-lib.org/articles/stages.html#deprecated)

...[](https://ggplot2.tidyverse.org/reference/guide_axis_logticks.html#arg--)

Arguments passed on to `[guide_axis](https://ggplot2.tidyverse.org/reference/guide_axis.html) `

`check.overlap`

silently remove overlapping labels, (recursively) prioritizing the first, last, and middle labels.

`angle`

Compared to setting the angle in `[theme()](https://ggplot2.tidyverse.org/reference/theme.html) ` / `[element_text()](https://ggplot2.tidyverse.org/reference/element.html) `, this also uses some heuristics to automatically pick the `hjust` and `vjust` that you probably want. Can be one of the following:

*   `NULL` to take the angles and `hjust`/`vjust` directly from the theme.
    
*   `[waiver()](https://ggplot2.tidyverse.org/reference/waiver.html) ` to allow reasonable defaults in special cases.
    
*   A number representing the text angle in degrees.
    

`n.dodge`

The number of rows (for vertical axes) or columns (for horizontal axes) that should be used to render the labels. This is useful for displaying labels that would otherwise overlap.

`order`

A positive `integer` of length 1 that specifies the order of this guide among multiple guides. This controls in which order guides are merged if there are multiple guides for the same position. If 0 (default), the order is determined by a secret algorithm.

`position`

Where this guide should be drawn: one of top, bottom, left, or right.

`title`

A character string or expression indicating a title of guide. If `NULL`, the title is not shown. By default (`[waiver()](https://ggplot2.tidyverse.org/reference/waiver.html) `), the name of the scale object or the name specified in `[labs()](https://ggplot2.tidyverse.org/reference/labs.html) ` is used for the title.

Examples[](https://ggplot2.tidyverse.org/reference/guide_axis_logticks.html#ref-examples)

------------------------------------------------------------------------------------------

    # A standard plot
    p <- ggplot(msleep, aes(bodywt, brainwt)) +
      geom_point(na.rm = TRUE)
    
    # The logticks axis works well with log scales
    p + scale_x_log10(guide = "axis_logticks") +
      scale_y_log10(guide = "axis_logticks")
    
    
    # Or with log-transformed coordinates
    p + coord_transform(x = "log10", y = "log10") +
      guides(x = "axis_logticks", y = "axis_logticks")
    
    
    # When data is transformed manually, one should provide `prescale.base`
    # Keep in mind that this axis uses log10 space for placement, not log2
    p + aes(x = log2(bodywt), y = log10(brainwt)) +
      guides(
        x = guide_axis_logticks(prescale.base = 2),
        y = guide_axis_logticks(prescale.base = 10)
      )
    
    
    # A plot with both positive and negative extremes, pseudo-log transformed
    set.seed(42)
    p2 <- ggplot(data.frame(x = rcauchy(1000)), aes(x = x)) +
      geom_density() +
      scale_x_continuous(
        breaks = c(-10^(4:0), 0, 10^(0:4)),
        transform = "pseudo_log"
      )
    
    # The log ticks are mirrored when 0 is included
    p2 + guides(x = "axis_logticks")
    
    
    # To control the tick density around 0, one can set `negative.small`
    p2 + guides(x = guide_axis_logticks(negative.small = 1))