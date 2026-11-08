[Skip to content](https://purrr.tidyverse.org/reference/map_raw.html#container)

![](https://purrr.tidyverse.org/logo.png)

Functions that return raw vectors
=================================

Source: [`R/map-raw.R`](https://github.com/tidyverse/purrr/blob/main/R/map-raw.R)

`map_raw.Rd`

[![[Deprecated]](https://purrr.tidyverse.org/reference/figures/lifecycle-deprecated.svg)](https://lifecycle.r-lib.org/articles/stages.html#deprecated)

These functions were deprecated in purrr 1.0.0 because they are of limited use and you can now use `[map_vec()](https://purrr.tidyverse.org/reference/map.html) ` instead. They are variants of `[map()](https://purrr.tidyverse.org/reference/map.html) `, `[map2()](https://purrr.tidyverse.org/reference/map2.html) `, `[imap()](https://purrr.tidyverse.org/reference/imap.html) `, `[pmap()](https://purrr.tidyverse.org/reference/pmap.html) `, and `[flatten()](https://purrr.tidyverse.org/reference/flatten.html) ` that return raw vectors.

Usage[](https://purrr.tidyverse.org/reference/map_raw.html#ref-usage)

----------------------------------------------------------------------

    map_raw(.x, .f, ...)
    
    map2_raw(.x, .y, .f, ...)
    
    imap_raw(.x, .f, ...)
    
    pmap_raw(.l, .f, ...)
    
    flatten_raw(.x)