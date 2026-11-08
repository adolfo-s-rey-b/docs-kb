[Skip to content](https://ggplot2.tidyverse.org/reference/class_ggplot_built.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

The ggplot built class
======================

Source: [`R/all-classes.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/all-classes.R)

`class_ggplot_built.Rd`

The ggplot built class is an intermediate class and represents a processed ggplot object ready for rendering. It is constructed by calling `[ggplot_build()](https://ggplot2.tidyverse.org/reference/ggplot_build.html) ` on a [ggplot](https://ggplot2.tidyverse.org/reference/class_ggplot.html)
 object and is not meant to be instantiated directly. The class can be rendered to a gtable object by calling the `[ggplot_gtable()](https://ggplot2.tidyverse.org/reference/ggplot_gtable.html) ` function on a ggplot built class object.

Usage[](https://ggplot2.tidyverse.org/reference/class_ggplot_built.html#ref-usage)

-----------------------------------------------------------------------------------

    class_ggplot_built(..., data = NULL, layout = NULL, plot = NULL)

Arguments[](https://ggplot2.tidyverse.org/reference/class_ggplot_built.html#arguments)

---------------------------------------------------------------------------------------

...[](https://ggplot2.tidyverse.org/reference/class_ggplot_built.html#arg--)

Reserved for future expansion.

data[](https://ggplot2.tidyverse.org/reference/class_ggplot_built.html#arg-data)

A list of plain data frames; one for each layer.

layout[](https://ggplot2.tidyverse.org/reference/class_ggplot_built.html#arg-layout)

A Layout ggproto object.

plot[](https://ggplot2.tidyverse.org/reference/class_ggplot_built.html#arg-plot)

A completed ggplot class object.