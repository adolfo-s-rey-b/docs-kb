[Skip to content](https://ggplot2.tidyverse.org/reference/layer_positions.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Layer position adjustments
==========================

Source: [`R/docs_layer.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/docs_layer.R)

`layer_positions.Rd`

In ggplot2, a plot is constructed by adding layers to it. In addition to [geoms](https://ggplot2.tidyverse.org/reference/layer_geoms.html)
 and [stats](https://ggplot2.tidyverse.org/reference/layer_stats.html)
, position adjustments are the third required part of a layer. The 'position' part of a layer is responsible for dodging, jittering and nudging groups of data to minimise their overlap, or otherwise tweaking their positions.

For example if you add `position = position_nudge(x = 1)` to a layer, you can offset every x-position by 1. For many layers, the default position adjustment is `[position_identity()](https://ggplot2.tidyverse.org/reference/position_identity.html) `, which performs no adjustment.

Specifying positions[](https://ggplot2.tidyverse.org/reference/layer_positions.html#specifying-positions)

----------------------------------------------------------------------------------------------------------

There are 4 ways in which the 'position' part of a layer can be specified.

    1. A layer can have default position adjustments
    geom_jitter() # has `position = "jitter"`
    
    2. It can be given to a layer as a string
    geom_point(position = "jitter")
    
    3. The position function can be used to pass extra arguments
    geom_point(position = position_jitter(width = 1))
    
    4. It can be given to `layer()` directly
    layer(
      geom = "point",
      stat = "identity",
      position = "jitter"
    )
    

These ways are not always equivalent. Some layers may not understand what to do with a position adjustment, and require additional parameters passed through the `position_*()` function, or may not work correctly. For example `[position_dodge()](https://ggplot2.tidyverse.org/reference/position_dodge.html) ` requires non-overlapping x intervals, whereas `[geom_point()](https://ggplot2.tidyverse.org/reference/geom_point.html) ` doesn't have dimensions to calculate intervals for. To give positions as a string, take the function name, and remove the `position_` prefix, such that `position_fill` becomes `"fill"`.

Pairing geoms with positions[](https://ggplot2.tidyverse.org/reference/layer_positions.html#pairing-geoms-with-positions)

--------------------------------------------------------------------------------------------------------------------------

Some geoms work better with some positions than others. Below follows a brief overview of geoms and position adjustments that work well together.

### Identity[](https://ggplot2.tidyverse.org/reference/layer_positions.html#identity)

`[position_identity()](https://ggplot2.tidyverse.org/reference/position_identity.html) ` can work with virtually any geom.

### Dodging[](https://ggplot2.tidyverse.org/reference/layer_positions.html#dodging)

`[position_dodge()](https://ggplot2.tidyverse.org/reference/position_dodge.html) ` pushes overlapping objects away from one another and requires a `group` variable. `[position_dodge2()](https://ggplot2.tidyverse.org/reference/position_dodge.html) ` can work without group variables and can handle variable widths. As a rule of thumb, layers where groups occupy a range on the x-axis pair well with dodging. If layers have no width, you may be required to specify it manually with `position_dodge(width = ...)`. Some geoms that pair well with dodging are `[geom_bar()](https://ggplot2.tidyverse.org/reference/geom_bar.html) `, `[geom_boxplot()](https://ggplot2.tidyverse.org/reference/geom_boxplot.html) `, `[geom_linerange()](https://ggplot2.tidyverse.org/reference/geom_linerange.html) `, `[geom_errorbar()](https://ggplot2.tidyverse.org/reference/geom_linerange.html) ` and `[geom_text()](https://ggplot2.tidyverse.org/reference/geom_text.html) `.

### Jittering[](https://ggplot2.tidyverse.org/reference/layer_positions.html#jittering)

`[position_jitter()](https://ggplot2.tidyverse.org/reference/position_jitter.html) ` adds a some random noise to every point, which can help with overplotting. `[position_jitterdodge()](https://ggplot2.tidyverse.org/reference/position_jitterdodge.html) ` does the same, but also dodges the points. As a rule of thumb, jittering works best when points have discrete x-positions. Jittering is most useful for `[geom_point()](https://ggplot2.tidyverse.org/reference/geom_point.html) `, but can also be used in `[geom_path()](https://ggplot2.tidyverse.org/reference/geom_path.html) ` for example.

### Nudging[](https://ggplot2.tidyverse.org/reference/layer_positions.html#nudging)

`[position_nudge()](https://ggplot2.tidyverse.org/reference/position_nudge.html) ` can add offsets to x- and y-positions. This can be useful for discrete positions where you don't want to put an object exactly in the middle. While most useful for `[geom_text()](https://ggplot2.tidyverse.org/reference/geom_text.html) `, it can be used with virtually all geoms.

### Stacking[](https://ggplot2.tidyverse.org/reference/layer_positions.html#stacking)

`[position_stack()](https://ggplot2.tidyverse.org/reference/position_stack.html) ` is useful for displaying data on top of one another. It can be used for geoms that are usually anchored to the x-axis, for example `[geom_bar()](https://ggplot2.tidyverse.org/reference/geom_bar.html) `, `[geom_area()](https://ggplot2.tidyverse.org/reference/geom_ribbon.html) ` or `[geom_histogram()](https://ggplot2.tidyverse.org/reference/geom_histogram.html) `.

### Filling[](https://ggplot2.tidyverse.org/reference/layer_positions.html#filling)

`[position_fill()](https://ggplot2.tidyverse.org/reference/position_stack.html) ` can be used to give proportions at every x-position. Like stacking, filling is most useful for geoms that are anchored to the x-axis, like `[geom_bar()](https://ggplot2.tidyverse.org/reference/geom_bar.html) `, `[geom_area()](https://ggplot2.tidyverse.org/reference/geom_ribbon.html) ` or `[geom_histogram()](https://ggplot2.tidyverse.org/reference/geom_histogram.html) `.

Under the hood[](https://ggplot2.tidyverse.org/reference/layer_positions.html#under-the-hood)

----------------------------------------------------------------------------------------------

Internally, positions are represented as `[ggproto](https://ggplot2.tidyverse.org/reference/ggproto.html) ` classes that occupy a slot in a layer. All these classes inherit from the parental `[Position](https://ggplot2.tidyverse.org/reference/Position.html) ` ggproto object that orchestrates how positions work. Briefly, positions are given the opportunity to adjust the data of each facet panel. For more information about extending positions, see the **New positions** section of the [online book](https://ggplot2-book.org/extensions.html#new-positions)
.

See also[](https://ggplot2.tidyverse.org/reference/layer_positions.html#see-also)

----------------------------------------------------------------------------------

For an overview of all position adjustments, see the [online reference](https://ggplot2.tidyverse.org/reference/index.html#position-adjustment)
.

Other layer documentation: `[layer()](https://ggplot2.tidyverse.org/reference/layer.html) `, `[layer_geoms](https://ggplot2.tidyverse.org/reference/layer_geoms.html) `, `[layer_stats](https://ggplot2.tidyverse.org/reference/layer_stats.html) `