[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.Holiday.dates.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.holiday.Holiday.dates.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.Holiday.dates.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.holiday.Holiday.dates.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.holiday.Holiday.dates.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.holiday.Holiday.dates.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.holiday.Holiday.dates.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.holiday.Holiday.dates.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.holiday.Holiday.dates.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.holiday.Holiday.dates.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.holiday.Holiday.dates.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.holiday.Holiday.dates.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.holiday.Holiday.dates.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.holiday.Holiday.dates.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.holiday.Holiday.dates[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.Holiday.dates.html#pandas-tseries-holiday-holiday-dates "Link to this heading")

============================================================================================================================================================================================

Holiday.dates(_start\_date_, _end\_date_, _return\_name\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/tseries/holiday.py#L605-L686)
[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.Holiday.dates.html#pandas.tseries.holiday.Holiday.dates "Link to this definition")

Calculate holidays observed between start date and end date.

Dates are computed from the rules defined for this holiday, i.e. its fixed `year`/`month`/`day`, or its `offset`/`observance` applied to each occurrence of `month`/`day` between the year before `start_date` and the year after `end_date`.

Parameters:

**start\_date**starting date, datetime-like, optional

The earliest date to consider in the search.

**end\_date**ending date, datetime-like, optional

The latest date to consider in the search.

**return\_name**bool, optional, default=False

If True, return a series that has dates and holiday names. False will only return dates.

Returns:

Series or DatetimeIndex

Series if return\_name is True, otherwise a DatetimeIndex of the holiday’s dates.

See also

`tseries.holiday.AbstractHolidayCalendar.holidays`

Return a curve with holidays between start\_date and end\_date.

Examples

\>>> from dateutil.relativedelta import MO
\>>> USMemorialDay \= pd.tseries.holiday.Holiday(
...     "Memorial Day", month\=5, day\=31, offset\=pd.DateOffset(weekday\=MO(\-1))
... )
\>>> USMemorialDay.dates("2020-01-01", "2021-12-31")
DatetimeIndex(\['2020-05-25', '2021-05-31'\], dtype='datetime64\[us\]', freq=None)

Copy to clipboard

On this page