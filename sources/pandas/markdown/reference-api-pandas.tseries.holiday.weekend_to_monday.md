[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.weekend_to_monday.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.holiday.weekend_to_monday.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.weekend_to_monday.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.holiday.weekend_to_monday.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.holiday.weekend_to_monday.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.holiday.weekend_to_monday.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.holiday.weekend_to_monday.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.holiday.weekend_to_monday.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.holiday.weekend_to_monday.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.holiday.weekend_to_monday.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.holiday.weekend_to_monday.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.holiday.weekend_to_monday.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.holiday.weekend_to_monday.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.holiday.weekend_to_monday.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.holiday.weekend\_to\_monday[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.weekend_to_monday.html#pandas-tseries-holiday-weekend-to-monday "Link to this heading")

==========================================================================================================================================================================================================

pandas.tseries.holiday.weekend\_to\_monday(_dt_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/tseries/holiday.py#L211-L249)
[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.weekend_to_monday.html#pandas.tseries.holiday.weekend_to_monday "Link to this definition")

Move Saturday and Sunday to the following Monday.

Same as `next_monday`. Needed for holidays such as the Christmas observation in Europe.

Parameters:

**dt**datetime

The date the holiday falls on.

Returns:

datetime

The date the holiday is observed on.

See also

`tseries.holiday.next_monday`

Move Saturday and Sunday to the following Monday.

`tseries.holiday.sunday_to_monday`

Move Sunday to the following Monday.

`tseries.holiday.Holiday`

Class that defines a holiday with start/end dates and rules for observance.

Examples

\>>> from datetime import datetime
\>>> from pandas.tseries.holiday import weekend\_to\_monday
\>>> weekend\_to\_monday(datetime(2022, 1, 1))  \# Saturday
datetime.datetime(2022, 1, 3, 0, 0)
\>>> weekend\_to\_monday(datetime(2022, 1, 2))  \# Sunday
datetime.datetime(2022, 1, 3, 0, 0)

Copy to clipboard

On this page