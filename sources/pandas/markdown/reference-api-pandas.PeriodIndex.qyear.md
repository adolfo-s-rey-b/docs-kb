[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.qyear.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.PeriodIndex.qyear.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.qyear.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.PeriodIndex.qyear.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.PeriodIndex.qyear.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.PeriodIndex.qyear.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.PeriodIndex.qyear.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.PeriodIndex.qyear.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.PeriodIndex.qyear.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.PeriodIndex.qyear.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.PeriodIndex.qyear.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.PeriodIndex.qyear.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.PeriodIndex.qyear.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.PeriodIndex.qyear.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.PeriodIndex.qyear[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.qyear.html#pandas-periodindex-qyear "Link to this heading")

========================================================================================================================================================

property PeriodIndex.qyear[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/period.py#L643-L685)
[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.qyear.html#pandas.PeriodIndex.qyear "Link to this definition")

Fiscal year the Period lies in according to its starting-quarter.

The year and the qyear of the period will be the same if the fiscal and calendar years are the same. When they are not, the fiscal year can be different from the calendar year of the period.

Returns:

Index

The fiscal year of each period.

See also

[`PeriodIndex.quarter`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.quarter.html#pandas.PeriodIndex.quarter "pandas.PeriodIndex.quarter")

The quarter of the date.

[`PeriodIndex.year`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.year.html#pandas.PeriodIndex.year "pandas.PeriodIndex.year")

The year of the period.

Examples

If the natural and fiscal year are the same, qyear and year will be the same.

\>>> idx \= pd.PeriodIndex(\["2018Q1"\], freq\="Q")
\>>> idx.qyear
Index(\[2018\], dtype='int64')
\>>> idx.year
Index(\[2018\], dtype='int64')

Copy to clipboard

If the fiscal year starts in April (Q-MAR), the first quarter of 2018 will start in April 2017. year will then be 2017, but qyear will be the fiscal year, 2018.

\>>> idx \= pd.PeriodIndex(\["2018Q1"\], freq\="Q-MAR")
\>>> idx.start\_time
DatetimeIndex(\['2017-04-01'\], dtype='datetime64\[us\]', freq=None)
\>>> idx.qyear
Index(\[2018\], dtype='int64')
\>>> idx.year
Index(\[2017\], dtype='int64')

Copy to clipboard

On this page