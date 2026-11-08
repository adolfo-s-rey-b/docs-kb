[Skip to content](https://ggplot2.tidyverse.org/reference/ggplot_build.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Build ggplot for rendering.
===========================

Source: [`R/plot-build.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/plot-build.R)

`ggplot_build.Rd`

`build_ggplot()` takes the plot object, and performs all steps necessary to produce an object that can be rendered. This function outputs two pieces: a list of data frames (one for each layer), and a panel object, which contain all information about axis limits, breaks etc. The `ggplot_build()` function is vestigial and `build_ggplot()` should be used instead.

Usage[](https://ggplot2.tidyverse.org/reference/ggplot_build.html#ref-usage)

-----------------------------------------------------------------------------

    ggplot_build(plot, ...)
    
    get_layer_data(plot = get_last_plot(), i = 1L)
    
    layer_data(plot = get_last_plot(), i = 1L)
    
    get_panel_scales(plot = get_last_plot(), i = 1L, j = 1L)
    
    layer_scales(plot = get_last_plot(), i = 1L, j = 1L)
    
    get_layer_grob(plot = get_last_plot(), i = 1L)
    
    layer_grob(plot = get_last_plot(), i = 1L)

Arguments[](https://ggplot2.tidyverse.org/reference/ggplot_build.html#arguments)

---------------------------------------------------------------------------------

plot[](https://ggplot2.tidyverse.org/reference/ggplot_build.html#arg-plot)

ggplot object

...[](https://ggplot2.tidyverse.org/reference/ggplot_build.html#arg--)

Not currently in use.

i[](https://ggplot2.tidyverse.org/reference/ggplot_build.html#arg-i)

An integer. In `get_layer_data()`, the data to return (in the order added to the plot). In `get_layer_grob()`, the grob to return (in the order added to the plot). In `get_panel_scales()`, the row of a facet to return scales for.

j[](https://ggplot2.tidyverse.org/reference/ggplot_build.html#arg-j)

An integer. In `get_panel_scales()`, the column of a facet to return scales for.

Details[](https://ggplot2.tidyverse.org/reference/ggplot_build.html#details)

-----------------------------------------------------------------------------

`get_layer_data()`, `get_layer_grob()`, and `get_panel_scales()` are helper functions that return the data, grob, or scales associated with a given layer. These are useful for tests.

See also[](https://ggplot2.tidyverse.org/reference/ggplot_build.html#see-also)

-------------------------------------------------------------------------------

`[print.ggplot()](https://ggplot2.tidyverse.org/reference/print.ggplot.html) ` and `[benchplot()](https://ggplot2.tidyverse.org/reference/benchplot.html) ` for functions that contain the complete set of steps for generating a ggplot2 plot.

The [build step section](https://ggplot2-book.org/internals#sec-ggplotbuild)
 of the online ggplot2 book.