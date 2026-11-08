[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.MonthEnd.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.MonthEnd[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.MonthEnd.html#pandas-tseries-offsets-monthend "Link to this heading")

=============================================================================================================================================================================

class pandas.tseries.offsets.MonthEnd[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.MonthEnd.html#pandas.tseries.offsets.MonthEnd "Link to this definition")

DateOffset of one month end.

MonthEnd goes to the next date which is an end of the month.

Parameters:

**n**int, default 1

The number of months represented.

**normalize**bool, default False

Normalize start/end dates to midnight before generating date range.

See also

[`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.tseries.offsets.DateOffset")

Standard kind of date increment.

Examples

\>>> ts \= pd.Timestamp(2022, 1, 30)
\>>> ts + pd.offsets.MonthEnd()
Timestamp('2022-01-31 00:00:00')

Copy to clipboard

\>>> ts \= pd.Timestamp(2022, 1, 31)
\>>> ts + pd.offsets.MonthEnd()
Timestamp('2022-02-28 00:00:00')

Copy to clipboard

If you want to get the end of the current month:

\>>> ts \= pd.Timestamp(2022, 1, 31)
\>>> pd.offsets.MonthEnd().rollforward(ts)
Timestamp('2022-01-31 00:00:00')

Copy to clipboard

On this page