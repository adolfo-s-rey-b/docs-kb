[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.calendar.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.calendar.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.calendar.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.calendar.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.calendar.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.calendar.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.calendar.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.calendar.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.calendar.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.calendar.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.calendar.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.calendar.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.calendar.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.calendar.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.CustomBusinessMonthBegin.calendar[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.calendar.html#pandas-tseries-offsets-custombusinessmonthbegin-calendar "Link to this heading")

========================================================================================================================================================================================================================================================

CustomBusinessMonthBegin.calendar[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.calendar.html#pandas.tseries.offsets.CustomBusinessMonthBegin.calendar "Link to this definition")

Return the calendar used for business day calculations.

This property returns the numpy busdaycalendar object used for determining valid business days. For standard business day offsets (e.g., BusinessDay, BusinessHour), this returns None. For custom business day offsets, this returns the calendar that was either passed directly or constructed from weekmask and holidays.

Returns:

np.busdaycalendar or None

The business day calendar used for calculations, or None if using default business day rules.

See also

[`BusinessDay.holidays`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessDay.holidays.html#pandas.tseries.offsets.BusinessDay.holidays "pandas.tseries.offsets.BusinessDay.holidays")

Holidays for standard business day offset.

[`CustomBusinessDay.holidays`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessDay.holidays.html#pandas.tseries.offsets.CustomBusinessDay.holidays "pandas.tseries.offsets.CustomBusinessDay.holidays")

Holidays for custom business day offset.

[`CustomBusinessDay.weekmask`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessDay.weekmask.html#pandas.tseries.offsets.CustomBusinessDay.weekmask "pandas.tseries.offsets.CustomBusinessDay.weekmask")

Weekmask for custom business day offset.

Examples

For standard business offsets, calendar is None:

\>>> bd \= pd.offsets.BusinessDay()
\>>> bd.calendar is None
True

Copy to clipboard

\>>> bh \= pd.offsets.BusinessHour()
\>>> bh.calendar is None
True

Copy to clipboard

For custom business day with explicit holidays:

\>>> holidays \= \[pd.Timestamp("2023-12-25"), pd.Timestamp("2024-01-01")\]
\>>> cbd \= pd.offsets.CustomBusinessDay(holidays\=holidays)
\>>> isinstance(cbd.calendar, np.busdaycalendar)
True

Copy to clipboard

On this page