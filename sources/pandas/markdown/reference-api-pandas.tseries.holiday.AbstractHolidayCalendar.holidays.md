[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.holidays.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.holidays.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.holidays.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.holidays.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.holidays.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.holidays.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.holidays.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.holidays.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.holidays.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.holidays.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.holidays.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.holidays.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.holidays.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.holidays.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.holiday.AbstractHolidayCalendar.holidays[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.holidays.html#pandas-tseries-holiday-abstractholidaycalendar-holidays "Link to this heading")

=====================================================================================================================================================================================================================================================

AbstractHolidayCalendar.holidays(_start\=None_, _end\=None_, _return\_name\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/tseries/holiday.py#L940-L1017)
[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.holidays.html#pandas.tseries.holiday.AbstractHolidayCalendar.holidays "Link to this definition")

Return a curve with holidays between start\_date and end\_date.

The holidays for the calendar are computed by evaluating the `dates` of each rule in `self.rules` and merging the results, caching them so that repeated calls covering a previously requested date range do not need to be recomputed.

Parameters:

**start**starting date, datetime-like, optional

The earliest date to consider, defaults to `AbstractHolidayCalendar.start_date`.

**end**ending date, datetime-like, optional

The latest date to consider, defaults to `AbstractHolidayCalendar.end_date`.

**return\_name**bool, optional

If True, return a series that has dates and holiday names. False will only return a DatetimeIndex of dates.

Returns:

DatetimeIndex or Series

DatetimeIndex of holidays, or a Series mapping holiday dates to their names if `return_name` is True.

See also

`tseries.holiday.Holiday.dates`

Calculate holidays observed between start date and end date.

Examples

\>>> from pandas.tseries.holiday import AbstractHolidayCalendar, USLaborDay
\>>> class MyCalendar(AbstractHolidayCalendar):
...     rules \= \[USLaborDay\]
\>>> MyCalendar().holidays(start\="2020-01-01", end\="2020-12-31")
DatetimeIndex(\['2020-09-07'\], dtype='datetime64\[us\]', freq=None)

Copy to clipboard

On this page