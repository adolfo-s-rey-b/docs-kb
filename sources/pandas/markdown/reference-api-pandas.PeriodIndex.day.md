[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.day.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.PeriodIndex.day.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.day.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.PeriodIndex.day.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.PeriodIndex.day.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.PeriodIndex.day.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.PeriodIndex.day.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.PeriodIndex.day.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.PeriodIndex.day.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.PeriodIndex.day.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.PeriodIndex.day.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.PeriodIndex.day.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.PeriodIndex.day.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.PeriodIndex.day.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.PeriodIndex.day[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.day.html#pandas-periodindex-day "Link to this heading")

==================================================================================================================================================

property PeriodIndex.day[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/period.py#L412-L431)
[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.day.html#pandas.PeriodIndex.day "Link to this definition")

The days of the period.

Returns the day-of-month component for each period in the index.

See also

[`PeriodIndex.day_of_week`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.day_of_week.html#pandas.PeriodIndex.day_of_week "pandas.PeriodIndex.day_of_week")

The day of the week with Monday=0, Sunday=6.

[`PeriodIndex.day_of_year`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.day_of_year.html#pandas.PeriodIndex.day_of_year "pandas.PeriodIndex.day_of_year")

The ordinal day of the year.

[`PeriodIndex.days_in_month`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.days_in_month.html#pandas.PeriodIndex.days_in_month "pandas.PeriodIndex.days_in_month")

The number of days in the month.

Examples

\>>> idx \= pd.PeriodIndex(\["2020-01-31", "2020-02-28"\], freq\="D")
\>>> idx.day
Index(\[31, 28\], dtype='int64')

Copy to clipboard

On this page