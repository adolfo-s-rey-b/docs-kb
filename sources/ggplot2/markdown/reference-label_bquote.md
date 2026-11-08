[Skip to content](https://ggplot2.tidyverse.org/reference/label_bquote.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Label with mathematical expressions
===================================

Source: [`R/labeller.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/labeller.R)

`label_bquote.Rd`

`label_bquote()` offers a flexible way of labelling facet rows or columns with plotmath expressions. Backquoted variables will be replaced with their value in the facet.

Usage[](https://ggplot2.tidyverse.org/reference/label_bquote.html#ref-usage)

-----------------------------------------------------------------------------

    label_bquote(rows = NULL, cols = NULL, default)

Arguments[](https://ggplot2.tidyverse.org/reference/label_bquote.html#arguments)

---------------------------------------------------------------------------------

rows[](https://ggplot2.tidyverse.org/reference/label_bquote.html#arg-rows)

Backquoted labelling expression for rows.

cols[](https://ggplot2.tidyverse.org/reference/label_bquote.html#arg-cols)

Backquoted labelling expression for columns.

default[](https://ggplot2.tidyverse.org/reference/label_bquote.html#arg-default)

Unused, kept for compatibility.

See also[](https://ggplot2.tidyverse.org/reference/label_bquote.html#see-also)

-------------------------------------------------------------------------------

[labellers](https://ggplot2.tidyverse.org/reference/labellers.html)
, `[labeller()](https://ggplot2.tidyverse.org/reference/labeller.html) `,

Examples[](https://ggplot2.tidyverse.org/reference/label_bquote.html#ref-examples)

-----------------------------------------------------------------------------------

    # The variables mentioned in the plotmath expression must be
    # backquoted and referred to by their names.
    p <- ggplot(mtcars, aes(wt, mpg)) + geom_point()
    p + facet_grid(vs ~ ., labeller = label_bquote(alpha ^ .(vs)))
    
    p + facet_grid(. ~ vs, labeller = label_bquote(cols = .(vs) ^ .(vs)))
    
    p + facet_grid(. ~ vs + am, labeller = label_bquote(cols = .(am) ^ .(vs)))