[Skip to content](https://ggplot2.tidyverse.org/reference/expansion.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Generate expansion vector for scales
====================================

Source: [`R/scale-expansion.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/scale-expansion.R)

`expansion.Rd`

This is a convenience function for generating scale expansion vectors for the `expand` argument of [scale\_(x|y)\_continuous](https://ggplot2.tidyverse.org/reference/scale_continuous.html)
 and [scale\_(x|y)\_discrete](https://ggplot2.tidyverse.org/reference/scale_discrete.html)
. The expansion vectors are used to add some space between the data and the axes.

Usage[](https://ggplot2.tidyverse.org/reference/expansion.html#ref-usage)

--------------------------------------------------------------------------

    expansion(mult = 0, add = 0)
    
    expand_scale(mult = 0, add = 0)

Arguments[](https://ggplot2.tidyverse.org/reference/expansion.html#arguments)

------------------------------------------------------------------------------

mult[](https://ggplot2.tidyverse.org/reference/expansion.html#arg-mult)

vector of multiplicative range expansion factors. If length 1, both the lower and upper limits of the scale are expanded outwards by `mult`. If length 2, the lower limit is expanded by `mult[1]` and the upper limit by `mult[2]`.

add[](https://ggplot2.tidyverse.org/reference/expansion.html#arg-add)

vector of additive range expansion constants. If length 1, both the lower and upper limits of the scale are expanded outwards by `add` units. If length 2, the lower limit is expanded by `add[1]` and the upper limit by `add[2]`.

Examples[](https://ggplot2.tidyverse.org/reference/expansion.html#ref-examples)

--------------------------------------------------------------------------------

    # No space below the bars but 10% above them
    ggplot(mtcars) +
      geom_bar(aes(x = factor(cyl))) +
      scale_y_continuous(expand = expansion(mult = c(0, .1)))
    
    
    # Add 2 units of space on the left and right of the data
    ggplot(subset(diamonds, carat > 2), aes(cut, clarity)) +
      geom_jitter() +
      scale_x_discrete(expand = expansion(add = 2))
    
    
    # Reproduce the default range expansion used
    # when the 'expand' argument is not specified
    ggplot(subset(diamonds, carat > 2), aes(cut, price)) +
      geom_jitter() +
      scale_x_discrete(expand = expansion(add = .6)) +
      scale_y_continuous(expand = expansion(mult = .05))