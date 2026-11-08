[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.indexer_between_time.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DatetimeIndex.indexer_between_time.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.indexer_between_time.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DatetimeIndex.indexer_between_time.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DatetimeIndex.indexer_between_time.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DatetimeIndex.indexer_between_time.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DatetimeIndex.indexer_between_time.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DatetimeIndex.indexer_between_time.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DatetimeIndex.indexer_between_time.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DatetimeIndex.indexer_between_time.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DatetimeIndex.indexer_between_time.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DatetimeIndex.indexer_between_time.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DatetimeIndex.indexer_between_time.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DatetimeIndex.indexer_between_time.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.indexer\_between\_time[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.indexer_between_time.html#pandas-datetimeindex-indexer-between-time "Link to this heading")

=============================================================================================================================================================================================================

DatetimeIndex.indexer\_between\_time(_start\_time_, _end\_time_, _include\_start\=True_, _include\_end\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L2431-L2495)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.indexer_between_time.html#pandas.DatetimeIndex.indexer_between_time "Link to this definition")

Return index locations of values between particular times of day.

This method returns the integer indices of the DatetimeIndex entries whose time-of-day components fall within the specified range.

Parameters:

**start\_time, end\_time**datetime.time, str

Time passed either as object (datetime.time) or as string in appropriate format (“%H:%M”, “%H%M”, “%I:%M%p”, “%I%M%p”, “%H:%M:%S”, “%H%M%S”, “%I:%M:%S%p”,”%I%M%S%p”).

**include\_start**bool, default True

Include boundaries; whether to set start bound as closed or open.

**include\_end**bool, default True

Include boundaries; whether to set end bound as closed or open.

Returns:

np.ndarray\[np.intp\]

Index locations of values between particular times of day.

See also

[`indexer_at_time`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.indexer_at_time.html#pandas.DatetimeIndex.indexer_at_time "pandas.DatetimeIndex.indexer_at_time")

Get index locations of values at particular time of day.

[`DataFrame.between_time`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.between_time.html#pandas.DataFrame.between_time "pandas.DataFrame.between_time")

Select values between particular times of day.

Examples

\>>> idx \= pd.date\_range("2023-01-01", periods\=4, freq\="h")
\>>> idx
DatetimeIndex(\['2023-01-01 00:00:00', '2023-01-01 01:00:00',\
                   '2023-01-01 02:00:00', '2023-01-01 03:00:00'\],
                  dtype='datetime64\[us\]', freq='h')
\>>> idx.indexer\_between\_time("00:00", "2:00", include\_end\=False)
array(\[0, 1\])

Copy to clipboard

On this page