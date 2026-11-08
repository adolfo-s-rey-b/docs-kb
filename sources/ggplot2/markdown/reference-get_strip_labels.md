[Skip to content](https://ggplot2.tidyverse.org/reference/get_strip_labels.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Accessing a plot's facet strip labels
=====================================

Source: [`R/facet-.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/facet-.R)

`get_strip_labels.Rd`

This functions retrieves labels from facet strips with the labeller applied.

Usage[](https://ggplot2.tidyverse.org/reference/get_strip_labels.html#ref-usage)

---------------------------------------------------------------------------------

    get_strip_labels(plot = get_last_plot())

Arguments[](https://ggplot2.tidyverse.org/reference/get_strip_labels.html#arguments)

-------------------------------------------------------------------------------------

plot[](https://ggplot2.tidyverse.org/reference/get_strip_labels.html#arg-plot)

A ggplot or build ggplot object.

Value[](https://ggplot2.tidyverse.org/reference/get_strip_labels.html#value)

-----------------------------------------------------------------------------

`NULL` if there are no labels, otherwise a list of data.frames containing the labels.

Examples[](https://ggplot2.tidyverse.org/reference/get_strip_labels.html#ref-examples)

---------------------------------------------------------------------------------------

    # Basic plot
    p <- ggplot(mpg, aes(displ, hwy)) +
      geom_point()
    
    get_strip_labels(p) # empty facets
    #> NULL
    get_strip_labels(p + facet_wrap(year ~ cyl))
    #> $facets
    #>   year cyl
    #> 1 1999   4
    #> 2 1999   6
    #> 3 1999   8
    #> 4 2008   4
    #> 5 2008   5
    #> 6 2008   6
    #> 7 2008   8
    #> 
    get_strip_labels(p + facet_grid(year ~ cyl))
    #> $cols
    #>   cyl
    #> 1   4
    #> 2   5
    #> 3   6
    #> 4   8
    #> 
    #> $rows
    #>   year
    #> 1 1999
    #> 2 2008
    #>