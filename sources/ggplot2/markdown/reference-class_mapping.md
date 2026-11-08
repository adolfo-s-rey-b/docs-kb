[Skip to content](https://ggplot2.tidyverse.org/reference/class_mapping.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

The mapping class
=================

Source: [`R/all-classes.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/all-classes.R)

`class_mapping.Rd`

The mapping class holds a list of quoted expressions ([quosures](https://rlang.r-lib.org/reference/topic-quosure.html)
) or constants. An object is typically constructed using the `[aes()](https://ggplot2.tidyverse.org/reference/aes.html) ` function.

Usage[](https://ggplot2.tidyverse.org/reference/class_mapping.html#ref-usage)

------------------------------------------------------------------------------

    class_mapping(x = list(), ..., env = globalenv())

Arguments[](https://ggplot2.tidyverse.org/reference/class_mapping.html#arguments)

----------------------------------------------------------------------------------

x[](https://ggplot2.tidyverse.org/reference/class_mapping.html#arg-x)

A list of quosures and constants.

...[](https://ggplot2.tidyverse.org/reference/class_mapping.html#arg--)

Reserved for future expansion.

env[](https://ggplot2.tidyverse.org/reference/class_mapping.html#arg-env)

An environment for symbols that are not quosures or constants.