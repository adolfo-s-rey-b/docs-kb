[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.floor.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.TimedeltaIndex.floor[#](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.floor.html#pandas-timedeltaindex-floor "Link to this heading")

=================================================================================================================================================================

TimedeltaIndex.floor(_freq_, _ambiguous\='raise'_, _nonexistent\='raise'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/timedeltas.py#L281-L334)
[#](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.floor.html#pandas.TimedeltaIndex.floor "Link to this definition")

Perform floor operation on the data to the specified freq.

This method rounds each timedelta value in the Series/Index down to the specified frequency (i.e., towards negative infinity).

Parameters:

**freq**str or Offset

The frequency level to floor the index to. Must be a fixed frequency like ‘s’ (second) not ‘ME’ (month end). See [frequency aliases](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-offset-aliases)
 for a list of possible freq values.

**ambiguous**‘infer’, bool-ndarray, ‘NaT’, default ‘raise’

Accepted for compatibility with [`DatetimeIndex.floor()`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.floor.html#pandas.DatetimeIndex.floor "pandas.DatetimeIndex.floor")
; has no effect since TimedeltaIndex values are never tz-aware.

**nonexistent**‘shift\_forward’, ‘shift\_backward’, ‘NaT’, timedelta, default ‘raise’

Accepted for compatibility with [`DatetimeIndex.floor()`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.floor.html#pandas.DatetimeIndex.floor "pandas.DatetimeIndex.floor")
; has no effect since TimedeltaIndex values are never tz-aware.

Returns:

TimedeltaIndex

Values rounded down to the given freq.

Raises:

ValueError if the freq cannot be converted.

See also

[`TimedeltaIndex.round`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.round.html#pandas.TimedeltaIndex.round "pandas.TimedeltaIndex.round")

Perform round operation on the data to the specified freq.

[`TimedeltaIndex.ceil`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.ceil.html#pandas.TimedeltaIndex.ceil "pandas.TimedeltaIndex.ceil")

Perform ceil operation on the data to the specified freq.

Examples

\>>> tdelta\_idx \= pd.timedelta\_range("1 day", periods\=3, freq\="6h20min")
\>>> tdelta\_idx
TimedeltaIndex(\['1 days 00:00:00', '1 days 06:20:00', '1 days 12:40:00'\],
               dtype='timedelta64\[us\]', freq='380min')
\>>> tdelta\_idx.floor("h")
TimedeltaIndex(\['1 days 00:00:00', '1 days 06:00:00', '1 days 12:00:00'\],
               dtype='timedelta64\[us\]', freq=None)

Copy to clipboard

On this page