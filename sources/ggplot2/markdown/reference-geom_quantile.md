[Skip to content](https://ggplot2.tidyverse.org/reference/geom_quantile.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Quantile regression
===================

Source: [`R/geom-quantile.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/geom-quantile.R)
, [`R/stat-quantilemethods.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/stat-quantilemethods.R)

`geom_quantile.Rd`

This fits a quantile regression to the data and draws the fitted quantiles with lines. This is as a continuous analogue to `[geom_boxplot()](https://ggplot2.tidyverse.org/reference/geom_boxplot.html) `.

Usage[](https://ggplot2.tidyverse.org/reference/geom_quantile.html#ref-usage)

------------------------------------------------------------------------------

    geom_quantile(
      mapping = NULL,
      data = NULL,
      stat = "quantile",
      position = "identity",
      ...,
      arrow = NULL,
      arrow.fill = NULL,
      lineend = "butt",
      linejoin = "round",
      linemitre = 10,
      na.rm = FALSE,
      show.legend = NA,
      inherit.aes = TRUE
    )
    
    stat_quantile(
      mapping = NULL,
      data = NULL,
      geom = "quantile",
      position = "identity",
      ...,
      quantiles = c(0.25, 0.5, 0.75),
      formula = NULL,
      method = "rq",
      method.args = list(),
      na.rm = FALSE,
      show.legend = NA,
      inherit.aes = TRUE
    )

Arguments[](https://ggplot2.tidyverse.org/reference/geom_quantile.html#arguments)

----------------------------------------------------------------------------------

mapping[](https://ggplot2.tidyverse.org/reference/geom_quantile.html#arg-mapping)

Set of aesthetic mappings created by `[aes()](https://ggplot2.tidyverse.org/reference/aes.html) `. If specified and `inherit.aes = TRUE` (the default), it is combined with the default mapping at the top level of the plot. You must supply `mapping` if there is no plot mapping.

data[](https://ggplot2.tidyverse.org/reference/geom_quantile.html#arg-data)

The data to be displayed in this layer. There are three options:

If `NULL`, the default, the data is inherited from the plot data as specified in the call to `[ggplot()](https://ggplot2.tidyverse.org/reference/ggplot.html) `.

A `data.frame`, or other object, will override the plot data. All objects will be fortified to produce a data frame. See `[fortify()](https://ggplot2.tidyverse.org/reference/fortify.html) ` for which variables will be created.

A `function` will be called with a single argument, the plot data. The return value must be a `data.frame`, and will be used as the layer data. A `function` can be created from a `formula` (e.g. `~ head(.x, 10)`).

position[](https://ggplot2.tidyverse.org/reference/geom_quantile.html#arg-position)

A position adjustment to use on the data for this layer. This can be used in various ways, including to prevent overplotting and improving the display. The `position` argument accepts the following:

*   The result of calling a position function, such as `[position_jitter()](https://ggplot2.tidyverse.org/reference/position_jitter.html) `. This method allows for passing extra arguments to the position.
    
*   A string naming the position adjustment. To give the position as a string, strip the function name of the `position_` prefix. For example, to use `[position_jitter()](https://ggplot2.tidyverse.org/reference/position_jitter.html) `, give the position as `"jitter"`.
    
*   For more information and other ways to specify the position, see the [layer position](https://ggplot2.tidyverse.org/reference/layer_positions.html)
     documentation.
    

...[](https://ggplot2.tidyverse.org/reference/geom_quantile.html#arg--)

Other arguments passed on to `[layer()](https://ggplot2.tidyverse.org/reference/layer.html) `'s `params` argument. These arguments broadly fall into one of 4 categories below. Notably, further arguments to the `position` argument, or aesthetics that are required can _not_ be passed through `...`. Unknown arguments that are not part of the 4 categories below are ignored.

*   Static aesthetics that are not mapped to a scale, but are at a fixed value and apply to the layer as a whole. For example, `colour = "red"` or `linewidth = 3`. The geom's documentation has an **Aesthetics** section that lists the available options. The 'required' aesthetics cannot be passed on to the `params`. Please note that while passing unmapped aesthetics as vectors is technically possible, the order and required length is not guaranteed to be parallel to the input data.
    
*   When constructing a layer using a `stat_*()` function, the `...` argument can be used to pass on parameters to the `geom` part of the layer. An example of this is `stat_density(geom = "area", outline.type = "both")`. The geom's documentation lists which parameters it can accept.
    
*   Inversely, when constructing a layer using a `geom_*()` function, the `...` argument can be used to pass on parameters to the `stat` part of the layer. An example of this is `geom_area(stat = "density", adjust = 0.5)`. The stat's documentation lists which parameters it can accept.
    
*   The `key_glyph` argument of `[layer()](https://ggplot2.tidyverse.org/reference/layer.html) ` may also be passed on through `...`. This can be one of the functions described as [key glyphs](https://ggplot2.tidyverse.org/reference/draw_key.html)
    , to change the display of the layer in the legend.
    

arrow[](https://ggplot2.tidyverse.org/reference/geom_quantile.html#arg-arrow)

Arrow specification, as created by `[grid::arrow()](https://rdrr.io/r/grid/arrow.html) `.

arrow.fill[](https://ggplot2.tidyverse.org/reference/geom_quantile.html#arg-arrow-fill)

fill colour to use for the arrow head (if closed). `NULL` means use `colour` aesthetic.

lineend[](https://ggplot2.tidyverse.org/reference/geom_quantile.html#arg-lineend)

Line end style (round, butt, square).

linejoin[](https://ggplot2.tidyverse.org/reference/geom_quantile.html#arg-linejoin)

Line join style (round, mitre, bevel).

linemitre[](https://ggplot2.tidyverse.org/reference/geom_quantile.html#arg-linemitre)

Line mitre limit (number greater than 1).

na.rm[](https://ggplot2.tidyverse.org/reference/geom_quantile.html#arg-na-rm)

If `FALSE`, the default, missing values are removed with a warning. If `TRUE`, missing values are silently removed.

show.legend[](https://ggplot2.tidyverse.org/reference/geom_quantile.html#arg-show-legend)

logical. Should this layer be included in the legends? `NA`, the default, includes if any aesthetics are mapped. `FALSE` never includes, and `TRUE` always includes. It can also be a named logical vector to finely select the aesthetics to display. To include legend keys for all levels, even when no data exists, use `TRUE`. If `NA`, all levels are shown in legend, but unobserved levels are omitted.

inherit.aes[](https://ggplot2.tidyverse.org/reference/geom_quantile.html#arg-inherit-aes)

If `FALSE`, overrides the default aesthetics, rather than combining with them. This is most useful for helper functions that define both data and aesthetics and shouldn't inherit behaviour from the default plot specification, e.g. `[annotation_borders()](https://ggplot2.tidyverse.org/reference/annotation_borders.html) `.

geom, stat[](https://ggplot2.tidyverse.org/reference/geom_quantile.html#arg-geom-stat)

Use to override the default connection between `geom_quantile()` and `stat_quantile()`. For more information about overriding these connections, see how the [stat](https://ggplot2.tidyverse.org/reference/layer_stats.html)
 and [geom](https://ggplot2.tidyverse.org/reference/layer_geoms.html)
 arguments work.

quantiles[](https://ggplot2.tidyverse.org/reference/geom_quantile.html#arg-quantiles)

conditional quantiles of y to calculate and display

formula[](https://ggplot2.tidyverse.org/reference/geom_quantile.html#arg-formula)

formula relating y variables to x variables

method[](https://ggplot2.tidyverse.org/reference/geom_quantile.html#arg-method)

Quantile regression method to use. Available options are `"rq"` (for `[quantreg::rq()](https://rdrr.io/pkg/quantreg/man/rq.html) `) and `"rqss"` (for `[quantreg::rqss()](https://rdrr.io/pkg/quantreg/man/rqss.html) `).

method.args[](https://ggplot2.tidyverse.org/reference/geom_quantile.html#arg-method-args)

List of additional arguments passed on to the modelling function defined by `method`.

Computed variables[](https://ggplot2.tidyverse.org/reference/geom_quantile.html#computed-variables)

----------------------------------------------------------------------------------------------------

These are calculated by the 'stat' part of layers and can be accessed with [delayed evaluation](https://ggplot2.tidyverse.org/reference/aes_eval.html)
.

*   `after_stat(quantile)`  
    Quantile of distribution.
    

Aesthetics[](https://ggplot2.tidyverse.org/reference/geom_quantile.html#aesthetics)

------------------------------------------------------------------------------------

`geom_quantile()` understands the following aesthetics. Required aesthetics are displayed in bold and defaults are displayed for optional aesthetics:

|     |     |     |
| --- | --- | --- |
| •   | **`[x](https://ggplot2.tidyverse.org/reference/aes_position.html) `** |     |
| •   | **`[y](https://ggplot2.tidyverse.org/reference/aes_position.html) `** |     |
| •   | `[alpha](https://ggplot2.tidyverse.org/reference/aes_colour_fill_alpha.html) ` | → `NA` |
| •   | `[colour](https://ggplot2.tidyverse.org/reference/aes_colour_fill_alpha.html) ` | → via `[theme()](https://ggplot2.tidyverse.org/reference/theme.html) ` |
| •   | `[group](https://ggplot2.tidyverse.org/reference/aes_group_order.html) ` | → inferred |
| •   | `[linetype](https://ggplot2.tidyverse.org/reference/aes_linetype_size_shape.html) ` | → via `[theme()](https://ggplot2.tidyverse.org/reference/theme.html) ` |
| •   | `[linewidth](https://ggplot2.tidyverse.org/reference/aes_linetype_size_shape.html) ` | → via `[theme()](https://ggplot2.tidyverse.org/reference/theme.html) ` |
| •   | `weight` | → `1` |

Learn more about setting these aesthetics in `[vignette("ggplot2-specs")](https://ggplot2.tidyverse.org/articles/ggplot2-specs.html) `.

Examples[](https://ggplot2.tidyverse.org/reference/geom_quantile.html#ref-examples)

------------------------------------------------------------------------------------

    m <-
      ggplot(mpg, aes(displ, 1 / hwy)) +
      geom_point()
    m + geom_quantile()
    #> Smoothing formula not specified. Using: y ~ x
    
    m + geom_quantile(quantiles = 0.5)
    #> Smoothing formula not specified. Using: y ~ x
    
    q10 <- seq(0.05, 0.95, by = 0.05)
    m + geom_quantile(quantiles = q10)
    #> Smoothing formula not specified. Using: y ~ x
    
    
    # You can also use rqss to fit smooth quantiles
    m + geom_quantile(method = "rqss")
    #> Smoothing formula not specified. Using: y ~ qss(x, lambda = 1)
    
    # Note that rqss doesn't pick a smoothing constant automatically, so
    # you'll need to tweak lambda yourself
    m + geom_quantile(method = "rqss", lambda = 0.1)
    #> Smoothing formula not specified. Using: y ~ qss(x, lambda = 0.1)
    
    
    # Set aesthetics to fixed value
    m + geom_quantile(colour = "red", linewidth = 2, alpha = 0.5)
    #> Smoothing formula not specified. Using: y ~ x