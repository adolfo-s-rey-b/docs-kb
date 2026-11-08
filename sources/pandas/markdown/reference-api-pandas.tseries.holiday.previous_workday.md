[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.previous_workday.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.holiday.previous_workday.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.previous_workday.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.holiday.previous_workday.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.holiday.previous_workday.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.holiday.previous_workday.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.holiday.previous_workday.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.holiday.previous_workday.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.holiday.previous_workday.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.holiday.previous_workday.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.holiday.previous_workday.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.holiday.previous_workday.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.holiday.previous_workday.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.holiday.previous_workday.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.holiday.previous\_workday[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.previous_workday.html#pandas-tseries-holiday-previous-workday "Link to this heading")

======================================================================================================================================================================================================

pandas.tseries.holiday.previous\_workday(_dt_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/tseries/holiday.py#L335-L374)
[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.previous_workday.html#pandas.tseries.holiday.previous_workday "Link to this definition")

Move to the previous weekday.

The date is always moved back by at least one day, even when `dt` already falls on a weekday. To leave weekdays unchanged and move only weekend dates back, use `previous_friday`.

Parameters:

**dt**datetime

The date to move back from.

Returns:

datetime

The previous weekday before `dt`.

See also

`tseries.holiday.next_workday`

Move to the next weekday.

`tseries.holiday.previous_friday`

Move Saturday and Sunday back to the previous Friday.

`tseries.holiday.before_nearest_workday`

Move to the workday before the nearest workday.

Examples

\>>> from datetime import datetime
\>>> from pandas.tseries.holiday import previous\_workday
\>>> previous\_workday(datetime(2022, 1, 2))  \# Sunday
datetime.datetime(2021, 12, 31, 0, 0)
\>>> previous\_workday(datetime(2022, 1, 5))  \# Wednesday, still moves back
datetime.datetime(2022, 1, 4, 0, 0)

Copy to clipboard

On this page