[Skip to content](https://ggplot2.tidyverse.org/reference/facet_null.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Facet specification: a single panel.
====================================

Source: [`R/facet-null.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/facet-null.R)

`facet_null.Rd`

Facet specification: a single panel.

Usage[](https://ggplot2.tidyverse.org/reference/facet_null.html#ref-usage)

---------------------------------------------------------------------------

    facet_null(shrink = TRUE)

Arguments[](https://ggplot2.tidyverse.org/reference/facet_null.html#arguments)

-------------------------------------------------------------------------------

shrink[](https://ggplot2.tidyverse.org/reference/facet_null.html#arg-shrink)

If `TRUE`, will shrink scales to fit output of statistics, not raw data. If `FALSE`, will be range of raw data before statistical summary.

Layer layout[](https://ggplot2.tidyverse.org/reference/facet_null.html#layer-layout)

-------------------------------------------------------------------------------------

The `[layer(layout)](https://ggplot2.tidyverse.org/reference/layer.html) ` argument in context of `facet_null()` is completely ignored.

Examples[](https://ggplot2.tidyverse.org/reference/facet_null.html#ref-examples)

---------------------------------------------------------------------------------

    # facet_null is the default faceting specification if you
    # don't override it with facet_grid or facet_wrap
    ggplot(mtcars, aes(mpg, wt)) + geom_point()