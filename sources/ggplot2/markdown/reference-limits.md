[Skip to content](https://ggplot2.tidyverse.org/reference/limits.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Generate correct scale type for specified limits
================================================

Source: [`R/limits.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/limits.R)

`limits.Rd`

Generate correct scale type for specified limits

Usage[](https://ggplot2.tidyverse.org/reference/limits.html#ref-usage)

-----------------------------------------------------------------------

    limits(lims, var, call = caller_env())

Arguments[](https://ggplot2.tidyverse.org/reference/limits.html#arguments)

---------------------------------------------------------------------------

lims[](https://ggplot2.tidyverse.org/reference/limits.html#arg-lims)

vector of limits

var[](https://ggplot2.tidyverse.org/reference/limits.html#arg-var)

name of variable

Examples[](https://ggplot2.tidyverse.org/reference/limits.html#ref-examples)

-----------------------------------------------------------------------------

    ggplot2:::limits(c(1, 5), "x")
    #> <ScaleContinuousPosition>
    #>  Range:  
    #>  Limits:    1 --    5
    ggplot2:::limits(c(5, 1), "x")
    #> <ScaleContinuousPosition>
    #>  Range:  
    #>  Limits:   -5 --   -1
    ggplot2:::limits(c("A", "b", "c"), "x")
    #> <ggproto object: Class ScaleDiscretePosition, ScaleDiscrete, Scale, gg>
    #>     aesthetics: x xmin xmax xend xintercept xmin_final xmax_final xlower ...
    #>     axis_order: function
    #>     break_info: function
    #>     break_positions: function
    #>     breaks: waiver
    #>     call: environment
    #>     clone: function
    #>     continuous_limits: NULL
    #>     dimension: function
    #>     drop: TRUE
    #>     expand: waiver
    #>     fallback_palette: function
    #>     get_breaks: function
    #>     get_breaks_minor: function
    #>     get_labels: function
    #>     get_limits: function
    #>     get_transformation: function
    #>     guide: waiver
    #>     is_discrete: function
    #>     is_empty: function
    #>     labels: waiver
    #>     limits: A b c
    #>     make_sec_title: function
    #>     make_title: function
    #>     map: function
    #>     map_df: function
    #>     minor_breaks: waiver
    #>     n.breaks.cache: NULL
    #>     na.translate: TRUE
    #>     na.value: NA
    #>     name: waiver
    #>     palette: function
    #>     palette.cache: NULL
    #>     position: bottom
    #>     range: environment
    #>     range_c: environment
    #>     rescale: function
    #>     reset: function
    #>     sec_name: function
    #>     train: function
    #>     train_df: function
    #>     transform: function
    #>     transform_df: function
    #>     super:  <ggproto object: Class ScaleDiscretePosition, ScaleDiscrete, Scale, gg>
    ggplot2:::limits(c("A", "b", "c"), "fill")
    #> <ggproto object: Class ScaleDiscrete, Scale, gg>
    #>     aesthetics: fill
    #>     axis_order: function
    #>     break_info: function
    #>     break_positions: function
    #>     breaks: waiver
    #>     call: environment
    #>     clone: function
    #>     dimension: function
    #>     drop: TRUE
    #>     expand: waiver
    #>     fallback_palette: function
    #>     get_breaks: function
    #>     get_breaks_minor: function
    #>     get_labels: function
    #>     get_limits: function
    #>     get_transformation: function
    #>     guide: legend
    #>     is_discrete: function
    #>     is_empty: function
    #>     labels: waiver
    #>     limits: A b c
    #>     make_sec_title: function
    #>     make_title: function
    #>     map: function
    #>     map_df: function
    #>     minor_breaks: waiver
    #>     n.breaks.cache: NULL
    #>     na.translate: TRUE
    #>     na.value: grey50
    #>     name: waiver
    #>     palette: NULL
    #>     palette.cache: NULL
    #>     position: left
    #>     range: environment
    #>     rescale: function
    #>     reset: function
    #>     train: function
    #>     train_df: function
    #>     transform: function
    #>     transform_df: function
    #>     super:  <ggproto object: Class ScaleDiscrete, Scale, gg>
    ggplot2:::limits(as.Date(c("2008-01-01", "2009-01-01")), "x")
    #> <ScaleContinuousDate>
    #>  Range:  
    #>  Limits: 1.39e+04 -- 1.42e+04