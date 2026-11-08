[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge_class.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge_class.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge_class.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge_class.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge_class.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge_class.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge_class.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge_class.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge_class.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge_class.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge_class.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge_class.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge_class.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge_class.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.holiday.AbstractHolidayCalendar.merge\_class[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge_class.html#pandas-tseries-holiday-abstractholidaycalendar-merge-class "Link to this heading")

===============================================================================================================================================================================================================================================================

static AbstractHolidayCalendar.merge\_class(_base_, _other_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/tseries/holiday.py#L1019-L1080)
[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge_class.html#pandas.tseries.holiday.AbstractHolidayCalendar.merge_class "Link to this definition")

Merge holiday calendars together.

The base calendar will take precedence to other. The merge will be done based on each holiday’s name.

Parameters:

**base**AbstractHolidayCalendar

Instance/subclass or array of Holiday objects.

**other**AbstractHolidayCalendar

Instance/subclass or array of Holiday objects.

Returns:

list of Holiday

Combined list of holidays from both calendars, with `base` taking precedence over `other` for holidays sharing the same name.

See also

`tseries.holiday.AbstractHolidayCalendar.merge`

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
\>>> merged \= AbstractHolidayCalendar.merge\_class(Calendar1, Calendar2)
\>>> \[holiday.name for holiday in merged\]
\['Labor Day', 'Memorial Day'\]

Copy to clipboard

On this page