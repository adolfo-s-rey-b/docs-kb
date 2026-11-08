[Skip to content](https://tidyr.tidyverse.org/reference/nest_legacy.html#container)

![](https://tidyr.tidyverse.org/logo.png)

Legacy versions of `nest()` and `unnest()`
==========================================

Source: [`R/nest-legacy.R`](https://github.com/tidyverse/tidyr/blob/main/R/nest-legacy.R)

`nest_legacy.Rd`

[![[Superseded]](https://tidyr.tidyverse.org/reference/figures/lifecycle-superseded.svg)](https://lifecycle.r-lib.org/articles/stages.html#superseded)

tidyr 1.0.0 introduced a new syntax for `[nest()](https://tidyr.tidyverse.org/reference/nest.html) ` and `[unnest()](https://tidyr.tidyverse.org/reference/unnest.html) `. The majority of existing usage should be automatically translated to the new syntax with a warning. However, if you need to quickly roll back to the previous behaviour, these functions provide the previous interface. To make old code work as is, add the following code to the top of your script:

    library(tidyr)
    nest <- nest_legacy
    unnest <- unnest_legacy

Usage[](https://tidyr.tidyverse.org/reference/nest_legacy.html#ref-usage)

--------------------------------------------------------------------------

    nest_legacy(data, ..., .key = "data")
    
    unnest_legacy(data, ..., .drop = NA, .id = NULL, .sep = NULL, .preserve = NULL)

Arguments[](https://tidyr.tidyverse.org/reference/nest_legacy.html#arguments)

------------------------------------------------------------------------------

data[](https://tidyr.tidyverse.org/reference/nest_legacy.html#arg-data)

A data frame.

...[](https://tidyr.tidyverse.org/reference/nest_legacy.html#arg--)

Specification of columns to unnest. Use bare variable names or functions of variables. If omitted, defaults to all list-cols.

.key[](https://tidyr.tidyverse.org/reference/nest_legacy.html#arg--key)

The name of the new column, as a string or symbol. This argument is passed by expression and supports [quasiquotation](https://rlang.r-lib.org/reference/topic-inject.html)
 (you can unquote strings and symbols). The name is captured from the expression with `[rlang::ensym()](https://rlang.r-lib.org/reference/defusing-advanced.html) ` (note that this kind of interface where symbols do not represent actual objects is now discouraged in the tidyverse; we support it here for backward compatibility).

.drop[](https://tidyr.tidyverse.org/reference/nest_legacy.html#arg--drop)

Should additional list columns be dropped? By default, `[unnest()](https://tidyr.tidyverse.org/reference/unnest.html) ` will drop them if unnesting the specified columns requires the rows to be duplicated.

.id[](https://tidyr.tidyverse.org/reference/nest_legacy.html#arg--id)

Data frame identifier - if supplied, will create a new column with name `.id`, giving a unique identifier. This is most useful if the list column is named.

.sep[](https://tidyr.tidyverse.org/reference/nest_legacy.html#arg--sep)

If non-`NULL`, the names of unnested data frame columns will combine the name of the original list-col with the names from the nested data frame, separated by `.sep`.

.preserve[](https://tidyr.tidyverse.org/reference/nest_legacy.html#arg--preserve)

Optionally, list-columns to preserve in the output. These will be duplicated in the same way as atomic vectors. This has `[dplyr::select()](https://dplyr.tidyverse.org/reference/select.html) ` semantics so you can preserve multiple variables with `.preserve = c(x, y)` or `.preserve = starts_with("list")`.

Examples[](https://tidyr.tidyverse.org/reference/nest_legacy.html#ref-examples)

--------------------------------------------------------------------------------

    # Nest and unnest are inverses
    df <- tibble(x = c(1, 1, 2), y = 3:1)
    df |> nest_legacy(y)
    #> # A tibble: 2 × 2
    #>       x data            
    #>   <dbl> <list>          
    #> 1     1 <tibble [2 × 1]>
    #> 2     2 <tibble [1 × 1]>
    df |> nest_legacy(y) |> unnest_legacy()
    #> # A tibble: 3 × 2
    #>       x     y
    #>   <dbl> <int>
    #> 1     1     3
    #> 2     1     2
    #> 3     2     1
    
    # nesting -------------------------------------------------------------------
    as_tibble(iris) |> nest_legacy(!Species)
    #> # A tibble: 3 × 2
    #>   Species    data             
    #>   <fct>      <list>           
    #> 1 setosa     <tibble [50 × 4]>
    #> 2 versicolor <tibble [50 × 4]>
    #> 3 virginica  <tibble [50 × 4]>
    as_tibble(chickwts) |> nest_legacy(weight)
    #> # A tibble: 6 × 2
    #>   feed      data             
    #>   <fct>     <list>           
    #> 1 horsebean <tibble [10 × 1]>
    #> 2 linseed   <tibble [12 × 1]>
    #> 3 soybean   <tibble [14 × 1]>
    #> 4 sunflower <tibble [12 × 1]>
    #> 5 meatmeal  <tibble [11 × 1]>
    #> 6 casein    <tibble [12 × 1]>
    
    # unnesting -----------------------------------------------------------------
    df <- tibble(
      x = 1:2,
      y = list(
        tibble(z = 1),
        tibble(z = 3:4)
      )
    )
    df |> unnest_legacy(y)
    #> # A tibble: 3 × 2
    #>       x     z
    #>   <int> <dbl>
    #> 1     1     1
    #> 2     2     3
    #> 3     2     4
    
    # You can also unnest multiple columns simultaneously
    df <- tibble(
      a = list(c("a", "b"), "c"),
      b = list(1:2, 3),
      c = c(11, 22)
    )
    df |> unnest_legacy(a, b)
    #> # A tibble: 3 × 3
    #>       c a         b
    #>   <dbl> <chr> <dbl>
    #> 1    11 a         1
    #> 2    11 b         2
    #> 3    22 c         3
    # If you omit the column names, it'll unnest all list-cols
    df |> unnest_legacy()
    #> # A tibble: 3 × 3
    #>       c a         b
    #>   <dbl> <chr> <dbl>
    #> 1    11 a         1
    #> 2    11 b         2
    #> 3    22 c         3