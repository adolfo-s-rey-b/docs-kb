[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessMonthBegin.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.BusinessMonthBegin[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessMonthBegin.html#pandas-tseries-offsets-businessmonthbegin "Link to this heading")

===========================================================================================================================================================================================================

class pandas.tseries.offsets.BusinessMonthBegin[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessMonthBegin.html#pandas.tseries.offsets.BusinessMonthBegin "Link to this definition")

DateOffset of one month at the first business day.

BusinessMonthBegin goes to the next date which is the first business day of the month.

Parameters:

**n**int, default 1

The number of months represented.

**normalize**bool, default False

Normalize start/end dates to midnight before generating date range.

See also

[`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.tseries.offsets.DateOffset")

Standard kind of date increment.

Examples

\>>> ts \= pd.Timestamp(2022, 11, 30)
\>>> ts + pd.offsets.BMonthBegin()
Timestamp('2022-12-01 00:00:00')

Copy to clipboard

\>>> ts \= pd.Timestamp(2022, 12, 1)
\>>> ts + pd.offsets.BMonthBegin()
Timestamp('2023-01-02 00:00:00')

Copy to clipboard

If you want to get the start of the current business month:

\>>> ts \= pd.Timestamp(2022, 12, 1)
\>>> pd.offsets.BMonthBegin().rollback(ts)
Timestamp('2022-12-01 00:00:00')

Copy to clipboard

On this page