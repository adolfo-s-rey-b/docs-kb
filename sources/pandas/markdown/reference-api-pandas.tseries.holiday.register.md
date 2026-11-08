[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.register.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.holiday.register.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.register.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.holiday.register.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.holiday.register.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.holiday.register.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.holiday.register.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.holiday.register.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.holiday.register.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.holiday.register.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.holiday.register.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.holiday.register.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.holiday.register.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.holiday.register.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.holiday.register[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.register.html#pandas-tseries-holiday-register "Link to this heading")

=============================================================================================================================================================================

pandas.tseries.holiday.register(_cls_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/tseries/holiday.py#L759-L797)
[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.register.html#pandas.tseries.holiday.register "Link to this definition")

Add a holiday calendar class to the registry of named calendars.

Calendar classes register themselves as soon as they are defined, so this is rarely called directly. A class is registered under its `name` attribute if it has one and under its class name otherwise, and registering a class under a name that is already taken replaces the earlier one.

See also

`tseries.holiday.get_calendar`

Return an instance of a calendar based on its name.

`tseries.holiday.HolidayCalendarFactory`

Create a holiday calendar class from two sets of rules.

`tseries.holiday.AbstractHolidayCalendar`

Abstract interface to create holidays following certain rules.

Examples

\>>> from pandas.tseries.holiday import (
...     AbstractHolidayCalendar,
...     USLaborDay,
...     get\_calendar,
...     register,
... )
\>>> class MyCalendar(AbstractHolidayCalendar):
...     rules \= \[USLaborDay\]
\>>> MyCalendar.name \= "us\_labor\_only"
\>>> register(MyCalendar)
\>>> \[rule.name for rule in get\_calendar("us\_labor\_only").rules\]
\['Labor Day'\]

Copy to clipboard

On this page