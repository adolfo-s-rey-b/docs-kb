[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.nanosecond.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.nanosecond.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.nanosecond.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.nanosecond.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.nanosecond.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.nanosecond.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.nanosecond.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.nanosecond.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.nanosecond.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.nanosecond.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.nanosecond.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.nanosecond.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.nanosecond.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.nanosecond.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.nanosecond[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.nanosecond.html#pandas-series-dt-nanosecond "Link to this heading")

=================================================================================================================================================================

Series.dt.nanosecond[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L108-L109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.nanosecond.html#pandas.Series.dt.nanosecond "Link to this definition")

The nanoseconds of the datetime.

This attribute returns the nanosecond component of each datetime value in the Series/Index. Values range from 0 to 999 (one nanosecond is one billionth of a second).

See also

[`DatetimeIndex.second`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.second.html#pandas.DatetimeIndex.second "pandas.DatetimeIndex.second")

The seconds of the datetime.

[`DatetimeIndex.microsecond`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.microsecond.html#pandas.DatetimeIndex.microsecond "pandas.DatetimeIndex.microsecond")

The microseconds of the datetime.

Examples

\>>> datetime\_series \= pd.Series(
...     pd.date\_range("2000-01-01", periods\=3, freq\="ns")
... )
\>>> datetime\_series
0   2000-01-01 00:00:00.000000000
1   2000-01-01 00:00:00.000000001
2   2000-01-01 00:00:00.000000002
dtype: datetime64\[ns\]
\>>> datetime\_series.dt.nanosecond
0       0
1       1
2       2
dtype: int32

Copy to clipboard

On this page