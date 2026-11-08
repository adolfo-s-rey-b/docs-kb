[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.tz_convert.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DatetimeIndex.tz_convert.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.tz_convert.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DatetimeIndex.tz_convert.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DatetimeIndex.tz_convert.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DatetimeIndex.tz_convert.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DatetimeIndex.tz_convert.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DatetimeIndex.tz_convert.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DatetimeIndex.tz_convert.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DatetimeIndex.tz_convert.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DatetimeIndex.tz_convert.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DatetimeIndex.tz_convert.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DatetimeIndex.tz_convert.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DatetimeIndex.tz_convert.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.tz\_convert[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.tz_convert.html#pandas-datetimeindex-tz-convert "Link to this heading")

==============================================================================================================================================================================

DatetimeIndex.tz\_convert(_tz_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L1485-L1560)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.tz_convert.html#pandas.DatetimeIndex.tz_convert "Link to this definition")

Convert tz-aware Datetime Array/Index from one time zone to another.

This method converts each timestamp in the index to the target time zone while preserving the underlying UTC time. The index must already be timezone-aware.

Parameters:

**tz**str, zoneinfo.ZoneInfo, pytz.timezone, dateutil.tz.tzfile, datetime.tzinfo or None

Time zone for time. Corresponding timestamps would be converted to this time zone of the Datetime Array/Index. A tz of None will convert to UTC and remove the timezone information.

Returns:

Array or Index

Datetime Array/Index with target tz.

Raises:

TypeError

If Datetime Array/Index is tz-naive.

See also

[`DatetimeIndex.tz`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.tz.html#pandas.DatetimeIndex.tz "pandas.DatetimeIndex.tz")

A timezone that has a variable offset from UTC.

[`DatetimeIndex.tz_localize`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.tz_localize.html#pandas.DatetimeIndex.tz_localize "pandas.DatetimeIndex.tz_localize")

Localize tz-naive DatetimeIndex to a given time zone, or remove timezone from a tz-aware DatetimeIndex.

Examples

With the tz parameter, we can change the DatetimeIndex to other time zones:

\>>> dti \= pd.date\_range(
...     start\="2014-08-01 09:00", freq\="h", periods\=3, tz\="Europe/Berlin"
... )

Copy to clipboard

\>>> dti
DatetimeIndex(\['2014-08-01 09:00:00+02:00',\
               '2014-08-01 10:00:00+02:00',\
               '2014-08-01 11:00:00+02:00'\],
              dtype='datetime64\[us, Europe/Berlin\]', freq='h')

Copy to clipboard

\>>> dti.tz\_convert("US/Central")
DatetimeIndex(\['2014-08-01 02:00:00-05:00',\
               '2014-08-01 03:00:00-05:00',\
               '2014-08-01 04:00:00-05:00'\],
              dtype='datetime64\[us, US/Central\]', freq='h')

Copy to clipboard

With the `tz=None`, we can remove the timezone (after converting to UTC if necessary):

\>>> dti \= pd.date\_range(
...     start\="2014-08-01 09:00", freq\="h", periods\=3, tz\="Europe/Berlin"
... )

Copy to clipboard

\>>> dti
DatetimeIndex(\['2014-08-01 09:00:00+02:00',\
               '2014-08-01 10:00:00+02:00',\
               '2014-08-01 11:00:00+02:00'\],
                dtype='datetime64\[us, Europe/Berlin\]', freq='h')

Copy to clipboard

\>>> dti.tz\_convert(None)
DatetimeIndex(\['2014-08-01 07:00:00',\
               '2014-08-01 08:00:00',\
               '2014-08-01 09:00:00'\],
                dtype='datetime64\[us\]', freq='h')

Copy to clipboard

On this page