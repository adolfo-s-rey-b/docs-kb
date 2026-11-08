[Skip to content](https://dplyr.tidyverse.org/reference/copy_to.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Copy a local data frame to a remote src
=======================================

Source: [`R/copy-to.R`](https://github.com/tidyverse/dplyr/blob/main/R/copy-to.R)

`copy_to.Rd`

This function uploads a local data frame into a remote data source, creating the table definition as needed. Wherever possible, the new object will be temporary, limited to the current connection to the source.

Usage[](https://dplyr.tidyverse.org/reference/copy_to.html#ref-usage)

----------------------------------------------------------------------

    copy_to(dest, df, name = deparse(substitute(df)), overwrite = FALSE, ...)

Arguments[](https://dplyr.tidyverse.org/reference/copy_to.html#arguments)

--------------------------------------------------------------------------

dest[](https://dplyr.tidyverse.org/reference/copy_to.html#arg-dest)

remote data source

df[](https://dplyr.tidyverse.org/reference/copy_to.html#arg-df)

local data frame

name[](https://dplyr.tidyverse.org/reference/copy_to.html#arg-name)

name for new remote table.

overwrite[](https://dplyr.tidyverse.org/reference/copy_to.html#arg-overwrite)

If `TRUE`, will overwrite an existing table with name `name`. If `FALSE`, will throw an error if `name` already exists.

...[](https://dplyr.tidyverse.org/reference/copy_to.html#arg--)

other parameters passed to methods.

Value[](https://dplyr.tidyverse.org/reference/copy_to.html#value)

------------------------------------------------------------------

a `tbl` object in the remote source

Methods[](https://dplyr.tidyverse.org/reference/copy_to.html#methods)

----------------------------------------------------------------------

This function is a **generic**, which means that packages can provide implementations (methods) for other classes. See the documentation of individual methods for extra arguments and differences in behaviour.

The following methods are currently available in loaded packages: dbplyr (`[src_sql](https://dbplyr.tidyverse.org/reference/copy_to.src_sql.html) `), dplyr (`DBIConnection`) .

See also[](https://dplyr.tidyverse.org/reference/copy_to.html#see-also)

------------------------------------------------------------------------

`[collect()](https://dplyr.tidyverse.org/reference/compute.html) ` for the opposite action; downloading remote data into a local dbl.

Examples[](https://dplyr.tidyverse.org/reference/copy_to.html#ref-examples)

----------------------------------------------------------------------------

    if (FALSE) { # \dontrun{
    iris2 <- dbplyr::src_memdb() |> copy_to(iris, overwrite = TRUE)
    iris2
    } # }