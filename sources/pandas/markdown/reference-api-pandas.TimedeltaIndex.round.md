[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.round.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.TimedeltaIndex.round.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.round.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.TimedeltaIndex.round.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.TimedeltaIndex.round.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.TimedeltaIndex.round.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.TimedeltaIndex.round.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.TimedeltaIndex.round.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.TimedeltaIndex.round.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.TimedeltaIndex.round.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.TimedeltaIndex.round.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.TimedeltaIndex.round.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.TimedeltaIndex.round.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.TimedeltaIndex.round.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.TimedeltaIndex.round[#](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.round.html#pandas-timedeltaindex-round "Link to this heading")

=================================================================================================================================================================

TimedeltaIndex.round(_freq_, _ambiguous\='raise'_, _nonexistent\='raise'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/timedeltas.py#L225-L279)
[#](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.round.html#pandas.TimedeltaIndex.round "Link to this definition")

Perform round operation on the data to the specified freq.

This method rounds each timedelta value in the Series/Index to the nearest specified frequency using standard rounding rules (round half to even).

Parameters:

**freq**str or Offset

The frequency level to round the index to. Must be a fixed frequency like ‘s’ (second) not ‘ME’ (month end). See [frequency aliases](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-offset-aliases)
 for a list of possible freq values.

**ambiguous**‘infer’, bool-ndarray, ‘NaT’, default ‘raise’

Accepted for compatibility with [`DatetimeIndex.round()`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.round.html#pandas.DatetimeIndex.round "pandas.DatetimeIndex.round")
; has no effect since TimedeltaIndex values are never tz-aware.

**nonexistent**‘shift\_forward’, ‘shift\_backward’, ‘NaT’, timedelta, default ‘raise’

Accepted for compatibility with [`DatetimeIndex.round()`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.round.html#pandas.DatetimeIndex.round "pandas.DatetimeIndex.round")
; has no effect since TimedeltaIndex values are never tz-aware.

Returns:

TimedeltaIndex

Values rounded to the given freq.

Raises:

ValueError if the freq cannot be converted.

See also

[`TimedeltaIndex.floor`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.floor.html#pandas.TimedeltaIndex.floor "pandas.TimedeltaIndex.floor")

Perform floor operation on the data to the specified freq.

[`TimedeltaIndex.ceil`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.ceil.html#pandas.TimedeltaIndex.ceil "pandas.TimedeltaIndex.ceil")

Perform ceil operation on the data to the specified freq.

Examples

\>>> tdelta\_idx \= pd.timedelta\_range("1 day", periods\=3, freq\="6h20min")
\>>> tdelta\_idx
TimedeltaIndex(\['1 days 00:00:00', '1 days 06:20:00', '1 days 12:40:00'\],
               dtype='timedelta64\[us\]', freq='380min')
\>>> tdelta\_idx.round("h")
TimedeltaIndex(\['1 days 00:00:00', '1 days 06:00:00', '1 days 13:00:00'\],
               dtype='timedelta64\[us\]', freq=None)

Copy to clipboard

On this page