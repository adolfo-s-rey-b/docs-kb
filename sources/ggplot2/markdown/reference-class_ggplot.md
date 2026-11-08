[Skip to content](https://ggplot2.tidyverse.org/reference/class_ggplot.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

The ggplot class
================

Source: [`R/all-classes.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/all-classes.R)

`class_ggplot.Rd`

The ggplot class collects the needed information to render a plot. This class can be constructed using the `[ggplot()](https://ggplot2.tidyverse.org/reference/ggplot.html) ` function.

Usage[](https://ggplot2.tidyverse.org/reference/class_ggplot.html#ref-usage)

-----------------------------------------------------------------------------

    class_ggplot(
      data = waiver(),
      ...,
      layers = list(),
      scales = NULL,
      guides = NULL,
      mapping = aes(),
      theme = NULL,
      coordinates = coord_cartesian(default = TRUE),
      facet = facet_null(),
      layout = NULL,
      labels = labs(),
      meta = list(),
      plot_env = parent.frame()
    )

Arguments[](https://ggplot2.tidyverse.org/reference/class_ggplot.html#arguments)

---------------------------------------------------------------------------------

data[](https://ggplot2.tidyverse.org/reference/class_ggplot.html#arg-data)

A property containing any data coerced by `[fortify()](https://ggplot2.tidyverse.org/reference/fortify.html) `.

...[](https://ggplot2.tidyverse.org/reference/class_ggplot.html#arg--)

Reserved for future expansion.

layers[](https://ggplot2.tidyverse.org/reference/class_ggplot.html#arg-layers)

A list of layer instances created by `[layer()](https://ggplot2.tidyverse.org/reference/layer.html) `.

scales[](https://ggplot2.tidyverse.org/reference/class_ggplot.html#arg-scales)

A ScalesList ggproto object.

guides[](https://ggplot2.tidyverse.org/reference/class_ggplot.html#arg-guides)

A Guides ggproto object created by `[guides()](https://ggplot2.tidyverse.org/reference/guides.html) `.

mapping[](https://ggplot2.tidyverse.org/reference/class_ggplot.html#arg-mapping)

A mapping class object created by `[aes()](https://ggplot2.tidyverse.org/reference/aes.html) `.

theme[](https://ggplot2.tidyverse.org/reference/class_ggplot.html#arg-theme)

A theme class object created by `[theme()](https://ggplot2.tidyverse.org/reference/theme.html) `.

coordinates[](https://ggplot2.tidyverse.org/reference/class_ggplot.html#arg-coordinates)

A Coord ggproto object created by `coord_*()` family of functions.

facet[](https://ggplot2.tidyverse.org/reference/class_ggplot.html#arg-facet)

A Facet ggproto object created by `facet_*()` family of functions.

layout[](https://ggplot2.tidyverse.org/reference/class_ggplot.html#arg-layout)

A Layout ggproto object.

labels[](https://ggplot2.tidyverse.org/reference/class_ggplot.html#arg-labels)

A labels object created by `[labs()](https://ggplot2.tidyverse.org/reference/labs.html) `.

meta[](https://ggplot2.tidyverse.org/reference/class_ggplot.html#arg-meta)

A list for additional metadata. This will be deprecated in the future.

plot\_env[](https://ggplot2.tidyverse.org/reference/class_ggplot.html#arg-plot-env)

An environment.