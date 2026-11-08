[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.qyear.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.qyear.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.qyear.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.qyear.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.qyear.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.qyear.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.qyear.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.qyear.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.qyear.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.qyear.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.qyear.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.qyear.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.qyear.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.qyear.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.qyear[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.qyear.html#pandas-series-dt-qyear "Link to this heading")

==================================================================================================================================================

Series.dt.qyear[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L108-L109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.qyear.html#pandas.Series.dt.qyear "Link to this definition")

Fiscal year the Period lies in according to its starting-quarter.

The year and the qyear of the period will be the same if the fiscal and calendar years are the same. When they are not, the fiscal year can be different from the calendar year of the period.

Returns:

int

The fiscal year of the period.

See also

[`PeriodIndex.quarter`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.quarter.html#pandas.PeriodIndex.quarter "pandas.PeriodIndex.quarter")

The quarter of the date.

[`PeriodIndex.year`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.year.html#pandas.PeriodIndex.year "pandas.PeriodIndex.year")

The year of the period.

Examples

If the natural and fiscal year are the same, qyear and year will be the same.

\>>> per \= pd.Period('2018Q1', freq\='Q')
\>>> per.qyear
2018
\>>> per.year
2018

Copy to clipboard

If the fiscal year starts in April (Q-MAR), the first quarter of 2018 will start in April 2017. year will then be 2017, but qyear will be the fiscal year, 2018.

\>>> per \= pd.Period('2018Q1', freq\='Q-MAR')
\>>> per.start\_time
Timestamp('2017-04-01 00:00:00')
\>>> per.qyear
2018
\>>> per.year
2017

Copy to clipboard

On this page