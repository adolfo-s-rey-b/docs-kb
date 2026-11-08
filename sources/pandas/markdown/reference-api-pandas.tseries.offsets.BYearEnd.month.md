[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BYearEnd.month.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.BYearEnd.month[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BYearEnd.month.html#pandas-tseries-offsets-byearend-month "Link to this heading")

===============================================================================================================================================================================================

BYearEnd.month[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BYearEnd.month.html#pandas.tseries.offsets.BYearEnd.month "Link to this definition")

Return the month of the year on which this offset applies.

Returns an integer representing the month (1-12) that this offset targets. For year-based offsets, this determines which month is used for calculations.

See also

`tseries.offsets.YearEnd`

Offset to end of year.

`tseries.offsets.YearBegin`

Offset to start of year.

`tseries.offsets.BYearEnd`

Offset to last business day of year.

`tseries.offsets.BYearBegin`

Offset to first business day of year.

Examples

\>>> pd.offsets.BYearBegin().month
1

Copy to clipboard

\>>> pd.offsets.BYearBegin(month\=6).month
6

Copy to clipboard

On this page