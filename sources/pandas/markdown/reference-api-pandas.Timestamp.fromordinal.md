[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromordinal.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.fromordinal.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromordinal.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.fromordinal.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.fromordinal.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.fromordinal.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.fromordinal.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.fromordinal.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.fromordinal.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.fromordinal.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.fromordinal.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.fromordinal.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.fromordinal.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.fromordinal.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.fromordinal[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromordinal.html#pandas-timestamp-fromordinal "Link to this heading")

====================================================================================================================================================================

classmethod Timestamp.fromordinal(_ordinal_, _tz\=None_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromordinal.html#pandas.Timestamp.fromordinal "Link to this definition")

Construct a timestamp from a proleptic Gregorian ordinal.

This method creates a Timestamp object corresponding to the given proleptic Gregorian ordinal, which is a count of days from January 1, 0001 (using the proleptic Gregorian calendar). The time part of the Timestamp is set to midnight (00:00:00) by default.

Parameters:

**ordinal**int

Date corresponding to a proleptic Gregorian ordinal.

**tz**str, zoneinfo.ZoneInfo, pytz.timezone, dateutil.tz.tzfile or None

Time zone for the Timestamp.

Returns:

Timestamp

A Timestamp object representing the specified ordinal date.

See also

[`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")

Represents a single timestamp, similar to datetime.

[`to_datetime`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "pandas.to_datetime")

Converts various types of data to datetime.

Notes

By definition there cannot be any tz info on the ordinal itself.

Examples

Convert an ordinal to a Timestamp:

\>>> pd.Timestamp.fromordinal(737425)
Timestamp('2020-01-01 00:00:00')

Copy to clipboard

Create a Timestamp from an ordinal with timezone information:

\>>> pd.Timestamp.fromordinal(737425, tz\='UTC')
Timestamp('2020-01-01 00:00:00+0000', tz='UTC')

Copy to clipboard

On this page