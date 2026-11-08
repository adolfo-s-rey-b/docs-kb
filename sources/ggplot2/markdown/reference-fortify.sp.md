[Skip to content](https://ggplot2.tidyverse.org/reference/fortify.sp.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Fortify method for classes from the sp package.
===============================================

Source: [`R/fortify-spatial.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/fortify-spatial.R)

`fortify.sp.Rd`

[![[Deprecated]](https://ggplot2.tidyverse.org/reference/figures/lifecycle-deprecated.svg)](https://lifecycle.r-lib.org/articles/stages.html#deprecated)

To figure out the correct variable name for region, inspect `as.data.frame(model)`.

Usage[](https://ggplot2.tidyverse.org/reference/fortify.sp.html#ref-usage)

---------------------------------------------------------------------------

    # S3 method for class 'SpatialPolygonsDataFrame'
    fortify(model, data, region = NULL, ...)
    
    # S3 method for class 'SpatialPolygons'
    fortify(model, data, ...)
    
    # S3 method for class 'Polygons'
    fortify(model, data, ...)
    
    # S3 method for class 'Polygon'
    fortify(model, data, ...)
    
    # S3 method for class 'SpatialLinesDataFrame'
    fortify(model, data, ...)
    
    # S3 method for class 'Lines'
    fortify(model, data, ...)
    
    # S3 method for class 'Line'
    fortify(model, data, ...)

Arguments[](https://ggplot2.tidyverse.org/reference/fortify.sp.html#arguments)

-------------------------------------------------------------------------------

model[](https://ggplot2.tidyverse.org/reference/fortify.sp.html#arg-model)

`SpatialPolygonsDataFrame` to convert into a dataframe.

data[](https://ggplot2.tidyverse.org/reference/fortify.sp.html#arg-data)

not used by this method

region[](https://ggplot2.tidyverse.org/reference/fortify.sp.html#arg-region)

name of variable used to split up regions

...[](https://ggplot2.tidyverse.org/reference/fortify.sp.html#arg--)

not used by this method