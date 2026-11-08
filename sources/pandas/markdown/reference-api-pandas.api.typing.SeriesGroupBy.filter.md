[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.filter.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.filter.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.filter.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.filter.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.filter.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.filter.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.filter.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.filter.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.filter.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.filter.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.filter.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.filter.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.filter.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.filter.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.filter[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.filter.html#pandas-api-typing-seriesgroupby-filter "Link to this heading")

==================================================================================================================================================================================================

SeriesGroupBy.filter(_func_, _dropna\=True_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L817-L888)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.filter.html#pandas.api.typing.SeriesGroupBy.filter "Link to this definition")

Filter elements from groups that don’t satisfy a criterion.

Elements from groups are filtered if they do not satisfy the boolean criterion specified by func.

Parameters:

**func**function

Criterion to apply to each group. Should return True or False.

**dropna**bool, optional

Drop groups that do not pass the filter. True by default; if False, groups that evaluate False are filled with NaNs.

**\*args**tuple

Optional positional arguments to pass to func.

**\*\*kwargs**dict

Optional keyword arguments to pass to func.

Returns:

Series

The filtered subset of the original Series.

See also

`Series.filter`

Filter elements of ungrouped Series.

[`DataFrameGroupBy.filter`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.filter.html#pandas.api.typing.DataFrameGroupBy.filter "pandas.api.typing.DataFrameGroupBy.filter")

Filter elements from groups based on criterion.

Notes

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
\>>> df.groupby("A").B.filter(lambda x: x.mean() \> 3.0)
1    2
3    4
5    6
Name: B, dtype: int64

Copy to clipboard

On this page