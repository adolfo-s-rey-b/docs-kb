[Skip to content](https://ggplot2.tidyverse.org/reference/is_tests.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Reports wether `x` is a type of object
======================================

Source: [`R/ggproto.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/ggproto.R)
, [`R/aes.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/aes.R)
, [`R/geom-.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/geom-.R)
, and 12 more

`is_tests.Rd`

Reports wether `x` is a type of object

Usage[](https://ggplot2.tidyverse.org/reference/is_tests.html#ref-usage)

-------------------------------------------------------------------------

    is_ggproto(x)
    
    is.ggproto(x) # Deprecated
    
    is_mapping(x)
    
    is_geom(x)
    
    is_layer(x)
    
    is_coord(x)
    
    is.Coord(x) # Deprecated
    
    is_facet(x)
    
    is.facet(x) # Deprecated
    
    is_stat(x)
    
    is_margin(x)
    
    is_theme_element(x, type = "any")
    
    is_guide(x)
    
    is_guides(x)
    
    is_ggplot(x)
    
    is.ggplot(x) # Deprecated
    
    is_position(x)
    
    is_scale(x)
    
    is_theme(x)
    
    is.theme(x) # Deprecated

Arguments[](https://ggplot2.tidyverse.org/reference/is_tests.html#arguments)

-----------------------------------------------------------------------------

x[](https://ggplot2.tidyverse.org/reference/is_tests.html#arg-x)

An object to test

type[](https://ggplot2.tidyverse.org/reference/is_tests.html#arg-type)

For testing elements: the type of element to expect. One of `"blank"`, `"rect"`, `"line"`, `"text"`, `"polygon"`, `"point"` or `"geom"`.