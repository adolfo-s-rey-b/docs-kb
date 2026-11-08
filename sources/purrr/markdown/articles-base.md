[Skip to content](https://purrr.tidyverse.org/articles/base.html#container)

![](https://purrr.tidyverse.org/logo.png)

purrr <-> base R
================

Source: [`vignettes/base.Rmd`](https://github.com/tidyverse/purrr/blob/main/vignettes/base.Rmd)

`base.Rmd`

Introduction[](https://purrr.tidyverse.org/articles/base.html#introduction)

----------------------------------------------------------------------------

This vignette compares purrr’s functionals to their base R equivalents, focusing primarily on the map family and related functions. This helps those familiar with base R understand better what purrr does, and shows purrr users how you might express the same ideas in base R code. We’ll start with a rough overview of the major differences, give a rough translation guide, and then show a few examples.

    library(purrr)
    library(tibble)

### Key differences[](https://purrr.tidyverse.org/articles/base.html#key-differences)

There are two primary differences between the base apply family and the purrr map family: purrr functions are named more consistently, and more fully explore the space of input and output variants.

*   purrr functions consistently use `.` as prefix to avoid [inadvertently matching arguments](https://adv-r.hadley.nz/functionals.html#argument-names)
     of the purrr function, instead of the function that you’re trying to call. Base functions use a variety of techniques including upper case (e.g. `lapply(X, FUN, ...)`) or require anonymous functions (e.g. `[Map()](https://rdrr.io/r/base/funprog.html) `).
    
*   All map functions are type stable: you can predict the type of the output using little information about the inputs. In contrast, the base functions `[sapply()](https://rdrr.io/r/base/lapply.html) ` and `[mapply()](https://rdrr.io/r/base/mapply.html) ` automatically simplify making the return value hard to predict.
    
*   The map functions all start with the data, followed by the function, then any additional constant argument. Most base apply functions also follow this pattern, but `[mapply()](https://rdrr.io/r/base/mapply.html) ` starts with the function, and `[Map()](https://rdrr.io/r/base/funprog.html) ` has no way to supply additional constant arguments.
    
*   purrr functions provide all combinations of input and output variants, and include variants specifically for the common two argument case.
    

### Direct translations[](https://purrr.tidyverse.org/articles/base.html#direct-translations)

The following sections give a high-level translation between base R commands and their purrr equivalents. See function documentation for the details.

#### `Map` functions[](https://purrr.tidyverse.org/articles/base.html#map-functions)

Here `x` denotes a vector and `f` denotes a function

|     |     |     |     |
| --- | --- | --- | --- |   
| List | 1 vector | `[lapply()](https://rdrr.io/r/base/lapply.html) ` | `[map()](https://purrr.tidyverse.org/reference/map.html) ` |
| List | 2 vectors | `[mapply()](https://rdrr.io/r/base/mapply.html) `, `[Map()](https://rdrr.io/r/base/funprog.html) ` | `[map2()](https://purrr.tidyverse.org/reference/map2.html) ` |
| List | \>2 vectors | `[mapply()](https://rdrr.io/r/base/mapply.html) `, `[Map()](https://rdrr.io/r/base/funprog.html) ` | `[pmap()](https://purrr.tidyverse.org/reference/pmap.html) ` |
| Atomic vector of desired type | 1 vector | `[vapply()](https://rdrr.io/r/base/lapply.html) ` | `[map_lgl()](https://purrr.tidyverse.org/reference/map.html) ` (logical), `[map_int()](https://purrr.tidyverse.org/reference/map.html) ` (integer), `[map_dbl()](https://purrr.tidyverse.org/reference/map.html) ` (double), `[map_chr()](https://purrr.tidyverse.org/reference/map.html) ` (character), `[map_vec()](https://purrr.tidyverse.org/reference/map.html) ` (other vectors) |
| Atomic vector of desired type | 2 vectors | `[mapply()](https://rdrr.io/r/base/mapply.html) `, `[Map()](https://rdrr.io/r/base/funprog.html) `, then `is.*()` to check type | `[map2_lgl()](https://purrr.tidyverse.org/reference/map2.html) ` (logical), `[map2_int()](https://purrr.tidyverse.org/reference/map2.html) ` (integer), `[map2_dbl()](https://purrr.tidyverse.org/reference/map2.html) ` (double), `[map2_chr()](https://purrr.tidyverse.org/reference/map2.html) ` (character), `[map2_vec()](https://purrr.tidyverse.org/reference/map2.html) ` (other vectors) |
| Atomic vector of desired type | \>2 vectors | `[mapply()](https://rdrr.io/r/base/mapply.html) `, `[Map()](https://rdrr.io/r/base/funprog.html) `, then `is.*()` to check type | `[pmap_lgl()](https://purrr.tidyverse.org/reference/pmap.html) ` (logical), `[pmap_int()](https://purrr.tidyverse.org/reference/pmap.html) ` (integer), `[pmap_dbl()](https://purrr.tidyverse.org/reference/pmap.html) ` (double), `[pmap_chr()](https://purrr.tidyverse.org/reference/pmap.html) ` (character), `[pmap_vec()](https://purrr.tidyverse.org/reference/pmap.html) ` (other vectors) |
| Side effect only | 2 vectors | loops | `[walk2()](https://purrr.tidyverse.org/reference/map2.html) ` |
| Side effect only | 1 vector | loops | `[walk()](https://purrr.tidyverse.org/reference/map.html) ` |
| Side effect only | \>2 vectors | loops | `[pwalk()](https://purrr.tidyverse.org/reference/pmap.html) ` |
| Data frame (`rbind` outputs) | 1 vector | `[lapply()](https://rdrr.io/r/base/lapply.html) ` then `[rbind()](https://rdrr.io/r/base/cbind.html) ` | `[map()](https://purrr.tidyverse.org/reference/map.html) ` then `[list_rbind()](https://purrr.tidyverse.org/reference/list_c.html) ` |
| Data frame (`rbind` outputs) | 2 vectors | `[mapply()](https://rdrr.io/r/base/mapply.html) `/`[Map()](https://rdrr.io/r/base/funprog.html) ` then `[rbind()](https://rdrr.io/r/base/cbind.html) ` | `[map2()](https://purrr.tidyverse.org/reference/map2.html) ` then `[list_rbind()](https://purrr.tidyverse.org/reference/list_c.html) ` |
| Data frame (`rbind` outputs) | \>2 vectors | `[mapply()](https://rdrr.io/r/base/mapply.html) `/`[Map()](https://rdrr.io/r/base/funprog.html) ` then `[rbind()](https://rdrr.io/r/base/cbind.html) ` | `[pmap()](https://purrr.tidyverse.org/reference/pmap.html) ` then `[list_rbind()](https://purrr.tidyverse.org/reference/list_c.html) ` |
| Data frame (`cbind` outputs) | 1 vector | `[lapply()](https://rdrr.io/r/base/lapply.html) ` then `[cbind()](https://rdrr.io/r/base/cbind.html) ` | `[map()](https://purrr.tidyverse.org/reference/map.html) ` then `[list_cbind()](https://purrr.tidyverse.org/reference/list_c.html) ` |
| Data frame (`cbind` outputs) | 2 vectors | `[mapply()](https://rdrr.io/r/base/mapply.html) `/`[Map()](https://rdrr.io/r/base/funprog.html) ` then `[cbind()](https://rdrr.io/r/base/cbind.html) ` | `[map2()](https://purrr.tidyverse.org/reference/map2.html) ` then `[list_cbind()](https://purrr.tidyverse.org/reference/list_c.html) ` |
| Data frame (`cbind` outputs) | \>2 vectors | `[mapply()](https://rdrr.io/r/base/mapply.html) `/`[Map()](https://rdrr.io/r/base/funprog.html) ` then `[cbind()](https://rdrr.io/r/base/cbind.html) ` | `[pmap()](https://purrr.tidyverse.org/reference/pmap.html) ` then `[list_cbind()](https://purrr.tidyverse.org/reference/list_c.html) ` |
| Any | Vector and its names | `l/s/vapply(X, function(x) f(x, names(x)))` or `mapply/Map(f, x, names(x))` | `[imap()](https://purrr.tidyverse.org/reference/imap.html) `, `imap_*()` (`lgl`, `dbl`, `chr`, and etc. just like for `[map()](https://purrr.tidyverse.org/reference/map.html) `, `[map2()](https://purrr.tidyverse.org/reference/map2.html) `, and `[pmap()](https://purrr.tidyverse.org/reference/pmap.html) `) |
| Any | Selected elements of the vector | `l/s/vapply(X[index], FUN, ...)` | `[map_if()](https://purrr.tidyverse.org/reference/map_if.html) `, `[map_at()](https://purrr.tidyverse.org/reference/map_if.html) ` |
| List | Recursively apply to list within list | `[rapply()](https://rdrr.io/r/base/rapply.html) ` | `[map_depth()](https://purrr.tidyverse.org/reference/map_depth.html) ` |
| List | List only | `[lapply()](https://rdrr.io/r/base/lapply.html) ` | `[lmap()](https://purrr.tidyverse.org/reference/lmap.html) `, `[lmap_at()](https://purrr.tidyverse.org/reference/lmap.html) `, `[lmap_if()](https://purrr.tidyverse.org/reference/lmap.html) ` |

#### Extractor shorthands[](https://purrr.tidyverse.org/articles/base.html#extractor-shorthands)

Since a common use case for map functions is list extracting components, purrr provides a handful of shortcut functions for various uses of `[[`.\
\
|     |     |     |\
| --- | --- | --- |  \
| Extract by name | ``lapply(x, `[[`, "a")`` | `map(x, "a")` |\
| Extract by position | ``lapply(x, `[[`, 3)`` | `map(x, 3)` |\
| Extract deeply | `lapply(x, \(y) y[[1]][["x"]][[3]])` | `map(x, list(1, "x", 3))` |\
| Extract with default value | `lapply(x, function(y) tryCatch(y[[3]], error = function(e) NA))` | `map(x, 3, .default = NA)` |\
\
#### Predicates[](https://purrr.tidyverse.org/articles/base.html#predicates)\
\
Here `p`, a predicate, denotes a function that returns `TRUE` or `FALSE` indicating whether an object fulfills a criterion, e.g. `[is.character()](https://rdrr.io/r/base/character.html) `.\
\
|     |     |     |\
| --- | --- | --- |  \
| Find a matching element | `Find(p, x)` | `detect(x, p)`, |\
| Find position of matching element | `Position(p, x)` | `detect_index(x, p)` |\
| Do all elements of a vector satisfy a predicate? | `all(sapply(x, p))` | `every(x, p)` |\
| Does any elements of a vector satisfy a predicate? | `any(sapply(x, p))` | `some(x, p)` |\
| Does a list contain an object? | `any(sapply(x, identical, obj))` | `has_element(x, obj)` |\
| Keep elements that satisfy a predicate | `x[sapply(x, p)]` | `keep(x, p)` |\
| Discard elements that satisfy a predicate | `x[!sapply(x, p)]` | `discard(x, p)` |\
| Negate a predicate function | `function(x) !p(x)` | `negate(p)` |\
\
#### Other vector transforms[](https://purrr.tidyverse.org/articles/base.html#other-vector-transforms)\
\
|     |     |     |\
| --- | --- | --- |  \
| Accumulate intermediate results of a vector reduction | `Reduce(f, x, accumulate = TRUE)` | `accumulate(x, f)` |\
| Recursively combine two lists | `c(X, Y)`, but more complicated to merge recursively | `[list_merge()](https://purrr.tidyverse.org/reference/list_assign.html) `, `[list_modify()](https://purrr.tidyverse.org/reference/list_assign.html) ` |\
| Reduce a list to a single value by iteratively applying a binary function | `Reduce(f, x)` | `reduce(x, f)` |\
\
### Examples[](https://purrr.tidyverse.org/articles/base.html#examples)\
\
#### Varying inputs[](https://purrr.tidyverse.org/articles/base.html#varying-inputs)\
\
##### One input[](https://purrr.tidyverse.org/articles/base.html#one-input)\
\
Suppose we would like to generate a list of samples of 5 from normal distributions with different means:\
\
    means <- 1:4\
\
There’s little difference when generating the samples:\
\
*   Base R uses `[lapply()](https://rdrr.io/r/base/lapply.html) `:\
    \
        set.seed(2020)\
        samples <- lapply(means, rnorm, n = 5, sd = 1)\
        str(samples)\
        #> List of 4\
        #>  $ : num [1:5] 1.377 1.302 -0.098 -0.13 -1.797\
        #>  $ : num [1:5] 2.72 2.94 1.77 3.76 2.12\
        #>  $ : num [1:5] 2.15 3.91 4.2 2.63 2.88\
        #>  $ : num [1:5] 5.8 5.704 0.961 1.711 4.058\
    \
*   purrr uses `[map()](https://purrr.tidyverse.org/reference/map.html) `:\
    \
        set.seed(2020)\
        samples <- map(means, rnorm, n = 5, sd = 1)\
        str(samples)\
        #> List of 4\
        #>  $ : num [1:5] 1.377 1.302 -0.098 -0.13 -1.797\
        #>  $ : num [1:5] 2.72 2.94 1.77 3.76 2.12\
        #>  $ : num [1:5] 2.15 3.91 4.2 2.63 2.88\
        #>  $ : num [1:5] 5.8 5.704 0.961 1.711 4.058\
    \
\
##### Two inputs[](https://purrr.tidyverse.org/articles/base.html#two-inputs)\
\
Lets make the example a little more complicated by also varying the standard deviations:\
\
    means <- 1:4\
    sds <- 1:4\
\
*   This is relatively tricky in base R because we have to adjust a number of `[mapply()](https://rdrr.io/r/base/mapply.html) `’s defaults.\
    \
        set.seed(2020)\
        samples <- mapply(\
          rnorm, \
          mean = means, \
          sd = sds, \
          MoreArgs = list(n = 5), \
          SIMPLIFY = FALSE\
        )\
        str(samples)\
        #> List of 4\
        #>  $ : num [1:5] 1.377 1.302 -0.098 -0.13 -1.797\
        #>  $ : num [1:5] 3.44 3.88 1.54 5.52 2.23\
        #>  $ : num [1:5] 0.441 5.728 6.589 1.885 2.63\
        #>  $ : num [1:5] 11.2 10.82 -8.16 -5.16 4.23\
    \
    Alternatively, we could use `[Map()](https://rdrr.io/r/base/funprog.html) ` which doesn’t simplify, but also doesn’t take any constant arguments, so we need to use an anonymous function:\
    \
        samples <- Map(function(...) rnorm(..., n = 5), mean = means, sd = sds)\
    \
    In R 4.1 and up, you could use the shorter anonymous function form:\
    \
        samples <- Map(\(...) rnorm(..., n = 5), mean = means, sd = sds)\
    \
*   Working with a pair of vectors is a common situation so purrr provides the `[map2()](https://purrr.tidyverse.org/reference/map2.html) ` family of functions:\
    \
        set.seed(2020)\
        samples <- map2(means, sds, rnorm, n = 5)\
        str(samples)\
        #> List of 4\
        #>  $ : num [1:5] 1.377 1.302 -0.098 -0.13 -1.797\
        #>  $ : num [1:5] 3.44 3.88 1.54 5.52 2.23\
        #>  $ : num [1:5] 0.441 5.728 6.589 1.885 2.63\
        #>  $ : num [1:5] 11.2 10.82 -8.16 -5.16 4.23\
    \
\
##### Any number of inputs[](https://purrr.tidyverse.org/articles/base.html#any-number-of-inputs)\
\
We can make the challenge still more complex by also varying the number of samples:\
\
    ns <- 4:1\
\
*   Using base R’s `[Map()](https://rdrr.io/r/base/funprog.html) ` becomes more straightforward because there are no constant arguments.\
    \
        set.seed(2020)\
        samples <- Map(rnorm, mean = means, sd = sds, n = ns)\
        str(samples)\
        #> List of 4\
        #>  $ : num [1:4] 1.377 1.302 -0.098 -0.13\
        #>  $ : num [1:3] -3.59 3.44 3.88\
        #>  $ : num [1:2] 2.31 8.28\
        #>  $ : num 4.47\
    \
*   In purrr, we need to switch from `[map2()](https://purrr.tidyverse.org/reference/map2.html) ` to `[pmap()](https://purrr.tidyverse.org/reference/pmap.html) ` which takes a list of any number of arguments.\
    \
        set.seed(2020)\
        samples <- pmap(list(mean = means, sd = sds, n = ns), rnorm)\
        str(samples)\
        #> List of 4\
        #>  $ : num [1:4] 1.377 1.302 -0.098 -0.13\
        #>  $ : num [1:3] -3.59 3.44 3.88\
        #>  $ : num [1:2] 2.31 8.28\
        #>  $ : num 4.47\
    \
\
#### Outputs[](https://purrr.tidyverse.org/articles/base.html#outputs)\
\
Given the samples, imagine we want to compute their means. A mean is a single number, so we want the output to be a numeric vector rather than a list.\
\
*   There are two options in base R: `[vapply()](https://rdrr.io/r/base/lapply.html) ` or `[sapply()](https://rdrr.io/r/base/lapply.html) `. `[vapply()](https://rdrr.io/r/base/lapply.html) ` requires you to specific the output type (so is relatively verbose), but will always return a numeric vector. `[sapply()](https://rdrr.io/r/base/lapply.html) ` is concise, but if you supply an empty list you’ll get a list instead of a numeric vector.\
    \
        # type stable\
        medians <- vapply(samples, median, FUN.VALUE = numeric(1L))\
        medians\
        #> [1] 0.6017626 3.4411470 5.2946304 4.4694671\
        \
        # not type stable\
        medians <- sapply(samples, median)\
    \
*   purrr is little more compact because we can use `[map_dbl()](https://purrr.tidyverse.org/reference/map.html) `.\
    \
        medians <- map_dbl(samples, median)\
        medians\
        #> [1] 0.6017626 3.4411470 5.2946304 4.4694671\
    \
\
What if we want just the side effect, such as a plot or a file output, but not the returned values?\
\
*   In base R we can either use a for loop or hide the results of `lapply`.\
    \
        # for loop\
        for (s in samples) {\
          hist(s, xlab = "value", main = "")\
        }\
        \
        # lapply\
        invisible(lapply(samples, function(s) {\
          hist(s, xlab = "value", main = "")\
        }))\
    \
*   In purrr, we can use `[walk()](https://purrr.tidyverse.org/reference/map.html) `.\
    \
        walk(samples, ~ hist(.x, xlab = "value", main = ""))\
    \
\
#### Pipes[](https://purrr.tidyverse.org/articles/base.html#pipes)\
\
You can join multiple steps together with the pipe:\
\
    set.seed(2020)\
    means |>\
      map(rnorm, n = 5, sd = 1) |>\
      map_dbl(median)\
    #> [1] -0.09802317  2.72057350  2.87673977  4.05830349\
\
The pipe is particularly compelling when working with longer transformations. For example, the following code splits `mtcars` up by `cyl`, fits a linear model, extracts the coefficients, and extracts the first one (the intercept).\
\
    mtcars |>\
      split(mtcars$cyl) |> \
      map(\(df) lm(mpg ~ wt, data = df))|> \
      map(coef) |> \
      map_dbl(1)\
    #>        4        6        8 \
    #> 39.57120 28.40884 23.86803