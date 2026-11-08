[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.day_of_year.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.PeriodIndex.day\_of\_year[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.day_of_year.html#pandas-periodindex-day-of-year "Link to this heading")

============================================================================================================================================================================

property PeriodIndex.day\_of\_year[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/period.py#L578-L605)
[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.day_of_year.html#pandas.PeriodIndex.day_of_year "Link to this definition")

The ordinal day of the year.

Returns the day-of-year component for each period, ranging from 1 (January 1st) to 365 or 366 for leap years.

See also

[`PeriodIndex.day`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.day.html#pandas.PeriodIndex.day "pandas.PeriodIndex.day")

The days of the period.

[`PeriodIndex.day_of_week`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.day_of_week.html#pandas.PeriodIndex.day_of_week "pandas.PeriodIndex.day_of_week")

The day of the week with Monday=0, Sunday=6.

[`PeriodIndex.weekofyear`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.weekofyear.html#pandas.PeriodIndex.weekofyear "pandas.PeriodIndex.weekofyear")

The week ordinal of the year.

[`PeriodIndex.year`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.year.html#pandas.PeriodIndex.year "pandas.PeriodIndex.year")

The year of the period.

Examples

\>>> idx \= pd.PeriodIndex(\["2023-01-10", "2023-02-01", "2023-03-01"\], freq\="D")
\>>> idx.day\_of\_year
Index(\[10, 32, 60\], dtype='int64')

Copy to clipboard

\>>> idx \= pd.PeriodIndex(\["2023", "2024", "2025"\], freq\="Y")
\>>> idx
PeriodIndex(\['2023', '2024', '2025'\], dtype='period\[Y-DEC\]')
\>>> idx.day\_of\_year
Index(\[365, 366, 365\], dtype='int64')

Copy to clipboard

On this page