[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.dst.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.dst.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.dst.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.dst.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.dst.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.dst.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.dst.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.dst.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.dst.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.dst.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.dst.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.dst.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.dst.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.dst.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.dst[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.dst.html#pandas-timestamp-dst "Link to this heading")

============================================================================================================================================

Timestamp.dst()[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.dst.html#pandas.Timestamp.dst "Link to this definition")

Return the daylight saving time (DST) adjustment.

This method returns the DST adjustment as a datetime.timedelta object if the Timestamp is timezone-aware and DST is applicable.

See also

[`Timestamp.tz_localize`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz_localize.html#pandas.Timestamp.tz_localize "pandas.Timestamp.tz_localize")

Localize the Timestamp to a timezone.

[`Timestamp.tz_convert`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz_convert.html#pandas.Timestamp.tz_convert "pandas.Timestamp.tz_convert")

Convert timezone-aware Timestamp to another time zone.

Examples

\>>> ts \= pd.Timestamp('2000-06-01 00:00:00', tz\='Europe/Brussels')
\>>> ts
Timestamp('2000-06-01 00:00:00+0200', tz='Europe/Brussels')
\>>> ts.dst()
datetime.timedelta(seconds=3600)

Copy to clipboard

On this page