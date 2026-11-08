[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.USFederalHolidayCalendar.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.holiday.USFederalHolidayCalendar.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.USFederalHolidayCalendar.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.holiday.USFederalHolidayCalendar.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.holiday.USFederalHolidayCalendar.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.holiday.USFederalHolidayCalendar.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.holiday.USFederalHolidayCalendar.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.holiday.USFederalHolidayCalendar.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.holiday.USFederalHolidayCalendar.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.holiday.USFederalHolidayCalendar.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.holiday.USFederalHolidayCalendar.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.holiday.USFederalHolidayCalendar.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.holiday.USFederalHolidayCalendar.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.holiday.USFederalHolidayCalendar.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.holiday.USFederalHolidayCalendar[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.USFederalHolidayCalendar.html#pandas-tseries-holiday-usfederalholidaycalendar "Link to this heading")

=============================================================================================================================================================================================================================

class pandas.tseries.holiday.USFederalHolidayCalendar(_name\=''_, _rules\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/tseries/holiday.py#L1156-L1210)
[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.USFederalHolidayCalendar.html#pandas.tseries.holiday.USFederalHolidayCalendar "Link to this definition")

US Federal Government holiday calendar.

The rules follow the federal holiday schedule published by the US Office of Personnel Management: [https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays/](https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays/)

Holidays that land on a weekend are observed on the nearest weekday. Pass an instance as the `calendar` argument of [`CustomBusinessDay`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessDay.html#pandas.tseries.offsets.CustomBusinessDay "pandas.tseries.offsets.CustomBusinessDay")
 to skip these dates in business day arithmetic.

Parameters:

**name**str

Name of the holiday calendar, defaults to class name.

**rules**array of Holiday objects

A set of rules used to create the holidays.

See also

`tseries.holiday.AbstractHolidayCalendar`

Abstract interface to create holidays following certain rules.

`tseries.holiday.nearest_workday`

Move Saturday to Friday and Sunday to Monday.

`tseries.holiday.get_calendar`

Return an instance of a calendar based on its name.

Examples

\>>> from pandas.tseries.holiday import USFederalHolidayCalendar
\>>> USFederalHolidayCalendar().holidays(start\="2024-06-01", end\="2024-07-31")
DatetimeIndex(\['2024-06-19', '2024-07-04'\], dtype='datetime64\[us\]', freq=None)

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
| `holidays`(\[start, end, return\_name\]) | Return a curve with holidays between start\_date and end\_date. |
| `merge`(other\[, inplace\]) | Merge holiday calendars together. |
| `merge_class`(base, other) | Merge holiday calendars together. |
| `rule_from_name`(name) | Return the rule for the holiday with the given name. |

On this page