[Skip to content](https://ggplot2.tidyverse.org/reference/annotation_logticks.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Annotation: log tick marks
==========================

Source: [`R/annotation-logticks.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/annotation-logticks.R)

`annotation_logticks.Rd`

[![[Superseded]](https://ggplot2.tidyverse.org/reference/figures/lifecycle-superseded.svg)](https://lifecycle.r-lib.org/articles/stages.html#superseded)

This function is superseded by using `[guide_axis_logticks()](https://ggplot2.tidyverse.org/reference/guide_axis_logticks.html) `.

This annotation adds log tick marks with diminishing spacing. These tick marks probably make sense only for base 10.

Usage[](https://ggplot2.tidyverse.org/reference/annotation_logticks.html#ref-usage)

------------------------------------------------------------------------------------

    annotation_logticks(
      base = 10,
      sides = "bl",
      outside = FALSE,
      scaled = TRUE,
      short = unit(0.1, "cm"),
      mid = unit(0.2, "cm"),
      long = unit(0.3, "cm"),
      colour = "black",
      linewidth = 0.5,
      linetype = 1,
      alpha = 1,
      color = NULL,
      ...,
      size = deprecated()
    )

Arguments[](https://ggplot2.tidyverse.org/reference/annotation_logticks.html#arguments)

----------------------------------------------------------------------------------------

base[](https://ggplot2.tidyverse.org/reference/annotation_logticks.html#arg-base)

the base of the log (default 10)

sides[](https://ggplot2.tidyverse.org/reference/annotation_logticks.html#arg-sides)

a string that controls which sides of the plot the log ticks appear on. It can be set to a string containing any of `"trbl"`, for top, right, bottom, and left.

outside[](https://ggplot2.tidyverse.org/reference/annotation_logticks.html#arg-outside)

logical that controls whether to move the log ticks outside of the plot area. Default is off (`FALSE`). You will also need to use `coord_cartesian(clip = "off")`. See examples.

scaled[](https://ggplot2.tidyverse.org/reference/annotation_logticks.html#arg-scaled)

is the data already log-scaled? This should be `TRUE` (default) when the data is already transformed with `[log10()](https://rdrr.io/r/base/Log.html) ` or when using `[scale_y_log10()](https://ggplot2.tidyverse.org/reference/scale_continuous.html) `. It should be `FALSE` when using `coord_transform(y = "log10")`.

short[](https://ggplot2.tidyverse.org/reference/annotation_logticks.html#arg-short)

a `[grid::unit()](https://rdrr.io/r/grid/unit.html) ` object specifying the length of the short tick marks

mid[](https://ggplot2.tidyverse.org/reference/annotation_logticks.html#arg-mid)

a `[grid::unit()](https://rdrr.io/r/grid/unit.html) ` object specifying the length of the middle tick marks. In base 10, these are the "5" ticks.

long[](https://ggplot2.tidyverse.org/reference/annotation_logticks.html#arg-long)

a `[grid::unit()](https://rdrr.io/r/grid/unit.html) ` object specifying the length of the long tick marks. In base 10, these are the "1" (or "10") ticks.

colour[](https://ggplot2.tidyverse.org/reference/annotation_logticks.html#arg-colour)

Colour of the tick marks.

linewidth[](https://ggplot2.tidyverse.org/reference/annotation_logticks.html#arg-linewidth)

Thickness of tick marks, in mm.

linetype[](https://ggplot2.tidyverse.org/reference/annotation_logticks.html#arg-linetype)

Linetype of tick marks (`solid`, `dashed`, etc.)

alpha[](https://ggplot2.tidyverse.org/reference/annotation_logticks.html#arg-alpha)

The transparency of the tick marks.

color[](https://ggplot2.tidyverse.org/reference/annotation_logticks.html#arg-color)

An alias for `colour`.

...[](https://ggplot2.tidyverse.org/reference/annotation_logticks.html#arg--)

Other parameters passed on to the layer

size[](https://ggplot2.tidyverse.org/reference/annotation_logticks.html#arg-size)

[![[Deprecated]](https://ggplot2.tidyverse.org/reference/figures/lifecycle-deprecated.svg)](https://lifecycle.r-lib.org/articles/stages.html#deprecated)

See also[](https://ggplot2.tidyverse.org/reference/annotation_logticks.html#see-also)

--------------------------------------------------------------------------------------

`[scale_y_continuous()](https://ggplot2.tidyverse.org/reference/scale_continuous.html) `, `[scale_y_log10()](https://ggplot2.tidyverse.org/reference/scale_continuous.html) ` for log scale transformations.

`[coord_transform()](https://ggplot2.tidyverse.org/reference/coord_transform.html) ` for log coordinate transformations.

Examples[](https://ggplot2.tidyverse.org/reference/annotation_logticks.html#ref-examples)

------------------------------------------------------------------------------------------

    # Make a log-log plot (without log ticks)
    a <- ggplot(msleep, aes(bodywt, brainwt)) +
     geom_point(na.rm = TRUE) +
     scale_x_log10(
       breaks = scales::trans_breaks("log10", \(x) 10^x),
       labels = scales::trans_format("log10", scales::math_format(10^.x))
     ) +
     scale_y_log10(
       breaks = scales::trans_breaks("log10", \(x) 10^x),
       labels = scales::trans_format("log10", scales::math_format(10^.x))
     ) +
     theme_bw()
    
    a + annotation_logticks()                # Default: log ticks on bottom and left
    
    a + annotation_logticks(sides = "lr")    # Log ticks for y, on left and right
    
    a + annotation_logticks(sides = "trbl")  # All four sides
    
    
    a + annotation_logticks(sides = "lr", outside = TRUE) +
     coord_cartesian(clip = "off")  # Ticks outside plot
    
    
    # Hide the minor grid lines because they don't align with the ticks
    a + annotation_logticks(sides = "trbl") + theme(panel.grid.minor = element_blank())
    
    
    # Another way to get the same results as 'a' above: log-transform the data before
    # plotting it. Also hide the minor grid lines.
    b <- ggplot(msleep, aes(log10(bodywt), log10(brainwt))) +
     geom_point(na.rm = TRUE) +
     scale_x_continuous(name = "body", labels = scales::label_math(10^.x)) +
     scale_y_continuous(name = "brain", labels = scales::label_math(10^.x)) +
     theme_bw() + theme(panel.grid.minor = element_blank())
    
    b + annotation_logticks()
    
    
    # Using a coordinate transform requires scaled = FALSE
    t <- ggplot(msleep, aes(bodywt, brainwt)) +
      geom_point() +
      coord_transform(x = "log10", y = "log10") +
      theme_bw()
    t + annotation_logticks(scaled = FALSE)
    #> Warning: Removed 27 rows containing missing values or values outside the scale
    #> range (`geom_point()`).
    
    
    # Change the length of the ticks
    a + annotation_logticks(
      short = unit(.5,"mm"),
      mid = unit(3,"mm"),
      long = unit(4,"mm")
    )