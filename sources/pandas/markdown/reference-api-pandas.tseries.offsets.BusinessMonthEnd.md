[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessMonthEnd.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.BusinessMonthEnd.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessMonthEnd.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.BusinessMonthEnd.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.BusinessMonthEnd.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.BusinessMonthEnd.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.BusinessMonthEnd.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.BusinessMonthEnd.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.BusinessMonthEnd.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.BusinessMonthEnd.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.BusinessMonthEnd.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.BusinessMonthEnd.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.BusinessMonthEnd.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.BusinessMonthEnd.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.BusinessMonthEnd[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessMonthEnd.html#pandas-tseries-offsets-businessmonthend "Link to this heading")

=====================================================================================================================================================================================================

class pandas.tseries.offsets.BusinessMonthEnd[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessMonthEnd.html#pandas.tseries.offsets.BusinessMonthEnd "Link to this definition")

DateOffset increments between the last business day of the month.

BusinessMonthEnd goes to the next date which is the last business day of the month.

Parameters:

**n**int, default 1

The number of months represented.

**normalize**bool, default False

Normalize start/end dates to midnight before generating date range.

See also

[`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.tseries.offsets.DateOffset")

Standard kind of date increment.

Examples

\>>> ts \= pd.Timestamp(2022, 11, 29)
\>>> ts + pd.offsets.BMonthEnd()
Timestamp('2022-11-30 00:00:00')

Copy to clipboard

\>>> ts \= pd.Timestamp(2022, 11, 30)
\>>> ts + pd.offsets.BMonthEnd()
Timestamp('2022-12-30 00:00:00')

Copy to clipboard

If you want to get the end of the current business month:

\>>> ts \= pd.Timestamp(2022, 11, 30)
\>>> pd.offsets.BMonthEnd().rollforward(ts)
Timestamp('2022-11-30 00:00:00')

Copy to clipboard

On this page