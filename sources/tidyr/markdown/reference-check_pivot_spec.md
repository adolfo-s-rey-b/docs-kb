[Skip to content](https://tidyr.tidyverse.org/reference/check_pivot_spec.html#container)

![](https://tidyr.tidyverse.org/logo.png)

Check assumptions about a pivot `spec`
======================================

Source: [`R/pivot.R`](https://github.com/tidyverse/tidyr/blob/main/R/pivot.R)

`check_pivot_spec.Rd`

`check_pivot_spec()` is a developer facing helper function for validating the pivot spec used in `[pivot_longer_spec()](https://tidyr.tidyverse.org/reference/pivot_longer_spec.html) ` or `[pivot_wider_spec()](https://tidyr.tidyverse.org/reference/pivot_wider_spec.html) `. It is only useful if you are extending `[pivot_longer()](https://tidyr.tidyverse.org/reference/pivot_longer.html) ` or `[pivot_wider()](https://tidyr.tidyverse.org/reference/pivot_wider.html) ` with new S3 methods.

`check_pivot_spec()` makes the following assertions:

*   `spec` must be a data frame.
    
*   `spec` must have a character column named `.name`.
    
*   `spec` must have a character column named `.value`.
    
*   The `.name` column must be unique.
    
*   The `.name` and `.value` columns must be the first two columns in the data frame, and will be reordered if that is not true.
    

Usage[](https://tidyr.tidyverse.org/reference/check_pivot_spec.html#ref-usage)

-------------------------------------------------------------------------------

    check_pivot_spec(spec, call = caller_env())

Arguments[](https://tidyr.tidyverse.org/reference/check_pivot_spec.html#arguments)

-----------------------------------------------------------------------------------

spec[](https://tidyr.tidyverse.org/reference/check_pivot_spec.html#arg-spec)

A specification data frame. This is useful for more complex pivots because it gives you greater control on how metadata stored in the columns become column names in the result.

Must be a data frame containing character `.name` and `.value` columns. Additional columns in `spec` should be named to match columns in the long format of the dataset and contain values corresponding to columns pivoted from the wide format. The special `.seq` variable is used to disambiguate rows internally; it is automatically removed after pivoting.

Examples[](https://tidyr.tidyverse.org/reference/check_pivot_spec.html#ref-examples)

-------------------------------------------------------------------------------------

    # A valid spec
    spec <- tibble(.name = "a", .value = "b", foo = 1)
    check_pivot_spec(spec)
    #> # A tibble: 1 × 3
    #>   .name .value   foo
    #>   <chr> <chr>  <dbl>
    #> 1 a     b          1
    
    spec <- tibble(.name = "a")
    try(check_pivot_spec(spec))
    #> Error in eval(expr, envir) : 
    #>   `spec` must have `.name` and `.value` columns.
    
    # `.name` and `.value` are forced to be the first two columns
    spec <- tibble(foo = 1, .value = "b", .name = "a")
    check_pivot_spec(spec)
    #> # A tibble: 1 × 3
    #>   .name .value   foo
    #>   <chr> <chr>  <dbl>
    #> 1 a     b          1