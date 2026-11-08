[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.WeekOfMonth.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.WeekOfMonth.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.WeekOfMonth.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.WeekOfMonth.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.WeekOfMonth.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.WeekOfMonth.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.WeekOfMonth.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.WeekOfMonth.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.WeekOfMonth.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.WeekOfMonth.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.WeekOfMonth.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.WeekOfMonth.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.WeekOfMonth.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.WeekOfMonth.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.WeekOfMonth[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.WeekOfMonth.html#pandas-tseries-offsets-weekofmonth "Link to this heading")

======================================================================================================================================================================================

class pandas.tseries.offsets.WeekOfMonth[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.WeekOfMonth.html#pandas.tseries.offsets.WeekOfMonth "Link to this definition")

Describes monthly dates like “the Tuesday of the 2nd week of each month”.

This offset allows for generating or adjusting dates by specifying a particular week and weekday within a month. The week is zero-indexed, where 0 corresponds to the first week of the month, and weekday follows a Monday=0 convention.

Parameters:

**n**int, default 1

The number of months represented.

**normalize**bool, default False

Normalize start/end dates to midnight before generating date range.

**week**int {0, 1, 2, 3, …}, default 0

A specific integer for the week of the month. e.g. 0 is 1st week of month, 1 is the 2nd week, etc.

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
| [`week`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.WeekOfMonth.week.html#pandas.tseries.offsets.WeekOfMonth.week "pandas.tseries.offsets.WeekOfMonth.week") | Return the week of the month on which this offset applies. |
| [`weekday`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.WeekOfMonth.weekday.html#pandas.tseries.offsets.WeekOfMonth.weekday "pandas.tseries.offsets.WeekOfMonth.weekday") | Return the day of the week on which this offset applies. |

See also

`offsets.Week`

Describes weekly frequency adjustments.

`offsets.MonthEnd`

Describes month-end frequency adjustments.

`date_range`

Generates a range of dates based on a specific frequency.

Examples

\>>> ts \= pd.Timestamp(2022, 1, 1)
\>>> ts + pd.offsets.WeekOfMonth()
Timestamp('2022-01-03 00:00:00')

Copy to clipboard

On this page