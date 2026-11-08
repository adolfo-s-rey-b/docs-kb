[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.HolidayCalendarFactory.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.holiday.HolidayCalendarFactory[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.HolidayCalendarFactory.html#pandas-tseries-holiday-holidaycalendarfactory "Link to this heading")

=======================================================================================================================================================================================================================

pandas.tseries.holiday.HolidayCalendarFactory(_name_, _base_, _other_, _base\_class\=<class 'pandas.tseries.holiday.AbstractHolidayCalendar'>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/tseries/holiday.py#L1213-L1264)
[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.HolidayCalendarFactory.html#pandas.tseries.holiday.HolidayCalendarFactory "Link to this definition")

Create a holiday calendar class from two sets of rules.

The rules of `base` and `other` are merged by holiday name, with `base` winning any clash, and the result becomes the `rules` of a new calendar class. That class registers itself under `name`, so [`get_calendar()`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.get_calendar.html#pandas.tseries.holiday.get_calendar "pandas.tseries.holiday.get_calendar")
 can find it later.

Parameters:

**name**str

Name of the calendar class to create.

**base**AbstractHolidayCalendar

Instance/subclass or array of Holiday objects whose rules take precedence.

**other**AbstractHolidayCalendar

Instance/subclass or array of Holiday objects to merge into `base`.

**base\_class**type, default AbstractHolidayCalendar

The class the new calendar class inherits from.

Returns:

type

A new subclass of `base_class` holding the merged rules.

See also

`tseries.holiday.AbstractHolidayCalendar.merge_class`

Merge holiday calendars together.

`tseries.holiday.get_calendar`

Return an instance of a calendar based on its name.

`tseries.holiday.register`

Add a holiday calendar class to the registry of named calendars.

Examples

\>>> from pandas.tseries.holiday import (
...     AbstractHolidayCalendar,
...     HolidayCalendarFactory,
...     USLaborDay,
...     USMemorialDay,
... )
\>>> class MyCalendar(AbstractHolidayCalendar):
...     rules \= \[USMemorialDay\]
\>>> NewCalendar \= HolidayCalendarFactory("NewCalendar", MyCalendar, USLaborDay)
\>>> \[rule.name for rule in NewCalendar.rules\]
\['Labor Day', 'Memorial Day'\]

Copy to clipboard

On this page