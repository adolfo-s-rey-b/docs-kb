[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.before_nearest_workday.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.holiday.before_nearest_workday.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.before_nearest_workday.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.holiday.before_nearest_workday.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.holiday.before_nearest_workday.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.holiday.before_nearest_workday.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.holiday.before_nearest_workday.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.holiday.before_nearest_workday.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.holiday.before_nearest_workday.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.holiday.before_nearest_workday.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.holiday.before_nearest_workday.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.holiday.before_nearest_workday.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.holiday.before_nearest_workday.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.holiday.before_nearest_workday.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.holiday.before\_nearest\_workday[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.before_nearest_workday.html#pandas-tseries-holiday-before-nearest-workday "Link to this heading")

=========================================================================================================================================================================================================================

pandas.tseries.holiday.before\_nearest\_workday(_dt_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/tseries/holiday.py#L377-L411)
[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.before_nearest_workday.html#pandas.tseries.holiday.before_nearest_workday "Link to this definition")

Move to the workday before the nearest workday.

`nearest_workday` runs first, so a Saturday holiday ends up on the Thursday before it.

Parameters:

**dt**datetime

The date the holiday falls on.

Returns:

datetime

The date the holiday is observed on.

See also

`tseries.holiday.nearest_workday`

Move Saturday to Friday and Sunday to Monday.

`tseries.holiday.after_nearest_workday`

Move to the workday after the nearest workday.

`tseries.holiday.previous_workday`

Move to the previous weekday.

Examples

\>>> from datetime import datetime
\>>> from pandas.tseries.holiday import before\_nearest\_workday
\>>> before\_nearest\_workday(datetime(2022, 1, 1))  \# Saturday
datetime.datetime(2021, 12, 30, 0, 0)
\>>> before\_nearest\_workday(datetime(2022, 1, 2))  \# Sunday
datetime.datetime(2021, 12, 31, 0, 0)

Copy to clipboard

On this page