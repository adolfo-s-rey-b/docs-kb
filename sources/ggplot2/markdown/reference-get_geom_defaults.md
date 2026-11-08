[Skip to content](https://ggplot2.tidyverse.org/reference/get_geom_defaults.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Resolve and get geom defaults
=============================

Source: [`R/geom-defaults.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/geom-defaults.R)

`get_geom_defaults.Rd`

Resolve and get geom defaults

Usage[](https://ggplot2.tidyverse.org/reference/get_geom_defaults.html#ref-usage)

----------------------------------------------------------------------------------

    get_geom_defaults(geom, theme = theme_get())

Arguments[](https://ggplot2.tidyverse.org/reference/get_geom_defaults.html#arguments)

--------------------------------------------------------------------------------------

geom[](https://ggplot2.tidyverse.org/reference/get_geom_defaults.html#arg-geom)

Some definition of a geom:

*   A `function` that creates a layer, e.g. `[geom_path()](https://ggplot2.tidyverse.org/reference/geom_path.html) `.
    
*   A layer created by such function
    
*   A string naming a geom class in snake case without the `geom_`\-prefix, e.g. `"contour_filled"`.
    
*   A geom class object.
    

theme[](https://ggplot2.tidyverse.org/reference/get_geom_defaults.html#arg-theme)

A `[theme](https://ggplot2.tidyverse.org/reference/theme.html) ` object. Defaults to the current global theme.

Value[](https://ggplot2.tidyverse.org/reference/get_geom_defaults.html#value)

------------------------------------------------------------------------------

A list of aesthetics

Examples[](https://ggplot2.tidyverse.org/reference/get_geom_defaults.html#ref-examples)

----------------------------------------------------------------------------------------

    # Using a function
    get_geom_defaults(geom_raster)
    #>        fill alpha
    #> 1 #333333FF    NA
    
    # Using a layer includes static aesthetics as default
    get_geom_defaults(geom_tile(fill = "white"))
    #>    fill colour linewidth linetype alpha width height
    #> 1 white     NA       0.2        1    NA     1      1
    
    # Using a class name
    get_geom_defaults("density_2d")
    #>    colour linewidth linetype alpha
    #> 1 #3366FF       0.5        1    NA
    
    # Using a class
    get_geom_defaults(GeomPoint)
    #>   shape colour fill size alpha stroke
    #> 1    19  black   NA  1.5    NA    0.5
    
    # Changed theme
    get_geom_defaults("point", theme(geom = element_geom(ink = "purple")))
    #>   shape colour fill size alpha stroke
    #> 1    19 purple   NA  1.5    NA    0.5