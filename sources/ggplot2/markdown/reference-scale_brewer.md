[Skip to content](https://ggplot2.tidyverse.org/reference/scale_brewer.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Sequential, diverging and qualitative colour scales from ColorBrewer
====================================================================

Source: [`R/scale-brewer.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/scale-brewer.R)
, [`R/zxx.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/zxx.R)

`scale_brewer.Rd`

The `brewer` scales provide sequential, diverging and qualitative colour schemes from ColorBrewer. These are particularly well suited to display discrete values on a map. See [https://colorbrewer2.org](https://colorbrewer2.org/)
 for more information.

Usage[](https://ggplot2.tidyverse.org/reference/scale_brewer.html#ref-usage)

-----------------------------------------------------------------------------

    scale_colour_brewer(
      name = waiver(),
      ...,
      type = "seq",
      palette = 1,
      direction = 1,
      aesthetics = "colour"
    )
    
    scale_fill_brewer(
      name = waiver(),
      ...,
      type = "seq",
      palette = 1,
      direction = 1,
      aesthetics = "fill"
    )
    
    scale_colour_distiller(
      name = waiver(),
      ...,
      type = "seq",
      palette = 1,
      direction = -1,
      values = NULL,
      space = "Lab",
      na.value = "grey50",
      guide = "colourbar",
      aesthetics = "colour"
    )
    
    scale_fill_distiller(
      name = waiver(),
      ...,
      type = "seq",
      palette = 1,
      direction = -1,
      values = NULL,
      space = "Lab",
      na.value = "grey50",
      guide = "colourbar",
      aesthetics = "fill"
    )
    
    scale_colour_fermenter(
      name = waiver(),
      ...,
      type = "seq",
      palette = 1,
      direction = -1,
      na.value = "grey50",
      guide = "coloursteps",
      aesthetics = "colour"
    )
    
    scale_fill_fermenter(
      name = waiver(),
      ...,
      type = "seq",
      palette = 1,
      direction = -1,
      na.value = "grey50",
      guide = "coloursteps",
      aesthetics = "fill"
    )

Arguments[](https://ggplot2.tidyverse.org/reference/scale_brewer.html#arguments)

---------------------------------------------------------------------------------

name[](https://ggplot2.tidyverse.org/reference/scale_brewer.html#arg-name)

The name of the scale. Used as the axis or legend title. If `[waiver()](https://ggplot2.tidyverse.org/reference/waiver.html) `, the default, the name of the scale is taken from the first mapping used for that aesthetic. If `NULL`, the legend title will be omitted.

...[](https://ggplot2.tidyverse.org/reference/scale_brewer.html#arg--)

Other arguments passed on to `[discrete_scale()](https://ggplot2.tidyverse.org/reference/discrete_scale.html) `, `[continuous_scale()](https://ggplot2.tidyverse.org/reference/continuous_scale.html) `, or `[binned_scale()](https://ggplot2.tidyverse.org/reference/binned_scale.html) `, for `brewer`, `distiller`, and `fermenter` variants respectively, to control name, limits, breaks, labels and so forth.

type[](https://ggplot2.tidyverse.org/reference/scale_brewer.html#arg-type)

One of "seq" (sequential), "div" (diverging) or "qual" (qualitative)

palette[](https://ggplot2.tidyverse.org/reference/scale_brewer.html#arg-palette)

If a string, will use that named palette. If a number, will index into the list of palettes of appropriate `type`. The list of available palettes can found in the Palettes section.

direction[](https://ggplot2.tidyverse.org/reference/scale_brewer.html#arg-direction)

Sets the order of colours in the scale. If 1, the default, colours are as output by `[RColorBrewer::brewer.pal()](https://rdrr.io/pkg/RColorBrewer/man/ColorBrewer.html) `. If -1, the order of colours is reversed.

aesthetics[](https://ggplot2.tidyverse.org/reference/scale_brewer.html#arg-aesthetics)

Character string or vector of character strings listing the name(s) of the aesthetic(s) that this scale works with. This can be useful, for example, to apply colour settings to the `colour` and `fill` aesthetics at the same time, via `aesthetics = c("colour", "fill")`.

values[](https://ggplot2.tidyverse.org/reference/scale_brewer.html#arg-values)

if colours should not be evenly positioned along the gradient this vector gives the position (between 0 and 1) for each colour in the `colours` vector. See `[rescale()](https://scales.r-lib.org/reference/rescale.html) ` for a convenience function to map an arbitrary range to between 0 and 1.

space[](https://ggplot2.tidyverse.org/reference/scale_brewer.html#arg-space)

colour space in which to calculate gradient. Must be "Lab" - other values are deprecated.

na.value[](https://ggplot2.tidyverse.org/reference/scale_brewer.html#arg-na-value)

Colour to use for missing values

guide[](https://ggplot2.tidyverse.org/reference/scale_brewer.html#arg-guide)

Type of legend. Use `"colourbar"` for continuous colour bar, or `"legend"` for discrete colour legend.

Details[](https://ggplot2.tidyverse.org/reference/scale_brewer.html#details)

-----------------------------------------------------------------------------

The `brewer` scales were carefully designed and tested on discrete data. They were not designed to be extended to continuous data, but results often look good. Your mileage may vary.

Note[](https://ggplot2.tidyverse.org/reference/scale_brewer.html#note)

-----------------------------------------------------------------------

The `distiller` scales extend `brewer` scales by smoothly interpolating 7 colours from any palette to a continuous scale. The `distiller` scales have a default direction = -1. To reverse, use direction = 1. The `fermenter` scales provide binned versions of the `brewer` scales.

Palettes[](https://ggplot2.tidyverse.org/reference/scale_brewer.html#palettes)

-------------------------------------------------------------------------------

The following palettes are available for use with these scales:

Diverging

BrBG, PiYG, PRGn, PuOr, RdBu, RdGy, RdYlBu, RdYlGn, Spectral

Qualitative

Accent, Dark2, Paired, Pastel1, Pastel2, Set1, Set2, Set3

Sequential

Blues, BuGn, BuPu, GnBu, Greens, Greys, Oranges, OrRd, PuBu, PuBuGn, PuRd, Purples, RdPu, Reds, YlGn, YlGnBu, YlOrBr, YlOrRd

Modify the palette through the `palette` argument.

See also[](https://ggplot2.tidyverse.org/reference/scale_brewer.html#see-also)

-------------------------------------------------------------------------------

The documentation on [colour aesthetics](https://ggplot2.tidyverse.org/reference/aes_colour_fill_alpha.html)
.

The [brewer scales section](https://ggplot2-book.org/scales-colour#brewer-scales)
 of the online ggplot2 book.

Other colour scales: `[scale_alpha()](https://ggplot2.tidyverse.org/reference/scale_alpha.html) `, `[scale_colour_continuous()](https://ggplot2.tidyverse.org/reference/scale_colour_continuous.html) `, `[scale_colour_discrete()](https://ggplot2.tidyverse.org/reference/scale_colour_discrete.html) `, `[scale_colour_gradient()](https://ggplot2.tidyverse.org/reference/scale_gradient.html) `, `[scale_colour_grey()](https://ggplot2.tidyverse.org/reference/scale_grey.html) `, `[scale_colour_hue()](https://ggplot2.tidyverse.org/reference/scale_hue.html) `, `[scale_colour_identity()](https://ggplot2.tidyverse.org/reference/scale_identity.html) `, `[scale_colour_manual()](https://ggplot2.tidyverse.org/reference/scale_manual.html) `, `[scale_colour_steps()](https://ggplot2.tidyverse.org/reference/scale_steps.html) `, `[scale_colour_viridis_d()](https://ggplot2.tidyverse.org/reference/scale_viridis.html) `

Examples[](https://ggplot2.tidyverse.org/reference/scale_brewer.html#ref-examples)

-----------------------------------------------------------------------------------

    set.seed(596)
    dsamp <- diamonds[sample(nrow(diamonds), 1000), ]
    (d <- ggplot(dsamp, aes(carat, price)) +
      geom_point(aes(colour = clarity)))
    
    d + scale_colour_brewer()
    
    
    # Change scale label
    d + scale_colour_brewer("Diamond\nclarity")
    
    
    # Select brewer palette to use, see ?scales::pal_brewer for more details
    d + scale_colour_brewer(palette = "Greens")
    
    d + scale_colour_brewer(palette = "Set1")
    
    
    # \donttest{
    # scale_fill_brewer works just the same as
    # scale_colour_brewer but for fill colours
    p <- ggplot(diamonds, aes(x = price, fill = cut)) +
      geom_histogram(position = "dodge", binwidth = 1000)
    p + scale_fill_brewer()
    
    # the order of colour can be reversed
    p + scale_fill_brewer(direction = -1)
    
    # the brewer scales look better on a darker background
    p +
      scale_fill_brewer(direction = -1) +
      theme_dark()
    
    # }
    
    # Use distiller variant with continuous data
    v <- ggplot(faithfuld) +
      geom_tile(aes(waiting, eruptions, fill = density))
    v
    
    v + scale_fill_distiller()
    
    v + scale_fill_distiller(palette = "Spectral")
    
    # the order of colour can be reversed, but with scale_*_distiller(),
    # the default direction = -1, so to reverse, use direction = 1.
    v + scale_fill_distiller(palette = "Spectral", direction = 1)
    
    
    # or use blender variants to discretise continuous data
    v + scale_fill_fermenter()