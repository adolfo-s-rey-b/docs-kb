[Skip to content](https://dplyr.tidyverse.org/reference/ident.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Flag a character vector as SQL identifiers
==========================================

Source: [`R/compat-dbplyr.R`](https://github.com/tidyverse/dplyr/blob/main/R/compat-dbplyr.R)

`ident.Rd`

`ident()` takes strings and turns them as database identifiers (e.g. table or column names) quoting them using the identifer rules for your database. `ident_q()` does the same, but assumes the names have already been quoted, preventing them from being quoted again.

These are generally for internal use only; if you need to supply an table name that is qualified with schema or catalog, or has already been quoted for some other reason, use `[I()](https://rdrr.io/r/base/AsIs.html) `.

Usage[](https://dplyr.tidyverse.org/reference/ident.html#ref-usage)

--------------------------------------------------------------------

    ident(...)

Arguments[](https://dplyr.tidyverse.org/reference/ident.html#arguments)

------------------------------------------------------------------------

...[](https://dplyr.tidyverse.org/reference/ident.html#arg--)

A character vector, or name-value pairs.

Examples[](https://dplyr.tidyverse.org/reference/ident.html#ref-examples)

--------------------------------------------------------------------------

    # Identifiers are escaped with "
    ident("x")
    #> <IDENT> x