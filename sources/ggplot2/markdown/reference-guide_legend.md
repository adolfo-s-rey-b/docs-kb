[Skip to content](https://ggplot2.tidyverse.org/reference/guide_legend.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Legend guide
============

Source: [`R/guide-legend.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/guide-legend.R)

`guide_legend.Rd`

Legend type guide shows key (i.e., geoms) mapped onto values. Legend guides for various scales are integrated if possible.

Usage[](https://ggplot2.tidyverse.org/reference/guide_legend.html#ref-usage)

-----------------------------------------------------------------------------

    guide_legend(
      title = waiver(),
      theme = NULL,
      position = NULL,
      direction = NULL,
      override.aes = list(),
      nrow = NULL,
      ncol = NULL,
      reverse = FALSE,
      order = 0,
      ...
    )

Arguments[](https://ggplot2.tidyverse.org/reference/guide_legend.html#arguments)

---------------------------------------------------------------------------------

title[](https://ggplot2.tidyverse.org/reference/guide_legend.html#arg-title)

A character string or expression indicating a title of guide. If `NULL`, the title is not shown. By default (`[waiver()](https://ggplot2.tidyverse.org/reference/waiver.html) `), the name of the scale object or the name specified in `[labs()](https://ggplot2.tidyverse.org/reference/labs.html) ` is used for the title.

theme[](https://ggplot2.tidyverse.org/reference/guide_legend.html#arg-theme)

A `[theme](https://ggplot2.tidyverse.org/reference/theme.html) ` object to style the guide individually or differently from the plot's theme settings. The `theme` argument in the guide partially overrides, and is combined with, the plot's theme. Arguments that apply to a single legend are respected, most of which have the `legend`\-prefix. Arguments that apply to combined legends (the legend box) are ignored, including `legend.position`, `legend.justification.*`, `legend.location` and `legend.box.*`.

position[](https://ggplot2.tidyverse.org/reference/guide_legend.html#arg-position)

A character string indicating where the legend should be placed relative to the plot panels. One of "top", "right", "bottom", "left", or "inside".

direction[](https://ggplot2.tidyverse.org/reference/guide_legend.html#arg-direction)

A character string indicating the direction of the guide. One of "horizontal" or "vertical".

override.aes[](https://ggplot2.tidyverse.org/reference/guide_legend.html#arg-override-aes)

A list specifying aesthetic parameters of legend key. See details and examples.

nrow, ncol[](https://ggplot2.tidyverse.org/reference/guide_legend.html#arg-nrow-ncol)

The desired number of rows and column of legends respectively.

reverse[](https://ggplot2.tidyverse.org/reference/guide_legend.html#arg-reverse)

logical. If `TRUE` the order of legends is reversed.

order[](https://ggplot2.tidyverse.org/reference/guide_legend.html#arg-order)

positive integer less than 99 that specifies the order of this guide among multiple guides. This controls the order in which multiple guides are displayed, not the contents of the guide itself. If 0 (default), the order is determined by a secret algorithm.

...[](https://ggplot2.tidyverse.org/reference/guide_legend.html#arg--)

ignored.

Details[](https://ggplot2.tidyverse.org/reference/guide_legend.html#details)

-----------------------------------------------------------------------------

Guides can be specified in each `scale_*` or in `[guides()](https://ggplot2.tidyverse.org/reference/guides.html) `. `guide = "legend"` in `scale_*` is syntactic sugar for `guide = guide_legend()` (e.g. `scale_color_manual(guide = "legend")`). As for how to specify the guide for each scale in more detail, see `[guides()](https://ggplot2.tidyverse.org/reference/guides.html) `.

See also[](https://ggplot2.tidyverse.org/reference/guide_legend.html#see-also)

-------------------------------------------------------------------------------

The [legends section](https://ggplot2-book.org/scales-colour#sec-guide-legend)
 of the online ggplot2 book.

Other guides: `[guide_bins()](https://ggplot2.tidyverse.org/reference/guide_bins.html) `, `[guide_colourbar()](https://ggplot2.tidyverse.org/reference/guide_colourbar.html) `, `[guide_coloursteps()](https://ggplot2.tidyverse.org/reference/guide_coloursteps.html) `, `[guides()](https://ggplot2.tidyverse.org/reference/guides.html) `

Examples[](https://ggplot2.tidyverse.org/reference/guide_legend.html#ref-examples)

-----------------------------------------------------------------------------------

    # \donttest{
    df <- expand.grid(X1 = 1:10, X2 = 1:10)
    df$value <- df$X1 * df$X2
    
    p1 <- ggplot(df, aes(X1, X2)) + geom_tile(aes(fill = value))
    p2 <- p1 + geom_point(aes(size = value))
    
    # Basic form
    p1 + scale_fill_continuous(guide = guide_legend())
    
    
    # Control styles
    
    # title position
    p1 + guides(fill = guide_legend(
      title = "LEFT", theme(legend.title.position = "left")
    ))
    
    
    # title text styles via element_text
    p1 + guides(fill = guide_legend(theme = theme(
      legend.title = element_text(size = 15, face = "italic", colour = "red")
    )))
    
    
    # label position
    p1 + guides(fill = guide_legend(theme = theme(
      legend.text.position = "left",
      legend.text = element_text(hjust = 1)
    )))
    
    
    # label styles
    p1 +
      scale_fill_continuous(
        breaks = c(5, 10, 15),
        labels = paste("long", c(5, 10, 15)),
        guide = guide_legend(theme = theme(
          legend.direction = "horizontal",
          legend.title.position = "top",
          legend.text.position = "bottom",
          legend.text = element_text(hjust = 0.5, vjust = 1, angle = 90)
        ))
      )
    
    
    # Set aesthetic of legend key
    # very low alpha value make it difficult to see legend key
    p3 <- ggplot(mtcars, aes(vs, am, colour = factor(cyl))) +
      geom_jitter(alpha = 1/5, width = 0.01, height = 0.01)
    p3
    
    # override.aes overwrites the alpha
    p3 + guides(colour = guide_legend(override.aes = list(alpha = 1)))
    
    
    # multiple row/col legends
    df <- data.frame(x = 1:20, y = 1:20, color = letters[1:20])
    p <- ggplot(df, aes(x, y)) +
      geom_point(aes(colour = color))
    p + guides(col = guide_legend(nrow = 8))
    
    p + guides(col = guide_legend(ncol = 8))
    
    p + guides(col = guide_legend(nrow = 8, theme = theme(legend.byrow = TRUE)))
    
    
    # reversed order legend
    p + guides(col = guide_legend(reverse = TRUE))
    
    # }