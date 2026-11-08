[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.nearest_workday.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.holiday.nearest\_workday[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.nearest_workday.html#pandas-tseries-holiday-nearest-workday "Link to this heading")

===================================================================================================================================================================================================

pandas.tseries.holiday.nearest\_workday(_dt_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/tseries/holiday.py#L252-L290)
[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.nearest_workday.html#pandas.tseries.holiday.nearest_workday "Link to this definition")

Move Saturday to Friday and Sunday to Monday.

Most US federal holidays follow this rule.

Parameters:

**dt**datetime

The date the holiday falls on.

Returns:

datetime

The date the holiday is observed on.

See also

`tseries.holiday.before_nearest_workday`

Move to the workday before the nearest workday.

`tseries.holiday.after_nearest_workday`

Move to the workday after the nearest workday.

`tseries.holiday.USFederalHolidayCalendar`

US Federal Government holiday calendar.

Examples

\>>> from datetime import datetime
\>>> from pandas.tseries.holiday import nearest\_workday
\>>> nearest\_workday(datetime(2022, 1, 1))  \# Saturday
datetime.datetime(2021, 12, 31, 0, 0)
\>>> nearest\_workday(datetime(2022, 1, 2))  \# Sunday
datetime.datetime(2022, 1, 3, 0, 0)

Copy to clipboard

On this page