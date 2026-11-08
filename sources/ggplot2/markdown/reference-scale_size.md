[Skip to content](https://ggplot2.tidyverse.org/reference/scale_size.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Scales for area or radius
=========================

Source: [`R/scale-size.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/scale-size.R)

`scale_size.Rd`

`scale_size()` scales area, `scale_radius()` scales radius. The size aesthetic is most commonly used for points and text, and humans perceive the area of points (not their radius), so this provides for optimal perception. `scale_size_area()` ensures that a value of 0 is mapped to a size of 0. `scale_size_binned()` is a binned version of `scale_size()` that scales by area (but does not ensure 0 equals an area of zero). For a binned equivalent of `scale_size_area()` use `scale_size_binned_area()`.

Usage[](https://ggplot2.tidyverse.org/reference/scale_size.html#ref-usage)

---------------------------------------------------------------------------

    scale_size(
      name = waiver(),
      breaks = waiver(),
      labels = waiver(),
      limits = NULL,
      range = NULL,
      transform = "identity",
      trans = deprecated(),
      guide = "legend",
      aesthetics = "size"
    )
    
    scale_radius(
      name = waiver(),
      breaks = waiver(),
      labels = waiver(),
      limits = NULL,
      range = c(1, 6),
      transform = "identity",
      trans = deprecated(),
      guide = "legend",
      aesthetics = "size"
    )
    
    scale_size_binned(
      name = waiver(),
      breaks = waiver(),
      labels = waiver(),
      limits = NULL,
      range = NULL,
      n.breaks = NULL,
      nice.breaks = TRUE,
      transform = "identity",
      trans = deprecated(),
      guide = "bins",
      aesthetics = "size"
    )
    
    scale_size_area(name = waiver(), ..., max_size = 6, aesthetics = "size")
    
    scale_size_binned_area(name = waiver(), ..., max_size = 6, aesthetics = "size")

Arguments[](https://ggplot2.tidyverse.org/reference/scale_size.html#arguments)

-------------------------------------------------------------------------------

name[](https://ggplot2.tidyverse.org/reference/scale_size.html#arg-name)

The name of the scale. Used as the axis or legend title. If `[waiver()](https://ggplot2.tidyverse.org/reference/waiver.html) `, the default, the name of the scale is taken from the first mapping used for that aesthetic. If `NULL`, the legend title will be omitted.

breaks[](https://ggplot2.tidyverse.org/reference/scale_size.html#arg-breaks)

One of:

*   `NULL` for no breaks
    
*   `[waiver()](https://ggplot2.tidyverse.org/reference/waiver.html) ` for the default breaks computed by the [transformation object](https://scales.r-lib.org/reference/new_transform.html)
    
*   A numeric vector of positions
    
*   A function that takes the limits as input and returns breaks as output (e.g., a function returned by `[scales::extended_breaks()](https://scales.r-lib.org/reference/breaks_extended.html) `). Note that for position scales, limits are provided after scale expansion. Also accepts rlang [lambda](https://rlang.r-lib.org/reference/as_function.html)
     function notation.
    

labels[](https://ggplot2.tidyverse.org/reference/scale_size.html#arg-labels)

One of the options below. Please note that when `labels` is a vector, it is highly recommended to also set the `breaks` argument as a vector to protect against unintended mismatches.

*   `NULL` for no labels
    
*   `[waiver()](https://ggplot2.tidyverse.org/reference/waiver.html) ` for the default labels computed by the transformation object
    
*   A character vector giving labels (must be same length as `breaks`)
    
*   An expression vector (must be the same length as breaks). See ?plotmath for details.
    
*   A function that takes the breaks as input and returns labels as output. Also accepts rlang [lambda](https://rlang.r-lib.org/reference/as_function.html)
     function notation.
    

limits[](https://ggplot2.tidyverse.org/reference/scale_size.html#arg-limits)

One of:

*   `NULL` to use the default scale range
    
*   A numeric vector of length two providing limits of the scale. Use `NA` to refer to the existing minimum or maximum
    
*   A function that accepts the existing (automatic) limits and returns new limits. Also accepts rlang [lambda](https://rlang.r-lib.org/reference/as_function.html)
     function notation. Note that setting limits on positional scales will **remove** data outside of the limits. If the purpose is to zoom, use the limit argument in the coordinate system (see `[coord_cartesian()](https://ggplot2.tidyverse.org/reference/coord_cartesian.html) `).
    

range[](https://ggplot2.tidyverse.org/reference/scale_size.html#arg-range)

a numeric vector of length 2 that specifies the minimum and maximum size of the plotting symbol after transformation.

transform[](https://ggplot2.tidyverse.org/reference/scale_size.html#arg-transform)

For continuous scales, the name of a transformation object or the object itself. Built-in transformations include "asn", "atanh", "boxcox", "date", "exp", "hms", "identity", "log", "log10", "log1p", "log2", "logit", "modulus", "probability", "probit", "pseudo\_log", "reciprocal", "reverse", "sqrt" and "time".

A transformation object bundles together a transform, its inverse, and methods for generating breaks and labels. Transformation objects are defined in the scales package, and are called `transform_<name>`. If transformations require arguments, you can call them from the scales package, e.g. `[scales::transform_boxcox(p = 2)](https://scales.r-lib.org/reference/transform_boxcox.html) `. You can create your own transformation with `[scales::new_transform()](https://scales.r-lib.org/reference/new_transform.html) `.

trans[](https://ggplot2.tidyverse.org/reference/scale_size.html#arg-trans)

[![[Deprecated]](https://ggplot2.tidyverse.org/reference/figures/lifecycle-deprecated.svg)](https://lifecycle.r-lib.org/articles/stages.html#deprecated)
 Deprecated in favour of `transform`.

guide[](https://ggplot2.tidyverse.org/reference/scale_size.html#arg-guide)

A function used to create a guide or its name. See `[guides()](https://ggplot2.tidyverse.org/reference/guides.html) ` for more information.

aesthetics[](https://ggplot2.tidyverse.org/reference/scale_size.html#arg-aesthetics)

The names of the aesthetics that this scale works with.

n.breaks[](https://ggplot2.tidyverse.org/reference/scale_size.html#arg-n-breaks)

An integer guiding the number of major breaks. The algorithm may choose a slightly different number to ensure nice break labels. Will only have an effect if `breaks = waiver()`. Use `NULL` to use the default number of breaks given by the transformation.

nice.breaks[](https://ggplot2.tidyverse.org/reference/scale_size.html#arg-nice-breaks)

Logical. Should breaks be attempted placed at nice values instead of exactly evenly spaced between the limits. If `TRUE` (default) the scale will ask the transformation object to create breaks, and this may result in a different number of breaks than requested. Ignored if breaks are given explicitly.

...[](https://ggplot2.tidyverse.org/reference/scale_size.html#arg--)

Arguments passed on to `[continuous_scale](https://ggplot2.tidyverse.org/reference/continuous_scale.html) `

`minor_breaks`

One of:

*   `NULL` for no minor breaks
    
*   `[waiver()](https://ggplot2.tidyverse.org/reference/waiver.html) ` for the default breaks (none for discrete, one minor break between each major break for continuous)
    
*   A numeric vector of positions
    
*   A function that given the limits returns a vector of minor breaks. Also accepts rlang [lambda](https://rlang.r-lib.org/reference/as_function.html)
     function notation. When the function has two arguments, it will be given the limits and major break positions.
    

`oob`

One of:

*   Function that handles limits outside of the scale limits (out of bounds). Also accepts rlang [lambda](https://rlang.r-lib.org/reference/as_function.html)
     function notation.
    
*   The default (`[scales::censor()](https://scales.r-lib.org/reference/oob.html) `) replaces out of bounds values with `NA`.
    
*   `[scales::squish()](https://scales.r-lib.org/reference/oob.html) ` for squishing out of bounds values into range.
    
*   `[scales::squish_infinite()](https://scales.r-lib.org/reference/oob.html) ` for squishing infinite values into range.
    

`na.value`

Missing values will be replaced with this value.

`call`

The `call` used to construct the scale for reporting messages.

`super`

The super class to use for the constructed scale

max\_size[](https://ggplot2.tidyverse.org/reference/scale_size.html#arg-max-size)

Size of largest points.

Note[](https://ggplot2.tidyverse.org/reference/scale_size.html#note)

---------------------------------------------------------------------

Historically the size aesthetic was used for two different things: Scaling the size of object (like points and glyphs) and scaling the width of lines. From ggplot2 3.4.0 the latter has been moved to its own linewidth aesthetic. For backwards compatibility using size is still possible, but it is highly advised to switch to the new linewidth aesthetic for these cases.

See also[](https://ggplot2.tidyverse.org/reference/scale_size.html#see-also)

-----------------------------------------------------------------------------

`scale_size_area()` if you want 0 values to be mapped to points with size 0. `[scale_linewidth()](https://ggplot2.tidyverse.org/reference/scale_linewidth.html) ` if you want to scale the width of lines.

The documentation for [differentiation related aesthetics](https://ggplot2.tidyverse.org/reference/aes_linetype_size_shape.html)
.

The [size section](https://ggplot2-book.org/scales-other#sec-scale-size)
 of the online ggplot2 book.

Examples[](https://ggplot2.tidyverse.org/reference/scale_size.html#ref-examples)

---------------------------------------------------------------------------------

    p <- ggplot(mpg, aes(displ, hwy, size = hwy)) +
       geom_point()
    p
    
    p + scale_size("Highway mpg")
    
    p + scale_size(range = c(0, 10))
    
    
    # If you want zero value to have zero size, use scale_size_area:
    p + scale_size_area()
    
    
    # Binning can sometimes make it easier to match the scaled data to the legend
    p + scale_size_binned()
    
    
    # This is most useful when size is a count
    ggplot(mpg, aes(class, cyl)) +
      geom_count() +
      scale_size_area()
    
    
    # If you want to map size to radius (usually bad idea), use scale_radius
    p + scale_radius()