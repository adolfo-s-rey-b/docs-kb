[Skip to content](https://ggplot2.tidyverse.org/reference/remove_missing.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

Convenience function to remove missing values from a data.frame
===============================================================

Source: [`R/utilities.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/utilities.R)

`remove_missing.Rd`

Remove all non-complete rows, with a warning if `na.rm = FALSE`. ggplot is somewhat more accommodating of missing values than R generally. For those stats which require complete data, missing values will be automatically removed with a warning. If `na.rm = TRUE` is supplied to the statistic, the warning will be suppressed.

Usage[](https://ggplot2.tidyverse.org/reference/remove_missing.html#ref-usage)

-------------------------------------------------------------------------------

    remove_missing(df, na.rm = FALSE, vars = names(df), name = "", finite = FALSE)

Arguments[](https://ggplot2.tidyverse.org/reference/remove_missing.html#arguments)

-----------------------------------------------------------------------------------

df[](https://ggplot2.tidyverse.org/reference/remove_missing.html#arg-df)

data.frame

na.rm[](https://ggplot2.tidyverse.org/reference/remove_missing.html#arg-na-rm)

If true, will suppress warning message.

vars[](https://ggplot2.tidyverse.org/reference/remove_missing.html#arg-vars)

Character vector of variables to check for missings in

name[](https://ggplot2.tidyverse.org/reference/remove_missing.html#arg-name)

Optional function name to improve error message.

finite[](https://ggplot2.tidyverse.org/reference/remove_missing.html#arg-finite)

If `TRUE`, will also remove non-finite values.