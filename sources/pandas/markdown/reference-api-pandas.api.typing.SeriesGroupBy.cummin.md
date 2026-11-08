[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.cummin.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.cummin.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.cummin.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.cummin.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.cummin.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.cummin.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.cummin.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.cummin.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.cummin.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.cummin.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.cummin.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.cummin.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.cummin.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.cummin.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.cummin[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.cummin.html#pandas-api-typing-seriesgroupby-cummin "Link to this heading")

==================================================================================================================================================================================================

SeriesGroupBy.cummin(_numeric\_only\=False_, _skipna\=True_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L4965-L5053)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.cummin.html#pandas.api.typing.SeriesGroupBy.cummin "Link to this definition")

Cumulative min for each group.

Returns a same-sized object where each value is replaced by the minimum of all preceding values in its group.

Parameters:

**numeric\_only**bool, default False

Include only float, int or boolean data.

**skipna**bool, default True

Exclude NA/null values. If an entire row/column is NA, the result will be NA.

**\*\*kwargs**dict, optional

Additional keyword arguments to be passed to the function.

Deprecated since version 3.1.0: Passing `**kwargs` to GroupBy.cummin is deprecated and will be removed in a future version of pandas.

Returns:

Series or DataFrame

Cumulative min for each group. Same object type as the caller.

See also

`Series.cummin`

Apply function cummin to a Series.

`DataFrame.cummin`

Apply function cummin to each row or column of a DataFrame.

Examples

For SeriesGroupBy:

\>>> lst \= \["a", "a", "a", "b", "b", "b"\]
\>>> ser \= pd.Series(\[1, 6, 2, 3, 0, 4\], index\=lst)
\>>> ser
a    1
a    6
a    2
b    3
b    0
b    4
dtype: int64
\>>> ser.groupby(level\=0).cummin()
a    1
a    1
a    1
b    3
b    0
b    0
dtype: int64

Copy to clipboard

For DataFrameGroupBy:

\>>> data \= \[\[1, 0, 2\], \[1, 1, 5\], \[6, 6, 9\]\]
\>>> df \= pd.DataFrame(
...     data, columns\=\["a", "b", "c"\], index\=\["snake", "rabbit", "turtle"\]
... )
\>>> df
        a   b   c
snake   1   0   2
rabbit  1   1   5
turtle  6   6   9
\>>> df.groupby("a").groups
{1: \['snake', 'rabbit'\], 6: \['turtle'\]}
\>>> df.groupby("a").cummin()
        b   c
snake   0   2
rabbit  0   2
turtle  6   9

Copy to clipboard

On this page