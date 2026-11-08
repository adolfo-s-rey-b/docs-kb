[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.previous_friday.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.holiday.previous\_friday[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.previous_friday.html#pandas-tseries-holiday-previous-friday "Link to this heading")

===================================================================================================================================================================================================

pandas.tseries.holiday.previous\_friday(_dt_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/tseries/holiday.py#L132-L169)
[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.previous_friday.html#pandas.tseries.holiday.previous_friday "Link to this definition")

Move Saturday and Sunday back to the previous Friday.

A holiday on a weekday keeps its date.

Parameters:

**dt**datetime

The date the holiday falls on.

Returns:

datetime

The date the holiday is observed on.

See also

`tseries.holiday.next_monday`

Move Saturday and Sunday to the following Monday.

`tseries.holiday.previous_workday`

Move to the previous weekday.

`tseries.holiday.Holiday`

Class that defines a holiday with start/end dates and rules for observance.

Examples

\>>> from datetime import datetime
\>>> from pandas.tseries.holiday import previous\_friday
\>>> previous\_friday(datetime(2022, 1, 1))  \# Saturday
datetime.datetime(2021, 12, 31, 0, 0)
\>>> previous\_friday(datetime(2022, 1, 2))  \# Sunday
datetime.datetime(2021, 12, 31, 0, 0)

Copy to clipboard

On this page