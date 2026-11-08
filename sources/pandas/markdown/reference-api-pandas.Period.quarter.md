[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Period.quarter.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Period.quarter[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.quarter.html#pandas-period-quarter "Link to this heading")

===============================================================================================================================================

Period.quarter[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.quarter.html#pandas.Period.quarter "Link to this definition")

Return the quarter this Period falls on.

Quarter 1 includes January through March, quarter 2 includes April through June, quarter 3 includes July through September, and quarter 4 includes October through December.

See also

[`Timestamp.quarter`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.quarter.html#pandas.Timestamp.quarter "pandas.Timestamp.quarter")

Return the quarter of the Timestamp.

[`Period.year`](https://pandas.pydata.org/docs/reference/api/pandas.Period.year.html#pandas.Period.year "pandas.Period.year")

Return the year of the period.

[`Period.month`](https://pandas.pydata.org/docs/reference/api/pandas.Period.month.html#pandas.Period.month "pandas.Period.month")

Return the month of the period.

Examples

\>>> period \= pd.Period('2022-04', 'M')
\>>> period.quarter
2

Copy to clipboard

On this page