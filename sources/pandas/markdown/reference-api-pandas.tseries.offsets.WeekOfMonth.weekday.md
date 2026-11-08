[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.WeekOfMonth.weekday.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.WeekOfMonth.weekday.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.WeekOfMonth.weekday.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.WeekOfMonth.weekday.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.WeekOfMonth.weekday.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.WeekOfMonth.weekday.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.WeekOfMonth.weekday.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.WeekOfMonth.weekday.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.WeekOfMonth.weekday.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.WeekOfMonth.weekday.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.WeekOfMonth.weekday.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.WeekOfMonth.weekday.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.WeekOfMonth.weekday.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.WeekOfMonth.weekday.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.WeekOfMonth.weekday[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.WeekOfMonth.weekday.html#pandas-tseries-offsets-weekofmonth-weekday "Link to this heading")

==============================================================================================================================================================================================================

WeekOfMonth.weekday[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.WeekOfMonth.weekday.html#pandas.tseries.offsets.WeekOfMonth.weekday "Link to this definition")

Return the day of the week on which this offset applies.

The weekday is represented as an integer where 0 is Monday and 6 is Sunday. This is the specific day of the week targeted within the specified week of the month.

Returns:

int

An integer from 0 (Monday) to 6 (Sunday) representing the day of the week.

See also

`tseries.offsets.WeekOfMonth`

Describes monthly dates in a specific week.

`tseries.offsets.LastWeekOfMonth`

Describes monthly dates in last week.

`tseries.offsets.Week.weekday`

Return the day of the week for Week offset.

Examples

\>>> pd.offsets.WeekOfMonth(week\=0, weekday\=0).weekday
0

Copy to clipboard

\>>> pd.offsets.WeekOfMonth(week\=2, weekday\=3).weekday
3

Copy to clipboard

\>>> pd.offsets.LastWeekOfMonth(weekday\=5).weekday
5

Copy to clipboard

On this page