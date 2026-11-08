[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.year.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.year[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.year.html#pandas-datetimeindex-year "Link to this heading")

===========================================================================================================================================================

property DatetimeIndex.year[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L340-L359)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.year.html#pandas.DatetimeIndex.year "Link to this definition")

The year of the datetime.

This attribute returns the year component of each datetime value in the DatetimeIndex.

See also

[`DatetimeIndex.month`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.month.html#pandas.DatetimeIndex.month "pandas.DatetimeIndex.month")

The month as January=1, December=12.

[`DatetimeIndex.day`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day.html#pandas.DatetimeIndex.day "pandas.DatetimeIndex.day")

The day of the datetime.

Examples

\>>> idx \= pd.DatetimeIndex(\["2000-12-31", "2001-12-31", "2002-12-31"\])
\>>> idx.year
Index(\[2000, 2001, 2002\], dtype='int32')

Copy to clipboard

On this page