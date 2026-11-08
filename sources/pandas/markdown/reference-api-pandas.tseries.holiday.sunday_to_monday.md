[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.sunday_to_monday.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.holiday.sunday\_to\_monday[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.sunday_to_monday.html#pandas-tseries-holiday-sunday-to-monday "Link to this heading")

=======================================================================================================================================================================================================

pandas.tseries.holiday.sunday\_to\_monday(_dt_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/tseries/holiday.py#L172-L208)
[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.sunday_to_monday.html#pandas.tseries.holiday.sunday_to_monday "Link to this definition")

Move Sunday to the following Monday.

A holiday on a Saturday stays where it is.

Parameters:

**dt**datetime

The date the holiday falls on.

Returns:

datetime

The date the holiday is observed on.

See also

`tseries.holiday.weekend_to_monday`

Move Saturday and Sunday to the following Monday.

`tseries.holiday.nearest_workday`

Move Saturday to Friday and Sunday to Monday.

`tseries.holiday.Holiday`

Class that defines a holiday with start/end dates and rules for observance.

Examples

\>>> from datetime import datetime
\>>> from pandas.tseries.holiday import sunday\_to\_monday
\>>> sunday\_to\_monday(datetime(2022, 1, 2))  \# Sunday
datetime.datetime(2022, 1, 3, 0, 0)
\>>> sunday\_to\_monday(datetime(2022, 1, 1))  \# Saturday, unchanged
datetime.datetime(2022, 1, 1, 0, 0)

Copy to clipboard

On this page