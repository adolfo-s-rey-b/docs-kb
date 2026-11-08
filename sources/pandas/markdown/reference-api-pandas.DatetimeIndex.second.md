[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.second.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.second[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.second.html#pandas-datetimeindex-second "Link to this heading")

=================================================================================================================================================================

property DatetimeIndex.second[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L447-L467)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.second.html#pandas.DatetimeIndex.second "Link to this definition")

The seconds of the datetime.

This attribute returns the second component of each datetime value in the DatetimeIndex.

See also

[`DatetimeIndex.minute`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.minute.html#pandas.DatetimeIndex.minute "pandas.DatetimeIndex.minute")

The minutes of the datetime.

[`DatetimeIndex.microsecond`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.microsecond.html#pandas.DatetimeIndex.microsecond "pandas.DatetimeIndex.microsecond")

The microseconds of the datetime.

[`DatetimeIndex.nanosecond`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.nanosecond.html#pandas.DatetimeIndex.nanosecond "pandas.DatetimeIndex.nanosecond")

The nanoseconds of the datetime.

Examples

\>>> idx \= pd.date\_range("2000-01-01", periods\=3, freq\="s")
\>>> idx.second
Index(\[0, 1, 2\], dtype='int32')

Copy to clipboard

On this page