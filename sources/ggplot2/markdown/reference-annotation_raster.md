[Skip to content](https://ggplot2.tidyverse.org/reference/annotation_raster.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Annotation: high-performance rectangular tiling
===============================================

Source: [`R/annotation-raster.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/annotation-raster.R)

`annotation_raster.Rd`

This is a special version of `[geom_raster()](https://ggplot2.tidyverse.org/reference/geom_tile.html) ` optimised for static annotations that are the same in every panel. These annotations will not affect scales (i.e. the x and y axes will not grow to cover the range of the raster, and the raster must already have its own colours). This is useful for adding bitmap images.

Usage[](https://ggplot2.tidyverse.org/reference/annotation_raster.html#ref-usage)

----------------------------------------------------------------------------------

    annotation_raster(raster, xmin, xmax, ymin, ymax, interpolate = FALSE)

Arguments[](https://ggplot2.tidyverse.org/reference/annotation_raster.html#arguments)

--------------------------------------------------------------------------------------

raster[](https://ggplot2.tidyverse.org/reference/annotation_raster.html#arg-raster)

raster object to display, may be an `array` or a `nativeRaster`

xmin, xmax[](https://ggplot2.tidyverse.org/reference/annotation_raster.html#arg-xmin-xmax)

x location (in data coordinates) giving horizontal location of raster

ymin, ymax[](https://ggplot2.tidyverse.org/reference/annotation_raster.html#arg-ymin-ymax)

y location (in data coordinates) giving vertical location of raster

interpolate[](https://ggplot2.tidyverse.org/reference/annotation_raster.html#arg-interpolate)

If `TRUE` interpolate linearly, if `FALSE` (the default) don't interpolate.

Examples[](https://ggplot2.tidyverse.org/reference/annotation_raster.html#ref-examples)

----------------------------------------------------------------------------------------

    # Generate data
    rainbow <- matrix(hcl(seq(0, 360, length.out = 50 * 50), 80, 70), nrow = 50)
    ggplot(mtcars, aes(mpg, wt)) +
      geom_point() +
      annotation_raster(rainbow, 15, 20, 3, 4)
    
    # To fill up whole plot
    ggplot(mtcars, aes(mpg, wt)) +
      annotation_raster(rainbow, -Inf, Inf, -Inf, Inf) +
      geom_point()
    
    
    rainbow2 <- matrix(hcl(seq(0, 360, length.out = 10), 80, 70), nrow = 1)
    ggplot(mtcars, aes(mpg, wt)) +
      annotation_raster(rainbow2, -Inf, Inf, -Inf, Inf) +
      geom_point()
    
    rainbow2 <- matrix(hcl(seq(0, 360, length.out = 10), 80, 70), nrow = 1)
    ggplot(mtcars, aes(mpg, wt)) +
      annotation_raster(rainbow2, -Inf, Inf, -Inf, Inf, interpolate = TRUE) +
      geom_point()