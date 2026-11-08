[Skip to content](https://tidyr.tidyverse.org/reference/unnest_auto.html#container)

![](https://tidyr.tidyverse.org/logo.png)

Automatically call `unnest_wider()` or `unnest_longer()`
========================================================

Source: [`R/unnest-auto.R`](https://github.com/tidyverse/tidyr/blob/main/R/unnest-auto.R)

`unnest_auto.Rd`

`unnest_auto()` picks between `[unnest_wider()](https://tidyr.tidyverse.org/reference/unnest_wider.html) ` or `[unnest_longer()](https://tidyr.tidyverse.org/reference/unnest_longer.html) ` by inspecting the inner names of the list-col:

*   If all elements are unnamed, it uses `unnest_longer(indices_include = FALSE)`.
    
*   If all elements are named, and there's at least one name in common across all components, it uses `[unnest_wider()](https://tidyr.tidyverse.org/reference/unnest_wider.html) `.
    
*   Otherwise, it falls back to `unnest_longer(indices_include = TRUE)`.
    

It's handy for very rapid interactive exploration but I don't recommend using it in scripts, because it will succeed even if the underlying data radically changes.

Usage[](https://tidyr.tidyverse.org/reference/unnest_auto.html#ref-usage)

--------------------------------------------------------------------------

    unnest_auto(data, col)

Arguments[](https://tidyr.tidyverse.org/reference/unnest_auto.html#arguments)

------------------------------------------------------------------------------

data[](https://tidyr.tidyverse.org/reference/unnest_auto.html#arg-data)

A data frame.

col[](https://tidyr.tidyverse.org/reference/unnest_auto.html#arg-col)

<`[tidy-select](https://tidyr.tidyverse.org/reference/tidyr_tidy_select.html) `\> List-column to unnest.