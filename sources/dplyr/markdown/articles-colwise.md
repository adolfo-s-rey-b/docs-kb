[Skip to content](https://dplyr.tidyverse.org/articles/colwise.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Column-wise operations
======================

Source: [`vignettes/colwise.Rmd`](https://github.com/tidyverse/dplyr/blob/main/vignettes/colwise.Rmd)

`colwise.Rmd`

It’s often useful to perform the same operation on multiple columns, but copying and pasting is both tedious and error prone:

    df |>
      group_by(g1, g2) |>
      summarise(a = mean(a), b = mean(b), c = mean(c), d = mean(d))

(If you’re trying to compute `mean(a, b, c, d)` for each row, instead see `[vignette("rowwise")](https://dplyr.tidyverse.org/articles/rowwise.html) `)

This vignette will introduce you to the `[across()](https://dplyr.tidyverse.org/reference/across.html) ` function, which lets you rewrite the previous code more succinctly:

    df |>
      group_by(g1, g2) |>
      summarise(across(a:d, mean))

We’ll start by discussing the basic usage of `[across()](https://dplyr.tidyverse.org/reference/across.html) `, particularly as it applies to `[summarise()](https://dplyr.tidyverse.org/reference/summarise.html) `, and show how to use it with multiple functions. We’ll then show a few uses with other verbs. We’ll finish off with a bit of history, showing why we prefer `[across()](https://dplyr.tidyverse.org/reference/across.html) ` to our last approach (the `_if()`, `_at()` and `_all()` functions) and how to translate your old code to the new syntax.

    library(dplyr, warn.conflicts = FALSE)

Basic usage[](https://dplyr.tidyverse.org/articles/colwise.html#basic-usage)

-----------------------------------------------------------------------------

`[across()](https://dplyr.tidyverse.org/reference/across.html) ` has two primary arguments:

*   The first argument, `.cols`, selects the columns you want to operate on. It uses tidy selection (like `[select()](https://dplyr.tidyverse.org/reference/select.html) `) so you can pick variables by position, name, and type.
    
*   The second argument, `.fns`, is a function or list of functions to apply to each column. This can also be a purrr style formula (or list of formulas) like `~ .x / 2`. (This argument is optional, and you can omit it if you just want to get the underlying data; you’ll see that technique used in `[vignette("rowwise")](https://dplyr.tidyverse.org/articles/rowwise.html) `.)
    

Here are a couple of examples of `[across()](https://dplyr.tidyverse.org/reference/across.html) ` in conjunction with its favourite verb, `[summarise()](https://dplyr.tidyverse.org/reference/summarise.html) `. But you can use `[across()](https://dplyr.tidyverse.org/reference/across.html) ` with any dplyr verb, as you’ll see a little later.

    starwars |>
      summarise(across(where(is.character), n_distinct))
    #> # A tibble: 1 × 8
    #>    name hair_color skin_color eye_color   sex gender homeworld species
    #>   <int>      <int>      <int>     <int> <int>  <int>     <int>   <int>
    #> 1    87         12         31        15     5      3        49      38
    
    starwars |>
      group_by(species) |>
      filter(n() > 1) |>
      summarise(across(c(sex, gender, homeworld), n_distinct))
    #> # A tibble: 9 × 4
    #>   species    sex gender homeworld
    #>   <chr>    <int>  <int>     <int>
    #> 1 Droid        1      2         3
    #> 2 Gungan       1      1         1
    #> 3 Human        2      2        15
    #> 4 Kaminoan     2      2         1
    #> # ℹ 5 more rows
    
    starwars |>
      group_by(homeworld) |>
      filter(n() > 1) |>
      summarise(across(where(is.numeric), ~ mean(.x, na.rm = TRUE)))
    #> # A tibble: 10 × 4
    #>   homeworld height  mass birth_year
    #>   <chr>      <dbl> <dbl>      <dbl>
    #> 1 Alderaan    176.  64         43  
    #> 2 Corellia    175   78.5       25  
    #> 3 Coruscant   174.  50         91  
    #> 4 Kamino      208.  83.1       31.5
    #> # ℹ 6 more rows

Because `[across()](https://dplyr.tidyverse.org/reference/across.html) ` is usually used in combination with `[summarise()](https://dplyr.tidyverse.org/reference/summarise.html) ` and `[mutate()](https://dplyr.tidyverse.org/reference/mutate.html) `, it doesn’t select grouping variables in order to avoid accidentally modifying them:

    df <- data.frame(g = c(1, 1, 2), x = c(-1, 1, 3), y = c(-1, -4, -9))
    df |>
      group_by(g) |>
      summarise(across(where(is.numeric), sum))
    #> # A tibble: 2 × 3
    #>       g     x     y
    #>   <dbl> <dbl> <dbl>
    #> 1     1     0    -5
    #> 2     2     3    -9

### Multiple functions[](https://dplyr.tidyverse.org/articles/colwise.html#multiple-functions)

You can transform each variable with more than one function by supplying a named list of functions or lambda functions in the second argument:

    min_max <- list(
      min = ~ min(.x, na.rm = TRUE),
      max = ~ max(.x, na.rm = TRUE)
    )
    starwars |> summarise(across(where(is.numeric), min_max))
    #> # A tibble: 1 × 6
    #>   height_min height_max mass_min mass_max birth_year_min birth_year_max
    #>        <int>      <int>    <dbl>    <dbl>          <dbl>          <dbl>
    #> 1         66        264       15     1358              8            896
    starwars |> summarise(across(c(height, mass, birth_year), min_max))
    #> # A tibble: 1 × 6
    #>   height_min height_max mass_min mass_max birth_year_min birth_year_max
    #>        <int>      <int>    <dbl>    <dbl>          <dbl>          <dbl>
    #> 1         66        264       15     1358              8            896

Control how the names are created with the `.names` argument which takes a [glue](https://glue.tidyverse.org/)
 spec:

    starwars |>
      summarise(across(
        where(is.numeric),
        min_max,
        .names = "{.fn}.{.col}"
      ))
    #> # A tibble: 1 × 6
    #>   min.height max.height min.mass max.mass min.birth_year max.birth_year
    #>        <int>      <int>    <dbl>    <dbl>          <dbl>          <dbl>
    #> 1         66        264       15     1358              8            896
    starwars |>
      summarise(across(
        c(height, mass, birth_year),
        min_max,
        .names = "{.fn}.{.col}"
      ))
    #> # A tibble: 1 × 6
    #>   min.height max.height min.mass max.mass min.birth_year max.birth_year
    #>        <int>      <int>    <dbl>    <dbl>          <dbl>          <dbl>
    #> 1         66        264       15     1358              8            896

If you’d prefer all summaries with the same function to be grouped together, you’ll have to expand the calls yourself:

    starwars |>
      summarise(
        across(
          c(height, mass, birth_year),
          ~ min(.x, na.rm = TRUE),
          .names = "min_{.col}"
        ),
        across(
          c(height, mass, birth_year),
          ~ max(.x, na.rm = TRUE),
          .names = "max_{.col}"
        )
      )
    #> # A tibble: 1 × 6
    #>   min_height min_mass min_birth_year max_height max_mass max_birth_year
    #>        <int>    <dbl>          <dbl>      <int>    <dbl>          <dbl>
    #> 1         66       15              8        264     1358            896

(One day this might become an argument to `[across()](https://dplyr.tidyverse.org/reference/across.html) ` but we’re not yet sure how it would work.)

We cannot however use `where(is.numeric)` in that last case because the second `[across()](https://dplyr.tidyverse.org/reference/across.html) ` would pick up the variables that were newly created (“min\_height”, “min\_mass” and “min\_birth\_year”).

We can work around this by combining both calls to `[across()](https://dplyr.tidyverse.org/reference/across.html) ` into a single expression that returns a tibble:

    starwars |>
      summarise(
        tibble(
          across(where(is.numeric), ~ min(.x, na.rm = TRUE), .names = "min_{.col}"),
          across(where(is.numeric), ~ max(.x, na.rm = TRUE), .names = "max_{.col}")
        )
      )
    #> # A tibble: 1 × 6
    #>   min_height min_mass min_birth_year max_height max_mass max_birth_year
    #>        <int>    <dbl>          <dbl>      <int>    <dbl>          <dbl>
    #> 1         66       15              8        264     1358            896

Alternatively we could reorganize results with `[relocate()](https://dplyr.tidyverse.org/reference/relocate.html) `:

    starwars |>
      summarise(across(where(is.numeric), min_max, .names = "{.fn}.{.col}")) |>
      relocate(starts_with("min"))
    #> # A tibble: 1 × 6
    #>   min.height min.mass min.birth_year max.height max.mass max.birth_year
    #>        <int>    <dbl>          <dbl>      <int>    <dbl>          <dbl>
    #> 1         66       15              8        264     1358            896

### Current column[](https://dplyr.tidyverse.org/articles/colwise.html#current-column)

If you need to, you can access the name of the “current” column inside by calling `[cur_column()](https://dplyr.tidyverse.org/reference/context.html) `. This can be useful if you want to perform some sort of context dependent transformation that’s already encoded in a vector:

    df <- tibble(x = 1:3, y = 3:5, z = 5:7)
    mult <- list(x = 1, y = 10, z = 100)
    
    df |>
      mutate(across(all_of(names(mult)), ~ .x * mult[[cur_column()]]))
    #> # A tibble: 3 × 3
    #>       x     y     z
    #>   <dbl> <dbl> <dbl>
    #> 1     1    30   500
    #> 2     2    40   600
    #> 3     3    50   700

### Gotchas[](https://dplyr.tidyverse.org/articles/colwise.html#gotchas)

Be careful when combining numeric summaries with `where(is.numeric)`:

    df <- data.frame(x = c(1, 2, 3), y = c(1, 4, 9))
    
    df |>
      summarise(n = n(), across(where(is.numeric), sd))
    #>    n x        y
    #> 1 NA 1 4.041452

Here `n` becomes `NA` because `n` is numeric, so the `[across()](https://dplyr.tidyverse.org/reference/across.html) ` computes its standard deviation, and the standard deviation of 3 (a constant) is `NA`. You probably want to compute `[n()](https://dplyr.tidyverse.org/reference/context.html) ` last to avoid this problem:

    df |>
      summarise(across(where(is.numeric), sd), n = n())
    #>   x        y n
    #> 1 1 4.041452 3

Alternatively, you could explicitly exclude `n` from the columns to operate on:

    df |>
      summarise(n = n(), across(where(is.numeric) & !n, sd))
    #>   n x        y
    #> 1 3 1 4.041452

Another approach is to combine both the call to `[n()](https://dplyr.tidyverse.org/reference/context.html) ` and `[across()](https://dplyr.tidyverse.org/reference/across.html) ` in a single expression that returns a tibble:

    df |>
      summarise(tibble(n = n(), across(where(is.numeric), sd)))
    #>   n x        y
    #> 1 3 1 4.041452

### Other verbs[](https://dplyr.tidyverse.org/articles/colwise.html#other-verbs)

So far we’ve focused on the use of `[across()](https://dplyr.tidyverse.org/reference/across.html) ` with `[summarise()](https://dplyr.tidyverse.org/reference/summarise.html) `, but it works with any other dplyr verb that uses data masking:

*   Rescale all numeric variables to range 0-1:
    
        rescale01 <- function(x) {
          rng <- range(x, na.rm = TRUE)
          (x - rng[1]) / (rng[2] - rng[1])
        }
        df <- tibble(x = 1:4, y = rnorm(4))
        df |> mutate(across(where(is.numeric), rescale01))
        #> # A tibble: 4 × 2
        #>       x     y
        #>   <dbl> <dbl>
        #> 1 0     0.385
        #> 2 0.333 1    
        #> 3 0.667 0    
        #> 4 1     0.903
    

For some verbs, like `[group_by()](https://dplyr.tidyverse.org/reference/group_by.html) `, `[count()](https://dplyr.tidyverse.org/reference/count.html) ` and `[distinct()](https://dplyr.tidyverse.org/reference/distinct.html) `, you don’t need to supply a summary function, but it can be useful to use tidy-selection to dynamically select a set of columns. In those cases, we recommend using the complement to `[across()](https://dplyr.tidyverse.org/reference/across.html) `, `[pick()](https://dplyr.tidyverse.org/reference/pick.html) `, which works like `[across()](https://dplyr.tidyverse.org/reference/across.html) ` but doesn’t apply any functions and instead returns a data frame containing the selected columns.

*   Find all distinct
    
        starwars |> distinct(pick(contains("color")))
        #> # A tibble: 67 × 3
        #>   hair_color skin_color  eye_color
        #>   <chr>      <chr>       <chr>    
        #> 1 blond      fair        blue     
        #> 2 NA         gold        yellow   
        #> 3 NA         white, blue red      
        #> 4 none       white       yellow   
        #> # ℹ 63 more rows
    
*   Count all combinations of variables with a given pattern:
    
        starwars |> count(pick(contains("color")), sort = TRUE)
        #> # A tibble: 67 × 4
        #>   hair_color skin_color eye_color     n
        #>   <chr>      <chr>      <chr>     <int>
        #> 1 brown      light      brown         6
        #> 2 brown      fair       blue          4
        #> 3 none       grey       black         4
        #> 4 black      dark       brown         3
        #> # ℹ 63 more rows
    

`[across()](https://dplyr.tidyverse.org/reference/across.html) ` doesn’t work with `[select()](https://dplyr.tidyverse.org/reference/select.html) ` or `[rename()](https://dplyr.tidyverse.org/reference/rename.html) ` because they already use tidy select syntax; if you want to transform column names with a function, you can use `[rename_with()](https://dplyr.tidyverse.org/reference/rename.html) `.

### filter() and filter\_out()[](https://dplyr.tidyverse.org/articles/colwise.html#filter-and-filter_out)

We cannot directly use `[across()](https://dplyr.tidyverse.org/reference/across.html) ` in `[filter()](https://dplyr.tidyverse.org/reference/filter.html) ` or `[filter_out()](https://dplyr.tidyverse.org/reference/filter.html) ` because we need an extra step to combine the results into a single logical vector. To that end, `[filter()](https://dplyr.tidyverse.org/reference/filter.html) ` and `[filter_out()](https://dplyr.tidyverse.org/reference/filter.html) ` have two special purpose companion functions:

*   `[if_any()](https://dplyr.tidyverse.org/reference/across.html) ` keeps the rows where the predicate is true for _at least one_ selected column:

    starwars |>
      filter_out(if_any(everything(), is.na))
    #> # A tibble: 29 × 14
    #>   name    height  mass hair_color skin_color eye_color birth_year sex  
    #>   <chr>    <int> <dbl> <chr>      <chr>      <chr>          <dbl> <chr>
    #> 1 Luke S…    172    77 blond      fair       blue            19   male 
    #> 2 Darth …    202   136 none       white      yellow          41.9 male 
    #> 3 Leia O…    150    49 brown      light      brown           19   fema…
    #> 4 Owen L…    178   120 brown, gr… light      blue            52   male 
    #> # ℹ 25 more rows
    #> # ℹ 6 more variables: gender <chr>, homeworld <chr>, species <chr>,
    #> #   films <list>, vehicles <list>, starships <list>

*   `[if_all()](https://dplyr.tidyverse.org/reference/across.html) ` keeps the rows where the predicate is true for _all_ selected columns:

    starwars |>
      filter_out(if_all(everything(), is.na))
    #> # A tibble: 87 × 14
    #>   name    height  mass hair_color skin_color eye_color birth_year sex  
    #>   <chr>    <int> <dbl> <chr>      <chr>      <chr>          <dbl> <chr>
    #> 1 Luke S…    172    77 blond      fair       blue            19   male 
    #> 2 C-3PO      167    75 NA         gold       yellow         112   none 
    #> 3 R2-D2       96    32 NA         white, bl… red             33   none 
    #> 4 Darth …    202   136 none       white      yellow          41.9 male 
    #> # ℹ 83 more rows
    #> # ℹ 6 more variables: gender <chr>, homeworld <chr>, species <chr>,
    #> #   films <list>, vehicles <list>, starships <list>

`_if`, `_at`, `_all`[](https://dplyr.tidyverse.org/articles/colwise.html#if-_at-_all)

--------------------------------------------------------------------------------------

Prior versions of dplyr allowed you to apply a function to multiple columns in a different way: using functions with `_if`, `_at`, and `_all()` suffixes. These functions solved a pressing need and are used by many people, but are now superseded. That means that they’ll stay around, but won’t receive any new features and will only get critical bug fixes.

### Why do we like `across()`?[](https://dplyr.tidyverse.org/articles/colwise.html#why-do-we-like-across)

Why did we decide to move away from these functions in favour of `[across()](https://dplyr.tidyverse.org/reference/across.html) `?

1.  `[across()](https://dplyr.tidyverse.org/reference/across.html) ` makes it possible to express useful summaries that were previously impossible:
    
        df |>
          group_by(g1, g2) |>
          summarise(
            across(where(is.numeric), mean),
            across(where(is.factor), nlevels),
            n = n(),
          )
    
2.  `[across()](https://dplyr.tidyverse.org/reference/across.html) ` reduces the number of functions that dplyr needs to provide. This makes dplyr easier for you to use (because there are fewer functions to remember) and easier for us to implement new verbs (since we only need to implement one function, not four).
    
3.  `[across()](https://dplyr.tidyverse.org/reference/across.html) ` unifies `_if` and `_at` semantics so that you can select by position, name, and type, and you can now create compound selections that were previously impossible. For example, you can now transform all numeric columns whose name begins with “x”: `across(where(is.numeric) & starts_with("x"))`.
    
4.  `[across()](https://dplyr.tidyverse.org/reference/across.html) ` doesn’t need to use `[vars()](https://dplyr.tidyverse.org/reference/vars.html) `. The `_at()` functions are the only place in dplyr where you have to manually quote variable names, which makes them a little weird and hence harder to remember.
    

### Why did it take so long to discover `across()`?[](https://dplyr.tidyverse.org/articles/colwise.html#why-did-it-take-so-long-to-discover-across)

It’s disappointing that we didn’t discover `[across()](https://dplyr.tidyverse.org/reference/across.html) ` earlier, and instead worked through several false starts (first not realising that it was a common problem, then with the `_each()` functions, and most recently with the `_if()`/`_at()`/`_all()` functions). But `[across()](https://dplyr.tidyverse.org/reference/across.html) ` couldn’t work without three recent discoveries:

*   You can have a column of a data frame that is itself a data frame. This is something provided by base R, but it’s not very well documented, and it took a while to see that it was useful, not just a theoretical curiosity.
    
*   We can use data frames to allow summary functions to return multiple columns.
    
*   We can use the absence of an outer name as a convention that you want to unpack a data frame column into individual columns.
    

### How do you convert existing code?[](https://dplyr.tidyverse.org/articles/colwise.html#how-do-you-convert-existing-code)

Fortunately, it’s generally straightforward to translate your existing code to use `[across()](https://dplyr.tidyverse.org/reference/across.html) `:

*   Strip the `_if()`, `_at()` and `_all()` suffix off the function.
    
*   Call `[across()](https://dplyr.tidyverse.org/reference/across.html) `. The first argument will be:
    
    1.  For `_if()`, the old second argument wrapped in `[where()](https://tidyselect.r-lib.org/reference/where.html) `.
    2.  For `_at()`, the old second argument, with the call to `[vars()](https://dplyr.tidyverse.org/reference/vars.html) ` removed.
    3.  For `_all()`, `[everything()](https://tidyselect.r-lib.org/reference/everything.html) `.
    
    The subsequent arguments can be copied as is.
    

For example:

    df |> mutate_if(is.numeric, ~ mean(.x, na.rm = TRUE))
    # ->
    df |> mutate(across(where(is.numeric), ~ mean(.x, na.rm = TRUE)))
    
    df |> mutate_at(vars(c(x, starts_with("y"))), mean)
    # ->
    df |> mutate(across(c(x, starts_with("y")), mean))
    
    df |> mutate_all(mean)
    # ->
    df |> mutate(across(everything(), mean))

There are a few exceptions to this rule:

*   `rename_*()` and `select_*()` follow a different pattern. They already have select semantics, so are generally used in a different way that doesn’t have a direct equivalent with `[across()](https://dplyr.tidyverse.org/reference/across.html) `; use the new `[rename_with()](https://dplyr.tidyverse.org/reference/rename.html) ` instead.
    
*   Previously, `filter_*()` were paired with the `[all_vars()](https://dplyr.tidyverse.org/reference/all_vars.html) ` and `[any_vars()](https://dplyr.tidyverse.org/reference/all_vars.html) ` helpers. The new helpers `[if_any()](https://dplyr.tidyverse.org/reference/across.html) ` and `[if_all()](https://dplyr.tidyverse.org/reference/across.html) ` can be used inside `[filter()](https://dplyr.tidyverse.org/reference/filter.html) ` to keep rows for which the predicate is true for at least one, or all selected columns:
    
        df <- tibble(x = c("a", "b"), y = c(1, 1), z = c(-1, 1))
        
        # Find all rows where EVERY numeric variable is greater than zero
        df |> filter(if_all(where(is.numeric), ~ .x > 0))
        #> # A tibble: 1 × 3
        #>   x         y     z
        #>   <chr> <dbl> <dbl>
        #> 1 b         1     1
        
        # Find all rows where ANY numeric variable is greater than zero
        df |> filter(if_any(where(is.numeric), ~ .x > 0))
        #> # A tibble: 2 × 3
        #>   x         y     z
        #>   <chr> <dbl> <dbl>
        #> 1 a         1    -1
        #> 2 b         1     1
    
*   When used in a `[mutate()](https://dplyr.tidyverse.org/reference/mutate.html) `, all transformations performed by an `[across()](https://dplyr.tidyverse.org/reference/across.html) ` are applied at once. This is different to the behaviour of `[mutate_if()](https://dplyr.tidyverse.org/reference/mutate_all.html) `, `[mutate_at()](https://dplyr.tidyverse.org/reference/mutate_all.html) `, and `[mutate_all()](https://dplyr.tidyverse.org/reference/mutate_all.html) `, which apply the transformations one at a time. We expect that you’ll generally find the new behaviour less surprising:
    
        df <- tibble(x = 2, y = 4, z = 8)
        df |> mutate_all(~ .x / y)
        #> # A tibble: 1 × 3
        #>       x     y     z
        #>   <dbl> <dbl> <dbl>
        #> 1   0.5     1     8
        
        df |> mutate(across(everything(), ~ .x / y))
        #> # A tibble: 1 × 3
        #>       x     y     z
        #>   <dbl> <dbl> <dbl>
        #> 1   0.5     1     2