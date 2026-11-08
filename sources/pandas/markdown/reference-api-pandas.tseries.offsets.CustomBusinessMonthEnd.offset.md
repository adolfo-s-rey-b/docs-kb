[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.offset.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.offset.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.offset.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.offset.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.offset.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.offset.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.offset.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.offset.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.offset.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.offset.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.offset.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.offset.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.offset.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.offset.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.CustomBusinessMonthEnd.offset[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.offset.html#pandas-tseries-offsets-custombusinessmonthend-offset "Link to this heading")

============================================================================================================================================================================================================================================

CustomBusinessMonthEnd.offset[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.offset.html#pandas.tseries.offsets.CustomBusinessMonthEnd.offset "Link to this definition")

Return the time offset applied to the business day.

This property returns the timedelta offset that is added to the business day calculation result. It allows for shifting the result by a fixed time amount.

Returns:

timedelta

The time offset applied to the business day.

See also

[`BusinessDay`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessDay.html#pandas.tseries.offsets.BusinessDay "pandas.tseries.offsets.BusinessDay")

Represents a single business day offset.

[`CustomBusinessDay`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessDay.html#pandas.tseries.offsets.CustomBusinessDay "pandas.tseries.offsets.CustomBusinessDay")

Custom business day offset with configurable weekmask.

Examples

\>>> bd \= pd.offsets.BusinessDay()
\>>> bd.offset
datetime.timedelta(0)

Copy to clipboard

\>>> import datetime as dt
\>>> bd \= pd.offsets.BusinessDay(offset\=dt.timedelta(hours\=2))
\>>> bd.offset
datetime.timedelta(seconds=7200)

Copy to clipboard

On this page