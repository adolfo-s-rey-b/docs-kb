[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.minute.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.minute[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.minute.html#pandas-series-dt-minute "Link to this heading")

=====================================================================================================================================================

Series.dt.minute[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L108-L109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.minute.html#pandas.Series.dt.minute "Link to this definition")

The minutes of the datetime.

This attribute returns the minute component of each datetime value in the Series/Index. Values range from 0 to 59.

See also

[`DatetimeIndex.hour`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.hour.html#pandas.DatetimeIndex.hour "pandas.DatetimeIndex.hour")

The hours of the datetime.

[`DatetimeIndex.second`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.second.html#pandas.DatetimeIndex.second "pandas.DatetimeIndex.second")

The seconds of the datetime.

Examples

\>>> datetime\_series \= pd.Series(
...     pd.date\_range("2000-01-01", periods\=3, freq\="min")
... )
\>>> datetime\_series
0   2000-01-01 00:00:00
1   2000-01-01 00:01:00
2   2000-01-01 00:02:00
dtype: datetime64\[us\]
\>>> datetime\_series.dt.minute
0    0
1    1
2    2
dtype: int32

Copy to clipboard

On this page