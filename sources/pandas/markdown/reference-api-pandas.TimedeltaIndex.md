[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.TimedeltaIndex.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.TimedeltaIndex.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.TimedeltaIndex.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.TimedeltaIndex.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.TimedeltaIndex.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.TimedeltaIndex.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.TimedeltaIndex.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.TimedeltaIndex.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.TimedeltaIndex.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.TimedeltaIndex.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.TimedeltaIndex.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.TimedeltaIndex.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.TimedeltaIndex[#](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.html#pandas-timedeltaindex "Link to this heading")

===============================================================================================================================================

class pandas.TimedeltaIndex(_data\=None_, _freq\=<no\_default>_, _dtype\=None_, _copy\=None_, _name\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/timedeltas.py#L94-L933)
[#](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.html#pandas.TimedeltaIndex "Link to this definition")

Immutable Index of timedelta64 data.

Represented internally as int64, and scalars returned Timedelta objects.

Parameters:

**data**array-like (1-dimensional), optional

Optional timedelta-like data to construct index with.

**freq**str or pandas offset object, optional

One of pandas date offset strings or corresponding objects. The string `'infer'` can be passed in order to set the frequency of the index as the inferred frequency upon creation.

**dtype**numpy.dtype or str, default None

Valid `numpy` dtypes are `timedelta64[ns]`, `timedelta64[us]`, `timedelta64[ms]`, and `timedelta64[s]`.

**copy**bool, default None

Whether to copy input data, only relevant for array, Series, and Index inputs (for other input, e.g. a list, a new array is created anyway). Defaults to True for array input and False for Index/Series. Set to False to avoid copying array input at your own risk (if you know the input data won’t be modified elsewhere). Set to True to force copying Series/Index input up front.

**name**object

Name to be stored in the index.

Attributes

|     |     |
| --- | --- |
| [`days`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.days.html#pandas.TimedeltaIndex.days "pandas.TimedeltaIndex.days") | Number of days for each element. |
| [`seconds`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.seconds.html#pandas.TimedeltaIndex.seconds "pandas.TimedeltaIndex.seconds") | Number of seconds (>= 0 and less than 1 day) for each element. |
| [`microseconds`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.microseconds.html#pandas.TimedeltaIndex.microseconds "pandas.TimedeltaIndex.microseconds") | Number of microseconds (>= 0 and less than 1 second) for each element. |
| [`nanoseconds`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.nanoseconds.html#pandas.TimedeltaIndex.nanoseconds "pandas.TimedeltaIndex.nanoseconds") | Number of nanoseconds (>= 0 and less than 1 microsecond) for each element. |
| [`components`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.components.html#pandas.TimedeltaIndex.components "pandas.TimedeltaIndex.components") | Return a DataFrame of the individual resolution components of the Timedeltas. |
| [`inferred_freq`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.inferred_freq.html#pandas.TimedeltaIndex.inferred_freq "pandas.TimedeltaIndex.inferred_freq") | (DEPRECATED) Return the inferred frequency of the index. |

Methods

|     |     |
| --- | --- |
| [`to_pytimedelta`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.to_pytimedelta.html#pandas.TimedeltaIndex.to_pytimedelta "pandas.TimedeltaIndex.to_pytimedelta")<br>() | Return an ndarray of datetime.timedelta objects. |
| [`to_series`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.to_series.html#pandas.TimedeltaIndex.to_series "pandas.TimedeltaIndex.to_series")<br>(\[index, name\]) | Create a Series with both index and values equal to the index keys. |
| [`round`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.round.html#pandas.TimedeltaIndex.round "pandas.TimedeltaIndex.round")<br>(freq\[, ambiguous, nonexistent\]) | Perform round operation on the data to the specified freq. |
| [`floor`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.floor.html#pandas.TimedeltaIndex.floor "pandas.TimedeltaIndex.floor")<br>(freq\[, ambiguous, nonexistent\]) | Perform floor operation on the data to the specified freq. |
| [`ceil`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.ceil.html#pandas.TimedeltaIndex.ceil "pandas.TimedeltaIndex.ceil")<br>(freq\[, ambiguous, nonexistent\]) | Perform ceil operation on the data to the specified freq. |
| [`to_frame`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.to_frame.html#pandas.TimedeltaIndex.to_frame "pandas.TimedeltaIndex.to_frame")<br>(\[index, name\]) | Create a DataFrame with a column containing the Index. |
| [`mean`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.mean.html#pandas.TimedeltaIndex.mean "pandas.TimedeltaIndex.mean")<br>(\*\[, skipna, axis\]) | Return the mean value of the Array. |

See also

[`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")

The base pandas Index type.

[`Timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html#pandas.Timedelta "pandas.Timedelta")

Represents a duration between two dates or times.

[`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")

Index of datetime64 data.

[`PeriodIndex`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.html#pandas.PeriodIndex "pandas.PeriodIndex")

Index of Period data.

[`timedelta_range`](https://pandas.pydata.org/docs/reference/api/pandas.timedelta_range.html#pandas.timedelta_range "pandas.timedelta_range")

Create a fixed-frequency TimedeltaIndex.

Notes

To learn more about the frequency strings, please see [this link](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-offset-aliases)
.

Examples

\>>> pd.TimedeltaIndex(\["0 days", "1 days", "2 days", "3 days", "4 days"\])
TimedeltaIndex(\['0 days', '1 days', '2 days', '3 days', '4 days'\],
               dtype='timedelta64\[us\]', freq=None)

Copy to clipboard

We can also let pandas infer the frequency when possible.

\>>> pd.TimedeltaIndex(np.arange(5) \* 24 \* 3600 \* 1e9, freq\="infer")
TimedeltaIndex(\['0 days', '1 days', '2 days', '3 days', '4 days'\],
               dtype='timedelta64\[ns\]', freq='D')

Copy to clipboard

On this page