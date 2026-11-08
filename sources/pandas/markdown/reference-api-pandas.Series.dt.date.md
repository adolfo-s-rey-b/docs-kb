[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.date.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.date.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.date.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.date.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.date.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.date.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.date.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.date.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.date.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.date.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.date.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.date.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.date.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.date.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.date[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.date.html#pandas-series-dt-date "Link to this heading")

===============================================================================================================================================

Series.dt.date[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L108-L109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.date.html#pandas.Series.dt.date "Link to this definition")

Returns numpy array of python [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.15)")
 objects.

Namely, the date part of Timestamps without time and timezone information.

See also

[`DatetimeIndex.time`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.time.html#pandas.DatetimeIndex.time "pandas.DatetimeIndex.time")

Returns numpy array of [`datetime.time`](https://docs.python.org/3/library/datetime.html#datetime.time "(in Python v3.15)")
 objects. The time part of the Timestamps.

[`DatetimeIndex.year`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.year.html#pandas.DatetimeIndex.year "pandas.DatetimeIndex.year")

The year of the datetime.

[`DatetimeIndex.month`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.month.html#pandas.DatetimeIndex.month "pandas.DatetimeIndex.month")

The month as January=1, December=12.

[`DatetimeIndex.day`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day.html#pandas.DatetimeIndex.day "pandas.DatetimeIndex.day")

The day of the datetime.

Examples

For Series:

\>>> s \= pd.Series(\["1/1/2020 10:00:00+00:00", "2/1/2020 11:00:00+00:00"\])
\>>> s \= pd.to\_datetime(s)
\>>> s
0   2020-01-01 10:00:00+00:00
1   2020-02-01 11:00:00+00:00
dtype: datetime64\[us, UTC\]
\>>> s.dt.date
0    2020-01-01
1    2020-02-01
dtype: object

Copy to clipboard

For DatetimeIndex:

\>>> idx \= pd.DatetimeIndex(
...     \["1/1/2020 10:00:00+00:00", "2/1/2020 11:00:00+00:00"\]
... )
\>>> idx.date
array(\[datetime.date(2020, 1, 1), datetime.date(2020, 2, 1)\], dtype=object)

Copy to clipboard

On this page