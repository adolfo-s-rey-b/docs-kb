[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.timestamp.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.timestamp.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.timestamp.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.timestamp.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.timestamp.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.timestamp.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.timestamp.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.timestamp.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.timestamp.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.timestamp.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.timestamp.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.timestamp.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.timestamp.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.timestamp.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.timestamp[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.timestamp.html#pandas-timestamp-timestamp "Link to this heading")

==============================================================================================================================================================

Timestamp.timestamp()[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.timestamp.html#pandas.Timestamp.timestamp "Link to this definition")

Return POSIX timestamp as float.

This method converts the Timestamp object to a POSIX timestamp, which is the number of seconds since the Unix epoch (January 1, 1970). The returned value is a floating-point number, where the integer part represents the seconds, and the fractional part represents the microseconds.

Returns:

float

The POSIX timestamp representation of the Timestamp object.

See also

[`Timestamp.fromtimestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromtimestamp.html#pandas.Timestamp.fromtimestamp "pandas.Timestamp.fromtimestamp")

Construct a Timestamp from a POSIX timestamp.

[`datetime.datetime.timestamp`](https://docs.python.org/3/library/datetime.html#datetime.datetime.timestamp "(in Python v3.15)")

Equivalent method from the datetime module.

[`Timestamp.to_pydatetime`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_pydatetime.html#pandas.Timestamp.to_pydatetime "pandas.Timestamp.to_pydatetime")

Convert the Timestamp to a datetime object.

[`Timestamp.to_datetime64`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_datetime64.html#pandas.Timestamp.to_datetime64 "pandas.Timestamp.to_datetime64")

Converts Timestamp to numpy.datetime64.

Examples

\>>> ts \= pd.Timestamp('2020-03-14T15:32:52.192548')
\>>> ts.timestamp()
1584199972.192548

Copy to clipboard

On this page