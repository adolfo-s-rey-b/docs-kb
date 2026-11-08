[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.holiday.AbstractHolidayCalendar.merge[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge.html#pandas-tseries-holiday-abstractholidaycalendar-merge "Link to this heading")

============================================================================================================================================================================================================================================

AbstractHolidayCalendar.merge(_other_, _inplace\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/tseries/holiday.py#L1082-L1128)
[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge.html#pandas.tseries.holiday.AbstractHolidayCalendar.merge "Link to this definition")

Merge holiday calendars together.

The caller’s class rules take precedence. The merge will be done based on each holiday’s name.

Parameters:

**other**holiday calendar

Calendar, instance/subclass, or array of Holiday objects to merge into this calendar’s rules.

**inplace**bool (default=False)

If True set rule\_table to holidays, else return array of Holidays.

Returns:

list of Holiday or None

The combined list of holidays if `inplace` is False, otherwise None.

See also

`tseries.holiday.AbstractHolidayCalendar.merge_class`

Merge holiday calendars together.

Examples

\>>> from pandas.tseries.holiday import (
...     AbstractHolidayCalendar,
...     USLaborDay,
...     USMemorialDay,
... )
\>>> class Calendar1(AbstractHolidayCalendar):
...     rules \= \[USMemorialDay\]
\>>> class Calendar2(AbstractHolidayCalendar):
...     rules \= \[USLaborDay\]
\>>> merged \= Calendar1().merge(Calendar2())
\>>> \[holiday.name for holiday in merged\]
\['Labor Day', 'Memorial Day'\]

Copy to clipboard

On this page