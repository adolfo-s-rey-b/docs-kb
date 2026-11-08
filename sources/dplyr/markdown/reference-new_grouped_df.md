[Skip to content](https://dplyr.tidyverse.org/reference/new_grouped_df.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Low-level construction and validation for the grouped\_df and rowwise\_df classes
=================================================================================

Source: [`R/grouped-df.R`](https://github.com/tidyverse/dplyr/blob/main/R/grouped-df.R)
, [`R/rowwise.R`](https://github.com/tidyverse/dplyr/blob/main/R/rowwise.R)

`new_grouped_df.Rd`

`new_grouped_df()` and `new_rowwise_df()` are constructors designed to be high-performance so only check types, not values. This means it is the caller's responsibility to create valid values, and hence this is for expert use only.

`validate_grouped_df()` and `validate_rowwise_df()` validate the attributes of a `grouped_df` or a `rowwise_df`.

Usage[](https://dplyr.tidyverse.org/reference/new_grouped_df.html#ref-usage)

-----------------------------------------------------------------------------

    new_grouped_df(x, groups, ..., class = character())
    
    validate_grouped_df(x, check_bounds = FALSE)
    
    new_rowwise_df(data, group_data = NULL, ..., class = character())
    
    validate_rowwise_df(x)

Arguments[](https://dplyr.tidyverse.org/reference/new_grouped_df.html#arguments)

---------------------------------------------------------------------------------

x[](https://dplyr.tidyverse.org/reference/new_grouped_df.html#arg-x)

A data frame

groups[](https://dplyr.tidyverse.org/reference/new_grouped_df.html#arg-groups)

The grouped structure, `groups` should be a data frame. Its last column should be called `.rows` and be a list of 1 based integer vectors that all are between 1 and the number of rows of `.data`.

...[](https://dplyr.tidyverse.org/reference/new_grouped_df.html#arg--)

additional attributes

class[](https://dplyr.tidyverse.org/reference/new_grouped_df.html#arg-class)

additional class, will be prepended to canonical classes.

check\_bounds[](https://dplyr.tidyverse.org/reference/new_grouped_df.html#arg-check-bounds)

whether to check all indices for out of bounds problems in `grouped_df` objects

Examples[](https://dplyr.tidyverse.org/reference/new_grouped_df.html#ref-examples)

-----------------------------------------------------------------------------------

    # 5 bootstrap samples
    tbl <- new_grouped_df(
      tibble(x = rnorm(10)),
      groups = tibble(".rows" := replicate(5, sample(1:10, replace = TRUE), simplify = FALSE))
    )
    # mean of each bootstrap sample
    summarise(tbl, x = mean(x))
    #> # A tibble: 5 × 1
    #>          x
    #>      <dbl>
    #> 1  0.177  
    #> 2  0.0262 
    #> 3  0.103  
    #> 4  0.202  
    #> 5 -0.00267