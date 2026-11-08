[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.snap.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.snap[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.snap.html#pandas-datetimeindex-snap "Link to this heading")

===========================================================================================================================================================

DatetimeIndex.snap(_freq\='S'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L2064-L2119)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.snap.html#pandas.DatetimeIndex.snap "Link to this definition")

Snap time stamps to nearest occurring frequency.

Each timestamp in the index is adjusted to the nearest occurrence of the specified frequency, snapping backward or forward as appropriate.

Parameters:

**freq**str, Timedelta, datetime.timedelta, or DateOffset, default ‘S’

Frequency strings can have multiples, e.g. ‘5h’. See [here](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-offset-aliases)
 for a list of frequency aliases.

Returns:

DatetimeIndex

Time stamps to nearest occurring freq.

See also

[`DatetimeIndex.round`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.round.html#pandas.DatetimeIndex.round "pandas.DatetimeIndex.round")

Perform round operation on the data to the specified freq.

[`DatetimeIndex.floor`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.floor.html#pandas.DatetimeIndex.floor "pandas.DatetimeIndex.floor")

Perform floor operation on the data to the specified freq.

Examples

\>>> idx \= pd.DatetimeIndex(
...     \["2023-01-01", "2023-01-02", "2023-02-01", "2023-02-02"\],
...     dtype\="M8\[ns\]",
... )
\>>> idx
DatetimeIndex(\['2023-01-01', '2023-01-02', '2023-02-01', '2023-02-02'\],
dtype='datetime64\[ns\]', freq=None)
\>>> idx.snap("MS")
DatetimeIndex(\['2023-01-01', '2023-01-01', '2023-02-01', '2023-02-01'\],
dtype='datetime64\[ns\]', freq=None)

Copy to clipboard

On this page