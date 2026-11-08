[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BYearBegin.month.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.BYearBegin.month.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BYearBegin.month.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.BYearBegin.month.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.BYearBegin.month.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.BYearBegin.month.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.BYearBegin.month.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.BYearBegin.month.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.BYearBegin.month.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.BYearBegin.month.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.BYearBegin.month.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.BYearBegin.month.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.BYearBegin.month.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.BYearBegin.month.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.BYearBegin.month[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BYearBegin.month.html#pandas-tseries-offsets-byearbegin-month "Link to this heading")

=====================================================================================================================================================================================================

BYearBegin.month[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BYearBegin.month.html#pandas.tseries.offsets.BYearBegin.month "Link to this definition")

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