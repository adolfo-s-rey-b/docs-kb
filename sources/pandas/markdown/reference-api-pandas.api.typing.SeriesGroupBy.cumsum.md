[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.cumsum.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.cumsum.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.cumsum.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.cumsum.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.cumsum.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.cumsum.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.cumsum.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.cumsum.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.cumsum.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.cumsum.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.cumsum.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.cumsum.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.cumsum.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.cumsum.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.cumsum[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.cumsum.html#pandas-api-typing-seriesgroupby-cumsum "Link to this heading")

==================================================================================================================================================================================================

SeriesGroupBy.cumsum(_numeric\_only\=False_, _skipna\=True_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L4874-L4963)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.cumsum.html#pandas.api.typing.SeriesGroupBy.cumsum "Link to this definition")

Cumulative sum for each group.

Returns a Series or DataFrame of the same size with the cumulative sum computed within each group.

Parameters:

**numeric\_only**bool, default False

Include only float, int, boolean columns.

**skipna**bool, default True

Exclude NA/null values. If an entire row/column is NA, the result will be NA.

**\*args**tuple

Positional arguments to be passed to func.

Deprecated since version 3.1.0: Passing `*args` to GroupBy.cumsum is deprecated and will be removed in a future version of pandas.

**\*\*kwargs**dict

Additional keyword arguments to be passed to the function.

Deprecated since version 3.1.0: Passing `**kwargs` to GroupBy.cumsum is deprecated and will be removed in a future version of pandas.

Returns:

Series or DataFrame

Cumulative sum for each group. Same object type as the caller.

See also

`Series.cumsum`

Apply function cumsum to a Series.

`DataFrame.cumsum`

Apply function cumsum to each row or column of a DataFrame.

Examples

For SeriesGroupBy:

\>>> lst \= \["a", "a", "b"\]
\>>> ser \= pd.Series(\[6, 2, 0\], index\=lst)
\>>> ser
a    6
a    2
b    0
dtype: int64
\>>> ser.groupby(level\=0).cumsum()
a    6
a    8
b    0
dtype: int64

Copy to clipboard

For DataFrameGroupBy:

\>>> data \= \[\[1, 8, 2\], \[1, 2, 5\], \[2, 6, 9\]\]
\>>> df \= pd.DataFrame(
...     data, columns\=\["a", "b", "c"\], index\=\["fox", "gorilla", "lion"\]
... )
\>>> df
          a   b   c
fox       1   8   2
gorilla   1   2   5
lion      2   6   9
\>>> df.groupby("a").groups
{1: \['fox', 'gorilla'\], 2: \['lion'\]}
\>>> df.groupby("a").cumsum()
          b   c
fox       8   2
gorilla  10   7
lion      6   9

Copy to clipboard

On this page