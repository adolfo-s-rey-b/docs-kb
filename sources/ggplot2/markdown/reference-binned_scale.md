[Skip to content](https://ggplot2.tidyverse.org/reference/binned_scale.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Binning scale constructor
=========================

Source: [`R/scale-.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/scale-.R)

`binned_scale.Rd`

Binning scale constructor

Usage[](https://ggplot2.tidyverse.org/reference/binned_scale.html#ref-usage)

-----------------------------------------------------------------------------

    binned_scale(
      aesthetics,
      scale_name = deprecated(),
      palette,
      name = waiver(),
      breaks = waiver(),
      labels = waiver(),
      limits = NULL,
      rescaler = rescale,
      oob = squish,
      expand = waiver(),
      na.value = NA_real_,
      n.breaks = NULL,
      nice.breaks = TRUE,
      right = TRUE,
      transform = "identity",
      trans = deprecated(),
      show.limits = FALSE,
      guide = "bins",
      position = "left",
      fallback.palette = NULL,
      call = caller_call(),
      super = ScaleBinned
    )

Arguments[](https://ggplot2.tidyverse.org/reference/binned_scale.html#arguments)

---------------------------------------------------------------------------------

aesthetics[](https://ggplot2.tidyverse.org/reference/binned_scale.html#arg-aesthetics)

The names of the aesthetics that this scale works with.

scale\_name[](https://ggplot2.tidyverse.org/reference/binned_scale.html#arg-scale-name)

[![[Deprecated]](https://ggplot2.tidyverse.org/reference/figures/lifecycle-deprecated.svg)](https://lifecycle.r-lib.org/articles/stages.html#deprecated)
 The name of the scale that should be used for error messages associated with this scale.

palette[](https://ggplot2.tidyverse.org/reference/binned_scale.html#arg-palette)

A palette function that when called with a numeric vector with values between 0 and 1 returns the corresponding output values (e.g., `[scales::pal_area()](https://scales.r-lib.org/reference/pal_area.html) `).

name[](https://ggplot2.tidyverse.org/reference/binned_scale.html#arg-name)

The name of the scale. Used as the axis or legend title. If `[waiver()](https://ggplot2.tidyverse.org/reference/waiver.html) `, the default, the name of the scale is taken from the first mapping used for that aesthetic. If `NULL`, the legend title will be omitted.

breaks[](https://ggplot2.tidyverse.org/reference/binned_scale.html#arg-breaks)

One of:

*   `NULL` for no breaks
    
*   `[waiver()](https://ggplot2.tidyverse.org/reference/waiver.html) ` for the default breaks computed by the [transformation object](https://scales.r-lib.org/reference/new_transform.html)
    
*   A numeric vector of positions
    
*   A function that takes the limits as input and returns breaks as output (e.g., a function returned by `[scales::extended_breaks()](https://scales.r-lib.org/reference/breaks_extended.html) `). Note that for position scales, limits are provided after scale expansion. Also accepts rlang [lambda](https://rlang.r-lib.org/reference/as_function.html)
     function notation.
    

labels[](https://ggplot2.tidyverse.org/reference/binned_scale.html#arg-labels)

One of the options below. Please note that when `labels` is a vector, it is highly recommended to also set the `breaks` argument as a vector to protect against unintended mismatches.

*   `NULL` for no labels
    
*   `[waiver()](https://ggplot2.tidyverse.org/reference/waiver.html) ` for the default labels computed by the transformation object
    
*   A character vector giving labels (must be same length as `breaks`)
    
*   An expression vector (must be the same length as breaks). See ?plotmath for details.
    
*   A function that takes the breaks as input and returns labels as output. Also accepts rlang [lambda](https://rlang.r-lib.org/reference/as_function.html)
     function notation.
    

limits[](https://ggplot2.tidyverse.org/reference/binned_scale.html#arg-limits)

One of:

*   `NULL` to use the default scale range
    
*   A numeric vector of length two providing limits of the scale. Use `NA` to refer to the existing minimum or maximum
    
*   A function that accepts the existing (automatic) limits and returns new limits. Also accepts rlang [lambda](https://rlang.r-lib.org/reference/as_function.html)
     function notation. Note that setting limits on positional scales will **remove** data outside of the limits. If the purpose is to zoom, use the limit argument in the coordinate system (see `[coord_cartesian()](https://ggplot2.tidyverse.org/reference/coord_cartesian.html) `).
    

rescaler[](https://ggplot2.tidyverse.org/reference/binned_scale.html#arg-rescaler)

A function used to scale the input values to the range \[0, 1\]. This is always `[scales::rescale()](https://scales.r-lib.org/reference/rescale.html) `, except for diverging and n colour gradients (i.e., `[scale_colour_gradient2()](https://ggplot2.tidyverse.org/reference/scale_gradient.html) `, `[scale_colour_gradientn()](https://ggplot2.tidyverse.org/reference/scale_gradient.html) `). The `rescaler` is ignored by position scales, which always use `[scales::rescale()](https://scales.r-lib.org/reference/rescale.html) `. Also accepts rlang [lambda](https://rlang.r-lib.org/reference/as_function.html)
 function notation.

oob[](https://ggplot2.tidyverse.org/reference/binned_scale.html#arg-oob)

One of:

*   Function that handles limits outside of the scale limits (out of bounds). Also accepts rlang [lambda](https://rlang.r-lib.org/reference/as_function.html)
     function notation.
    
*   The default (`[scales::squish()](https://scales.r-lib.org/reference/oob.html) `) squishes out of bounds values into range.
    
*   [scales::censor](https://scales.r-lib.org/reference/oob.html)
     for replacing out of bounds values with `NA`.
    
*   `[scales::squish_infinite()](https://scales.r-lib.org/reference/oob.html) ` for squishing infinite values into range.
    

expand[](https://ggplot2.tidyverse.org/reference/binned_scale.html#arg-expand)

For position scales, a vector of range expansion constants used to add some padding around the data to ensure that they are placed some distance away from the axes. Use the convenience function `[expansion()](https://ggplot2.tidyverse.org/reference/expansion.html) ` to generate the values for the `expand` argument. The defaults are to expand the scale by 5% on each side for continuous variables, and by 0.6 units on each side for discrete variables.

na.value[](https://ggplot2.tidyverse.org/reference/binned_scale.html#arg-na-value)

Missing values will be replaced with this value.

n.breaks[](https://ggplot2.tidyverse.org/reference/binned_scale.html#arg-n-breaks)

The number of break points to create if breaks are not given directly.

nice.breaks[](https://ggplot2.tidyverse.org/reference/binned_scale.html#arg-nice-breaks)

Logical. Should breaks be attempted placed at nice values instead of exactly evenly spaced between the limits. If `TRUE` (default) the scale will ask the transformation object to create breaks, and this may result in a different number of breaks than requested. Ignored if breaks are given explicitly.

right[](https://ggplot2.tidyverse.org/reference/binned_scale.html#arg-right)

Should the intervals be closed on the right (`TRUE`, default) or should the intervals be closed on the left (`FALSE`)? 'Closed on the right' means that values at break positions are part of the lower bin (open on the left), whereas they are part of the upper bin when intervals are closed on the left (open on the right).

transform[](https://ggplot2.tidyverse.org/reference/binned_scale.html#arg-transform)

For continuous scales, the name of a transformation object or the object itself. Built-in transformations include "asn", "atanh", "boxcox", "date", "exp", "hms", "identity", "log", "log10", "log1p", "log2", "logit", "modulus", "probability", "probit", "pseudo\_log", "reciprocal", "reverse", "sqrt" and "time".

A transformation object bundles together a transform, its inverse, and methods for generating breaks and labels. Transformation objects are defined in the scales package, and are called `transform_<name>`. If transformations require arguments, you can call them from the scales package, e.g. `[scales::transform_boxcox(p = 2)](https://scales.r-lib.org/reference/transform_boxcox.html) `. You can create your own transformation with `[scales::new_transform()](https://scales.r-lib.org/reference/new_transform.html) `.

trans[](https://ggplot2.tidyverse.org/reference/binned_scale.html#arg-trans)

[![[Deprecated]](https://ggplot2.tidyverse.org/reference/figures/lifecycle-deprecated.svg)](https://lifecycle.r-lib.org/articles/stages.html#deprecated)
 Deprecated in favour of `transform`.

show.limits[](https://ggplot2.tidyverse.org/reference/binned_scale.html#arg-show-limits)

should the limits of the scale appear as ticks

guide[](https://ggplot2.tidyverse.org/reference/binned_scale.html#arg-guide)

A function used to create a guide or its name. See `[guides()](https://ggplot2.tidyverse.org/reference/guides.html) ` for more information.

position[](https://ggplot2.tidyverse.org/reference/binned_scale.html#arg-position)

For position scales, The position of the axis. `left` or `right` for y axes, `top` or `bottom` for x axes.

fallback.palette[](https://ggplot2.tidyverse.org/reference/binned_scale.html#arg-fallback-palette)

Function to use when `palette = NULL` and the palette is not represented in the theme.

call[](https://ggplot2.tidyverse.org/reference/binned_scale.html#arg-call)

The `call` used to construct the scale for reporting messages.

super[](https://ggplot2.tidyverse.org/reference/binned_scale.html#arg-super)

The super class to use for the constructed scale

See also[](https://ggplot2.tidyverse.org/reference/binned_scale.html#see-also)

-------------------------------------------------------------------------------

The [new scales section](https://ggplot2-book.org/extensions#sec-new-scales)
 of the online ggplot2 book.