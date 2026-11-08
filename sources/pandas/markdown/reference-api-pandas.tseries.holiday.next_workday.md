[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.next_workday.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.holiday.next_workday.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.next_workday.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.holiday.next_workday.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.holiday.next_workday.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.holiday.next_workday.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.holiday.next_workday.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.holiday.next_workday.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.holiday.next_workday.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.holiday.next_workday.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.holiday.next_workday.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.holiday.next_workday.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.holiday.next_workday.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.holiday.next_workday.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.holiday.next\_workday[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.next_workday.html#pandas-tseries-holiday-next-workday "Link to this heading")

==========================================================================================================================================================================================

pandas.tseries.holiday.next\_workday(_dt_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/tseries/holiday.py#L293-L332)
[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.next_workday.html#pandas.tseries.holiday.next_workday "Link to this definition")

Move to the next weekday.

The date is always advanced by at least one day, even when `dt` already falls on a weekday. To leave weekdays unchanged and move only weekend dates forward, use `next_monday` or `weekend_to_monday`.

Parameters:

**dt**datetime

The date to move forward from.

Returns:

datetime

The next weekday after `dt`.

See also

`tseries.holiday.previous_workday`

Move to the previous weekday.

`tseries.holiday.next_monday`

Move Saturday and Sunday to the following Monday.

`tseries.holiday.after_nearest_workday`

Move to the workday after the nearest workday.

Examples

\>>> from datetime import datetime
\>>> from pandas.tseries.holiday import next\_workday
\>>> next\_workday(datetime(2022, 1, 1))  \# Saturday
datetime.datetime(2022, 1, 3, 0, 0)
\>>> next\_workday(datetime(2022, 1, 5))  \# Wednesday, still advances
datetime.datetime(2022, 1, 6, 0, 0)

Copy to clipboard

On this page