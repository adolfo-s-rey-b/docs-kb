[Skip to content](https://ggplot2.tidyverse.org/reference/element_render.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Render a specified theme element into a grob
============================================

Source: [`R/theme-elements.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/theme-elements.R)

`element_render.Rd`

Given a theme object and element name, returns a grob for the element. Uses `[element_grob()](https://ggplot2.tidyverse.org/reference/element_grob.html) ` to generate the grob.

Usage[](https://ggplot2.tidyverse.org/reference/element_render.html#ref-usage)

-------------------------------------------------------------------------------

    element_render(theme, element, ..., name = NULL)

Arguments[](https://ggplot2.tidyverse.org/reference/element_render.html#arguments)

-----------------------------------------------------------------------------------

theme[](https://ggplot2.tidyverse.org/reference/element_render.html#arg-theme)

The theme object

element[](https://ggplot2.tidyverse.org/reference/element_render.html#arg-element)

The element name given as character vector

...[](https://ggplot2.tidyverse.org/reference/element_render.html#arg--)

Other arguments provided to `[element_grob()](https://ggplot2.tidyverse.org/reference/element_grob.html) `

name[](https://ggplot2.tidyverse.org/reference/element_render.html#arg-name)

Character vector added to the name of the grob