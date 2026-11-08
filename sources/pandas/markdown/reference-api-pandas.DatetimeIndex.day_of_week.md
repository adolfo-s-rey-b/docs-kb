[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day_of_week.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.day\_of\_week[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day_of_week.html#pandas-datetimeindex-day-of-week "Link to this heading")

==================================================================================================================================================================================

property DatetimeIndex.day\_of\_week[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L502-L522)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day_of_week.html#pandas.DatetimeIndex.day_of_week "Link to this definition")

The day of the week with Monday=0, Sunday=6.

Return the day of the week. It is assumed the week starts on Monday, which is denoted by 0 and ends on Sunday which is denoted by 6.

See also

[`DatetimeIndex.day_of_year`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day_of_year.html#pandas.DatetimeIndex.day_of_year "pandas.DatetimeIndex.day_of_year")

The ordinal day of the year.

[`DatetimeIndex.day_name`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day_name.html#pandas.DatetimeIndex.day_name "pandas.DatetimeIndex.day_name")

Return the name of the day of the week.

Examples

\>>> idx \= pd.DatetimeIndex(\["2016-12-31", "2017-01-01", "2017-01-02"\])
\>>> idx.day\_of\_week
Index(\[5, 6, 0\], dtype='int32')

Copy to clipboard

On this page