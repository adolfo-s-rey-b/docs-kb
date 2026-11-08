[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.timetz.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.timetz.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.timetz.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.timetz.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.timetz.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.timetz.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.timetz.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.timetz.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.timetz.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.timetz.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.timetz.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.timetz.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.timetz.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.timetz.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.timetz[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.timetz.html#pandas-timestamp-timetz "Link to this heading")

=====================================================================================================================================================

Timestamp.timetz()[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.timetz.html#pandas.Timestamp.timetz "Link to this definition")

Return time object with same time and tzinfo.

This method returns a datetime.time object with the time and tzinfo corresponding to the pd.Timestamp object, ignoring any information about the day/date.

See also

[`datetime.datetime.timetz`](https://docs.python.org/3/library/datetime.html#datetime.datetime.timetz "(in Python v3.15)")

Return datetime.time object with the same time attributes as the datetime object.

[`datetime.time`](https://docs.python.org/3/library/datetime.html#datetime.time "(in Python v3.15)")

Class to represent the time of day, independent of any particular day.

[`datetime.datetime.tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo "(in Python v3.15)")

Attribute of datetime.datetime objects representing the timezone of the datetime object.

Examples

\>>> ts \= pd.Timestamp('2023-01-01 10:00:00', tz\='Europe/Brussels')
\>>> ts
Timestamp('2023-01-01 10:00:00+0100', tz='Europe/Brussels')
\>>> ts.timetz()
datetime.time(10, 0, tzinfo=zoneinfo.ZoneInfo(key='Europe/Brussels'))

Copy to clipboard

On this page