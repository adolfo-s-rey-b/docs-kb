[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromtimestamp.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.fromtimestamp.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromtimestamp.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.fromtimestamp.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.fromtimestamp.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.fromtimestamp.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.fromtimestamp.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.fromtimestamp.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.fromtimestamp.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.fromtimestamp.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.fromtimestamp.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.fromtimestamp.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.fromtimestamp.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.fromtimestamp.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.fromtimestamp[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromtimestamp.html#pandas-timestamp-fromtimestamp "Link to this heading")

==========================================================================================================================================================================

classmethod Timestamp.fromtimestamp(_ts_, _tz\=None_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromtimestamp.html#pandas.Timestamp.fromtimestamp "Link to this definition")

Create a Timestamp object from a POSIX timestamp.

This method converts a POSIX timestamp (the number of seconds since January 1, 1970, 00:00:00 UTC) into a Timestamp object. The resulting Timestamp can be localized to a specific time zone if provided.

Parameters:

**ts**float

The POSIX timestamp to convert, representing seconds since the epoch (1970-01-01 00:00:00 UTC).

**tz**str, zoneinfo.ZoneInfo, pytz.timezone, dateutil.tz.tzfile, optional

Time zone for the Timestamp. If not provided, the Timestamp will be timezone-naive (i.e., without time zone information).

Returns:

Timestamp

A Timestamp object representing the given POSIX timestamp.

See also

[`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")

Represents a single timestamp, similar to datetime.

[`to_datetime`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "pandas.to_datetime")

Converts various types of data to datetime.

[`datetime.datetime.fromtimestamp`](https://docs.python.org/3/library/datetime.html#datetime.datetime.fromtimestamp "(in Python v3.15)")

Returns a datetime from a POSIX timestamp.

Examples

Convert a POSIX timestamp to a Timestamp:

\>>> pd.Timestamp.fromtimestamp(1584199972)
Timestamp('2020-03-14 15:32:52')

Copy to clipboard

Note that the output may change depending on your local time and time zone:

\>>> pd.Timestamp.fromtimestamp(1584199972, tz\='UTC')
Timestamp('2020-03-14 15:32:52+0000', tz='UTC')

Copy to clipboard

On this page