[Skip to content](https://ggplot2.tidyverse.org/reference/scale_binned.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Positional scales for binning continuous data (x & y)
=====================================================

Source: [`R/scale-binned.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/scale-binned.R)

`scale_binned.Rd`

`scale_x_binned()` and `scale_y_binned()` are scales that discretize continuous position data. You can use these scales to transform continuous inputs before using it with a geom that requires discrete positions. An example is using `scale_x_binned()` with `[geom_bar()](https://ggplot2.tidyverse.org/reference/geom_bar.html) ` to create a histogram.

Usage[](https://ggplot2.tidyverse.org/reference/scale_binned.html#ref-usage)

-----------------------------------------------------------------------------

    scale_x_binned(
      name = waiver(),
      n.breaks = 10,
      nice.breaks = TRUE,
      breaks = waiver(),
      labels = waiver(),
      limits = NULL,
      expand = waiver(),
      oob = squish,
      na.value = NA_real_,
      right = TRUE,
      show.limits = FALSE,
      transform = "identity",
      trans = deprecated(),
      guide = waiver(),
      position = "bottom"
    )
    
    scale_y_binned(
      name = waiver(),
      n.breaks = 10,
      nice.breaks = TRUE,
      breaks = waiver(),
      labels = waiver(),
      limits = NULL,
      expand = waiver(),
      oob = squish,
      na.value = NA_real_,
      right = TRUE,
      show.limits = FALSE,
      transform = "identity",
      trans = deprecated(),
      guide = waiver(),
      position = "left"
    )

Arguments[](https://ggplot2.tidyverse.org/reference/scale_binned.html#arguments)

---------------------------------------------------------------------------------

name[](https://ggplot2.tidyverse.org/reference/scale_binned.html#arg-name)

The name of the scale. Used as the axis or legend title. If `[waiver()](https://ggplot2.tidyverse.org/reference/waiver.html) `, the default, the name of the scale is taken from the first mapping used for that aesthetic. If `NULL`, the legend title will be omitted.

n.breaks[](https://ggplot2.tidyverse.org/reference/scale_binned.html#arg-n-breaks)

The number of break points to create if breaks are not given directly.

nice.breaks[](https://ggplot2.tidyverse.org/reference/scale_binned.html#arg-nice-breaks)

Logical. Should breaks be attempted placed at nice values instead of exactly evenly spaced between the limits. If `TRUE` (default) the scale will ask the transformation object to create breaks, and this may result in a different number of breaks than requested. Ignored if breaks are given explicitly.

breaks[](https://ggplot2.tidyverse.org/reference/scale_binned.html#arg-breaks)

One of:

*   `NULL` for no breaks
    
*   `[waiver()](https://ggplot2.tidyverse.org/reference/waiver.html) ` for the default breaks computed by the [transformation object](https://scales.r-lib.org/reference/new_transform.html)
    
*   A numeric vector of positions
    
*   A function that takes the limits as input and returns breaks as output (e.g., a function returned by `[scales::extended_breaks()](https://scales.r-lib.org/reference/breaks_extended.html) `). Note that for position scales, limits are provided after scale expansion. Also accepts rlang [lambda](https://rlang.r-lib.org/reference/as_function.html)
     function notation.
    

labels[](https://ggplot2.tidyverse.org/reference/scale_binned.html#arg-labels)

One of the options below. Please note that when `labels` is a vector, it is highly recommended to also set the `breaks` argument as a vector to protect against unintended mismatches.

*   `NULL` for no labels
    
*   `[waiver()](https://ggplot2.tidyverse.org/reference/waiver.html) ` for the default labels computed by the transformation object
    
*   A character vector giving labels (must be same length as `breaks`)
    
*   An expression vector (must be the same length as breaks). See ?plotmath for details.
    
*   A function that takes the breaks as input and returns labels as output. Also accepts rlang [lambda](https://rlang.r-lib.org/reference/as_function.html)
     function notation.
    

limits[](https://ggplot2.tidyverse.org/reference/scale_binned.html#arg-limits)

One of:

*   `NULL` to use the default scale range
    
*   A numeric vector of length two providing limits of the scale. Use `NA` to refer to the existing minimum or maximum
    
*   A function that accepts the existing (automatic) limits and returns new limits. Also accepts rlang [lambda](https://rlang.r-lib.org/reference/as_function.html)
     function notation. Note that setting limits on positional scales will **remove** data outside of the limits. If the purpose is to zoom, use the limit argument in the coordinate system (see `[coord_cartesian()](https://ggplot2.tidyverse.org/reference/coord_cartesian.html) `).
    

expand[](https://ggplot2.tidyverse.org/reference/scale_binned.html#arg-expand)

For position scales, a vector of range expansion constants used to add some padding around the data to ensure that they are placed some distance away from the axes. Use the convenience function `[expansion()](https://ggplot2.tidyverse.org/reference/expansion.html) ` to generate the values for the `expand` argument. The defaults are to expand the scale by 5% on each side for continuous variables, and by 0.6 units on each side for discrete variables.

oob[](https://ggplot2.tidyverse.org/reference/scale_binned.html#arg-oob)

One of:

*   Function that handles limits outside of the scale limits (out of bounds). Also accepts rlang [lambda](https://rlang.r-lib.org/reference/as_function.html)
     function notation.
    
*   The default (`[scales::squish()](https://scales.r-lib.org/reference/oob.html) `) squishes out of bounds values into range.
    
*   [scales::censor](https://scales.r-lib.org/reference/oob.html)
     for replacing out of bounds values with `NA`.
    
*   `[scales::squish_infinite()](https://scales.r-lib.org/reference/oob.html) ` for squishing infinite values into range.
    

na.value[](https://ggplot2.tidyverse.org/reference/scale_binned.html#arg-na-value)

Missing values will be replaced with this value.

right[](https://ggplot2.tidyverse.org/reference/scale_binned.html#arg-right)

Should the intervals be closed on the right (`TRUE`, default) or should the intervals be closed on the left (`FALSE`)? 'Closed on the right' means that values at break positions are part of the lower bin (open on the left), whereas they are part of the upper bin when intervals are closed on the left (open on the right).

show.limits[](https://ggplot2.tidyverse.org/reference/scale_binned.html#arg-show-limits)

should the limits of the scale appear as ticks

transform[](https://ggplot2.tidyverse.org/reference/scale_binned.html#arg-transform)

For continuous scales, the name of a transformation object or the object itself. Built-in transformations include "asn", "atanh", "boxcox", "date", "exp", "hms", "identity", "log", "log10", "log1p", "log2", "logit", "modulus", "probability", "probit", "pseudo\_log", "reciprocal", "reverse", "sqrt" and "time".

A transformation object bundles together a transform, its inverse, and methods for generating breaks and labels. Transformation objects are defined in the scales package, and are called `transform_<name>`. If transformations require arguments, you can call them from the scales package, e.g. `[scales::transform_boxcox(p = 2)](https://scales.r-lib.org/reference/transform_boxcox.html) `. You can create your own transformation with `[scales::new_transform()](https://scales.r-lib.org/reference/new_transform.html) `.

trans[](https://ggplot2.tidyverse.org/reference/scale_binned.html#arg-trans)

[![[Deprecated]](https://ggplot2.tidyverse.org/reference/figures/lifecycle-deprecated.svg)](https://lifecycle.r-lib.org/articles/stages.html#deprecated)
 Deprecated in favour of `transform`.

guide[](https://ggplot2.tidyverse.org/reference/scale_binned.html#arg-guide)

A function used to create a guide or its name. See `[guides()](https://ggplot2.tidyverse.org/reference/guides.html) ` for more information.

position[](https://ggplot2.tidyverse.org/reference/scale_binned.html#arg-position)

For position scales, The position of the axis. `left` or `right` for y axes, `top` or `bottom` for x axes.

See also[](https://ggplot2.tidyverse.org/reference/scale_binned.html#see-also)

-------------------------------------------------------------------------------

The [position documentation](https://ggplot2.tidyverse.org/reference/aes_position.html)
.

The [binned position scales section](https://ggplot2-book.org/scales-position#sec-binned-position)
 of the online ggplot2 book.

Other position scales: `[scale_x_continuous()](https://ggplot2.tidyverse.org/reference/scale_continuous.html) `, `[scale_x_date()](https://ggplot2.tidyverse.org/reference/scale_date.html) `, `[scale_x_discrete()](https://ggplot2.tidyverse.org/reference/scale_discrete.html) `

Examples[](https://ggplot2.tidyverse.org/reference/scale_binned.html#ref-examples)

-----------------------------------------------------------------------------------

    # Create a histogram by binning the x-axis
    ggplot(mtcars) +
      geom_bar(aes(mpg)) +
      scale_x_binned()