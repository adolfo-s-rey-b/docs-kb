[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.weekmask.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.BusinessHour.weekmask[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.weekmask.html#pandas-tseries-offsets-businesshour-weekmask "Link to this heading")

====================================================================================================================================================================================================================

BusinessHour.weekmask[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.weekmask.html#pandas.tseries.offsets.BusinessHour.weekmask "Link to this definition")

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