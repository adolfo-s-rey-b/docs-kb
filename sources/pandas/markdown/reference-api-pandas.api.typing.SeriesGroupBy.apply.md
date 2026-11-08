[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.apply.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.apply[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.apply.html#pandas-api-typing-seriesgroupby-apply "Link to this heading")

===============================================================================================================================================================================================

SeriesGroupBy.apply(_func_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L213-L322)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.apply.html#pandas.api.typing.SeriesGroupBy.apply "Link to this definition")

Apply function `func` group-wise and combine the results together.

The function passed to `apply` must take a series as its first argument and return a DataFrame, Series or scalar. `apply` will then take care of combining the results back together into a single dataframe or series. `apply` is therefore a highly flexible grouping method.

While `apply` is a very flexible method, its downside is that using it can be quite a bit slower than using more specific methods like `agg` or `transform`. Pandas offers a wide range of method that will be much faster than using `apply` for their specific purposes, so try to use them before reaching for `apply`.

Parameters:

**func**callable

A callable that takes a series as its first argument, and returns a dataframe, a series or a scalar. In addition the callable may take positional and keyword arguments.

**\*args**tuple

Optional positional arguments to pass to `func`.

**\*\*kwargs**dict

Optional keyword arguments to pass to `func`.

Returns:

Series or DataFrame

A pandas object with the result of applying `func` to each group.

See also

[`pipe`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.pipe.html#pandas.api.typing.SeriesGroupBy.pipe "pandas.api.typing.SeriesGroupBy.pipe")

Apply function to the full GroupBy object instead of to each group.

[`aggregate`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.aggregate.html#pandas.api.typing.SeriesGroupBy.aggregate "pandas.api.typing.SeriesGroupBy.aggregate")

Apply aggregate function to the GroupBy object.

[`transform`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.transform.html#pandas.api.typing.SeriesGroupBy.transform "pandas.api.typing.SeriesGroupBy.transform")

Apply function column-by-column to the GroupBy object.

`Series.apply`

Apply a function to a Series.

`DataFrame.apply`

Apply a function to each row or column of a DataFrame.

Notes

See [Flexible apply](https://pandas.pydata.org/docs/user_guide/groupby.html#groupby-apply)
 in the User Guide for more details and examples.

The resulting dtype will reflect the return value of the passed `func`, see the examples below.

Functions that mutate the passed object can produce unexpected behavior or errors and are not supported. See [Mutating with User Defined Function (UDF) methods](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-udf-mutation)
 for more details.

Each group passed to `func` has a `name` attribute set to the group key (the value of the grouping for that group). This is useful for identifying the current group, as in the examples below.

Examples

\>>> s \= pd.Series(\[0, 1, 2\], index\="a a b".split())
\>>> g1 \= s.groupby(s.index, group\_keys\=False)
\>>> g2 \= s.groupby(s.index, group\_keys\=True)

Copy to clipboard

From `s` above we can see that `g` has two groups, `a` and `b`. Notice that `g1` have `g2` have two groups, `a` and `b`, and only differ in their `group_keys` argument. Calling apply in various ways, we can get different grouping results:

Example 1: The function passed to apply takes a Series as its argument and returns a Series. apply combines the result for each group together into a new Series.

The resulting dtype will reflect the return value of the passed `func`.

\>>> g1.apply(lambda x: x \* 2 if x.name \== "a" else x / 2)
a    0.0
a    2.0
b    1.0
dtype: float64

Copy to clipboard

In the above, the groups are not part of the index. We can have them included by using `g2` where `group_keys=True`:

\>>> g2.apply(lambda x: x \* 2 if x.name \== "a" else x / 2)
a  a    0.0
   a    2.0
b  b    1.0
dtype: float64

Copy to clipboard

Example 2: The function passed to apply takes a Series as its argument and returns a scalar. apply combines the result for each group together into a Series, including setting the index as appropriate:

\>>> g1.apply(lambda x: x.max() \- x.min())
a    1
b    0
dtype: int64

Copy to clipboard

The `group_keys` argument has no effect here because the result is not like-indexed (i.e. [a transform](https://pandas.pydata.org/docs/user_guide/groupby.html#groupby-transform)
) when compared to the input.

\>>> g2.apply(lambda x: x.max() \- x.min())
a    1
b    0
dtype: int64

Copy to clipboard

On this page