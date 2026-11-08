[Skip to content](https://dplyr.tidyverse.org/reference/index.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Package index
=============

Data frame verbs[](https://dplyr.tidyverse.org/reference/index.html#data-frame-verbs)

--------------------------------------------------------------------------------------

### Rows[](https://dplyr.tidyverse.org/reference/index.html#rows)

Verbs that principally operate on rows.

`[arrange()](https://dplyr.tidyverse.org/reference/arrange.html) `

Order rows using column values

`[distinct()](https://dplyr.tidyverse.org/reference/distinct.html) `

Keep distinct/unique rows

`[filter()](https://dplyr.tidyverse.org/reference/filter.html) ` `[filter_out()](https://dplyr.tidyverse.org/reference/filter.html) `

Keep or drop rows that match a condition

`[slice()](https://dplyr.tidyverse.org/reference/slice.html) ` `[slice_head()](https://dplyr.tidyverse.org/reference/slice.html) ` `[slice_tail()](https://dplyr.tidyverse.org/reference/slice.html) ` `[slice_min()](https://dplyr.tidyverse.org/reference/slice.html) ` `[slice_max()](https://dplyr.tidyverse.org/reference/slice.html) ` `[slice_sample()](https://dplyr.tidyverse.org/reference/slice.html) `

Subset rows using their positions

### Columns[](https://dplyr.tidyverse.org/reference/index.html#columns)

Verbs that principally operate on columns.

`[glimpse](https://dplyr.tidyverse.org/reference/glimpse.html) `

Get a glimpse of your data

`[mutate()](https://dplyr.tidyverse.org/reference/mutate.html) `

Create, modify, and delete columns

`[pull()](https://dplyr.tidyverse.org/reference/pull.html) `

Extract a single column

`[relocate()](https://dplyr.tidyverse.org/reference/relocate.html) `

Change column order

`[rename()](https://dplyr.tidyverse.org/reference/rename.html) ` `[rename_with()](https://dplyr.tidyverse.org/reference/rename.html) `

Rename columns

`[select()](https://dplyr.tidyverse.org/reference/select.html) `

Keep or drop columns using their names and types

### Groups[](https://dplyr.tidyverse.org/reference/index.html#groups)

Verbs that principally operate on groups of rows.

`[count()](https://dplyr.tidyverse.org/reference/count.html) ` `[tally()](https://dplyr.tidyverse.org/reference/count.html) ` `[add_count()](https://dplyr.tidyverse.org/reference/count.html) ` `[add_tally()](https://dplyr.tidyverse.org/reference/count.html) `

Count the observations in each group

`[group_by()](https://dplyr.tidyverse.org/reference/group_by.html) ` `[ungroup()](https://dplyr.tidyverse.org/reference/group_by.html) `

Group by one or more variables

`[dplyr_by](https://dplyr.tidyverse.org/reference/dplyr_by.html) `

Per-operation grouping with `.by`/`by`

`[rowwise()](https://dplyr.tidyverse.org/reference/rowwise.html) `

Group input by rows

`[summarise()](https://dplyr.tidyverse.org/reference/summarise.html) ` `[summarize()](https://dplyr.tidyverse.org/reference/summarise.html) `

Summarise each group down to one row

`[reframe()](https://dplyr.tidyverse.org/reference/reframe.html) `

Transform each group to an arbitrary number of rows

`[n()](https://dplyr.tidyverse.org/reference/context.html) ` `[cur_group()](https://dplyr.tidyverse.org/reference/context.html) ` `[cur_group_id()](https://dplyr.tidyverse.org/reference/context.html) ` `[cur_group_rows()](https://dplyr.tidyverse.org/reference/context.html) ` `[cur_column()](https://dplyr.tidyverse.org/reference/context.html) `

Information about the "current" group or variable

### Data frames[](https://dplyr.tidyverse.org/reference/index.html#data-frames)

Verbs that principally operate on pairs of data frames.

`[bind_cols()](https://dplyr.tidyverse.org/reference/bind_cols.html) `

Bind multiple data frames by column

`[bind_rows()](https://dplyr.tidyverse.org/reference/bind_rows.html) `

Bind multiple data frames by row

`[intersect()](https://dplyr.tidyverse.org/reference/setops.html) ` `[union()](https://dplyr.tidyverse.org/reference/setops.html) ` `[union_all()](https://dplyr.tidyverse.org/reference/setops.html) ` `[setdiff()](https://dplyr.tidyverse.org/reference/setops.html) ` `[setequal()](https://dplyr.tidyverse.org/reference/setops.html) ` `[symdiff()](https://dplyr.tidyverse.org/reference/setops.html) `

Set operations

`[inner_join()](https://dplyr.tidyverse.org/reference/mutate-joins.html) ` `[left_join()](https://dplyr.tidyverse.org/reference/mutate-joins.html) ` `[right_join()](https://dplyr.tidyverse.org/reference/mutate-joins.html) ` `[full_join()](https://dplyr.tidyverse.org/reference/mutate-joins.html) `

Mutating joins

`[nest_join()](https://dplyr.tidyverse.org/reference/nest_join.html) `

Nest join

`[semi_join()](https://dplyr.tidyverse.org/reference/filter-joins.html) ` `[anti_join()](https://dplyr.tidyverse.org/reference/filter-joins.html) `

Filtering joins

`[cross_join()](https://dplyr.tidyverse.org/reference/cross_join.html) `

Cross join

`[join_by()](https://dplyr.tidyverse.org/reference/join_by.html) `

Join specifications

`[rows_insert()](https://dplyr.tidyverse.org/reference/rows.html) ` `[rows_append()](https://dplyr.tidyverse.org/reference/rows.html) ` `[rows_update()](https://dplyr.tidyverse.org/reference/rows.html) ` `[rows_patch()](https://dplyr.tidyverse.org/reference/rows.html) ` `[rows_upsert()](https://dplyr.tidyverse.org/reference/rows.html) ` `[rows_delete()](https://dplyr.tidyverse.org/reference/rows.html) `

Manipulate individual rows

### Multiple columns[](https://dplyr.tidyverse.org/reference/index.html#multiple-columns)

Pair these functions with `[mutate()](https://dplyr.tidyverse.org/reference/mutate.html) `, `[summarise()](https://dplyr.tidyverse.org/reference/summarise.html) `, `[filter()](https://dplyr.tidyverse.org/reference/filter.html) `, and `[group_by()](https://dplyr.tidyverse.org/reference/group_by.html) ` to operate on multiple columns simultaneously.

`[across()](https://dplyr.tidyverse.org/reference/across.html) ` `[if_any()](https://dplyr.tidyverse.org/reference/across.html) ` `[if_all()](https://dplyr.tidyverse.org/reference/across.html) `

Apply a function (or functions) across multiple columns

`[c_across()](https://dplyr.tidyverse.org/reference/c_across.html) `

Combine values from multiple columns

`[pick()](https://dplyr.tidyverse.org/reference/pick.html) `

Select a subset of columns

Vector functions[](https://dplyr.tidyverse.org/reference/index.html#vector-functions)

--------------------------------------------------------------------------------------

Unlike other dplyr functions, these functions work on individual vectors, not data frames.

`[between()](https://dplyr.tidyverse.org/reference/between.html) `

Detect where values fall in a specified range

`[case_when()](https://dplyr.tidyverse.org/reference/case-and-replace-when.html) ` `[replace_when()](https://dplyr.tidyverse.org/reference/case-and-replace-when.html) `

A general vectorised if-else

`[coalesce()](https://dplyr.tidyverse.org/reference/coalesce.html) `

Find the first non-missing element

`[consecutive_id()](https://dplyr.tidyverse.org/reference/consecutive_id.html) `

Generate a unique identifier for consecutive combinations

`[cumall()](https://dplyr.tidyverse.org/reference/cumall.html) ` `[cumany()](https://dplyr.tidyverse.org/reference/cumall.html) ` `[cummean()](https://dplyr.tidyverse.org/reference/cumall.html) `

Cumulative versions of any, all, and mean

`[desc()](https://dplyr.tidyverse.org/reference/desc.html) `

Descending order

`[if_else()](https://dplyr.tidyverse.org/reference/if_else.html) `

Vectorised if-else

`[lag()](https://dplyr.tidyverse.org/reference/lead-lag.html) ` `[lead()](https://dplyr.tidyverse.org/reference/lead-lag.html) `

Compute lagged or leading values

`[n_distinct()](https://dplyr.tidyverse.org/reference/n_distinct.html) `

Count unique combinations

`[na_if()](https://dplyr.tidyverse.org/reference/na_if.html) `

Convert values to `NA`

`[near()](https://dplyr.tidyverse.org/reference/near.html) `

Compare two numeric vectors

`[nth()](https://dplyr.tidyverse.org/reference/nth.html) ` `[first()](https://dplyr.tidyverse.org/reference/nth.html) ` `[last()](https://dplyr.tidyverse.org/reference/nth.html) `

Extract the first, last, or nth value from a vector

`[ntile()](https://dplyr.tidyverse.org/reference/ntile.html) `

Bucket a numeric vector into `n` groups

`[order_by()](https://dplyr.tidyverse.org/reference/order_by.html) `

A helper function for ordering window function output

`[percent_rank()](https://dplyr.tidyverse.org/reference/percent_rank.html) ` `[cume_dist()](https://dplyr.tidyverse.org/reference/percent_rank.html) `

Proportional ranking functions

`[recode_values()](https://dplyr.tidyverse.org/reference/recode-and-replace-values.html) ` `[replace_values()](https://dplyr.tidyverse.org/reference/recode-and-replace-values.html) `

Recode and replace values

`[row_number()](https://dplyr.tidyverse.org/reference/row_number.html) ` `[min_rank()](https://dplyr.tidyverse.org/reference/row_number.html) ` `[dense_rank()](https://dplyr.tidyverse.org/reference/row_number.html) `

Integer ranking functions

`[when_any()](https://dplyr.tidyverse.org/reference/when-any-all.html) ` `[when_all()](https://dplyr.tidyverse.org/reference/when-any-all.html) `

Elementwise `[any()](https://rdrr.io/r/base/any.html) ` and `[all()](https://rdrr.io/r/base/all.html) `

Built in datasets[](https://dplyr.tidyverse.org/reference/index.html#built-in-datasets)

----------------------------------------------------------------------------------------

`[band_members](https://dplyr.tidyverse.org/reference/band_members.html) ` `[band_instruments](https://dplyr.tidyverse.org/reference/band_members.html) ` `[band_instruments2](https://dplyr.tidyverse.org/reference/band_members.html) `

Band membership

`[starwars](https://dplyr.tidyverse.org/reference/starwars.html) `

Starwars characters

`[storms](https://dplyr.tidyverse.org/reference/storms.html) `

Storm tracks data

Grouping helpers[](https://dplyr.tidyverse.org/reference/index.html#grouping-helpers)

--------------------------------------------------------------------------------------

This (mostly) experimental family of functions are used to manipulate groups in various ways.

`[group_cols()](https://dplyr.tidyverse.org/reference/group_cols.html) `

Select grouping variables

`[group_map()](https://dplyr.tidyverse.org/reference/group_map.html) ` `[group_modify()](https://dplyr.tidyverse.org/reference/group_map.html) ` `[group_walk()](https://dplyr.tidyverse.org/reference/group_map.html) ` experimental

Apply a function to each group

`[group_trim()](https://dplyr.tidyverse.org/reference/group_trim.html) ` experimental

Trim grouping structure

Superseded[](https://dplyr.tidyverse.org/reference/index.html#superseded)

--------------------------------------------------------------------------

Superseded functions have been replaced by new approaches that we believe to be superior, but we don’t want to force you to change until you’re ready, so the existing functions will stay around for several years.

`[all_vars()](https://dplyr.tidyverse.org/reference/all_vars.html) ` `[any_vars()](https://dplyr.tidyverse.org/reference/all_vars.html) ` superseded

Apply predicate to all variables

`[recode()](https://dplyr.tidyverse.org/reference/recode.html) ` `[recode_factor()](https://dplyr.tidyverse.org/reference/recode.html) ` superseded

Recode values

`[sample_n()](https://dplyr.tidyverse.org/reference/sample_n.html) ` `[sample_frac()](https://dplyr.tidyverse.org/reference/sample_n.html) ` superseded

Sample n rows from a table

`[scoped](https://dplyr.tidyverse.org/reference/scoped.html) ` superseded

Operate on a selection of variables

`[top_n()](https://dplyr.tidyverse.org/reference/top_n.html) ` `[top_frac()](https://dplyr.tidyverse.org/reference/top_n.html) ` superseded

Select top (or bottom) n rows (by value)

`[vars()](https://dplyr.tidyverse.org/reference/vars.html) ` superseded

Select variables

`[with_groups()](https://dplyr.tidyverse.org/reference/with_groups.html) ` superseded

Perform an operation with temporary groups

Remote tables[](https://dplyr.tidyverse.org/reference/index.html#remote-tables)

--------------------------------------------------------------------------------

`[auto_copy()](https://dplyr.tidyverse.org/reference/auto_copy.html) `

Copy tables to same source, if necessary

`[compute()](https://dplyr.tidyverse.org/reference/compute.html) ` `[collect()](https://dplyr.tidyverse.org/reference/compute.html) ` `[collapse()](https://dplyr.tidyverse.org/reference/compute.html) `

Force computation of a database query

`[copy_to()](https://dplyr.tidyverse.org/reference/copy_to.html) `

Copy a local data frame to a remote src

`[ident()](https://dplyr.tidyverse.org/reference/ident.html) `

Flag a character vector as SQL identifiers

`[explain()](https://dplyr.tidyverse.org/reference/explain.html) ` `[show_query()](https://dplyr.tidyverse.org/reference/explain.html) `

Explain details of a tbl

`[tbl()](https://dplyr.tidyverse.org/reference/tbl.html) ` `[is.tbl()](https://dplyr.tidyverse.org/reference/tbl.html) `

Create a table from a data source

`[sql()](https://dplyr.tidyverse.org/reference/sql.html) `

SQL escaping.