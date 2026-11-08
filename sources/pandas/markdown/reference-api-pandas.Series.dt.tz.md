[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.tz.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.tz.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.tz.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.tz.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.tz.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.tz.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.tz.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.tz.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.tz.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.tz.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.tz.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.tz.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.tz.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.tz.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.tz[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.tz.html#pandas-series-dt-tz "Link to this heading")

=========================================================================================================================================

Series.dt.tz[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L108-L109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.tz.html#pandas.Series.dt.tz "Link to this definition")

Return the timezone.

This property returns the timezone information associated with the datetime data. If the data is timezone-naive (i.e. has no timezone information), it returns None.

Returns:

zoneinfo.ZoneInfo, datetime.tzinfo, pytz.tzinfo.BaseTZInfo, dateutil.tz.tz.tzfile, or None

Returns None when the array is tz-naive.

See also

[`DatetimeIndex.tz_localize`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.tz_localize.html#pandas.DatetimeIndex.tz_localize "pandas.DatetimeIndex.tz_localize")

Localize tz-naive DatetimeIndex to a given time zone, or remove timezone from a tz-aware DatetimeIndex.

[`DatetimeIndex.tz_convert`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.tz_convert.html#pandas.DatetimeIndex.tz_convert "pandas.DatetimeIndex.tz_convert")

Convert tz-aware DatetimeIndex from one time zone to another.

Examples

For Series:

\>>> s \= pd.Series(\["1/1/2020 10:00:00+00:00", "2/1/2020 11:00:00+00:00"\])
\>>> s \= pd.to\_datetime(s)
\>>> s
0   2020-01-01 10:00:00+00:00
1   2020-02-01 11:00:00+00:00
dtype: datetime64\[us, UTC\]
\>>> s.dt.tz
datetime.timezone.utc

Copy to clipboard

For DatetimeIndex:

\>>> idx \= pd.DatetimeIndex(
...     \["1/1/2020 10:00:00+00:00", "2/1/2020 11:00:00+00:00"\]
... )
\>>> idx.tz
datetime.timezone.utc

Copy to clipboard

On this page