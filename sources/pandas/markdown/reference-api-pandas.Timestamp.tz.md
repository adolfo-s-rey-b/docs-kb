[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.tz[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz.html#pandas-timestamp-tz "Link to this heading")

=========================================================================================================================================

property Timestamp.tz[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz.html#pandas.Timestamp.tz "Link to this definition")

Alias for tzinfo.

The tz property provides a simple and direct way to retrieve the timezone information of a Timestamp object. It is particularly useful when working with time series data that includes timezone information, allowing for easy access and manipulation of the timezone context.

See also

[`Timestamp.tzinfo`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tzinfo.html#pandas.Timestamp.tzinfo "pandas.Timestamp.tzinfo")

Returns the timezone information of the Timestamp.

[`Timestamp.tz_convert`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz_convert.html#pandas.Timestamp.tz_convert "pandas.Timestamp.tz_convert")

Convert timezone-aware Timestamp to another time zone.

[`Timestamp.tz_localize`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz_localize.html#pandas.Timestamp.tz_localize "pandas.Timestamp.tz_localize")

Localize the Timestamp to a timezone.

Examples

\>>> ts \= pd.Timestamp(1584226800, unit\='s', tz\='Europe/Stockholm')
\>>> ts.tz
zoneinfo.ZoneInfo(key='Europe/Stockholm')

Copy to clipboard

On this page