[Skip to content](https://ggplot2.tidyverse.org/reference/discrete_scale.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Discrete scale constructor
==========================

Source: [`R/scale-.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/scale-.R)

`discrete_scale.Rd`

Discrete scale constructor

Usage[](https://ggplot2.tidyverse.org/reference/discrete_scale.html#ref-usage)

-------------------------------------------------------------------------------

    discrete_scale(
      aesthetics,
      scale_name = deprecated(),
      palette,
      name = waiver(),
      breaks = waiver(),
      minor_breaks = waiver(),
      labels = waiver(),
      limits = NULL,
      expand = waiver(),
      na.translate = TRUE,
      na.value = NA,
      drop = TRUE,
      guide = "legend",
      position = "left",
      fallback.palette = NULL,
      call = caller_call(),
      super = ScaleDiscrete
    )

Arguments[](https://ggplot2.tidyverse.org/reference/discrete_scale.html#arguments)

-----------------------------------------------------------------------------------

aesthetics[](https://ggplot2.tidyverse.org/reference/discrete_scale.html#arg-aesthetics)

The names of the aesthetics that this scale works with.

scale\_name[](https://ggplot2.tidyverse.org/reference/discrete_scale.html#arg-scale-name)

[![[Deprecated]](https://ggplot2.tidyverse.org/reference/figures/lifecycle-deprecated.svg)](https://lifecycle.r-lib.org/articles/stages.html#deprecated)
 The name of the scale that should be used for error messages associated with this scale.

palette[](https://ggplot2.tidyverse.org/reference/discrete_scale.html#arg-palette)

A palette function that when called with a single integer argument (the number of levels in the scale) returns the values that they should take (e.g., `[scales::pal_hue()](https://scales.r-lib.org/reference/pal_hue.html) `).

name[](https://ggplot2.tidyverse.org/reference/discrete_scale.html#arg-name)

The name of the scale. Used as the axis or legend title. If `[waiver()](https://ggplot2.tidyverse.org/reference/waiver.html) `, the default, the name of the scale is taken from the first mapping used for that aesthetic. If `NULL`, the legend title will be omitted.

breaks[](https://ggplot2.tidyverse.org/reference/discrete_scale.html#arg-breaks)

One of:

*   `NULL` for no breaks
    
*   `[waiver()](https://ggplot2.tidyverse.org/reference/waiver.html) ` for the default breaks (the scale limits)
    
*   A character vector of breaks
    
*   A function that takes the limits as input and returns breaks as output. Also accepts rlang [lambda](https://rlang.r-lib.org/reference/as_function.html)
     function notation.
    

minor\_breaks[](https://ggplot2.tidyverse.org/reference/discrete_scale.html#arg-minor-breaks)

One of:

*   `NULL` for no minor breaks
    
*   `[waiver()](https://ggplot2.tidyverse.org/reference/waiver.html) ` for the default breaks (none for discrete, one minor break between each major break for continuous)
    
*   A numeric vector of positions
    
*   A function that given the limits returns a vector of minor breaks. Also accepts rlang [lambda](https://rlang.r-lib.org/reference/as_function.html)
     function notation. When the function has two arguments, it will be given the limits and major break positions.
    

labels[](https://ggplot2.tidyverse.org/reference/discrete_scale.html#arg-labels)

One of the options below. Please note that when `labels` is a vector, it is highly recommended to also set the `breaks` argument as a vector to protect against unintended mismatches.

*   `NULL` for no labels
    
*   `[waiver()](https://ggplot2.tidyverse.org/reference/waiver.html) ` for the default labels computed by the transformation object
    
*   A character vector giving labels (must be same length as `breaks`)
    
*   An expression vector (must be the same length as breaks). See ?plotmath for details.
    
*   A function that takes the breaks as input and returns labels as output. Also accepts rlang [lambda](https://rlang.r-lib.org/reference/as_function.html)
     function notation.
    

limits[](https://ggplot2.tidyverse.org/reference/discrete_scale.html#arg-limits)

One of:

*   `NULL` to use the default scale values
    
*   A character vector that defines possible values of the scale and their order
    
*   A function that accepts the existing (automatic) values and returns new ones. Also accepts rlang [lambda](https://rlang.r-lib.org/reference/as_function.html)
     function notation.
    

expand[](https://ggplot2.tidyverse.org/reference/discrete_scale.html#arg-expand)

For position scales, a vector of range expansion constants used to add some padding around the data to ensure that they are placed some distance away from the axes. Use the convenience function `[expansion()](https://ggplot2.tidyverse.org/reference/expansion.html) ` to generate the values for the `expand` argument. The defaults are to expand the scale by 5% on each side for continuous variables, and by 0.6 units on each side for discrete variables.

na.translate[](https://ggplot2.tidyverse.org/reference/discrete_scale.html#arg-na-translate)

Unlike continuous scales, discrete scales can easily show missing values, and do so by default. If you want to remove missing values from a discrete scale, specify `na.translate = FALSE`.

na.value[](https://ggplot2.tidyverse.org/reference/discrete_scale.html#arg-na-value)

If `na.translate = TRUE`, what aesthetic value should the missing values be displayed as? Does not apply to position scales where `NA` is always placed at the far right.

drop[](https://ggplot2.tidyverse.org/reference/discrete_scale.html#arg-drop)

Should unused factor levels be omitted from the scale? The default, `TRUE`, uses the levels that appear in the data; `FALSE` includes the levels in the factor. Please note that to display every level in a legend, the layer should use `show.legend = TRUE`.

guide[](https://ggplot2.tidyverse.org/reference/discrete_scale.html#arg-guide)

A function used to create a guide or its name. See `[guides()](https://ggplot2.tidyverse.org/reference/guides.html) ` for more information.

position[](https://ggplot2.tidyverse.org/reference/discrete_scale.html#arg-position)

For position scales, The position of the axis. `left` or `right` for y axes, `top` or `bottom` for x axes.

fallback.palette[](https://ggplot2.tidyverse.org/reference/discrete_scale.html#arg-fallback-palette)

Function to use when `palette = NULL` and the palette is not represented in the theme.

call[](https://ggplot2.tidyverse.org/reference/discrete_scale.html#arg-call)

The `call` used to construct the scale for reporting messages.

super[](https://ggplot2.tidyverse.org/reference/discrete_scale.html#arg-super)

The super class to use for the constructed scale

See also[](https://ggplot2.tidyverse.org/reference/discrete_scale.html#see-also)

---------------------------------------------------------------------------------

The [new scales section](https://ggplot2-book.org/extensions#sec-new-scales)
 of the online ggplot2 book.