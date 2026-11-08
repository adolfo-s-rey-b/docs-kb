[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.LastWeekOfMonth.week.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.LastWeekOfMonth.week.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.LastWeekOfMonth.week.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.LastWeekOfMonth.week.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.LastWeekOfMonth.week.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.LastWeekOfMonth.week.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.LastWeekOfMonth.week.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.LastWeekOfMonth.week.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.LastWeekOfMonth.week.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.LastWeekOfMonth.week.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.LastWeekOfMonth.week.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.LastWeekOfMonth.week.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.LastWeekOfMonth.week.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.LastWeekOfMonth.week.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.LastWeekOfMonth.week[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.LastWeekOfMonth.week.html#pandas-tseries-offsets-lastweekofmonth-week "Link to this heading")

=================================================================================================================================================================================================================

LastWeekOfMonth.week[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.LastWeekOfMonth.week.html#pandas.tseries.offsets.LastWeekOfMonth.week "Link to this definition")

Return the week of the month on which this offset applies.

Returns an integer representing the week of the month (0-3) that this offset targets. The week is zero-indexed, where 0 corresponds to the first week of the month.

Returns:

int

An integer representing the week of the month (0-3).

See also

`tseries.offsets.WeekOfMonth`

Describes monthly dates in a specific week.

`tseries.offsets.LastWeekOfMonth`

Describes monthly dates in last week.

Examples

\>>> pd.offsets.WeekOfMonth(week\=0, weekday\=0).week
0

Copy to clipboard

\>>> pd.offsets.WeekOfMonth(week\=2, weekday\=3).week
2

Copy to clipboard

\>>> pd.offsets.LastWeekOfMonth(weekday\=0).week
\-1

Copy to clipboard

On this page