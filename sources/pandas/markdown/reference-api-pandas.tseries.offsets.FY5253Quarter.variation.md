[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.variation.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.FY5253Quarter.variation.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.variation.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.FY5253Quarter.variation.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.FY5253Quarter.variation.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.FY5253Quarter.variation.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.FY5253Quarter.variation.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.FY5253Quarter.variation.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.FY5253Quarter.variation.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.FY5253Quarter.variation.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.FY5253Quarter.variation.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.FY5253Quarter.variation.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.FY5253Quarter.variation.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.FY5253Quarter.variation.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.FY5253Quarter.variation[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.variation.html#pandas-tseries-offsets-fy5253quarter-variation "Link to this heading")

==========================================================================================================================================================================================================================

FY5253Quarter.variation[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.variation.html#pandas.tseries.offsets.FY5253Quarter.variation "Link to this definition")

Return the variation of the fiscal year.

The variation determines how the fiscal year end is calculated. It can be either “nearest” or “last”.

Returns:

str

Either “nearest” or “last”.

See also

[`FY5253.weekday`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.weekday.html#pandas.tseries.offsets.FY5253.weekday "pandas.tseries.offsets.FY5253.weekday")

Return the weekday used by the fiscal year.

[`FY5253.startingMonth`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.startingMonth.html#pandas.tseries.offsets.FY5253.startingMonth "pandas.tseries.offsets.FY5253.startingMonth")

Return the starting month of the fiscal year.

Examples

\>>> offset \= pd.offsets.FY5253(weekday\=4, startingMonth\=12, variation\="nearest")
\>>> offset.variation
'nearest'

Copy to clipboard

On this page