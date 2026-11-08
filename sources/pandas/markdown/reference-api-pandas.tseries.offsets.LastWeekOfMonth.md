[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.LastWeekOfMonth.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.LastWeekOfMonth.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.LastWeekOfMonth.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.LastWeekOfMonth.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.LastWeekOfMonth.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.LastWeekOfMonth.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.LastWeekOfMonth.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.LastWeekOfMonth.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.LastWeekOfMonth.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.LastWeekOfMonth.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.LastWeekOfMonth.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.LastWeekOfMonth.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.LastWeekOfMonth.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.LastWeekOfMonth.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.LastWeekOfMonth[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.LastWeekOfMonth.html#pandas-tseries-offsets-lastweekofmonth "Link to this heading")

==================================================================================================================================================================================================

class pandas.tseries.offsets.LastWeekOfMonth[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.LastWeekOfMonth.html#pandas.tseries.offsets.LastWeekOfMonth "Link to this definition")

Describes monthly dates in last week of month.

For example “the last Tuesday of each month”.

Parameters:

**n**int, default 1

The number of months represented.

**normalize**bool, default False

Normalize start/end dates to midnight before generating date range.

**weekday**int {0, 1, …, 6}, default 0

A specific integer for the day of the week.

*   0 is Monday
    
*   1 is Tuesday
    
*   2 is Wednesday
    
*   3 is Thursday
    
*   4 is Friday
    
*   5 is Saturday
    
*   6 is Sunday.
    

Attributes

|     |     |
| --- | --- |
| [`week`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.LastWeekOfMonth.week.html#pandas.tseries.offsets.LastWeekOfMonth.week "pandas.tseries.offsets.LastWeekOfMonth.week") | Return the week of the month on which this offset applies. |
| [`weekday`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.LastWeekOfMonth.weekday.html#pandas.tseries.offsets.LastWeekOfMonth.weekday "pandas.tseries.offsets.LastWeekOfMonth.weekday") | Return the day of the week on which this offset applies. |

See also

`tseries.offsets.WeekOfMonth`

Date offset for a specific weekday in a month.

`tseries.offsets.MonthEnd`

Date offset for the end of the month.

`tseries.offsets.BMonthEnd`

Date offset for the last business day of the month.

Examples

\>>> ts \= pd.Timestamp(2022, 1, 1)
\>>> ts + pd.offsets.LastWeekOfMonth()
Timestamp('2022-01-31 00:00:00')

Copy to clipboard

On this page