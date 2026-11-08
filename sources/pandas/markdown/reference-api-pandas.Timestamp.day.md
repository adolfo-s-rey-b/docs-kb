[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.day[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day.html#pandas-timestamp-day "Link to this heading")

============================================================================================================================================

Timestamp.day[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day.html#pandas.Timestamp.day "Link to this definition")

Return the day of the Timestamp.

Days are numbered from 1 through the number of days in the month.

Returns:

int

The day of the Timestamp.

See also

[`Timestamp.week`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.week.html#pandas.Timestamp.week "pandas.Timestamp.week")

Return the week number of the year.

[`Timestamp.weekday`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.weekday.html#pandas.Timestamp.weekday "pandas.Timestamp.weekday")

Return the day of the week.

Examples

\>>> ts \= pd.Timestamp("2024-08-31 16:16:30")
\>>> ts.day
31

Copy to clipboard

On this page