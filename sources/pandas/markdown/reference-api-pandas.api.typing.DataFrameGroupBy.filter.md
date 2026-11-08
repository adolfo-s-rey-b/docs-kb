[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.filter.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.DataFrameGroupBy.filter.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.filter.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.DataFrameGroupBy.filter.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.DataFrameGroupBy.filter.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.DataFrameGroupBy.filter.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.DataFrameGroupBy.filter.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.DataFrameGroupBy.filter.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.DataFrameGroupBy.filter.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.DataFrameGroupBy.filter.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.DataFrameGroupBy.filter.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.DataFrameGroupBy.filter.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.DataFrameGroupBy.filter.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.DataFrameGroupBy.filter.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.filter[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.filter.html#pandas-api-typing-dataframegroupby-filter "Link to this heading")

===========================================================================================================================================================================================================

DataFrameGroupBy.filter(_func_, _dropna\=True_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L2909-L2991)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.filter.html#pandas.api.typing.DataFrameGroupBy.filter "Link to this definition")

Filter elements from groups that don’t satisfy a criterion.

Elements from groups are filtered if they do not satisfy the boolean criterion specified by func.

Parameters:

**func**function

Criterion to apply to each group. Should return True or False.

**dropna**bool

Drop groups that do not pass the filter. True by default; if False, groups that evaluate False are filled with NaNs.

**\*args**tuple

Additional positional arguments to pass to func.

**\*\*kwargs**dict

Additional keyword arguments to pass to func.

Returns:

DataFrame

The filtered subset of the original DataFrame.

See also

`DataFrame.filter`

Filter elements of ungrouped DataFrame.

[`SeriesGroupBy.filter`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.filter.html#pandas.api.typing.SeriesGroupBy.filter "pandas.api.typing.SeriesGroupBy.filter")

Filter elements from groups based on criterion.

Notes

Each subframe is endowed the attribute ‘name’ in case you need to know which group you are working on.

Functions that mutate the passed object can produce unexpected behavior or errors and are not supported. See [Mutating with User Defined Function (UDF) methods](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-udf-mutation)
 for more details.

Examples

\>>> df \= pd.DataFrame(
...     {
...         "A": \["foo", "bar", "foo", "bar", "foo", "bar"\],
...         "B": \[1, 2, 3, 4, 5, 6\],
...         "C": \[2.0, 5.0, 8.0, 1.0, 2.0, 9.0\],
...     }
... )
\>>> grouped \= df.groupby("A")
\>>> grouped.filter(lambda x: x\["B"\].mean() \> 3.0)
     A  B    C
1  bar  2  5.0
3  bar  4  1.0
5  bar  6  9.0

Copy to clipboard

On this page