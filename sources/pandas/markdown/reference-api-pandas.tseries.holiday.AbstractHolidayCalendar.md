[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.holiday.AbstractHolidayCalendar[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.html#pandas-tseries-holiday-abstractholidaycalendar "Link to this heading")

==========================================================================================================================================================================================================================

class pandas.tseries.holiday.AbstractHolidayCalendar(_name\=''_, _rules\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/tseries/holiday.py#L855-L1128)
[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.html#pandas.tseries.holiday.AbstractHolidayCalendar "Link to this definition")

Abstract interface to create holidays following certain rules.

A subclass normally defines its holidays by setting `rules` to a list of [`Holiday`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.Holiday.html#pandas.tseries.holiday.Holiday "pandas.tseries.holiday.Holiday")
 instances directly on the class body. Alternatively, a set of rules can be passed to the constructor. The calendar can then be used to compute the holiday dates falling within a given date range via [`holidays()`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.holidays.html#pandas.tseries.holiday.AbstractHolidayCalendar.holidays "pandas.tseries.holiday.AbstractHolidayCalendar.holidays")
.

Parameters:

**name**str

Name of the holiday calendar, defaults to class name.

**rules**array of Holiday objects

A set of rules used to create the holidays.

See also

`tseries.holiday.Holiday`

Class that defines a holiday with start/end dates and rules for observance.

`tseries.offsets.CustomBusinessDay`

DateOffset subclass representing possibly n business days excluding holidays.

Examples

\>>> from pandas.tseries.holiday import AbstractHolidayCalendar, USLaborDay
\>>> class MyCalendar(AbstractHolidayCalendar):
...     rules \= \[USLaborDay\]
\>>> MyCalendar().holidays(start\="2020-01-01", end\="2020-12-31")
DatetimeIndex(\['2020-09-07'\], dtype='datetime64\[us\]', freq=None)

Copy to clipboard

Attributes

|     |     |
| --- | --- |
| `end_date` |     |
| `rules` |     |
| `start_date` |     |

Methods

|     |     |
| --- | --- |
| [`holidays`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.holidays.html#pandas.tseries.holiday.AbstractHolidayCalendar.holidays "pandas.tseries.holiday.AbstractHolidayCalendar.holidays")<br>(\[start, end, return\_name\]) | Return a curve with holidays between start\_date and end\_date. |
| [`merge`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge.html#pandas.tseries.holiday.AbstractHolidayCalendar.merge "pandas.tseries.holiday.AbstractHolidayCalendar.merge")<br>(other\[, inplace\]) | Merge holiday calendars together. |
| [`merge_class`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge_class.html#pandas.tseries.holiday.AbstractHolidayCalendar.merge_class "pandas.tseries.holiday.AbstractHolidayCalendar.merge_class")<br>(base, other) | Merge holiday calendars together. |
| [`rule_from_name`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.rule_from_name.html#pandas.tseries.holiday.AbstractHolidayCalendar.rule_from_name "pandas.tseries.holiday.AbstractHolidayCalendar.rule_from_name")<br>(name) | Return the rule for the holiday with the given name. |

On this page