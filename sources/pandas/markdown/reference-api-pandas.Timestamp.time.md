[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.time.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.time[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.time.html#pandas-timestamp-time "Link to this heading")

===============================================================================================================================================

Timestamp.time()[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.time.html#pandas.Timestamp.time "Link to this definition")

Return time object with same time but with tzinfo=None.

This method extracts the time part of the Timestamp object, excluding any timezone information. It returns a datetime.time object which only represents the time (hours, minutes, seconds, and microseconds).

See also

[`Timestamp.date`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.date.html#pandas.Timestamp.date "pandas.Timestamp.date")

Return date object with same year, month and day.

[`Timestamp.tz_convert`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz_convert.html#pandas.Timestamp.tz_convert "pandas.Timestamp.tz_convert")

Convert timezone-aware Timestamp to another time zone.

[`Timestamp.tz_localize`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz_localize.html#pandas.Timestamp.tz_localize "pandas.Timestamp.tz_localize")

Localize the Timestamp to a timezone.

Examples

\>>> ts \= pd.Timestamp('2023-01-01 10:00:00')
\>>> ts
Timestamp('2023-01-01 10:00:00')
\>>> ts.time()
datetime.time(10, 0)

Copy to clipboard

On this page