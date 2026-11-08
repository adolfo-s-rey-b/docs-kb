[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.round.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DatetimeIndex.round.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.round.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DatetimeIndex.round.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DatetimeIndex.round.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DatetimeIndex.round.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DatetimeIndex.round.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DatetimeIndex.round.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DatetimeIndex.round.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DatetimeIndex.round.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DatetimeIndex.round.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DatetimeIndex.round.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DatetimeIndex.round.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DatetimeIndex.round.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.round[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.round.html#pandas-datetimeindex-round "Link to this heading")

==============================================================================================================================================================

DatetimeIndex.round(_freq_, _ambiguous\='raise'_, _nonexistent\='raise'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L1159-L1250)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.round.html#pandas.DatetimeIndex.round "Link to this definition")

Perform round operation on the data to the specified freq.

This method rounds each datetime value in the Series/Index to the nearest specified frequency using standard rounding rules (round half to even).

Parameters:

**freq**str or Offset

The frequency level to round the index to. Must be a fixed frequency like ‘s’ (second) not ‘ME’ (month end). See [frequency aliases](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-offset-aliases)
 for a list of possible freq values.

**ambiguous**‘infer’, bool-ndarray, ‘NaT’, default ‘raise’

*   ‘infer’ will attempt to infer fall dst-transition hours based on order. Requires that the timestamps are monotonically increasing.
    
*   bool-ndarray where True signifies a DST time, False designates a non-DST time (note that this flag is only applicable for ambiguous times)
    
*   ‘NaT’ will return NaT where there are ambiguous times
    
*   ‘raise’ will raise a ValueError if there are ambiguous times.
    

**nonexistent**‘shift\_forward’, ‘shift\_backward’, ‘NaT’, timedelta, default ‘raise’

A nonexistent time does not exist in a particular timezone where clocks moved forward due to DST.

*   ‘shift\_forward’ will shift the nonexistent time forward to the closest existing time
    
*   ‘shift\_backward’ will shift the nonexistent time backward to the closest existing time
    
*   ‘NaT’ will return NaT where there are nonexistent times
    
*   timedelta objects will shift nonexistent times by the timedelta
    
*   ‘raise’ will raise a ValueError if there are nonexistent times.
    

Returns:

DatetimeIndex

Index with each value rounded to the specified freq.

Raises:

ValueError if the freq cannot be converted.

See also

[`DatetimeIndex.floor`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.floor.html#pandas.DatetimeIndex.floor "pandas.DatetimeIndex.floor")

Perform floor operation on the data to the specified freq.

[`DatetimeIndex.ceil`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.ceil.html#pandas.DatetimeIndex.ceil "pandas.DatetimeIndex.ceil")

Perform ceil operation on the data to the specified freq.

[`DatetimeIndex.snap`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.snap.html#pandas.DatetimeIndex.snap "pandas.DatetimeIndex.snap")

Snap time stamps to nearest occurring frequency.

Notes

If the timestamps have a timezone, rounding will take place relative to the local (“wall”) time and re-localized to the same timezone. When rounding near daylight savings time, use `nonexistent` and `ambiguous` to control the re-localization behavior.

Examples

\>>> rng \= pd.date\_range("1/1/2018 11:59:00", periods\=3, freq\="min")
\>>> rng
DatetimeIndex(\['2018-01-01 11:59:00', '2018-01-01 12:00:00',\
               '2018-01-01 12:01:00'\],
              dtype='datetime64\[us\]', freq='min')
\>>> rng.round("h")
DatetimeIndex(\['2018-01-01 12:00:00', '2018-01-01 12:00:00',\
               '2018-01-01 12:00:00'\],
              dtype='datetime64\[us\]', freq=None)

Copy to clipboard

When rounding near a daylight savings time transition, use `ambiguous` or `nonexistent` to control how the timestamp should be re-localized.

\>>> rng\_tz \= pd.DatetimeIndex(\["2021-10-31 01:30:00"\], tz\="Europe/Amsterdam")
\>>> rng\_tz.round("2h", ambiguous\=False)
DatetimeIndex(\['2021-10-31 02:00:00+01:00'\],
              dtype='datetime64\[us, Europe/Amsterdam\]', freq=None)
\>>> rng\_tz.round("2h", ambiguous\=True)
DatetimeIndex(\['2021-10-31 02:00:00+02:00'\],
              dtype='datetime64\[us, Europe/Amsterdam\]', freq=None)

Copy to clipboard

On this page