[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.quarter.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.PeriodIndex.quarter.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.quarter.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.PeriodIndex.quarter.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.PeriodIndex.quarter.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.PeriodIndex.quarter.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.PeriodIndex.quarter.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.PeriodIndex.quarter.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.PeriodIndex.quarter.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.PeriodIndex.quarter.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.PeriodIndex.quarter.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.PeriodIndex.quarter.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.PeriodIndex.quarter.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.PeriodIndex.quarter.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.PeriodIndex.quarter[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.quarter.html#pandas-periodindex-quarter "Link to this heading")

==============================================================================================================================================================

property PeriodIndex.quarter[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/period.py#L623-L641)
[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.quarter.html#pandas.PeriodIndex.quarter "Link to this definition")

The quarter of the date.

Returns the quarter (1 through 4) for each period in the index.

See also

[`PeriodIndex.qyear`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.qyear.html#pandas.PeriodIndex.qyear "pandas.PeriodIndex.qyear")

Fiscal year the Period lies in according to its starting-quarter.

Examples

\>>> idx \= pd.PeriodIndex(\["2023-01", "2023-02", "2023-03"\], freq\="M")
\>>> idx.quarter
Index(\[1, 1, 1\], dtype='int64')

Copy to clipboard

On this page