[Skip to content](https://ggplot2.tidyverse.org/reference/guide_coloursteps.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Discretized colourbar guide
===========================

Source: [`R/guide-colorsteps.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/guide-colorsteps.R)

`guide_coloursteps.Rd`

This guide is version of `[guide_colourbar()](https://ggplot2.tidyverse.org/reference/guide_colourbar.html) ` for binned colour and fill scales. It shows areas between breaks as a single constant colour instead of the gradient known from the colourbar counterpart.

Usage[](https://ggplot2.tidyverse.org/reference/guide_coloursteps.html#ref-usage)

----------------------------------------------------------------------------------

    guide_coloursteps(
      title = waiver(),
      theme = NULL,
      alpha = NA,
      angle = NULL,
      even.steps = TRUE,
      show.limits = NULL,
      direction = NULL,
      position = NULL,
      reverse = FALSE,
      order = 0,
      available_aes = c("colour", "color", "fill"),
      ...
    )
    
    guide_colorsteps(
      title = waiver(),
      theme = NULL,
      alpha = NA,
      angle = NULL,
      even.steps = TRUE,
      show.limits = NULL,
      direction = NULL,
      position = NULL,
      reverse = FALSE,
      order = 0,
      available_aes = c("colour", "color", "fill"),
      ...
    )

Arguments[](https://ggplot2.tidyverse.org/reference/guide_coloursteps.html#arguments)

--------------------------------------------------------------------------------------

title[](https://ggplot2.tidyverse.org/reference/guide_coloursteps.html#arg-title)

A character string or expression indicating a title of guide. If `NULL`, the title is not shown. By default (`[waiver()](https://ggplot2.tidyverse.org/reference/waiver.html) `), the name of the scale object or the name specified in `[labs()](https://ggplot2.tidyverse.org/reference/labs.html) ` is used for the title.

theme[](https://ggplot2.tidyverse.org/reference/guide_coloursteps.html#arg-theme)

A `[theme](https://ggplot2.tidyverse.org/reference/theme.html) ` object to style the guide individually or differently from the plot's theme settings. The `theme` argument in the guide partially overrides, and is combined with, the plot's theme. Arguments that apply to a single legend are respected, most of which have the `legend`\-prefix. Arguments that apply to combined legends (the legend box) are ignored, including `legend.position`, `legend.justification.*`, `legend.location` and `legend.box.*`.

alpha[](https://ggplot2.tidyverse.org/reference/guide_coloursteps.html#arg-alpha)

A numeric between 0 and 1 setting the colour transparency of the bar. Use `NA` to preserve the alpha encoded in the colour itself (default).

angle[](https://ggplot2.tidyverse.org/reference/guide_coloursteps.html#arg-angle)

Overrules the theme settings to automatically apply appropriate `hjust` and `vjust` for angled legend text. Can be a single number representing the text angle in degrees, or `NULL` to not overrule the settings (default).

even.steps[](https://ggplot2.tidyverse.org/reference/guide_coloursteps.html#arg-even-steps)

Should the rendered size of the bins be equal, or should they be proportional to their length in the data space? Defaults to `TRUE`

show.limits[](https://ggplot2.tidyverse.org/reference/guide_coloursteps.html#arg-show-limits)

Logical. Should the limits of the scale be shown with labels and ticks. Default is `NULL` meaning it will take the value from the scale. This argument is ignored if `labels` is given as a vector of values. If one or both of the limits is also given in `breaks` it will be shown irrespective of the value of `show.limits`.

direction[](https://ggplot2.tidyverse.org/reference/guide_coloursteps.html#arg-direction)

A character string indicating the direction of the guide. One of "horizontal" or "vertical."

position[](https://ggplot2.tidyverse.org/reference/guide_coloursteps.html#arg-position)

A character string indicating where the legend should be placed relative to the plot panels. One of "top", "right", "bottom", "left", or "inside".

reverse[](https://ggplot2.tidyverse.org/reference/guide_coloursteps.html#arg-reverse)

logical. If `TRUE` the colourbar is reversed. By default, the highest value is on the top and the lowest value is on the bottom

order[](https://ggplot2.tidyverse.org/reference/guide_coloursteps.html#arg-order)

positive integer less than 99 that specifies the order of this guide among multiple guides. This controls the order in which multiple guides are displayed, not the contents of the guide itself. If 0 (default), the order is determined by a secret algorithm.

available\_aes[](https://ggplot2.tidyverse.org/reference/guide_coloursteps.html#arg-available-aes)

A vector of character strings listing the aesthetics for which a colourbar can be drawn.

...[](https://ggplot2.tidyverse.org/reference/guide_coloursteps.html#arg--)

ignored.

Value[](https://ggplot2.tidyverse.org/reference/guide_coloursteps.html#value)

------------------------------------------------------------------------------

A guide object

Use with discrete scale[](https://ggplot2.tidyverse.org/reference/guide_coloursteps.html#use-with-discrete-scale)

------------------------------------------------------------------------------------------------------------------

This guide is intended to show binned data and work together with ggplot2's binning scales. However, it is sometimes desirable to perform the binning in a separate step, either as part of a stat (e.g. `[stat_contour_filled()](https://ggplot2.tidyverse.org/reference/geom_contour.html) `) or prior to the visualisation. If you want to use this guide for discrete data the levels must follow the naming scheme implemented by `[base::cut()](https://rdrr.io/r/base/cut.html) `. This means that a bin must be encoded as `"(<lower>, <upper>]"` with `<lower>` giving the lower bound of the bin and `<upper>` giving the upper bound (`"[<lower>, <upper>)"` is also accepted). If you use `[base::cut()](https://rdrr.io/r/base/cut.html) ` to perform the binning everything should work as expected, if not, some recoding may be needed.\
\
See also[](https://ggplot2.tidyverse.org/reference/guide_coloursteps.html#see-also)\
\
------------------------------------------------------------------------------------\
\
The [binned legend section](https://ggplot2-book.org/scales-colour#sec-guide-coloursteps)\
 of the online ggplot2 book.\
\
Other guides: `[guide_bins()](https://ggplot2.tidyverse.org/reference/guide_bins.html) `, `[guide_colourbar()](https://ggplot2.tidyverse.org/reference/guide_colourbar.html) `, `[guide_legend()](https://ggplot2.tidyverse.org/reference/guide_legend.html) `, `[guides()](https://ggplot2.tidyverse.org/reference/guides.html) `\
\
Examples[](https://ggplot2.tidyverse.org/reference/guide_coloursteps.html#ref-examples)\
\
----------------------------------------------------------------------------------------\
\
    df <- expand.grid(X1 = 1:10, X2 = 1:10)\
    df$value <- df$X1 * df$X2\
    \
    p <- ggplot(df, aes(X1, X2)) + geom_tile(aes(fill = value))\
    \
    # Coloursteps guide is the default for binned colour scales\
    p + scale_fill_binned()\
    \
    \
    # By default each bin in the guide is the same size irrespectively of how\
    # their sizes relate in data space\
    p + scale_fill_binned(breaks = c(10, 25, 50))\
    \
    \
    # This can be changed with the `even.steps` argument\
    p + scale_fill_binned(\
      breaks = c(10, 25, 50),\
      guide = guide_coloursteps(even.steps = FALSE)\
    )\
    \
    \
    # By default the limits is not shown, but this can be changed\
    p + scale_fill_binned(guide = guide_coloursteps(show.limits = TRUE))\
    \
    \
    # (can also be set in the scale)\
    p + scale_fill_binned(show.limits = TRUE)