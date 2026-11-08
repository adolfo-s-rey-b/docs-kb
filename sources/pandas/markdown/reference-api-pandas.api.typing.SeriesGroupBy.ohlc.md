[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.ohlc.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.ohlc.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.ohlc.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.ohlc.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.ohlc.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.ohlc.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.ohlc.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.ohlc.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.ohlc.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.ohlc.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.ohlc.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.ohlc.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.ohlc.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.ohlc.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.ohlc[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.ohlc.html#pandas-api-typing-seriesgroupby-ohlc "Link to this heading")

============================================================================================================================================================================================

SeriesGroupBy.ohlc()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L3357-L3471)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.ohlc.html#pandas.api.typing.SeriesGroupBy.ohlc "Link to this definition")

Compute open, high, low and close values of a group, excluding missing values.

For multiple groupings, the result index will be a MultiIndex

Returns:

DataFrame

Open, high, low and close values within each group.

See also

`DataFrame.agg`

Aggregate using one or more operations over the specified axis.

`DataFrame.resample`

Resample time-series data.

`DataFrame.groupby`

Group DataFrame using a mapper or by a Series of columns.

Examples

For SeriesGroupBy:

\>>> lst \= \[\
...     "SPX",\
...     "CAC",\
...     "SPX",\
...     "CAC",\
...     "SPX",\
...     "CAC",\
...     "SPX",\
...     "CAC",\
... \]
\>>> ser \= pd.Series(\[3.4, 9.0, 7.2, 5.2, 8.8, 9.4, 0.1, 0.5\], index\=lst)
\>>> ser
SPX     3.4
CAC     9.0
SPX     7.2
CAC     5.2
SPX     8.8
CAC     9.4
SPX     0.1
CAC     0.5
dtype: float64
\>>> ser.groupby(level\=0).ohlc()
     open  high  low  close
CAC   9.0   9.4  0.5    0.5
SPX   3.4   8.8  0.1    0.1

Copy to clipboard

For DataFrameGroupBy:

\>>> data \= {
...     2022: \[1.2, 2.3, 8.9, 4.5, 4.4, 3, 2, 1\],
...     2023: \[3.4, 9.0, 7.2, 5.2, 8.8, 9.4, 8.2, 1.0\],
... }
\>>> df \= pd.DataFrame(
...     data, index\=\["SPX", "CAC", "SPX", "CAC", "SPX", "CAC", "SPX", "CAC"\]
... )
\>>> df
     2022  2023
SPX   1.2   3.4
CAC   2.3   9.0
SPX   8.9   7.2
CAC   4.5   5.2
SPX   4.4   8.8
CAC   3.0   9.4
SPX   2.0   8.2
CAC   1.0   1.0
\>>> df.groupby(level\=0).ohlc()
    2022                 2023
    open high  low close open high  low close
CAC  2.3  4.5  1.0   1.0  9.0  9.4  1.0   1.0
SPX  1.2  8.9  1.2   2.0  3.4  8.8  3.4   8.2

Copy to clipboard

For Resampler:

\>>> ser \= pd.Series(
...     \[1, 3, 2, 4, 3, 5\],
...     index\=pd.DatetimeIndex(
...         \[\
...             "2023-01-01",\
...             "2023-01-10",\
...             "2023-01-15",\
...             "2023-02-01",\
...             "2023-02-10",\
...             "2023-02-15",\
...         \]
...     ),
... )
\>>> ser.resample("MS").ohlc()
            open  high  low  close
2023-01-01     1     3    1      2
2023-02-01     4     5    3      5

Copy to clipboard

On this page