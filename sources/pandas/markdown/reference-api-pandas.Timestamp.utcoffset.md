[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utcoffset.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.utcoffset.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utcoffset.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.utcoffset.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.utcoffset.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.utcoffset.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.utcoffset.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.utcoffset.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.utcoffset.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.utcoffset.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.utcoffset.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.utcoffset.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.utcoffset.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.utcoffset.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.utcoffset[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utcoffset.html#pandas-timestamp-utcoffset "Link to this heading")

==============================================================================================================================================================

Timestamp.utcoffset()[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utcoffset.html#pandas.Timestamp.utcoffset "Link to this definition")

Return utc offset.

This method returns the difference between UTC and the local time as a timedelta object. It is useful for understanding the time difference between the current timezone and UTC.

Returns:

timedelta

The difference between UTC and the local time as a timedelta object.

See also

[`datetime.datetime.utcoffset`](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcoffset "(in Python v3.15)")

Standard library method to get the UTC offset of a datetime object.

[`Timestamp.tzname`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tzname.html#pandas.Timestamp.tzname "pandas.Timestamp.tzname")

Return the name of the timezone.

[`Timestamp.dst`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.dst.html#pandas.Timestamp.dst "pandas.Timestamp.dst")

Return the daylight saving time (DST) adjustment.

Examples

\>>> ts \= pd.Timestamp('2023-01-01 10:00:00', tz\='Europe/Brussels')
\>>> ts
Timestamp('2023-01-01 10:00:00+0100', tz='Europe/Brussels')
\>>> ts.utcoffset()
datetime.timedelta(seconds=3600)

Copy to clipboard

On this page