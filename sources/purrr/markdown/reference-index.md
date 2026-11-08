[Skip to content](https://purrr.tidyverse.org/reference/index.html#container)

![](https://purrr.tidyverse.org/logo.png)

Package index
=============

Map family[](https://purrr.tidyverse.org/reference/index.html#map-family)

--------------------------------------------------------------------------

The `map(.x, .f)` functions transforms each element of the vector `.x` with the function `.f`, returning a vector defined by the suffix (`_lgl`, `_chr()` etc). `[walk()](https://purrr.tidyverse.org/reference/map.html) ` is a variant for functions called primarily for their side-effects; it returns `.x` invisibly.

As well as functions, `.f`, can take numbers and characters (used as a shorthand for `[[`), and formulas (used as a succint function definition). See details in `[as_mapper()](https://purrr.tidyverse.org/reference/as_mapper.html) `\
\
`[map()](https://purrr.tidyverse.org/reference/map.html) ` `[map_lgl()](https://purrr.tidyverse.org/reference/map.html) ` `[map_int()](https://purrr.tidyverse.org/reference/map.html) ` `[map_dbl()](https://purrr.tidyverse.org/reference/map.html) ` `[map_chr()](https://purrr.tidyverse.org/reference/map.html) ` `[map_vec()](https://purrr.tidyverse.org/reference/map.html) ` `[walk()](https://purrr.tidyverse.org/reference/map.html) `\
\
Apply a function to each element of a vector\
\
`[as_mapper()](https://purrr.tidyverse.org/reference/as_mapper.html) `\
\
Convert an object into a mapper function\
\
Map variants[](https://purrr.tidyverse.org/reference/index.html#map-variants)\
\
------------------------------------------------------------------------------\
\
A rich set of variants builds on the basic idea of `[map()](https://purrr.tidyverse.org/reference/map.html) `: `[modify()](https://purrr.tidyverse.org/reference/modify.html) ` modifies “in place”, returning a vector the same type as `.x`; `[map2()](https://purrr.tidyverse.org/reference/map2.html) ` iterates over two vectors in parallel; `[pmap()](https://purrr.tidyverse.org/reference/pmap.html) ` (parallel map) iterates over a list of vectors; `[imap()](https://purrr.tidyverse.org/reference/imap.html) ` (index map) is a shortcut for the common pattern `map2(x, names(x))`.\
\
`[map_if()](https://purrr.tidyverse.org/reference/map_if.html) ` `[map_at()](https://purrr.tidyverse.org/reference/map_if.html) `\
\
Apply a function to each element of a vector conditionally\
\
`[map_depth()](https://purrr.tidyverse.org/reference/map_depth.html) ` `[modify_depth()](https://purrr.tidyverse.org/reference/map_depth.html) `\
\
Map/modify elements at given depth\
\
`[map2()](https://purrr.tidyverse.org/reference/map2.html) ` `[map2_lgl()](https://purrr.tidyverse.org/reference/map2.html) ` `[map2_int()](https://purrr.tidyverse.org/reference/map2.html) ` `[map2_dbl()](https://purrr.tidyverse.org/reference/map2.html) ` `[map2_chr()](https://purrr.tidyverse.org/reference/map2.html) ` `[map2_vec()](https://purrr.tidyverse.org/reference/map2.html) ` `[walk2()](https://purrr.tidyverse.org/reference/map2.html) `\
\
Map over two inputs\
\
`[pmap()](https://purrr.tidyverse.org/reference/pmap.html) ` `[pmap_lgl()](https://purrr.tidyverse.org/reference/pmap.html) ` `[pmap_int()](https://purrr.tidyverse.org/reference/pmap.html) ` `[pmap_dbl()](https://purrr.tidyverse.org/reference/pmap.html) ` `[pmap_chr()](https://purrr.tidyverse.org/reference/pmap.html) ` `[pmap_vec()](https://purrr.tidyverse.org/reference/pmap.html) ` `[pwalk()](https://purrr.tidyverse.org/reference/pmap.html) `\
\
Map over multiple input simultaneously (in "parallel")\
\
`[modify()](https://purrr.tidyverse.org/reference/modify.html) ` `[modify_if()](https://purrr.tidyverse.org/reference/modify.html) ` `[modify_at()](https://purrr.tidyverse.org/reference/modify.html) ` `[modify2()](https://purrr.tidyverse.org/reference/modify.html) ` `[imodify()](https://purrr.tidyverse.org/reference/modify.html) `\
\
Modify elements selectively\
\
`[modify_tree()](https://purrr.tidyverse.org/reference/modify_tree.html) `\
\
Recursively modify a list\
\
`[imap()](https://purrr.tidyverse.org/reference/imap.html) ` `[imap_lgl()](https://purrr.tidyverse.org/reference/imap.html) ` `[imap_chr()](https://purrr.tidyverse.org/reference/imap.html) ` `[imap_int()](https://purrr.tidyverse.org/reference/imap.html) ` `[imap_dbl()](https://purrr.tidyverse.org/reference/imap.html) ` `[imap_vec()](https://purrr.tidyverse.org/reference/imap.html) ` `[iwalk()](https://purrr.tidyverse.org/reference/imap.html) `\
\
Apply a function to each element of a vector, and its index\
\
`[lmap()](https://purrr.tidyverse.org/reference/lmap.html) ` `[lmap_if()](https://purrr.tidyverse.org/reference/lmap.html) ` `[lmap_at()](https://purrr.tidyverse.org/reference/lmap.html) `\
\
Apply a function to list-elements of a list\
\
Predicate functionals[](https://purrr.tidyverse.org/reference/index.html#predicate-functionals)\
\
------------------------------------------------------------------------------------------------\
\
A predicate function is a function that either returns `TRUE` or `FALSE`. The predicate functionals take a vector and a predicate function and do something useful.\
\
`[detect()](https://purrr.tidyverse.org/reference/detect.html) ` `[detect_index()](https://purrr.tidyverse.org/reference/detect.html) `\
\
Find the value or position of the first match\
\
`[every()](https://purrr.tidyverse.org/reference/every.html) ` `[some()](https://purrr.tidyverse.org/reference/every.html) ` `[none()](https://purrr.tidyverse.org/reference/every.html) `\
\
Do every, some, or none of the elements of a list satisfy a predicate?\
\
`[has_element()](https://purrr.tidyverse.org/reference/has_element.html) `\
\
Does a list contain an object?\
\
`[head_while()](https://purrr.tidyverse.org/reference/head_while.html) ` `[tail_while()](https://purrr.tidyverse.org/reference/head_while.html) `\
\
Find head/tail that all satisfies a predicate.\
\
`[keep()](https://purrr.tidyverse.org/reference/keep.html) ` `[discard()](https://purrr.tidyverse.org/reference/keep.html) ` `[compact()](https://purrr.tidyverse.org/reference/keep.html) `\
\
Keep/discard elements based on their values\
\
`[keep_at()](https://purrr.tidyverse.org/reference/keep_at.html) ` `[discard_at()](https://purrr.tidyverse.org/reference/keep_at.html) `\
\
Keep/discard elements based on their name/position\
\
Plucking[](https://purrr.tidyverse.org/reference/index.html#plucking)\
\
----------------------------------------------------------------------\
\
Getting or setting a single element.\
\
`[pluck()](https://purrr.tidyverse.org/reference/pluck.html) ` ``[`pluck<-`()](https://purrr.tidyverse.org/reference/pluck.html) `` `[pluck_exists()](https://purrr.tidyverse.org/reference/pluck.html) `\
\
Safely get or set an element deep within a nested data structure\
\
`[chuck()](https://purrr.tidyverse.org/reference/chuck.html) `\
\
Get an element deep within a nested data structure, failing if it doesn't exist\
\
`[pluck_depth()](https://purrr.tidyverse.org/reference/pluck_depth.html) `\
\
Compute the depth of a vector\
\
`[modify_in()](https://purrr.tidyverse.org/reference/modify_in.html) ` `[assign_in()](https://purrr.tidyverse.org/reference/modify_in.html) `\
\
Modify a pluck location\
\
`[attr_getter()](https://purrr.tidyverse.org/reference/attr_getter.html) `\
\
Create an attribute getter function\
\
Other vector transforms[](https://purrr.tidyverse.org/reference/index.html#other-vector-transforms)\
\
----------------------------------------------------------------------------------------------------\
\
A grab bag of useful tools for manipulating vectors.\
\
`[accumulate()](https://purrr.tidyverse.org/reference/accumulate.html) ` `[accumulate2()](https://purrr.tidyverse.org/reference/accumulate.html) `\
\
Accumulate intermediate results of a vector reduction\
\
`[list_c()](https://purrr.tidyverse.org/reference/list_c.html) ` `[list_cbind()](https://purrr.tidyverse.org/reference/list_c.html) ` `[list_rbind()](https://purrr.tidyverse.org/reference/list_c.html) `\
\
Combine list elements into a single data structure\
\
`[list_flatten()](https://purrr.tidyverse.org/reference/list_flatten.html) `\
\
Flatten a list\
\
`[list_assign()](https://purrr.tidyverse.org/reference/list_assign.html) ` `[list_modify()](https://purrr.tidyverse.org/reference/list_assign.html) ` `[list_merge()](https://purrr.tidyverse.org/reference/list_assign.html) `\
\
Modify a list\
\
`[list_simplify()](https://purrr.tidyverse.org/reference/list_simplify.html) `\
\
Simplify a list to an atomic or S3 vector\
\
`[list_transpose()](https://purrr.tidyverse.org/reference/list_transpose.html) `\
\
Transpose a list\
\
`[reduce()](https://purrr.tidyverse.org/reference/reduce.html) ` `[reduce2()](https://purrr.tidyverse.org/reference/reduce.html) `\
\
Reduce a list to a single value by iteratively applying a binary function\
\
Superseded[](https://purrr.tidyverse.org/reference/index.html#superseded)\
\
--------------------------------------------------------------------------\
\
Superseded functions have been replaced by superior solutions, but due to their widespread use will not go away. However, they will not get any new features and will only receive critical bug fixes.\
\
`[flatten()](https://purrr.tidyverse.org/reference/flatten.html) ` `[flatten_lgl()](https://purrr.tidyverse.org/reference/flatten.html) ` `[flatten_int()](https://purrr.tidyverse.org/reference/flatten.html) ` `[flatten_dbl()](https://purrr.tidyverse.org/reference/flatten.html) ` `[flatten_chr()](https://purrr.tidyverse.org/reference/flatten.html) ` `[flatten_dfr()](https://purrr.tidyverse.org/reference/flatten.html) ` `[flatten_dfc()](https://purrr.tidyverse.org/reference/flatten.html) ` superseded\
\
Flatten a list of lists into a simple vector\
\
`[map_dfr()](https://purrr.tidyverse.org/reference/map_dfr.html) ` `[map_dfc()](https://purrr.tidyverse.org/reference/map_dfr.html) ` `[imap_dfr()](https://purrr.tidyverse.org/reference/map_dfr.html) ` `[imap_dfc()](https://purrr.tidyverse.org/reference/map_dfr.html) ` `[map2_dfr()](https://purrr.tidyverse.org/reference/map_dfr.html) ` `[map2_dfc()](https://purrr.tidyverse.org/reference/map_dfr.html) ` `[pmap_dfr()](https://purrr.tidyverse.org/reference/map_dfr.html) ` `[pmap_dfc()](https://purrr.tidyverse.org/reference/map_dfr.html) ` superseded\
\
Functions that return data frames\
\
`[as_vector()](https://purrr.tidyverse.org/reference/as_vector.html) ` `[simplify()](https://purrr.tidyverse.org/reference/as_vector.html) ` `[simplify_all()](https://purrr.tidyverse.org/reference/as_vector.html) ` superseded\
\
Coerce a list to a vector\
\
`[transpose()](https://purrr.tidyverse.org/reference/transpose.html) ` superseded\
\
Transpose a list.\
\
Adverbs[](https://purrr.tidyverse.org/reference/index.html#adverbs)\
\
--------------------------------------------------------------------\
\
Adverbs modify the action of a function; they take a function as input and return a function with modified action as output.\
\
`[auto_browse()](https://purrr.tidyverse.org/reference/auto_browse.html) `\
\
Wrap a function so it will automatically `browse()` on error\
\
`[compose()](https://purrr.tidyverse.org/reference/compose.html) `\
\
Compose multiple functions together to create a new function\
\
`[insistently()](https://purrr.tidyverse.org/reference/insistently.html) `\
\
Transform a function to wait then retry after an error\
\
`[negate()](https://purrr.tidyverse.org/reference/negate.html) `\
\
Negate a predicate function so it selects what it previously rejected\
\
`[partial()](https://purrr.tidyverse.org/reference/partial.html) `\
\
Partially apply a function, filling in some arguments\
\
`[possibly()](https://purrr.tidyverse.org/reference/possibly.html) `\
\
Wrap a function to return a value instead of an error\
\
`[quietly()](https://purrr.tidyverse.org/reference/quietly.html) `\
\
Wrap a function to capture side-effects\
\
`[safely()](https://purrr.tidyverse.org/reference/safely.html) `\
\
Wrap a function to capture errors\
\
`[slowly()](https://purrr.tidyverse.org/reference/slowly.html) `\
\
Wrap a function to wait between executions\
\
Misc[](https://purrr.tidyverse.org/reference/index.html#misc)\
\
--------------------------------------------------------------\
\
`[array_branch()](https://purrr.tidyverse.org/reference/array-coercion.html) ` `[array_tree()](https://purrr.tidyverse.org/reference/array-coercion.html) `\
\
Coerce array to list\
\
`[rate_delay()](https://purrr.tidyverse.org/reference/rate-helpers.html) ` `[rate_backoff()](https://purrr.tidyverse.org/reference/rate-helpers.html) ` `[is_rate()](https://purrr.tidyverse.org/reference/rate-helpers.html) `\
\
Create delaying rate settings\
\
`[progress_bars](https://purrr.tidyverse.org/reference/progress_bars.html) `\
\
Progress bars in purrr\
\
`[in_parallel()](https://purrr.tidyverse.org/reference/in_parallel.html) ` experimental\
\
Parallelization in purrr