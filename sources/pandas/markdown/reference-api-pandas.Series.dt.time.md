[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.time.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.time.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.time.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.time.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.time.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.time.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.time.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.time.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.time.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.time.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.time.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.time.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.time.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.time.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.time[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.time.html#pandas-series-dt-time "Link to this heading")

===============================================================================================================================================

Series.dt.time[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L108-L109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.time.html#pandas.Series.dt.time "Link to this definition")

Returns numpy array of [`datetime.time`](https://docs.python.org/3/library/datetime.html#datetime.time "(in Python v3.15)")
 objects.

The time part of the Timestamps.

See also

[`DatetimeIndex.timetz`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.timetz.html#pandas.DatetimeIndex.timetz "pandas.DatetimeIndex.timetz")

Returns numpy array of [`datetime.time`](https://docs.python.org/3/library/datetime.html#datetime.time "(in Python v3.15)")
 objects with timezones. The time part of the Timestamps.

[`DatetimeIndex.date`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.date.html#pandas.DatetimeIndex.date "pandas.DatetimeIndex.date")

Returns numpy array of python [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.15)")
 objects. Namely, the date part of Timestamps without time and timezone information.

Examples

For Series:

\>>> s \= pd.Series(\["1/1/2020 10:00:00+00:00", "2/1/2020 11:00:00+00:00"\])
\>>> s \= pd.to\_datetime(s)
\>>> s
0   2020-01-01 10:00:00+00:00
1   2020-02-01 11:00:00+00:00
dtype: datetime64\[us, UTC\]
\>>> s.dt.time
0    10:00:00
1    11:00:00
dtype: object

Copy to clipboard

For DatetimeIndex:

\>>> idx \= pd.DatetimeIndex(
...     \["1/1/2020 10:00:00+00:00", "2/1/2020 11:00:00+00:00"\]
... )
\>>> idx.time
array(\[datetime.time(10, 0), datetime.time(11, 0)\], dtype=object)

Copy to clipboard

On this page