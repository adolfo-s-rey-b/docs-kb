[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.next_monday_or_tuesday.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.holiday.next_monday_or_tuesday.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.next_monday_or_tuesday.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.holiday.next_monday_or_tuesday.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.holiday.next_monday_or_tuesday.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.holiday.next_monday_or_tuesday.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.holiday.next_monday_or_tuesday.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.holiday.next_monday_or_tuesday.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.holiday.next_monday_or_tuesday.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.holiday.next_monday_or_tuesday.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.holiday.next_monday_or_tuesday.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.holiday.next_monday_or_tuesday.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.holiday.next_monday_or_tuesday.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.holiday.next_monday_or_tuesday.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.holiday.next\_monday\_or\_tuesday[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.next_monday_or_tuesday.html#pandas-tseries-holiday-next-monday-or-tuesday "Link to this heading")

==========================================================================================================================================================================================================================

pandas.tseries.holiday.next\_monday\_or\_tuesday(_dt_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/tseries/holiday.py#L87-L129)
[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.next_monday_or_tuesday.html#pandas.tseries.holiday.next_monday_or_tuesday "Link to this definition")

Move Saturday to Monday, and Sunday or Monday to Tuesday.

Use this for the second of two adjacent holidays, where the Monday is already taken by the holiday of the day before.

Parameters:

**dt**datetime

The date the holiday falls on.

Returns:

datetime

The date the holiday is observed on.

See also

`tseries.holiday.next_monday`

Move Saturday and Sunday to the following Monday.

`tseries.holiday.after_nearest_workday`

Move to the workday after the nearest workday.

`tseries.holiday.Holiday`

Class that defines a holiday with start/end dates and rules for observance.

Examples

\>>> from datetime import datetime
\>>> from pandas.tseries.holiday import next\_monday\_or\_tuesday
\>>> next\_monday\_or\_tuesday(datetime(2022, 1, 1))  \# Saturday
datetime.datetime(2022, 1, 3, 0, 0)
\>>> next\_monday\_or\_tuesday(datetime(2022, 1, 2))  \# Sunday
datetime.datetime(2022, 1, 4, 0, 0)
\>>> next\_monday\_or\_tuesday(datetime(2022, 1, 3))  \# Monday
datetime.datetime(2022, 1, 4, 0, 0)

Copy to clipboard

On this page