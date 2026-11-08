[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.astimezone.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.astimezone.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.astimezone.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.astimezone.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.astimezone.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.astimezone.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.astimezone.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.astimezone.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.astimezone.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.astimezone.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.astimezone.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.astimezone.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.astimezone.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.astimezone.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.astimezone[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.astimezone.html#pandas-timestamp-astimezone "Link to this heading")

=================================================================================================================================================================

Timestamp.astimezone(_tz_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.astimezone.html#pandas.Timestamp.astimezone "Link to this definition")

Convert timezone-aware Timestamp to another time zone.

This method is used to convert a timezone-aware Timestamp object to a different time zone. The original UTC time remains the same; only the time zone information is changed. If the Timestamp is timezone-naive, a TypeError is raised.

Parameters:

**tz**str, zoneinfo.ZoneInfo, pytz.timezone, dateutil.tz.tzfile or None

Time zone for time which Timestamp will be converted to. None will remove timezone holding UTC time.

Returns:

**converted**Timestamp

Raises:

TypeError

If Timestamp is tz-naive.

See also

[`Timestamp.tz_localize`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz_localize.html#pandas.Timestamp.tz_localize "pandas.Timestamp.tz_localize")

Localize the Timestamp to a timezone.

[`DatetimeIndex.tz_convert`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.tz_convert.html#pandas.DatetimeIndex.tz_convert "pandas.DatetimeIndex.tz_convert")

Convert a DatetimeIndex to another time zone.

[`DatetimeIndex.tz_localize`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.tz_localize.html#pandas.DatetimeIndex.tz_localize "pandas.DatetimeIndex.tz_localize")

Localize a DatetimeIndex to a specific time zone.

[`datetime.datetime.astimezone`](https://docs.python.org/3/library/datetime.html#datetime.datetime.astimezone "(in Python v3.15)")

Convert a datetime object to another time zone.

Examples

Create a timestamp object with UTC timezone:

\>>> ts \= pd.Timestamp('2020-03-14T15:32:52.192548651', tz\='UTC')
\>>> ts
Timestamp('2020-03-14 15:32:52.192548651+0000', tz='UTC')

Copy to clipboard

Change to Tokyo timezone:

\>>> ts.tz\_convert(tz\='Asia/Tokyo')
Timestamp('2020-03-15 00:32:52.192548651+0900', tz='Asia/Tokyo')

Copy to clipboard

Can also use `astimezone`:

\>>> ts.astimezone(tz\='Asia/Tokyo')
Timestamp('2020-03-15 00:32:52.192548651+0900', tz='Asia/Tokyo')

Copy to clipboard

Analogous for `pd.NaT`:

\>>> pd.NaT.tz\_convert(tz\='Asia/Tokyo')
NaT

Copy to clipboard

On this page