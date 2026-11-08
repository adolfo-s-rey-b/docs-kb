[Skip to content](https://ggplot2.tidyverse.org/reference/fortify.map.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Fortify method for map objects
==============================

Source: [`R/fortify-map.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/fortify-map.R)

`fortify.map.Rd`

[![[Deprecated]](https://ggplot2.tidyverse.org/reference/figures/lifecycle-deprecated.svg)](https://lifecycle.r-lib.org/articles/stages.html#deprecated)

This function turns a map into a data frame that can more easily be plotted with ggplot2.

Usage[](https://ggplot2.tidyverse.org/reference/fortify.map.html#ref-usage)

----------------------------------------------------------------------------

    # S3 method for class 'map'
    fortify(model, data, ...)

Arguments[](https://ggplot2.tidyverse.org/reference/fortify.map.html#arguments)

--------------------------------------------------------------------------------

model[](https://ggplot2.tidyverse.org/reference/fortify.map.html#arg-model)

map object

data[](https://ggplot2.tidyverse.org/reference/fortify.map.html#arg-data)

not used by this method

...[](https://ggplot2.tidyverse.org/reference/fortify.map.html#arg--)

not used by this method

See also[](https://ggplot2.tidyverse.org/reference/fortify.map.html#see-also)

------------------------------------------------------------------------------

`[map_data()](https://ggplot2.tidyverse.org/reference/map_data.html) ` and `[annotation_borders()](https://ggplot2.tidyverse.org/reference/annotation_borders.html) `

Examples[](https://ggplot2.tidyverse.org/reference/fortify.map.html#ref-examples)

----------------------------------------------------------------------------------

    if (require("maps")) {
    ca <- map("county", "ca", plot = FALSE, fill = TRUE)
    head(fortify(ca))
    ggplot(ca, aes(long, lat)) +
      geom_polygon(aes(group = group))
    }
    #> Warning: `fortify(<map>)` was deprecated in ggplot2 4.0.0.
    #> ℹ Please use `map_data()` instead.
    
    
    if (require("maps")) {
    tx <- map("county", "texas", plot = FALSE, fill = TRUE)
    head(fortify(tx))
    ggplot(tx, aes(long, lat)) +
      geom_polygon(aes(group = group), colour = "white")
    }