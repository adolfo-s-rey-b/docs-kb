[Skip to content](https://ggplot2.tidyverse.org/reference/position_nudge.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Nudge points a fixed distance
=============================

Source: [`R/position-nudge.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/position-nudge.R)

`position_nudge.Rd`

`position_nudge()` is generally useful for adjusting the position of items on discrete scales by a small amount. Nudging is built in to `[geom_text()](https://ggplot2.tidyverse.org/reference/geom_text.html) ` because it's so useful for moving labels a small distance from what they're labelling.

Usage[](https://ggplot2.tidyverse.org/reference/position_nudge.html#ref-usage)

-------------------------------------------------------------------------------

    position_nudge(x = NULL, y = NULL)

Arguments[](https://ggplot2.tidyverse.org/reference/position_nudge.html#arguments)

-----------------------------------------------------------------------------------

x, y[](https://ggplot2.tidyverse.org/reference/position_nudge.html#arg-x-y)

Amount of vertical and horizontal distance to move.

See also[](https://ggplot2.tidyverse.org/reference/position_nudge.html#see-also)

---------------------------------------------------------------------------------

Other position adjustments: `[position_dodge()](https://ggplot2.tidyverse.org/reference/position_dodge.html) `, `[position_identity()](https://ggplot2.tidyverse.org/reference/position_identity.html) `, `[position_jitter()](https://ggplot2.tidyverse.org/reference/position_jitter.html) `, `[position_jitterdodge()](https://ggplot2.tidyverse.org/reference/position_jitterdodge.html) `, `[position_stack()](https://ggplot2.tidyverse.org/reference/position_stack.html) `

Aesthetics[](https://ggplot2.tidyverse.org/reference/position_nudge.html#aesthetics)

-------------------------------------------------------------------------------------

`position_nudge()` understands the following aesthetics. Required aesthetics are displayed in bold and defaults are displayed for optional aesthetics:

|     |     |     |
| --- | --- | --- |
| •   | `nudge_x` | → `0` |
| •   | `nudge_y` | → `0` |

Learn more about setting these aesthetics in `[vignette("ggplot2-specs")](https://ggplot2.tidyverse.org/articles/ggplot2-specs.html) `.

Examples[](https://ggplot2.tidyverse.org/reference/position_nudge.html#ref-examples)

-------------------------------------------------------------------------------------

    df <- data.frame(
      x = c(1,3,2,5),
      y = c("a","c","d","c")
    )
    
    ggplot(df, aes(x, y)) +
      geom_point() +
      geom_text(aes(label = y))
    
    
    ggplot(df, aes(x, y)) +
      geom_point() +
      geom_text(aes(label = y), position = position_nudge(y = -0.1))
    
    
    # Or, in brief
    ggplot(df, aes(x, y)) +
      geom_point() +
      geom_text(aes(label = y), nudge_y = -0.1)
    
    
    # For each text individually
    ggplot(df, aes(x, y)) +
      geom_point() +
      geom_text(aes(label = y, nudge_y = c(-0.1, 0.1, -0.1, 0.1)))