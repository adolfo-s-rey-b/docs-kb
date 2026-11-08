[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.day_of_week.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.PeriodIndex.day\_of\_week[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.day_of_week.html#pandas-periodindex-day-of-week "Link to this heading")

============================================================================================================================================================================

property PeriodIndex.day\_of\_week[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/period.py#L523-L544)
[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.day_of_week.html#pandas.PeriodIndex.day_of_week "Link to this definition")

The day of the week with Monday=0, Sunday=6.

Returns the day-of-week component for each period, following the Python convention where Monday is 0 and Sunday is 6.

See also

[`PeriodIndex.day`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.day.html#pandas.PeriodIndex.day "pandas.PeriodIndex.day")

The days of the period.

[`PeriodIndex.day_of_year`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.day_of_year.html#pandas.PeriodIndex.day_of_year "pandas.PeriodIndex.day_of_year")

The ordinal day of the year.

[`PeriodIndex.week`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.week.html#pandas.PeriodIndex.week "pandas.PeriodIndex.week")

The week ordinal of the year.

[`PeriodIndex.weekofyear`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.weekofyear.html#pandas.PeriodIndex.weekofyear "pandas.PeriodIndex.weekofyear")

The week ordinal of the year.

Examples

\>>> idx \= pd.PeriodIndex(\["2023-01-01", "2023-01-02", "2023-01-03"\], freq\="D")
\>>> idx.day\_of\_week
Index(\[6, 0, 1\], dtype='int64')

Copy to clipboard

On this page