[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.count.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.count.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.count.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.count.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.count.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.count.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.count.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.count.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.count.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.count.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.count.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.count.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.count.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.count.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.count[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.count.html#pandas-api-typing-seriesgroupby-count "Link to this heading")

===============================================================================================================================================================================================

SeriesGroupBy.count()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L1875-L1979)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.count.html#pandas.api.typing.SeriesGroupBy.count "Link to this definition")

Compute count of group, excluding missing values.

Returns the number of non-NA/null observations per group.

Returns:

Series or DataFrame

Count of values within each group.

See also

`Series.count`

Apply function count to a Series.

`DataFrame.count`

Apply function count to each row or column of a DataFrame.

Examples

For SeriesGroupBy:

\>>> lst \= \["a", "a", "b"\]
\>>> ser \= pd.Series(\[1, 2, np.nan\], index\=lst)
\>>> ser
a    1.0
a    2.0
b    NaN
dtype: float64
\>>> ser.groupby(level\=0).count()
a    2
b    0
dtype: int64

Copy to clipboard

For DataFrameGroupBy:

\>>> data \= \[\[1, np.nan, 3\], \[1, np.nan, 6\], \[7, 8, 9\]\]
\>>> df \= pd.DataFrame(
...     data, columns\=\["a", "b", "c"\], index\=\["cow", "horse", "bull"\]
... )
\>>> df
        a         b     c
cow     1       NaN     3
horse   1       NaN     6
bull    7       8.0     9
\>>> df.groupby("a").count()
    b   c
a
1   0   2
7   1   1

Copy to clipboard

For Resampler:

\>>> ser \= pd.Series(
...     \[1, 2, 3, 4\],
...     index\=pd.DatetimeIndex(
...         \["2023-01-01", "2023-01-15", "2023-02-01", "2023-02-15"\]
...     ),
... )
\>>> ser
2023-01-01    1
2023-01-15    2
2023-02-01    3
2023-02-15    4
dtype: int64
\>>> ser.resample("MS").count()
2023-01-01    2
2023-02-01    2
Freq: MS, dtype: int64

Copy to clipboard

On this page