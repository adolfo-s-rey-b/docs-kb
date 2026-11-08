[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.MonthBegin.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.MonthBegin.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.MonthBegin.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.MonthBegin.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.MonthBegin.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.MonthBegin.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.MonthBegin.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.MonthBegin.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.MonthBegin.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.MonthBegin.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.MonthBegin.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.MonthBegin.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.MonthBegin.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.MonthBegin.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.MonthBegin[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.MonthBegin.html#pandas-tseries-offsets-monthbegin "Link to this heading")

===================================================================================================================================================================================

class pandas.tseries.offsets.MonthBegin[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.MonthBegin.html#pandas.tseries.offsets.MonthBegin "Link to this definition")

DateOffset of one month at beginning.

MonthBegin goes to the next date which is a start of the month.

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
\>>> ts + pd.offsets.MonthBegin()
Timestamp('2022-12-01 00:00:00')

Copy to clipboard

\>>> ts \= pd.Timestamp(2022, 12, 1)
\>>> ts + pd.offsets.MonthBegin()
Timestamp('2023-01-01 00:00:00')

Copy to clipboard

If you want to get the start of the current month:

\>>> ts \= pd.Timestamp(2022, 12, 1)
\>>> pd.offsets.MonthBegin().rollback(ts)
Timestamp('2022-12-01 00:00:00')

Copy to clipboard

On this page