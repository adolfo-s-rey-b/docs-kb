[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.arrays.DatetimeArray.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.arrays.DatetimeArray[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.DatetimeArray.html#pandas-arrays-datetimearray "Link to this heading")

=================================================================================================================================================================

class pandas.arrays.DatetimeArray(_data_, _dtype\=None_, _freq\=None_, _copy\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/datetimes.py#L165-L2604)
[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.DatetimeArray.html#pandas.arrays.DatetimeArray "Link to this definition")

Pandas ExtensionArray for tz-naive or tz-aware datetime data.

Warning

DatetimeArray is currently experimental, and its API may change without warning. In particular, `DatetimeArray.dtype` is expected to change to always be an instance of an `ExtensionDtype` subclass.

Parameters:

**data**Series, Index, DatetimeArray, ndarray

The datetime data.

For DatetimeArray values (or a Series or Index boxing one), dtype and freq will be extracted from values.

**dtype**numpy.dtype or DatetimeTZDtype

Note that the only NumPy dtypes allowed are ‘datetime64\[ns\]’, ‘datetime64\[us\]’, ‘datetime64\[ms\]’, ‘datetime64\[s\]’.

**freq**str or Offset, optional

The frequency.

**copy**bool, default False

Whether to copy the underlying array of values.

See also

`DatetimeIndex`

Immutable Index for datetime-like data.

`Series`

One-dimensional labeled array capable of holding datetime-like data.

`Timestamp`

Pandas replacement for python datetime.datetime object.

`to_datetime`

Convert argument to datetime.

`period_range`

Return a fixed frequency PeriodIndex.

Examples

\>>> pd.arrays.DatetimeArray.\_from\_sequence(
...     pd.DatetimeIndex(\["2023-01-01", "2023-01-02"\], freq\="D")
... )
<DatetimeArray>
\['2023-01-01 00:00:00', '2023-01-02 00:00:00'\]
Length: 2, dtype: datetime64\[us\]

Copy to clipboard

On this page