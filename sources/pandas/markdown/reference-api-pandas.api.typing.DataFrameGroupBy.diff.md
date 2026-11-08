[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.diff.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.DataFrameGroupBy.diff.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.diff.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.DataFrameGroupBy.diff.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.DataFrameGroupBy.diff.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.DataFrameGroupBy.diff.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.DataFrameGroupBy.diff.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.DataFrameGroupBy.diff.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.DataFrameGroupBy.diff.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.DataFrameGroupBy.diff.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.DataFrameGroupBy.diff.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.DataFrameGroupBy.diff.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.DataFrameGroupBy.diff.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.DataFrameGroupBy.diff.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.diff[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.diff.html#pandas-api-typing-dataframegroupby-diff "Link to this heading")

=====================================================================================================================================================================================================

DataFrameGroupBy.diff(_periods\=1_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L5290-L5378)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.diff.html#pandas.api.typing.DataFrameGroupBy.diff "Link to this definition")

First discrete difference of element.

Calculates the difference of each element compared with another element in the group (default is element in previous row).

Parameters:

**periods**int, default 1

Periods to shift for calculating difference, accepts negative values.

Returns:

Series or DataFrame

First differences.

See also

`Series.diff`

Apply function diff to a Series.

`DataFrame.diff`

Apply function diff to each row or column of a DataFrame.

Examples

For SeriesGroupBy:

\>>> lst \= \["a", "a", "a", "b", "b", "b"\]
\>>> ser \= pd.Series(\[7, 2, 8, 4, 3, 3\], index\=lst)
\>>> ser
a     7
a     2
a     8
b     4
b     3
b     3
dtype: int64
\>>> ser.groupby(level\=0).diff()
a    NaN
a   -5.0
a    6.0
b    NaN
b   -1.0
b    0.0
dtype: float64

Copy to clipboard

For DataFrameGroupBy:

\>>> data \= {"a": \[1, 3, 5, 7, 7, 8, 3\], "b": \[1, 4, 8, 4, 4, 2, 1\]}
\>>> df \= pd.DataFrame(
...     data, index\=\["dog", "dog", "dog", "mouse", "mouse", "mouse", "mouse"\]
... )
\>>> df
         a  b
  dog    1  1
  dog    3  4
  dog    5  8
mouse    7  4
mouse    7  4
mouse    8  2
mouse    3  1
\>>> df.groupby(level\=0).diff()
         a    b
  dog  NaN  NaN
  dog  2.0  3.0
  dog  2.0  4.0
mouse  NaN  NaN
mouse  0.0  0.0
mouse  1.0 -2.0
mouse -5.0 -1.0

Copy to clipboard

On this page