[Skip to content](https://ggplot2.tidyverse.org/reference/geom_bin_2d.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Heatmap of 2d bin counts
========================

Source: [`R/geom-bin2d.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/geom-bin2d.R)
, [`R/stat-bin2d.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/stat-bin2d.R)

`geom_bin_2d.Rd`

Divides the plane into rectangles, counts the number of cases in each rectangle, and then (by default) maps the number of cases to the rectangle's fill. This is a useful alternative to `[geom_point()](https://ggplot2.tidyverse.org/reference/geom_point.html) ` in the presence of overplotting.

Usage[](https://ggplot2.tidyverse.org/reference/geom_bin_2d.html#ref-usage)

----------------------------------------------------------------------------

    geom_bin_2d(
      mapping = NULL,
      data = NULL,
      stat = "bin2d",
      position = "identity",
      ...,
      lineend = "butt",
      linejoin = "mitre",
      na.rm = FALSE,
      show.legend = NA,
      inherit.aes = TRUE
    )
    
    stat_bin_2d(
      mapping = NULL,
      data = NULL,
      geom = "tile",
      position = "identity",
      ...,
      binwidth = NULL,
      bins = 30,
      breaks = NULL,
      drop = TRUE,
      boundary = NULL,
      closed = NULL,
      center = NULL,
      na.rm = FALSE,
      show.legend = NA,
      inherit.aes = TRUE
    )

Arguments[](https://ggplot2.tidyverse.org/reference/geom_bin_2d.html#arguments)

--------------------------------------------------------------------------------

mapping[](https://ggplot2.tidyverse.org/reference/geom_bin_2d.html#arg-mapping)

Set of aesthetic mappings created by `[aes()](https://ggplot2.tidyverse.org/reference/aes.html) `. If specified and `inherit.aes = TRUE` (the default), it is combined with the default mapping at the top level of the plot. You must supply `mapping` if there is no plot mapping.

data[](https://ggplot2.tidyverse.org/reference/geom_bin_2d.html#arg-data)

The data to be displayed in this layer. There are three options:

If `NULL`, the default, the data is inherited from the plot data as specified in the call to `[ggplot()](https://ggplot2.tidyverse.org/reference/ggplot.html) `.

A `data.frame`, or other object, will override the plot data. All objects will be fortified to produce a data frame. See `[fortify()](https://ggplot2.tidyverse.org/reference/fortify.html) ` for which variables will be created.

A `function` will be called with a single argument, the plot data. The return value must be a `data.frame`, and will be used as the layer data. A `function` can be created from a `formula` (e.g. `~ head(.x, 10)`).

position[](https://ggplot2.tidyverse.org/reference/geom_bin_2d.html#arg-position)

A position adjustment to use on the data for this layer. This can be used in various ways, including to prevent overplotting and improving the display. The `position` argument accepts the following:

*   The result of calling a position function, such as `[position_jitter()](https://ggplot2.tidyverse.org/reference/position_jitter.html) `. This method allows for passing extra arguments to the position.
    
*   A string naming the position adjustment. To give the position as a string, strip the function name of the `position_` prefix. For example, to use `[position_jitter()](https://ggplot2.tidyverse.org/reference/position_jitter.html) `, give the position as `"jitter"`.
    
*   For more information and other ways to specify the position, see the [layer position](https://ggplot2.tidyverse.org/reference/layer_positions.html)
     documentation.
    

...[](https://ggplot2.tidyverse.org/reference/geom_bin_2d.html#arg--)

Other arguments passed on to `[layer()](https://ggplot2.tidyverse.org/reference/layer.html) `'s `params` argument. These arguments broadly fall into one of 4 categories below. Notably, further arguments to the `position` argument, or aesthetics that are required can _not_ be passed through `...`. Unknown arguments that are not part of the 4 categories below are ignored.

*   Static aesthetics that are not mapped to a scale, but are at a fixed value and apply to the layer as a whole. For example, `colour = "red"` or `linewidth = 3`. The geom's documentation has an **Aesthetics** section that lists the available options. The 'required' aesthetics cannot be passed on to the `params`. Please note that while passing unmapped aesthetics as vectors is technically possible, the order and required length is not guaranteed to be parallel to the input data.
    
*   When constructing a layer using a `stat_*()` function, the `...` argument can be used to pass on parameters to the `geom` part of the layer. An example of this is `stat_density(geom = "area", outline.type = "both")`. The geom's documentation lists which parameters it can accept.
    
*   Inversely, when constructing a layer using a `geom_*()` function, the `...` argument can be used to pass on parameters to the `stat` part of the layer. An example of this is `geom_area(stat = "density", adjust = 0.5)`. The stat's documentation lists which parameters it can accept.
    
*   The `key_glyph` argument of `[layer()](https://ggplot2.tidyverse.org/reference/layer.html) ` may also be passed on through `...`. This can be one of the functions described as [key glyphs](https://ggplot2.tidyverse.org/reference/draw_key.html)
    , to change the display of the layer in the legend.
    

lineend[](https://ggplot2.tidyverse.org/reference/geom_bin_2d.html#arg-lineend)

Line end style (round, butt, square).

linejoin[](https://ggplot2.tidyverse.org/reference/geom_bin_2d.html#arg-linejoin)

Line join style (round, mitre, bevel).

na.rm[](https://ggplot2.tidyverse.org/reference/geom_bin_2d.html#arg-na-rm)

If `FALSE`, the default, missing values are removed with a warning. If `TRUE`, missing values are silently removed.

show.legend[](https://ggplot2.tidyverse.org/reference/geom_bin_2d.html#arg-show-legend)

logical. Should this layer be included in the legends? `NA`, the default, includes if any aesthetics are mapped. `FALSE` never includes, and `TRUE` always includes. It can also be a named logical vector to finely select the aesthetics to display. To include legend keys for all levels, even when no data exists, use `TRUE`. If `NA`, all levels are shown in legend, but unobserved levels are omitted.

inherit.aes[](https://ggplot2.tidyverse.org/reference/geom_bin_2d.html#arg-inherit-aes)

If `FALSE`, overrides the default aesthetics, rather than combining with them. This is most useful for helper functions that define both data and aesthetics and shouldn't inherit behaviour from the default plot specification, e.g. `[annotation_borders()](https://ggplot2.tidyverse.org/reference/annotation_borders.html) `.

geom, stat[](https://ggplot2.tidyverse.org/reference/geom_bin_2d.html#arg-geom-stat)

Use to override the default connection between `geom_bin_2d()` and `stat_bin_2d()`. For more information about overriding these connections, see how the [stat](https://ggplot2.tidyverse.org/reference/layer_stats.html)
 and [geom](https://ggplot2.tidyverse.org/reference/layer_geoms.html)
 arguments work.

binwidth[](https://ggplot2.tidyverse.org/reference/geom_bin_2d.html#arg-binwidth)

The width of the bins. Can be specified as a numeric value or as a function that takes x after scale transformation as input and returns a single numeric value. When specifying a function along with a grouping structure, the function will be called once per group. The default is to use the number of bins in `bins`, covering the range of the data. You should always override this value, exploring multiple widths to find the best to illustrate the stories in your data.

The bin width of a date variable is the number of days in each time; the bin width of a time variable is the number of seconds.

bins[](https://ggplot2.tidyverse.org/reference/geom_bin_2d.html#arg-bins)

Number of bins. Overridden by `binwidth`. Defaults to 30.

breaks[](https://ggplot2.tidyverse.org/reference/geom_bin_2d.html#arg-breaks)

Alternatively, you can supply a numeric vector giving the bin boundaries. Overrides `binwidth`, `bins`, `center`, and `boundary`. Can also be a function that takes group-wise values as input and returns bin boundaries.

drop[](https://ggplot2.tidyverse.org/reference/geom_bin_2d.html#arg-drop)

if `TRUE` removes all cells with 0 counts.

closed[](https://ggplot2.tidyverse.org/reference/geom_bin_2d.html#arg-closed)

One of `"right"` or `"left"` indicating whether right or left edges of bins are included in the bin.

center, boundary[](https://ggplot2.tidyverse.org/reference/geom_bin_2d.html#arg-center-boundary)

bin position specifiers. Only one, `center` or `boundary`, may be specified for a single plot. `center` specifies the center of one of the bins. `boundary` specifies the boundary between two bins. Note that if either is above or below the range of the data, things will be shifted by the appropriate integer multiple of `binwidth`. For example, to center on integers use `binwidth = 1` and `center = 0`, even if `0` is outside the range of the data. Alternatively, this same alignment can be specified with `binwidth = 1` and `boundary = 0.5`, even if `0.5` is outside the range of the data.

Computed variables[](https://ggplot2.tidyverse.org/reference/geom_bin_2d.html#computed-variables)

--------------------------------------------------------------------------------------------------

These are calculated by the 'stat' part of layers and can be accessed with [delayed evaluation](https://ggplot2.tidyverse.org/reference/aes_eval.html)
.

*   `after_stat(count)`  
    number of points in bin.
    
*   `after_stat(density)`  
    density of points in bin, scaled to integrate to 1.
    
*   `after_stat(ncount)`  
    count, scaled to maximum of 1.
    
*   `after_stat(ndensity)`  
    density, scaled to a maximum of 1.
    

Controlling binning parameters for the x and y directions[](https://ggplot2.tidyverse.org/reference/geom_bin_2d.html#controlling-binning-parameters-for-the-x-and-y-directions)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The arguments `bins`, `binwidth`, `breaks`, `center`, and `boundary` can be set separately for the x and y directions. When given as a scalar, one value applies to both directions. When given as a vector of length two, the first is applied to the x direction and the second to the y direction. Alternatively, these can be a named list containing `x` and `y` elements, for example `list(x = 10, y = 20)`.

See also[](https://ggplot2.tidyverse.org/reference/geom_bin_2d.html#see-also)

------------------------------------------------------------------------------

`[stat_bin_hex()](https://ggplot2.tidyverse.org/reference/geom_hex.html) ` for hexagonal binning

Aesthetics[](https://ggplot2.tidyverse.org/reference/geom_bin_2d.html#aesthetics)

----------------------------------------------------------------------------------

`geom_bin2d()` understands the following aesthetics. Required aesthetics are displayed in bold and defaults are displayed for optional aesthetics:

|     |     |     |
| --- | --- | --- |
| •   | **`[x](https://ggplot2.tidyverse.org/reference/aes_position.html) `** |     |
| •   | **`[y](https://ggplot2.tidyverse.org/reference/aes_position.html) `** |     |
| •   | `[alpha](https://ggplot2.tidyverse.org/reference/aes_colour_fill_alpha.html) ` | → `NA` |
| •   | `[colour](https://ggplot2.tidyverse.org/reference/aes_colour_fill_alpha.html) ` | → via `[theme()](https://ggplot2.tidyverse.org/reference/theme.html) ` |
| •   | `[fill](https://ggplot2.tidyverse.org/reference/aes_colour_fill_alpha.html) ` | → via `[theme()](https://ggplot2.tidyverse.org/reference/theme.html) ` |
| •   | `[group](https://ggplot2.tidyverse.org/reference/aes_group_order.html) ` | → inferred |
| •   | `height` | → `1` |
| •   | `[linetype](https://ggplot2.tidyverse.org/reference/aes_linetype_size_shape.html) ` | → via `[theme()](https://ggplot2.tidyverse.org/reference/theme.html) ` |
| •   | `[linewidth](https://ggplot2.tidyverse.org/reference/aes_linetype_size_shape.html) ` | → via `[theme()](https://ggplot2.tidyverse.org/reference/theme.html) ` |
| •   | `width` | → `1` |

Learn more about setting these aesthetics in `[vignette("ggplot2-specs")](https://ggplot2.tidyverse.org/articles/ggplot2-specs.html) `.

Examples[](https://ggplot2.tidyverse.org/reference/geom_bin_2d.html#ref-examples)

----------------------------------------------------------------------------------

    d <- ggplot(diamonds, aes(x, y)) + xlim(4, 10) + ylim(4, 10)
    d + geom_bin_2d()
    #> `stat_bin2d()` using `bins = 30`. Pick better value `binwidth`.
    #> Warning: Removed 478 rows containing non-finite outside the scale range
    #> (`stat_bin2d()`).
    #> Warning: Removed 5 rows containing missing values or values outside the scale
    #> range (`geom_bin2d()`).
    
    
    # You can control the size of the bins by specifying the number of
    # bins in each direction:
    d + geom_bin_2d(bins = 10)
    #> Warning: Removed 478 rows containing non-finite outside the scale range
    #> (`stat_bin2d()`).
    
    d + geom_bin_2d(bins = list(x = 30, y = 10))
    #> Warning: Removed 478 rows containing non-finite outside the scale range
    #> (`stat_bin2d()`).
    #> Warning: Removed 2 rows containing missing values or values outside the scale
    #> range (`geom_bin2d()`).
    
    
    # Or by specifying the width of the bins
    d + geom_bin_2d(binwidth = c(0.1, 0.1))
    #> Warning: Removed 478 rows containing non-finite outside the scale range
    #> (`stat_bin2d()`).