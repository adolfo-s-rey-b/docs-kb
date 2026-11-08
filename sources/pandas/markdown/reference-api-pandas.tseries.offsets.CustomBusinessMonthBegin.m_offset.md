[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.m_offset.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.m_offset.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.m_offset.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.m_offset.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.m_offset.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.m_offset.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.m_offset.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.m_offset.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.m_offset.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.m_offset.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.m_offset.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.m_offset.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.m_offset.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.m_offset.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.CustomBusinessMonthBegin.m\_offset[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.m_offset.html#pandas-tseries-offsets-custombusinessmonthbegin-m-offset "Link to this heading")

=========================================================================================================================================================================================================================================================

CustomBusinessMonthBegin.m\_offset[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.m_offset.html#pandas.tseries.offsets.CustomBusinessMonthBegin.m_offset "Link to this definition")

Return a MonthBegin or MonthEnd offset.

This is used internally to compute the month-based component of the custom business month offset calculation.

See also

`tseries.offsets.MonthBegin`

Represents the start of the month.

`tseries.offsets.MonthEnd`

Represents the end of the month.

Examples

\>>> pd.offsets.CustomBusinessMonthBegin().m\_offset
<MonthBegin>

Copy to clipboard

\>>> pd.offsets.CustomBusinessMonthEnd().m\_offset
<MonthEnd>

Copy to clipboard

On this page