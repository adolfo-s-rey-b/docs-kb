[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isocalendar.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.isocalendar[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isocalendar.html#pandas-timestamp-isocalendar "Link to this heading")

====================================================================================================================================================================

Timestamp.isocalendar()[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isocalendar.html#pandas.Timestamp.isocalendar "Link to this definition")

Return a named tuple containing ISO year, week number, and weekday.

The ISO 8601 calendar is a widely used international standard. The returned named tuple has three components: `year`, `week`, and `weekday`. The ISO year may differ from the Gregorian year for dates near the start or end of a calendar year.

See also

`DatetimeIndex.isocalendar`

Return a 3-tuple containing ISO year, week number, and weekday for the given DatetimeIndex object.

[`datetime.date.isocalendar`](https://docs.python.org/3/library/datetime.html#datetime.date.isocalendar "(in Python v3.15)")

The equivalent method for datetime.date objects.

Examples

\>>> ts \= pd.Timestamp('2023-01-01 10:00:00')
\>>> ts
Timestamp('2023-01-01 10:00:00')
\>>> ts.isocalendar()
datetime.IsoCalendarDate(year=2022, week=52, weekday=7)

Copy to clipboard

On this page