[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.next_monday.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.holiday.next\_monday[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.next_monday.html#pandas-tseries-holiday-next-monday "Link to this heading")

=======================================================================================================================================================================================

pandas.tseries.holiday.next\_monday(_dt_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/tseries/holiday.py#L46-L84)
[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.next_monday.html#pandas.tseries.holiday.next_monday "Link to this definition")

Move Saturday and Sunday to the following Monday.

A holiday on a weekday keeps its date.

Parameters:

**dt**datetime

The date the holiday falls on.

Returns:

datetime

The date the holiday is observed on.

See also

`tseries.holiday.weekend_to_monday`

Move Saturday and Sunday to the following Monday.

`tseries.holiday.next_monday_or_tuesday`

Move Saturday to Monday, and Sunday or Monday to Tuesday.

`tseries.holiday.Holiday`

Class that defines a holiday with start/end dates and rules for observance.

Examples

\>>> from datetime import datetime
\>>> from pandas.tseries.holiday import next\_monday
\>>> next\_monday(datetime(2022, 1, 1))  \# Saturday
datetime.datetime(2022, 1, 3, 0, 0)
\>>> next\_monday(datetime(2022, 1, 2))  \# Sunday
datetime.datetime(2022, 1, 3, 0, 0)

Copy to clipboard

On this page