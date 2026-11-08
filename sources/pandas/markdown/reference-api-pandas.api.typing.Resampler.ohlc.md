[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.ohlc.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Resampler.ohlc.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.ohlc.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Resampler.ohlc.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Resampler.ohlc.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Resampler.ohlc.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Resampler.ohlc.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Resampler.ohlc.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Resampler.ohlc.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Resampler.ohlc.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Resampler.ohlc.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Resampler.ohlc.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Resampler.ohlc.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Resampler.ohlc.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Resampler.ohlc[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.ohlc.html#pandas-api-typing-resampler-ohlc "Link to this heading")

================================================================================================================================================================================

final Resampler.ohlc()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/resample.py#L1742-L1797)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.ohlc.html#pandas.api.typing.Resampler.ohlc "Link to this definition")

Compute open, high, low and close values of a group, excluding missing values.

This method computes OHLC (Open-High-Low-Close) values, commonly used in financial data analysis to summarize price movements within time periods.

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