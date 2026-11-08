[Skip to content](https://ggplot2.tidyverse.org/reference/new_guide.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Guide constructor
=================

Source: [`R/guide-.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/guide-.R)

`new_guide.Rd`

A constructor function for guides, which performs some standard compatibility checks between the guide and provided arguments.

Usage[](https://ggplot2.tidyverse.org/reference/new_guide.html#ref-usage)

--------------------------------------------------------------------------

    new_guide(..., available_aes = "any", super)

Arguments[](https://ggplot2.tidyverse.org/reference/new_guide.html#arguments)

------------------------------------------------------------------------------

...[](https://ggplot2.tidyverse.org/reference/new_guide.html#arg--)

Named arguments that match the parameters of `super$params` or the theme elements in `super$elements`.

available\_aes[](https://ggplot2.tidyverse.org/reference/new_guide.html#arg-available-aes)

A vector of character strings listing the aesthetics for which the guide can be drawn.

super[](https://ggplot2.tidyverse.org/reference/new_guide.html#arg-super)

The super class to use for the constructed guide. Should be a Guide class object.

Value[](https://ggplot2.tidyverse.org/reference/new_guide.html#value)

----------------------------------------------------------------------

A `Guide` ggproto object.