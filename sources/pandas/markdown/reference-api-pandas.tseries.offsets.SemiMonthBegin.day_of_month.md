[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.SemiMonthBegin.day_of_month.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.SemiMonthBegin.day_of_month.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.SemiMonthBegin.day_of_month.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.SemiMonthBegin.day_of_month.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.SemiMonthBegin.day_of_month.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.SemiMonthBegin.day_of_month.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.SemiMonthBegin.day_of_month.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.SemiMonthBegin.day_of_month.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.SemiMonthBegin.day_of_month.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.SemiMonthBegin.day_of_month.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.SemiMonthBegin.day_of_month.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.SemiMonthBegin.day_of_month.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.SemiMonthBegin.day_of_month.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.SemiMonthBegin.day_of_month.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.SemiMonthBegin.day\_of\_month[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.SemiMonthBegin.day_of_month.html#pandas-tseries-offsets-semimonthbegin-day-of-month "Link to this heading")

========================================================================================================================================================================================================================================

SemiMonthBegin.day\_of\_month[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.SemiMonthBegin.day_of_month.html#pandas.tseries.offsets.SemiMonthBegin.day_of_month "Link to this definition")

Return the day of the month for the semi-monthly offset.

This specifies the day of the month on which the offset falls, in addition to the start (1st) or end (last day) of the month.

See also

[`SemiMonthBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.SemiMonthBegin.html#pandas.tseries.offsets.SemiMonthBegin "pandas.tseries.offsets.SemiMonthBegin")

Offset at the start of the month and mid-month.

[`SemiMonthEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.SemiMonthEnd.html#pandas.tseries.offsets.SemiMonthEnd "pandas.tseries.offsets.SemiMonthEnd")

Offset at mid-month and end of month.

Examples

\>>> pd.offsets.SemiMonthBegin().day\_of\_month
15

Copy to clipboard

\>>> pd.offsets.SemiMonthBegin(day\_of\_month\=20).day\_of\_month
20

Copy to clipboard

On this page