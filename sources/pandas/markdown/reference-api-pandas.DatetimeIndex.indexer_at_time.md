[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.indexer_at_time.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.indexer\_at\_time[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.indexer_at_time.html#pandas-datetimeindex-indexer-at-time "Link to this heading")

==============================================================================================================================================================================================

DatetimeIndex.indexer\_at\_time(_time_, _asof\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L2349-L2429)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.indexer_at_time.html#pandas.DatetimeIndex.indexer_at_time "Link to this definition")

Return index locations of values at particular time of day.

This method returns the integer indices of the DatetimeIndex entries that match the specified time of day, regardless of the date.

Parameters:

**time**datetime.time or str

Time passed in either as object (datetime.time) or as string in appropriate format (“%H:%M”, “%H%M”, “%I:%M%p”, “%I%M%p”, “%H:%M:%S”, “%H%M%S”, “%I:%M:%S%p”, “%I%M%S%p”).

**asof**bool, default False

This parameter is currently not supported.

Returns:

np.ndarray\[np.intp\]

Index locations of values at given time of day.

See also

[`indexer_between_time`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.indexer_between_time.html#pandas.DatetimeIndex.indexer_between_time "pandas.DatetimeIndex.indexer_between_time")

Get index locations of values between particular times of day.

[`DataFrame.at_time`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.at_time.html#pandas.DataFrame.at_time "pandas.DataFrame.at_time")

Select values at particular time of day.

Examples

\>>> idx \= pd.DatetimeIndex(
...     \["1/1/2020 10:00", "2/1/2020 11:00", "3/1/2020 10:00"\]
... )
\>>> idx.indexer\_at\_time("10:00")
array(\[0, 2\])

Copy to clipboard

On this page