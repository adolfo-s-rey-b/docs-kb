[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.arrays.TimedeltaArray.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.arrays.TimedeltaArray.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.arrays.TimedeltaArray.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.arrays.TimedeltaArray.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.arrays.TimedeltaArray.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.arrays.TimedeltaArray.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.arrays.TimedeltaArray.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.arrays.TimedeltaArray.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.arrays.TimedeltaArray.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.arrays.TimedeltaArray.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.arrays.TimedeltaArray.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.arrays.TimedeltaArray.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.arrays.TimedeltaArray.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.arrays.TimedeltaArray.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.arrays.TimedeltaArray[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.TimedeltaArray.html#pandas-arrays-timedeltaarray "Link to this heading")

====================================================================================================================================================================

class pandas.arrays.TimedeltaArray(_data_, _dtype\=None_, _freq\=None_, _copy\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/timedeltas.py#L136-L1211)
[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.TimedeltaArray.html#pandas.arrays.TimedeltaArray "Link to this definition")

Pandas ExtensionArray for timedelta data.

Warning

TimedeltaArray is currently experimental, and its API may change without warning. In particular, `TimedeltaArray.dtype` is expected to change to be an instance of an `ExtensionDtype` subclass.

Parameters:

**data**array-like

The timedelta data.

**dtype**numpy.dtype

Valid `numpy` dtypes are `timedelta64[ns]`, `timedelta64[us]`, `timedelta64[ms]`, and `timedelta64[s]`.

**freq**Offset, optional

Frequency of the data.

**copy**bool, default False

Whether to copy the underlying array of data.

See also

`Timedelta`

Represents a duration, the difference between two dates or times.

`TimedeltaIndex`

Immutable Index of timedelta64 data.

`to_timedelta`

Convert argument to timedelta.

Examples

\>>> pd.arrays.TimedeltaArray.\_from\_sequence(pd.TimedeltaIndex(\["1h", "2h"\]))
<TimedeltaArray>
\['0 days 01:00:00', '0 days 02:00:00'\]
Length: 2, dtype: timedelta64\[us\]

Copy to clipboard

On this page