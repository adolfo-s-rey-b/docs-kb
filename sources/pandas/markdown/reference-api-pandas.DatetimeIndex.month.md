[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.month.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.month[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.month.html#pandas-datetimeindex-month "Link to this heading")

==============================================================================================================================================================

property DatetimeIndex.month[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L361-L380)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.month.html#pandas.DatetimeIndex.month "Link to this definition")

The month as January=1, December=12.

This attribute returns the month component of each datetime value in the DatetimeIndex.

See also

[`DatetimeIndex.year`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.year.html#pandas.DatetimeIndex.year "pandas.DatetimeIndex.year")

The year of the datetime.

[`DatetimeIndex.day`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day.html#pandas.DatetimeIndex.day "pandas.DatetimeIndex.day")

The day of the datetime.

Examples

\>>> idx \= pd.DatetimeIndex(\["2000-01-31", "2000-02-29", "2000-03-31"\])
\>>> idx.month
Index(\[1, 2, 3\], dtype='int32')

Copy to clipboard

On this page