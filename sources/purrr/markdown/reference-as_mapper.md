[Skip to content](https://purrr.tidyverse.org/reference/as_mapper.html#container)

![](https://purrr.tidyverse.org/logo.png)

Convert an object into a mapper function
========================================

Source: [`R/map-mapper.R`](https://github.com/tidyverse/purrr/blob/main/R/map-mapper.R)

`as_mapper.Rd`

`as_mapper` is the powerhouse behind the varied function specifications that most purrr functions allow. It is an S3 generic. The default method forwards its arguments to `[rlang::as_function()](https://rlang.r-lib.org/reference/as_function.html) `.

Usage[](https://purrr.tidyverse.org/reference/as_mapper.html#ref-usage)

------------------------------------------------------------------------

    as_mapper(.f, ...)
    
    # S3 method for class 'character'
    as_mapper(.f, ..., .null, .default = NULL)
    
    # S3 method for class 'numeric'
    as_mapper(.f, ..., .null, .default = NULL)
    
    # S3 method for class 'list'
    as_mapper(.f, ..., .null, .default = NULL)

Arguments[](https://purrr.tidyverse.org/reference/as_mapper.html#arguments)

----------------------------------------------------------------------------

.f[](https://purrr.tidyverse.org/reference/as_mapper.html#arg--f)

A function, formula, or vector (not necessarily atomic).

If a **function**, it is used as is.

If a **formula**, e.g. `~ .x + 2`, it is converted to a function. No longer recommended.

If **character vector**, **numeric vector**, or **list**, it is converted to an extractor function. Character vectors index by name and numeric vectors index by position; use a list to index by position and name at different levels. If a component is not present, the value of `.default` will be returned.

...[](https://purrr.tidyverse.org/reference/as_mapper.html#arg--)

Additional arguments passed on to methods.

.default, .null[](https://purrr.tidyverse.org/reference/as_mapper.html#arg--default-null)

Optional additional argument for extractor functions (i.e. when `.f` is character, integer, or list). Returned when value is absent (does not exist) or empty (has length 0). `.null` is deprecated; please use `.default` instead.

Examples[](https://purrr.tidyverse.org/reference/as_mapper.html#ref-examples)

------------------------------------------------------------------------------

    as_mapper(\(x) x + 1)
    #> function (x) 
    #> x + 1
    #> <environment: 0x55d4dcdca8e0>
    as_mapper(1)
    #> function (x, ...) 
    #> pluck_raw(x, list(1), .default = NULL)
    #> <environment: 0x55d4dcdfb028>
    
    as_mapper(c("a", "b", "c"))
    #> function (x, ...) 
    #> pluck_raw(x, list("a", "b", "c"), .default = NULL)
    #> <environment: 0x55d4dce2e420>
    # Equivalent to function(x) x[["a"]][["b"]][["c"]]
    
    as_mapper(list(1, "a", 2))
    #> function (x, ...) 
    #> pluck_raw(x, list(1, "a", 2), .default = NULL)
    #> <environment: 0x55d4dce67c88>
    # Equivalent to function(x) x[[1]][["a"]][[2]]
    
    as_mapper(list(1, attr_getter("a")))
    #> function (x, ...) 
    #> pluck_raw(x, list(1, function (x) 
    #> attr(x, attr, exact = TRUE)), .default = NULL)
    #> <environment: 0x55d4dcea5528>
    # Equivalent to function(x) attr(x[[1]], "a")
    
    as_mapper(c("a", "b", "c"), .default = NA)
    #> function (x, ...) 
    #> pluck_raw(x, list("a", "b", "c"), .default = NA)
    #> <environment: 0x55d4dcee1c38>