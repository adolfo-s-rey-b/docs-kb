[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.cummax.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.cummax.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.cummax.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.cummax.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.cummax.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.cummax.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.cummax.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.cummax.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.cummax.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.cummax.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.cummax.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.cummax.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.cummax.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.cummax.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.cummax[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.cummax.html#pandas-api-typing-seriesgroupby-cummax "Link to this heading")

==================================================================================================================================================================================================

SeriesGroupBy.cummax(_numeric\_only\=False_, _skipna\=True_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L5055-L5144)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.cummax.html#pandas.api.typing.SeriesGroupBy.cummax "Link to this definition")

Cumulative max for each group.

Returns the cumulative maximum of values within each group. The result has the same size as the input, with each element representing the maximum of all preceding elements (including itself) within its group.

Parameters:

**numeric\_only**bool, default False

Include only float, int or boolean data.

**skipna**bool, default True

Exclude NA/null values. If an entire row/column is NA, the result will be NA.

**\*\*kwargs**dict, optional

Additional keyword arguments to be passed to the function.

Deprecated since version 3.1.0: Passing `**kwargs` to GroupBy.cummax is deprecated and will be removed in a future version of pandas.

Returns:

Series or DataFrame

Cumulative max for each group. Same object type as the caller.

See also

`Series.cummax`

Apply function cummax to a Series.

`DataFrame.cummax`

Apply function cummax to each row or column of a DataFrame.

Examples

For SeriesGroupBy:

\>>> lst \= \["a", "a", "a", "b", "b", "b"\]
\>>> ser \= pd.Series(\[1, 6, 2, 3, 1, 4\], index\=lst)
\>>> ser
a    1
a    6
a    2
b    3
b    1
b    4
dtype: int64
\>>> ser.groupby(level\=0).cummax()
a    1
a    6
a    6
b    3
b    3
b    4
dtype: int64

Copy to clipboard

For DataFrameGroupBy:

\>>> data \= \[\[1, 8, 2\], \[1, 1, 0\], \[2, 6, 9\]\]
\>>> df \= pd.DataFrame(
...     data, columns\=\["a", "b", "c"\], index\=\["cow", "horse", "bull"\]
... )
\>>> df
        a   b   c
cow     1   8   2
horse   1   1   0
bull    2   6   9
\>>> df.groupby("a").groups
{1: \['cow', 'horse'\], 2: \['bull'\]}
\>>> df.groupby("a").cummax()
        b   c
cow     8   2
horse   8   2
bull    6   9

Copy to clipboard

On this page