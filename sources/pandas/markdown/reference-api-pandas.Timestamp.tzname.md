[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tzname.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.tzname.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tzname.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.tzname.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.tzname.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.tzname.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.tzname.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.tzname.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.tzname.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.tzname.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.tzname.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.tzname.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.tzname.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.tzname.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.tzname[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tzname.html#pandas-timestamp-tzname "Link to this heading")

=====================================================================================================================================================

Timestamp.tzname()[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tzname.html#pandas.Timestamp.tzname "Link to this definition")

Return time zone name.

This method returns the name of the Timestamp’s time zone as a string.

See also

[`Timestamp.tzinfo`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tzinfo.html#pandas.Timestamp.tzinfo "pandas.Timestamp.tzinfo")

Returns the timezone information of the Timestamp.

[`Timestamp.tz_convert`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz_convert.html#pandas.Timestamp.tz_convert "pandas.Timestamp.tz_convert")

Convert timezone-aware Timestamp to another time zone.

Examples

\>>> ts \= pd.Timestamp('2023-01-01 10:00:00', tz\='Europe/Brussels')
\>>> ts
Timestamp('2023-01-01 10:00:00+0100', tz='Europe/Brussels')
\>>> ts.tzname()
'CET'

Copy to clipboard

On this page