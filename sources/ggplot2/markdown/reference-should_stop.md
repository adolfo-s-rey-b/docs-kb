[Skip to content](https://ggplot2.tidyverse.org/reference/should_stop.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Used in examples to illustrate when errors should occur.
========================================================

Source: [`R/utilities.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/utilities.R)

`should_stop.Rd`

Used in examples to illustrate when errors should occur.

Usage[](https://ggplot2.tidyverse.org/reference/should_stop.html#ref-usage)

----------------------------------------------------------------------------

    should_stop(expr)

Arguments[](https://ggplot2.tidyverse.org/reference/should_stop.html#arguments)

--------------------------------------------------------------------------------

expr[](https://ggplot2.tidyverse.org/reference/should_stop.html#arg-expr)

code to evaluate.

Examples[](https://ggplot2.tidyverse.org/reference/should_stop.html#ref-examples)

----------------------------------------------------------------------------------

    should_stop(stop("Hi!"))
    should_stop(should_stop("Hi!"))
    #> [1] "Hi!"