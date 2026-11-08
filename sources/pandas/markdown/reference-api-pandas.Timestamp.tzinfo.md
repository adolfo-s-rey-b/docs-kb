[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tzinfo.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.tzinfo.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tzinfo.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.tzinfo.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.tzinfo.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.tzinfo.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.tzinfo.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.tzinfo.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.tzinfo.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.tzinfo.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.tzinfo.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.tzinfo.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.tzinfo.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.tzinfo.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.tzinfo[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tzinfo.html#pandas-timestamp-tzinfo "Link to this heading")

=====================================================================================================================================================

property Timestamp.tzinfo[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tzinfo.html#pandas.Timestamp.tzinfo "Link to this definition")

Returns the timezone info of the Timestamp.

This property returns a datetime.tzinfo object if the Timestamp is timezone-aware. If the Timestamp has no timezone, it returns None. If the Timestamp is in UTC or a fixed-offset timezone, it returns datetime.timezone. If the Timestamp uses an IANA timezone (e.g., “America/New\_York”), it returns zoneinfo.ZoneInfo.

See also

[`Timestamp.tz`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz.html#pandas.Timestamp.tz "pandas.Timestamp.tz")

Alias for tzinfo, may return a zoneinfo.ZoneInfo object.

[`Timestamp.tz_convert`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz_convert.html#pandas.Timestamp.tz_convert "pandas.Timestamp.tz_convert")

Convert timezone-aware Timestamp to another time zone.

[`Timestamp.tz_localize`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz_localize.html#pandas.Timestamp.tz_localize "pandas.Timestamp.tz_localize")

Localize the Timestamp to a specific timezone.

Examples

\>>> ts \= pd.Timestamp("2023-01-01 12:00:00", tz\="UTC")
\>>> ts.tzinfo
datetime.timezone.utc

Copy to clipboard

\>>> ts\_naive \= pd.Timestamp("2023-01-01 12:00:00")
\>>> ts\_naive.tzinfo

Copy to clipboard

On this page