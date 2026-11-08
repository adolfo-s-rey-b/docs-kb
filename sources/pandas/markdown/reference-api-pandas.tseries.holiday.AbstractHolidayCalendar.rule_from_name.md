[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.rule_from_name.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.rule_from_name.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.rule_from_name.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.rule_from_name.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.rule_from_name.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.rule_from_name.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.rule_from_name.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.rule_from_name.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.rule_from_name.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.rule_from_name.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.rule_from_name.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.rule_from_name.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.rule_from_name.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.rule_from_name.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.holiday.AbstractHolidayCalendar.rule\_from\_name[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.rule_from_name.html#pandas-tseries-holiday-abstractholidaycalendar-rule-from-name "Link to this heading")

=========================================================================================================================================================================================================================================================================

AbstractHolidayCalendar.rule\_from\_name(_name_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/tseries/holiday.py#L903-L938)
[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.rule_from_name.html#pandas.tseries.holiday.AbstractHolidayCalendar.rule_from_name "Link to this definition")

Return the rule for the holiday with the given name.

Searches `self.rules` for a [`Holiday`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.Holiday.html#pandas.tseries.holiday.Holiday "pandas.tseries.holiday.Holiday")
 whose `name` attribute matches exactly.

Parameters:

**name**str

Name of the holiday whose rule should be returned.

Returns:

Holiday or None

The matching rule from `self.rules`, or None if no rule with the given name is found.

See also

`tseries.holiday.AbstractHolidayCalendar.holidays`

Return a curve with holidays between start\_date and end\_date.

Examples

\>>> from pandas.tseries.holiday import AbstractHolidayCalendar, USLaborDay
\>>> class MyCalendar(AbstractHolidayCalendar):
...     rules \= \[USLaborDay\]
\>>> MyCalendar().rule\_from\_name("Labor Day")
Holiday: Labor Day (month=9, day=1, offset=<DateOffset: weekday=MO(+1)>)

Copy to clipboard

On this page