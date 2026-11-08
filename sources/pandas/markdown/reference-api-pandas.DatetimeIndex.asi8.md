[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.asi8.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DatetimeIndex.asi8.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.asi8.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DatetimeIndex.asi8.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DatetimeIndex.asi8.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DatetimeIndex.asi8.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DatetimeIndex.asi8.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DatetimeIndex.asi8.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DatetimeIndex.asi8.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DatetimeIndex.asi8.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DatetimeIndex.asi8.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DatetimeIndex.asi8.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DatetimeIndex.asi8.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DatetimeIndex.asi8.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.asi8[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.asi8.html#pandas-datetimeindex-asi8 "Link to this heading")

===========================================================================================================================================================

property DatetimeIndex.asi8[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimelike.py#L199-L240)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.asi8.html#pandas.DatetimeIndex.asi8 "Link to this definition")

Return Integer representation of the values.

For [`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")
 and [`TimedeltaIndex`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.html#pandas.TimedeltaIndex "pandas.TimedeltaIndex")
, the values are the number of time units (determined by the index resolution) since the epoch. For [`PeriodIndex`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.html#pandas.PeriodIndex "pandas.PeriodIndex")
, the values are ordinals.

Returns:

numpy.ndarray

An ndarray with int64 dtype.

See also

[`Index.values`](https://pandas.pydata.org/docs/reference/api/pandas.Index.values.html#pandas.Index.values "pandas.Index.values")

Return an array representing the data in the Index, using native types (datetime64, timedelta64) rather than int64.

[`Index.to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.Index.to_numpy.html#pandas.Index.to_numpy "pandas.Index.to_numpy")

Return a NumPy ndarray of the index values.

Examples

For [`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")
 with default microsecond resolution:

\>>> idx \= pd.DatetimeIndex(\["2023-01-01", "2023-01-02"\], dtype\="datetime64\[us\]")
\>>> idx.asi8
array(\[1672531200000000, 1672617600000000\])

Copy to clipboard

For [`TimedeltaIndex`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.html#pandas.TimedeltaIndex "pandas.TimedeltaIndex")
 with millisecond resolution:

\>>> idx \= pd.TimedeltaIndex(\["1 day", "2 days"\], dtype\="timedelta64\[ms\]")
\>>> idx.asi8
array(\[ 86400000, 172800000\])

Copy to clipboard

For [`PeriodIndex`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.html#pandas.PeriodIndex "pandas.PeriodIndex")
:

\>>> idx \= pd.PeriodIndex(\["2023-01", "2023-02", "2023-03"\], freq\="M")
\>>> idx.asi8
array(\[636, 637, 638\])

Copy to clipboard

On this page