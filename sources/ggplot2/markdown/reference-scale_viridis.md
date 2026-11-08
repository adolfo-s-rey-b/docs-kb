[Skip to content](https://ggplot2.tidyverse.org/reference/scale_viridis.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Viridis colour scales from viridisLite
======================================

Source: [`R/scale-viridis.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/scale-viridis.R)
, [`R/zxx.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/zxx.R)

`scale_viridis.Rd`

The `viridis` scales provide colour maps that are perceptually uniform in both colour and black-and-white. They are also designed to be perceived by viewers with common forms of colour blindness. See also [https://bids.github.io/colormap/](https://bids.github.io/colormap/)
.

Usage[](https://ggplot2.tidyverse.org/reference/scale_viridis.html#ref-usage)

------------------------------------------------------------------------------

    scale_colour_viridis_d(
      name = waiver(),
      ...,
      alpha = 1,
      begin = 0,
      end = 1,
      direction = 1,
      option = "D",
      aesthetics = "colour"
    )
    
    scale_fill_viridis_d(
      name = waiver(),
      ...,
      alpha = 1,
      begin = 0,
      end = 1,
      direction = 1,
      option = "D",
      aesthetics = "fill"
    )
    
    scale_colour_viridis_c(
      name = waiver(),
      ...,
      alpha = 1,
      begin = 0,
      end = 1,
      direction = 1,
      option = "D",
      values = NULL,
      space = "Lab",
      na.value = "grey50",
      guide = "colourbar",
      aesthetics = "colour"
    )
    
    scale_fill_viridis_c(
      name = waiver(),
      ...,
      alpha = 1,
      begin = 0,
      end = 1,
      direction = 1,
      option = "D",
      values = NULL,
      space = "Lab",
      na.value = "grey50",
      guide = "colourbar",
      aesthetics = "fill"
    )
    
    scale_colour_viridis_b(
      name = waiver(),
      ...,
      alpha = 1,
      begin = 0,
      end = 1,
      direction = 1,
      option = "D",
      values = NULL,
      space = "Lab",
      na.value = "grey50",
      guide = "coloursteps",
      aesthetics = "colour"
    )
    
    scale_fill_viridis_b(
      name = waiver(),
      ...,
      alpha = 1,
      begin = 0,
      end = 1,
      direction = 1,
      option = "D",
      values = NULL,
      space = "Lab",
      na.value = "grey50",
      guide = "coloursteps",
      aesthetics = "fill"
    )

Arguments[](https://ggplot2.tidyverse.org/reference/scale_viridis.html#arguments)

----------------------------------------------------------------------------------

name[](https://ggplot2.tidyverse.org/reference/scale_viridis.html#arg-name)

The name of the scale. Used as the axis or legend title. If `[waiver()](https://ggplot2.tidyverse.org/reference/waiver.html) `, the default, the name of the scale is taken from the first mapping used for that aesthetic. If `NULL`, the legend title will be omitted.

...[](https://ggplot2.tidyverse.org/reference/scale_viridis.html#arg--)

Other arguments passed on to `[discrete_scale()](https://ggplot2.tidyverse.org/reference/discrete_scale.html) `, `[continuous_scale()](https://ggplot2.tidyverse.org/reference/continuous_scale.html) `, or `[binned_scale()](https://ggplot2.tidyverse.org/reference/binned_scale.html) ` to control name, limits, breaks, labels and so forth.

alpha[](https://ggplot2.tidyverse.org/reference/scale_viridis.html#arg-alpha)

The alpha transparency, a number in \[0,1\], see argument alpha in `[hsv](https://rdrr.io/r/grDevices/hsv.html) `.

begin, end[](https://ggplot2.tidyverse.org/reference/scale_viridis.html#arg-begin-end)

The (corrected) hue in `[0,1]` at which the color map begins and ends.

direction[](https://ggplot2.tidyverse.org/reference/scale_viridis.html#arg-direction)

Sets the order of colors in the scale. If 1, the default, colors are ordered from darkest to lightest. If -1, the order of colors is reversed.

option[](https://ggplot2.tidyverse.org/reference/scale_viridis.html#arg-option)

A character string indicating the color map option to use. Eight options are available:

*   `"magma"` (or `"A"`)
    
*   `"inferno"` (or `"B"`)
    
*   `"plasma"` (or `"C"`)
    
*   `"viridis"` (or `"D"`)
    
*   `"cividis"` (or `"E"`)
    
*   `"rocket"` (or `"F"`)
    
*   `"mako"` (or `"G"`)
    
*   `"turbo"` (or `"H"`)
    

aesthetics[](https://ggplot2.tidyverse.org/reference/scale_viridis.html#arg-aesthetics)

Character string or vector of character strings listing the name(s) of the aesthetic(s) that this scale works with. This can be useful, for example, to apply colour settings to the `colour` and `fill` aesthetics at the same time, via `aesthetics = c("colour", "fill")`.

values[](https://ggplot2.tidyverse.org/reference/scale_viridis.html#arg-values)

if colours should not be evenly positioned along the gradient this vector gives the position (between 0 and 1) for each colour in the `colours` vector. See `[rescale()](https://scales.r-lib.org/reference/rescale.html) ` for a convenience function to map an arbitrary range to between 0 and 1.

space[](https://ggplot2.tidyverse.org/reference/scale_viridis.html#arg-space)

colour space in which to calculate gradient. Must be "Lab" - other values are deprecated.

na.value[](https://ggplot2.tidyverse.org/reference/scale_viridis.html#arg-na-value)

Missing values will be replaced with this value.

guide[](https://ggplot2.tidyverse.org/reference/scale_viridis.html#arg-guide)

A function used to create a guide or its name. See `[guides()](https://ggplot2.tidyverse.org/reference/guides.html) ` for more information.

See also[](https://ggplot2.tidyverse.org/reference/scale_viridis.html#see-also)

--------------------------------------------------------------------------------

The documentation on [colour aesthetics](https://ggplot2.tidyverse.org/reference/aes_colour_fill_alpha.html)
.

Other colour scales: `[scale_alpha()](https://ggplot2.tidyverse.org/reference/scale_alpha.html) `, `[scale_colour_brewer()](https://ggplot2.tidyverse.org/reference/scale_brewer.html) `, `[scale_colour_continuous()](https://ggplot2.tidyverse.org/reference/scale_colour_continuous.html) `, `[scale_colour_discrete()](https://ggplot2.tidyverse.org/reference/scale_colour_discrete.html) `, `[scale_colour_gradient()](https://ggplot2.tidyverse.org/reference/scale_gradient.html) `, `[scale_colour_grey()](https://ggplot2.tidyverse.org/reference/scale_grey.html) `, `[scale_colour_hue()](https://ggplot2.tidyverse.org/reference/scale_hue.html) `, `[scale_colour_identity()](https://ggplot2.tidyverse.org/reference/scale_identity.html) `, `[scale_colour_manual()](https://ggplot2.tidyverse.org/reference/scale_manual.html) `, `[scale_colour_steps()](https://ggplot2.tidyverse.org/reference/scale_steps.html) `

Examples[](https://ggplot2.tidyverse.org/reference/scale_viridis.html#ref-examples)

------------------------------------------------------------------------------------

    # viridis is the default colour/fill scale for ordered factors
    set.seed(596)
    dsamp <- diamonds[sample(nrow(diamonds), 1000), ]
    ggplot(dsamp, aes(carat, price)) +
      geom_point(aes(colour = clarity))
    
    
    # Use viridis_d with discrete data
    txsamp <- subset(txhousing, city %in%
      c("Houston", "Fort Worth", "San Antonio", "Dallas", "Austin"))
    (d <- ggplot(data = txsamp, aes(x = sales, y = median)) +
       geom_point(aes(colour = city)))
    
    d + scale_colour_viridis_d()
    
    
    # Change scale label
    d + scale_colour_viridis_d("City\nCenter")
    
    
    # Select palette to use, see ?scales::pal_viridis for more details
    d + scale_colour_viridis_d(option = "plasma")
    
    d + scale_colour_viridis_d(option = "inferno")
    
    
    # scale_fill_viridis_d works just the same as
    # scale_colour_viridis_d but for fill colours
    p <- ggplot(txsamp, aes(x = median, fill = city)) +
      geom_histogram(position = "dodge", binwidth = 15000)
    p + scale_fill_viridis_d()
    
    # the order of colour can be reversed
    p + scale_fill_viridis_d(direction = -1)
    
    
    # Use viridis_c with continuous data
    (v <- ggplot(faithfuld) +
      geom_tile(aes(waiting, eruptions, fill = density)))
    
    v + scale_fill_viridis_c()
    
    v + scale_fill_viridis_c(option = "plasma")
    
    
    # Use viridis_b to bin continuous data before mapping
    v + scale_fill_viridis_b()