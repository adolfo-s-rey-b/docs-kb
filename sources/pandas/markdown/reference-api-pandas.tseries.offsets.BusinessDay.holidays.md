[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessDay.holidays.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.BusinessDay.holidays.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessDay.holidays.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.BusinessDay.holidays.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.BusinessDay.holidays.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.BusinessDay.holidays.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.BusinessDay.holidays.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.BusinessDay.holidays.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.BusinessDay.holidays.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.BusinessDay.holidays.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.BusinessDay.holidays.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.BusinessDay.holidays.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.BusinessDay.holidays.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.BusinessDay.holidays.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.BusinessDay.holidays[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessDay.holidays.html#pandas-tseries-offsets-businessday-holidays "Link to this heading")

=================================================================================================================================================================================================================

BusinessDay.holidays[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessDay.holidays.html#pandas.tseries.offsets.BusinessDay.holidays "Link to this definition")

Return the holidays used for custom business day calculations.

This property returns a tuple or list of holidays used when calculating business days for custom business day offsets. For non-custom business offsets (e.g., standard BusinessDay, BusinessHour), this will be None.

Returns:

tuple, list, or None

Holidays used in business day calculations, or None if no custom holidays are specified.

See also

[`BusinessDay.holidays`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessDay.holidays.html#pandas.tseries.offsets.BusinessDay.holidays "pandas.tseries.offsets.BusinessDay.holidays")

Holidays for standard business day offset.

[`BusinessHour.holidays`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.holidays.html#pandas.tseries.offsets.BusinessHour.holidays "pandas.tseries.offsets.BusinessHour.holidays")

Holidays for standard business hour offset.

[`CustomBusinessDay.holidays`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessDay.holidays.html#pandas.tseries.offsets.CustomBusinessDay.holidays "pandas.tseries.offsets.CustomBusinessDay.holidays")

Holidays for custom business day offset.

[`CustomBusinessHour.holidays`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessHour.holidays.html#pandas.tseries.offsets.CustomBusinessHour.holidays "pandas.tseries.offsets.CustomBusinessHour.holidays")

Holidays for custom business hour offset.

[`CustomBusinessMonthEnd.holidays`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.holidays.html#pandas.tseries.offsets.CustomBusinessMonthEnd.holidays "pandas.tseries.offsets.CustomBusinessMonthEnd.holidays")

Holidays for custom business month end offset.

[`CustomBusinessMonthBegin.holidays`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.holidays.html#pandas.tseries.offsets.CustomBusinessMonthBegin.holidays "pandas.tseries.offsets.CustomBusinessMonthBegin.holidays")

Holidays for custom business month begin offset.

[`CustomBusinessDay.weekmask`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessDay.weekmask.html#pandas.tseries.offsets.CustomBusinessDay.weekmask "pandas.tseries.offsets.CustomBusinessDay.weekmask")

Weekmask for custom business day offset.

[`CustomBusinessDay.calendar`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessDay.calendar.html#pandas.tseries.offsets.CustomBusinessDay.calendar "pandas.tseries.offsets.CustomBusinessDay.calendar")

Calendar for custom business day offset.

Examples

For standard business offsets, holidays is None:

\>>> bd \= pd.offsets.BusinessDay()
\>>> bd.holidays is None
True

Copy to clipboard

\>>> bh \= pd.offsets.BusinessHour()
\>>> bh.holidays is None
True

Copy to clipboard

For custom business day with explicit holidays:

\>>> holidays \= \[pd.Timestamp("2023-12-25"), pd.Timestamp("2024-01-01")\]
\>>> cbd \= pd.offsets.CustomBusinessDay(holidays\=holidays)
\>>> cbd.holidays
(Timestamp('2023-12-25 00:00:00'), Timestamp('2024-01-01 00:00:00'))

Copy to clipboard

For custom business hour with explicit holidays:

\>>> cbh \= pd.offsets.CustomBusinessHour(holidays\=holidays)
\>>> cbh.holidays
(Timestamp('2023-12-25 00:00:00'), Timestamp('2024-01-01 00:00:00'))

Copy to clipboard

For custom business month end with explicit holidays:

\>>> cbme \= pd.offsets.CustomBusinessMonthEnd(holidays\=holidays)
\>>> cbme.holidays
(Timestamp('2023-12-25 00:00:00'), Timestamp('2024-01-01 00:00:00'))

Copy to clipboard

For custom business month begin with explicit holidays:

\>>> cbmb \= pd.offsets.CustomBusinessMonthBegin(holidays\=holidays)
\>>> cbmb.holidays
(Timestamp('2023-12-25 00:00:00'), Timestamp('2024-01-01 00:00:00'))

Copy to clipboard

For custom business offsets with a calendar:

\>>> from pandas.tseries.holiday import USFederalHolidayCalendar
\>>> cal \= USFederalHolidayCalendar()
\>>> cbd\_cal \= pd.offsets.CustomBusinessDay(calendar\=cal)
\>>> isinstance(cbd\_cal.holidays, tuple)
True

Copy to clipboard

\>>> cbh\_cal \= pd.offsets.CustomBusinessHour(calendar\=cal)
\>>> isinstance(cbh\_cal.holidays, tuple)
True

Copy to clipboard

On this page