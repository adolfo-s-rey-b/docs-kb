[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.weekmask.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.weekmask.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.weekmask.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.weekmask.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.weekmask.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.weekmask.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.weekmask.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.weekmask.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.weekmask.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.weekmask.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.weekmask.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.weekmask.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.weekmask.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.weekmask.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.CustomBusinessMonthEnd.weekmask[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.weekmask.html#pandas-tseries-offsets-custombusinessmonthend-weekmask "Link to this heading")

==================================================================================================================================================================================================================================================

CustomBusinessMonthEnd.weekmask[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.weekmask.html#pandas.tseries.offsets.CustomBusinessMonthEnd.weekmask "Link to this definition")

Return the weekmask used for custom business day calculations.

This property returns the weekmask string that defines which days of the week are considered business days. For non-custom business offsets (e.g., standard BusinessDay, BusinessHour), this will be None. For custom business day offsets, this returns the weekmask that was specified or the default ‘Mon Tue Wed Thu Fri’.

Returns:

str or None

String representing valid business days (e.g., ‘Mon Tue Wed Thu Fri’), or None if using default business day rules.

See also

[`BusinessDay.holidays`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessDay.holidays.html#pandas.tseries.offsets.BusinessDay.holidays "pandas.tseries.offsets.BusinessDay.holidays")

Holidays for standard business day offset.

[`CustomBusinessDay.holidays`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessDay.holidays.html#pandas.tseries.offsets.CustomBusinessDay.holidays "pandas.tseries.offsets.CustomBusinessDay.holidays")

Holidays for custom business day offset.

[`CustomBusinessDay.calendar`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessDay.calendar.html#pandas.tseries.offsets.CustomBusinessDay.calendar "pandas.tseries.offsets.CustomBusinessDay.calendar")

Calendar for custom business day offset.

Examples

For standard business offsets, weekmask is None:

\>>> bd \= pd.offsets.BusinessDay()
\>>> bd.weekmask is None
True

Copy to clipboard

\>>> bh \= pd.offsets.BusinessHour()
\>>> bh.weekmask is None
True

Copy to clipboard

For custom business day with default weekmask:

\>>> cbd \= pd.offsets.CustomBusinessDay()
\>>> cbd.weekmask
'Mon Tue Wed Thu Fri'

Copy to clipboard

For custom business day with custom weekmask:

\>>> cbd \= pd.offsets.CustomBusinessDay(weekmask\="Mon Wed Fri")
\>>> cbd.weekmask
'Mon Wed Fri'

Copy to clipboard

On this page