[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.apply.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.DataFrameGroupBy.apply.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.apply.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.DataFrameGroupBy.apply.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.DataFrameGroupBy.apply.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.DataFrameGroupBy.apply.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.DataFrameGroupBy.apply.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.DataFrameGroupBy.apply.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.DataFrameGroupBy.apply.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.DataFrameGroupBy.apply.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.DataFrameGroupBy.apply.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.DataFrameGroupBy.apply.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.DataFrameGroupBy.apply.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.DataFrameGroupBy.apply.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.apply[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.apply.html#pandas-api-typing-dataframegroupby-apply "Link to this heading")

========================================================================================================================================================================================================

DataFrameGroupBy.apply(_func_, _\*args_, _include\_groups\=False_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L1250-L1420)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.apply.html#pandas.api.typing.DataFrameGroupBy.apply "Link to this definition")

Apply function `func` group-wise and combine the results together.

The function passed to `apply` must take a dataframe as its first argument and return a DataFrame, Series or scalar. `apply` will then take care of combining the results back together into a single dataframe or series. `apply` is therefore a highly flexible grouping method.

While `apply` is a very flexible method, its downside is that using it can be quite a bit slower than using more specific methods like `agg` or `transform`. Pandas offers a wide range of method that will be much faster than using `apply` for their specific purposes, so try to use them before reaching for `apply`.

Parameters:

**func**callable

A callable that takes a dataframe as its first argument, and returns a dataframe, a series or a scalar. In addition the callable may take positional and keyword arguments.

**\*args**tuple

Optional positional arguments to pass to `func`.

**include\_groups**bool, default False

When True, will attempt to apply `func` to the groupings in the case that they are columns of the DataFrame. If this raises a TypeError, the result will be computed with the groupings excluded. When False, the groupings will be excluded when applying `func`.

Added in version 2.2.0.

Changed in version 3.0.0.

The default changed from True to False, and True is no longer allowed.

**\*\*kwargs**dict

Optional keyword arguments to pass to `func`.

Returns:

Series or DataFrame

A pandas object with the result of applying `func` to each group.

See also

[`pipe`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.pipe.html#pandas.api.typing.DataFrameGroupBy.pipe "pandas.api.typing.DataFrameGroupBy.pipe")

Apply function to the full GroupBy object instead of to each group.

[`aggregate`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.aggregate.html#pandas.api.typing.DataFrameGroupBy.aggregate "pandas.api.typing.DataFrameGroupBy.aggregate")

Apply aggregate function to the GroupBy object.

[`transform`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.transform.html#pandas.api.typing.DataFrameGroupBy.transform "pandas.api.typing.DataFrameGroupBy.transform")

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

Each group passed to `func` has a `name` attribute set to the group key (the value of the grouping for that group). This is useful for identifying the current group, for example when grouping by an external grouper rather than by a column of the object.

Examples

\>>> df \= pd.DataFrame({"A": "a a b".split(), "B": \[1, 2, 3\], "C": \[4, 6, 5\]})
\>>> g1 \= df.groupby("A", group\_keys\=False)
\>>> g2 \= df.groupby("A", group\_keys\=True)

Copy to clipboard

Notice that `g1` and `g2` have two groups, `a` and `b`, and only differ in their `group_keys` argument. Calling apply in various ways, we can get different grouping results:

Example 1: below the function passed to apply takes a DataFrame as its argument and returns a DataFrame. apply combines the result for each group together into a new DataFrame:

\>>> g1\[\["B", "C"\]\].apply(lambda x: x / x.sum())
          B    C
0  0.333333  0.4
1  0.666667  0.6
2  1.000000  1.0

Copy to clipboard

In the above, the groups are not part of the index. We can have them included by using `g2` where `group_keys=True`:

\>>> g2\[\["B", "C"\]\].apply(lambda x: x / x.sum())
            B    C
A
a 0  0.333333  0.4
  1  0.666667  0.6
b 2  1.000000  1.0

Copy to clipboard

Example 2: The function passed to apply takes a DataFrame as its argument and returns a Series. apply combines the result for each group together into a new DataFrame.

The resulting dtype will reflect the return value of the passed `func`.

\>>> g1\[\["B", "C"\]\].apply(lambda x: x.astype(float).max() \- x.min())
     B    C
A
a  1.0  2.0
b  0.0  0.0

Copy to clipboard

\>>> g2\[\["B", "C"\]\].apply(lambda x: x.astype(float).max() \- x.min())
     B    C
A
a  1.0  2.0
b  0.0  0.0

Copy to clipboard

The `group_keys` argument has no effect here because the result is not like-indexed (i.e. [a transform](https://pandas.pydata.org/docs/user_guide/groupby.html#groupby-transform)
) when compared to the input.

Example 3: The function passed to apply takes a DataFrame as its argument and returns a scalar. apply combines the result for each group together into a Series, including setting the index as appropriate:

\>>> g1.apply(lambda x: x.C.max() \- x.B.min())
A
a    5
b    2
dtype: int64

Copy to clipboard

Example 4: The function passed to `apply` returns `None` for one of the group. This group is filtered from the result:

\>>> g1.apply(lambda x: None if x.iloc\[0, 0\] \== 3 else x)
   B  C
0  1  4
1  2  6

Copy to clipboard

On this page