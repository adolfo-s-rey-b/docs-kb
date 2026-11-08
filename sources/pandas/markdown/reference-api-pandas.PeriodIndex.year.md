[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.year.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.PeriodIndex.year.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.year.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.PeriodIndex.year.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.PeriodIndex.year.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.PeriodIndex.year.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.PeriodIndex.year.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.PeriodIndex.year.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.PeriodIndex.year.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.PeriodIndex.year.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.PeriodIndex.year.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.PeriodIndex.year.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.PeriodIndex.year.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.PeriodIndex.year.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.PeriodIndex.year[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.year.html#pandas-periodindex-year "Link to this heading")

=====================================================================================================================================================

property PeriodIndex.year[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/period.py#L370-L390)
[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.year.html#pandas.PeriodIndex.year "Link to this definition")

The year of the period.

Returns the year component for each period in the index.

See also

[`PeriodIndex.day_of_year`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.day_of_year.html#pandas.PeriodIndex.day_of_year "pandas.PeriodIndex.day_of_year")

The ordinal day of the year.

[`PeriodIndex.is_leap_year`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.is_leap_year.html#pandas.PeriodIndex.is_leap_year "pandas.PeriodIndex.is_leap_year")

Logical indicating if the date belongs to a leap year.

[`PeriodIndex.weekofyear`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.weekofyear.html#pandas.PeriodIndex.weekofyear "pandas.PeriodIndex.weekofyear")

The week ordinal of the year.

Examples

\>>> idx \= pd.PeriodIndex(\["2023", "2024", "2025"\], freq\="Y")
\>>> idx.year
Index(\[2023, 2024, 2025\], dtype='int64')

Copy to clipboard

On this page