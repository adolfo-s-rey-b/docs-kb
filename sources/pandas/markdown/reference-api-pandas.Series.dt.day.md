[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.day.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.day.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.day.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.day.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.day.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.day.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.day.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.day.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.day.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.day.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.day.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.day.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.day.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.day.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.day[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.day.html#pandas-series-dt-day "Link to this heading")

============================================================================================================================================

Series.dt.day[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L108-L109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.day.html#pandas.Series.dt.day "Link to this definition")

The day of the datetime.

This attribute returns the day of the month component of each datetime value in the Series/Index. Values range from 1 to 31, depending on the month.

See also

[`DatetimeIndex.year`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.year.html#pandas.DatetimeIndex.year "pandas.DatetimeIndex.year")

The year of the datetime.

[`DatetimeIndex.month`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.month.html#pandas.DatetimeIndex.month "pandas.DatetimeIndex.month")

The month as January=1, December=12.

[`DatetimeIndex.hour`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.hour.html#pandas.DatetimeIndex.hour "pandas.DatetimeIndex.hour")

The hours of the datetime.

Examples

\>>> datetime\_series \= pd.Series(
...     pd.date\_range("2000-01-01", periods\=3, freq\="D")
... )
\>>> datetime\_series
0   2000-01-01
1   2000-01-02
2   2000-01-03
dtype: datetime64\[us\]
\>>> datetime\_series.dt.day
0    1
1    2
2    3
dtype: int32

Copy to clipboard

On this page