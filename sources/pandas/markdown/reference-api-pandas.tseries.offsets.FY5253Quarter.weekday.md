[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.weekday.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.FY5253Quarter.weekday.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.weekday.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.FY5253Quarter.weekday.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.FY5253Quarter.weekday.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.FY5253Quarter.weekday.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.FY5253Quarter.weekday.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.FY5253Quarter.weekday.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.FY5253Quarter.weekday.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.FY5253Quarter.weekday.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.FY5253Quarter.weekday.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.FY5253Quarter.weekday.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.FY5253Quarter.weekday.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.FY5253Quarter.weekday.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.FY5253Quarter.weekday[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.weekday.html#pandas-tseries-offsets-fy5253quarter-weekday "Link to this heading")

====================================================================================================================================================================================================================

FY5253Quarter.weekday[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.weekday.html#pandas.tseries.offsets.FY5253Quarter.weekday "Link to this definition")

Return the weekday used by the fiscal year.

This is the day of the week on which the fiscal year ends. The value is an integer from 0 (Monday) to 6 (Sunday).

See also

[`FY5253.startingMonth`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.startingMonth.html#pandas.tseries.offsets.FY5253.startingMonth "pandas.tseries.offsets.FY5253.startingMonth")

Return the starting month of the fiscal year.

[`FY5253.variation`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.variation.html#pandas.tseries.offsets.FY5253.variation "pandas.tseries.offsets.FY5253.variation")

Return the variation of the fiscal year.

Examples

\>>> offset \= pd.offsets.FY5253(weekday\=4, startingMonth\=12, variation\="nearest")
\>>> offset.weekday
4

Copy to clipboard

On this page