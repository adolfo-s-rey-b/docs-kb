[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.second.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.second.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.second.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.second.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.second.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.second.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.second.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.second.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.second.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.second.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.second.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.second.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.second.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.second.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.second[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.second.html#pandas-series-dt-second "Link to this heading")

=====================================================================================================================================================

Series.dt.second[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L108-L109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.second.html#pandas.Series.dt.second "Link to this definition")

The seconds of the datetime.

This attribute returns the second component of each datetime value in the Series/Index. Values range from 0 to 59.

See also

[`DatetimeIndex.minute`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.minute.html#pandas.DatetimeIndex.minute "pandas.DatetimeIndex.minute")

The minutes of the datetime.

[`DatetimeIndex.microsecond`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.microsecond.html#pandas.DatetimeIndex.microsecond "pandas.DatetimeIndex.microsecond")

The microseconds of the datetime.

[`DatetimeIndex.nanosecond`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.nanosecond.html#pandas.DatetimeIndex.nanosecond "pandas.DatetimeIndex.nanosecond")

The nanoseconds of the datetime.

Examples

\>>> datetime\_series \= pd.Series(
...     pd.date\_range("2000-01-01", periods\=3, freq\="s")
... )
\>>> datetime\_series
0   2000-01-01 00:00:00
1   2000-01-01 00:00:01
2   2000-01-01 00:00:02
dtype: datetime64\[us\]
\>>> datetime\_series.dt.second
0    0
1    1
2    2
dtype: int32

Copy to clipboard

On this page