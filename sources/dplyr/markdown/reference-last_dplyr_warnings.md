[Skip to content](https://dplyr.tidyverse.org/reference/last_dplyr_warnings.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Show warnings from the last command
===================================

Source: [`R/conditions.R`](https://github.com/tidyverse/dplyr/blob/main/R/conditions.R)

`last_dplyr_warnings.Rd`

Warnings that occur inside a dplyr verb like `[mutate()](https://dplyr.tidyverse.org/reference/mutate.html) ` are caught and stashed away instead of being emitted to the console. This prevents rowwise and grouped data frames from flooding the console with warnings. To see the original warnings, use `last_dplyr_warnings()`.

Usage[](https://dplyr.tidyverse.org/reference/last_dplyr_warnings.html#ref-usage)

----------------------------------------------------------------------------------

    last_dplyr_warnings(n = 5)

Arguments[](https://dplyr.tidyverse.org/reference/last_dplyr_warnings.html#arguments)

--------------------------------------------------------------------------------------

n[](https://dplyr.tidyverse.org/reference/last_dplyr_warnings.html#arg-n)

Passed to `[head()](https://rdrr.io/r/utils/head.html) ` so that only the first `n` warnings are displayed.