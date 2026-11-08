[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.is_leap_year.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.PeriodIndex.is_leap_year.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.is_leap_year.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.PeriodIndex.is_leap_year.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.PeriodIndex.is_leap_year.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.PeriodIndex.is_leap_year.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.PeriodIndex.is_leap_year.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.PeriodIndex.is_leap_year.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.PeriodIndex.is_leap_year.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.PeriodIndex.is_leap_year.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.PeriodIndex.is_leap_year.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.PeriodIndex.is_leap_year.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.PeriodIndex.is_leap_year.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.PeriodIndex.is_leap_year.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.PeriodIndex.is\_leap\_year[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.is_leap_year.html#pandas-periodindex-is-leap-year "Link to this heading")

===============================================================================================================================================================================

property PeriodIndex.is\_leap\_year[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/period.py#L724-L744)
[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.is_leap_year.html#pandas.PeriodIndex.is_leap_year "Link to this definition")

Logical indicating if the date belongs to a leap year.

Returns a boolean array where `True` indicates the period’s year is a leap year.

See also

[`PeriodIndex.qyear`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.qyear.html#pandas.PeriodIndex.qyear "pandas.PeriodIndex.qyear")

Fiscal year the Period lies in according to its starting-quarter.

[`PeriodIndex.year`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.year.html#pandas.PeriodIndex.year "pandas.PeriodIndex.year")

The year of the period.

Examples

\>>> idx \= pd.PeriodIndex(\["2023", "2024", "2025"\], freq\="Y")
\>>> idx.is\_leap\_year
array(\[False,  True, False\])

Copy to clipboard

On this page