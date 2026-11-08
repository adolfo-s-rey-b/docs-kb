[Skip to content](https://ggplot2.tidyverse.org/reference/class_theme.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

The theme class
===============

Source: [`R/all-classes.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/all-classes.R)

`class_theme.Rd`

The theme class holds information on how non-data elements of the plot should be rendered. The preferred way to construct an object of this class is through the `[theme()](https://ggplot2.tidyverse.org/reference/theme.html) ` function.

Usage[](https://ggplot2.tidyverse.org/reference/class_theme.html#ref-usage)

----------------------------------------------------------------------------

    class_theme(elements = list(), ..., complete = FALSE, validate = TRUE)

Arguments[](https://ggplot2.tidyverse.org/reference/class_theme.html#arguments)

--------------------------------------------------------------------------------

elements[](https://ggplot2.tidyverse.org/reference/class_theme.html#arg-elements)

A named list containing theme elements.

...[](https://ggplot2.tidyverse.org/reference/class_theme.html#arg--)

Reserved for future expansion.

complete[](https://ggplot2.tidyverse.org/reference/class_theme.html#arg-complete)

A boolean value stating whether a theme is complete.

validate[](https://ggplot2.tidyverse.org/reference/class_theme.html#arg-validate)

A boolean value stating whether a theme should still be validated.