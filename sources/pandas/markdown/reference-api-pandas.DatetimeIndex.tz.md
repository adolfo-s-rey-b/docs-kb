[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.tz.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DatetimeIndex.tz.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.tz.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DatetimeIndex.tz.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DatetimeIndex.tz.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DatetimeIndex.tz.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DatetimeIndex.tz.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DatetimeIndex.tz.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DatetimeIndex.tz.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DatetimeIndex.tz.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DatetimeIndex.tz.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DatetimeIndex.tz.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DatetimeIndex.tz.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DatetimeIndex.tz.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.tz[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.tz.html#pandas-datetimeindex-tz "Link to this heading")

=====================================================================================================================================================

property DatetimeIndex.tz[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L265-L294)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.tz.html#pandas.DatetimeIndex.tz "Link to this definition")

Return the timezone.

This property returns the timezone information associated with the DatetimeIndex. If the data is timezone-naive (i.e. has no timezone information), it returns None.

Returns:

zoneinfo.ZoneInfo, datetime.tzinfo, pytz.tzinfo.BaseTZInfo, dateutil.tz.tz.tzfile, or None

Returns None when the DatetimeIndex is tz-naive.

See also

[`DatetimeIndex.tz_localize`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.tz_localize.html#pandas.DatetimeIndex.tz_localize "pandas.DatetimeIndex.tz_localize")

Localize tz-naive DatetimeIndex to a given time zone, or remove timezone from a tz-aware DatetimeIndex.

[`DatetimeIndex.tz_convert`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.tz_convert.html#pandas.DatetimeIndex.tz_convert "pandas.DatetimeIndex.tz_convert")

Convert tz-aware DatetimeIndex from one time zone to another.

Examples

\>>> idx \= pd.DatetimeIndex(
...     \["1/1/2020 10:00:00+00:00", "2/1/2020 11:00:00+00:00"\]
... )
\>>> idx.tz
datetime.timezone.utc

Copy to clipboard

On this page