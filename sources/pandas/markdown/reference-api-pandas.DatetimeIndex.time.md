[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.time.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.time[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.time.html#pandas-datetimeindex-time "Link to this heading")

===========================================================================================================================================================

property DatetimeIndex.time[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L889-L912)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.time.html#pandas.DatetimeIndex.time "Link to this definition")

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

\>>> idx \= pd.DatetimeIndex(
...     \["1/1/2020 10:00:00+00:00", "2/1/2020 11:00:00+00:00"\]
... )
\>>> idx.time
array(\[datetime.time(10, 0), datetime.time(11, 0)\], dtype=object)

Copy to clipboard

On this page