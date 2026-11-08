[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.get_calendar.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.holiday.get_calendar.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.get_calendar.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.holiday.get_calendar.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.holiday.get_calendar.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.holiday.get_calendar.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.holiday.get_calendar.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.holiday.get_calendar.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.holiday.get_calendar.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.holiday.get_calendar.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.holiday.get_calendar.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.holiday.get_calendar.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.holiday.get_calendar.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.holiday.get_calendar.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.holiday.get\_calendar[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.get_calendar.html#pandas-tseries-holiday-get-calendar "Link to this heading")

==========================================================================================================================================================================================

pandas.tseries.holiday.get\_calendar(_name_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/tseries/holiday.py#L800-L845)
[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.get_calendar.html#pandas.tseries.holiday.get_calendar "Link to this definition")

Return an instance of a calendar based on its name.

The calendar class does not have to be kept around, since every calendar class is registered by name as soon as it is defined.

Parameters:

**name**str

Calendar name to return an instance of. This is the class name, unless the class sets a `name` attribute.

Returns:

AbstractHolidayCalendar

A new instance of the registered calendar class.

Raises:

KeyError

If no calendar is registered under `name`.

See also

`tseries.holiday.register`

Add a holiday calendar class to the registry of named calendars.

`tseries.holiday.HolidayCalendarFactory`

Create a holiday calendar class from two sets of rules.

`tseries.holiday.AbstractHolidayCalendar`

Abstract interface to create holidays following certain rules.

Examples

\>>> from pandas.tseries.holiday import (
...     AbstractHolidayCalendar,
...     USLaborDay,
...     get\_calendar,
... )
\>>> class MyCalendar(AbstractHolidayCalendar):
...     rules \= \[USLaborDay\]
\>>> cal \= get\_calendar("MyCalendar")
\>>> cal.holidays(start\="2020-01-01", end\="2020-12-31")
DatetimeIndex(\['2020-09-07'\], dtype='datetime64\[us\]', freq=None)

Copy to clipboard

On this page