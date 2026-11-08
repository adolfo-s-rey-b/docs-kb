[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utcfromtimestamp.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.utcfromtimestamp.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utcfromtimestamp.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.utcfromtimestamp.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.utcfromtimestamp.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.utcfromtimestamp.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.utcfromtimestamp.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.utcfromtimestamp.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.utcfromtimestamp.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.utcfromtimestamp.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.utcfromtimestamp.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.utcfromtimestamp.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.utcfromtimestamp.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.utcfromtimestamp.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.utcfromtimestamp[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utcfromtimestamp.html#pandas-timestamp-utcfromtimestamp "Link to this heading")

===================================================================================================================================================================================

classmethod Timestamp.utcfromtimestamp(_ts_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utcfromtimestamp.html#pandas.Timestamp.utcfromtimestamp "Link to this definition")

Construct a timezone-aware UTC datetime from a POSIX timestamp.

This method creates a datetime object from a POSIX timestamp, keeping the Timestamp object’s timezone.

Parameters:

**ts**float

POSIX timestamp.

See also

`Timezone.tzname`

Return time zone name.

[`Timestamp.utcnow`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utcnow.html#pandas.Timestamp.utcnow "pandas.Timestamp.utcnow")

Return a new Timestamp representing UTC day and time.

[`Timestamp.fromtimestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromtimestamp.html#pandas.Timestamp.fromtimestamp "pandas.Timestamp.fromtimestamp")

Transform timestamp\[, tz\] to tz’s local time from POSIX timestamp.

Notes

Timestamp.utcfromtimestamp behavior differs from datetime.utcfromtimestamp in returning a timezone-aware object.

Examples

\>>> pd.Timestamp.utcfromtimestamp(1584199972)
Timestamp('2020-03-14 15:32:52+0000', tz='UTC')

Copy to clipboard

On this page