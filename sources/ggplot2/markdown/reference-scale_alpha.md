[Skip to content](https://ggplot2.tidyverse.org/reference/scale_alpha.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Alpha transparency scales
=========================

Source: [`R/scale-alpha.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/scale-alpha.R)

`scale_alpha.Rd`

Alpha-transparency scales are not tremendously useful, but can be a convenient way to visually down-weight less important observations. `scale_alpha()` is an alias for `scale_alpha_continuous()` since that is the most common use of alpha, and it saves a bit of typing.

Usage[](https://ggplot2.tidyverse.org/reference/scale_alpha.html#ref-usage)

----------------------------------------------------------------------------

    scale_alpha(name = waiver(), ..., range = NULL, aesthetics = "alpha")
    
    scale_alpha_continuous(
      name = waiver(),
      ...,
      range = NULL,
      aesthetics = "alpha"
    )
    
    scale_alpha_binned(name = waiver(), ..., range = NULL, aesthetics = "alpha")
    
    scale_alpha_discrete(...)
    
    scale_alpha_ordinal(name = waiver(), ..., range = NULL, aesthetics = "alpha")

Arguments[](https://ggplot2.tidyverse.org/reference/scale_alpha.html#arguments)

--------------------------------------------------------------------------------

name[](https://ggplot2.tidyverse.org/reference/scale_alpha.html#arg-name)

The name of the scale. Used as the axis or legend title. If `[waiver()](https://ggplot2.tidyverse.org/reference/waiver.html) `, the default, the name of the scale is taken from the first mapping used for that aesthetic. If `NULL`, the legend title will be omitted.

...[](https://ggplot2.tidyverse.org/reference/scale_alpha.html#arg--)

Other arguments passed on to `[continuous_scale()](https://ggplot2.tidyverse.org/reference/continuous_scale.html) `, `[binned_scale()](https://ggplot2.tidyverse.org/reference/binned_scale.html) `, or `[discrete_scale()](https://ggplot2.tidyverse.org/reference/discrete_scale.html) ` as appropriate, to control name, limits, breaks, labels and so forth.

range[](https://ggplot2.tidyverse.org/reference/scale_alpha.html#arg-range)

Output range of alpha values. Must lie between 0 and 1.

aesthetics[](https://ggplot2.tidyverse.org/reference/scale_alpha.html#arg-aesthetics)

The names of the aesthetics that this scale works with.

See also[](https://ggplot2.tidyverse.org/reference/scale_alpha.html#see-also)

------------------------------------------------------------------------------

The documentation on [colour aesthetics](https://ggplot2.tidyverse.org/reference/aes_colour_fill_alpha.html)
.

Other alpha scales: `[scale_alpha_manual()](https://ggplot2.tidyverse.org/reference/scale_manual.html) `, `[scale_alpha_identity()](https://ggplot2.tidyverse.org/reference/scale_identity.html) `.

The [alpha scales section](https://ggplot2-book.org/scales-colour#sec-scales-alpha)
 of the online ggplot2 book.

Other colour scales: `[scale_colour_brewer()](https://ggplot2.tidyverse.org/reference/scale_brewer.html) `, `[scale_colour_continuous()](https://ggplot2.tidyverse.org/reference/scale_colour_continuous.html) `, `[scale_colour_discrete()](https://ggplot2.tidyverse.org/reference/scale_colour_discrete.html) `, `[scale_colour_gradient()](https://ggplot2.tidyverse.org/reference/scale_gradient.html) `, `[scale_colour_grey()](https://ggplot2.tidyverse.org/reference/scale_grey.html) `, `[scale_colour_hue()](https://ggplot2.tidyverse.org/reference/scale_hue.html) `, `[scale_colour_identity()](https://ggplot2.tidyverse.org/reference/scale_identity.html) `, `[scale_colour_manual()](https://ggplot2.tidyverse.org/reference/scale_manual.html) `, `[scale_colour_steps()](https://ggplot2.tidyverse.org/reference/scale_steps.html) `, `[scale_colour_viridis_d()](https://ggplot2.tidyverse.org/reference/scale_viridis.html) `

Examples[](https://ggplot2.tidyverse.org/reference/scale_alpha.html#ref-examples)

----------------------------------------------------------------------------------

    p <- ggplot(mpg, aes(displ, hwy)) +
      geom_point(aes(alpha = year))
    
    # The default range of 0.1-1.0 leaves all data visible
    p
    
    
    # Include 0 in the range to make data invisible
    p + scale_alpha(range = c(0, 1))
    
    
    # Changing the title
    p + scale_alpha("cylinders")