[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.month.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.PeriodIndex.month.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.month.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.PeriodIndex.month.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.PeriodIndex.month.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.PeriodIndex.month.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.PeriodIndex.month.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.PeriodIndex.month.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.PeriodIndex.month.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.PeriodIndex.month.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.PeriodIndex.month.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.PeriodIndex.month.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.PeriodIndex.month.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.PeriodIndex.month.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.PeriodIndex.month[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.month.html#pandas-periodindex-month "Link to this heading")

========================================================================================================================================================

property PeriodIndex.month[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/period.py#L392-L410)
[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.month.html#pandas.PeriodIndex.month "Link to this definition")

The month as January=1, December=12.

Returns the month component for each period in the index as an integer, where January is 1 and December is 12.

See also

[`PeriodIndex.days_in_month`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.days_in_month.html#pandas.PeriodIndex.days_in_month "pandas.PeriodIndex.days_in_month")

The number of days in the month.

Examples

\>>> idx \= pd.PeriodIndex(\["2023-01", "2023-02", "2023-03"\], freq\="M")
\>>> idx.month
Index(\[1, 2, 3\], dtype='int64')

Copy to clipboard

On this page