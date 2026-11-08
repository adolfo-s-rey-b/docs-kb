[Skip to content](https://ggplot2.tidyverse.org/reference/coord_munch.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Munch coordinates data
======================

Source: [`R/coord-munch.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/coord-munch.R)

`coord_munch.Rd`

This function "munches" lines, dividing each line into many small pieces so they can be transformed independently. Used inside geom functions.

Usage[](https://ggplot2.tidyverse.org/reference/coord_munch.html#ref-usage)

----------------------------------------------------------------------------

    coord_munch(coord, data, range, segment_length = 0.01, is_closed = FALSE)

Arguments[](https://ggplot2.tidyverse.org/reference/coord_munch.html#arguments)

--------------------------------------------------------------------------------

coord[](https://ggplot2.tidyverse.org/reference/coord_munch.html#arg-coord)

Coordinate system definition.

data[](https://ggplot2.tidyverse.org/reference/coord_munch.html#arg-data)

Data set to transform - should have variables `x` and `y` are chopped up into small pieces (as defined by `group`). All other variables are duplicated as needed.

range[](https://ggplot2.tidyverse.org/reference/coord_munch.html#arg-range)

Panel range specification.

segment\_length[](https://ggplot2.tidyverse.org/reference/coord_munch.html#arg-segment-length)

Target segment length

is\_closed[](https://ggplot2.tidyverse.org/reference/coord_munch.html#arg-is-closed)

Whether data should be considered as a closed polygon.