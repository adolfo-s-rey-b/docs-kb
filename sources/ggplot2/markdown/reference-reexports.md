[Skip to content](https://ggplot2.tidyverse.org/reference/reexports.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Objects exported from other packages
====================================

Source: [`R/utilities.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/utilities.R)
, [`R/utilities-grid.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/utilities-grid.R)

`reexports.Rd`

These objects are imported from other packages. Follow the links below to see their documentation.

grid

`[arrow](https://rdrr.io/r/grid/arrow.html) `, `[unit](https://rdrr.io/r/grid/unit.html) `

scales

`[alpha](https://scales.r-lib.org/reference/alpha.html) `

Examples[](https://ggplot2.tidyverse.org/reference/reexports.html#ref-examples)

--------------------------------------------------------------------------------

    ggplot(mpg, aes(displ, hwy)) +
      geom_point(alpha = 0.5, colour = "blue")
    
    
    ggplot(mpg, aes(displ, hwy)) +
      geom_point(colour = alpha("blue", 0.5))