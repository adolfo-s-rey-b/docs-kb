[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.to_numpy.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.to_numpy.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.to_numpy.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.to_numpy.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.to_numpy.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.to_numpy.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.to_numpy.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.to_numpy.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.to_numpy.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.to_numpy.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.to_numpy.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.to_numpy.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.to\_numpy[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#pandas-series-to-numpy "Link to this heading")

===================================================================================================================================================

Series.to\_numpy(_dtype\=None_, _copy\=False_, _na\_value\=<no\_default>_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/base.py#L601-L752)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy "Link to this definition")

A NumPy ndarray representing the values in this Series or Index.

This method converts the underlying data to a NumPy array, optionally specifying the desired dtype and handling of missing values. For extension types, this may require copying data and coercing to a NumPy type.

Parameters:

**dtype**str or numpy.dtype, optional

The dtype to pass to `numpy.asarray()`.

**copy**bool, default False

Whether to ensure that the returned value is not a view on another array. Note that `copy=False` does not _ensure_ that `to_numpy()` is no-copy. Rather, `copy=True` ensure that a copy is made, even if not strictly necessary.

**na\_value**Any, optional

The value to use for missing values. The default value depends on dtype and the type of the array.

**\*\*kwargs**

Additional keywords passed through to the `to_numpy` method of the underlying array (for extension arrays).

Returns:

numpy.ndarray

The NumPy ndarray holding the values from this Series or Index. The dtype of the array may differ. See Notes.

See also

[`Series.array`](https://pandas.pydata.org/docs/reference/api/pandas.Series.array.html#pandas.Series.array "pandas.Series.array")

Get the actual data stored within.

[`Index.array`](https://pandas.pydata.org/docs/reference/api/pandas.Index.array.html#pandas.Index.array "pandas.Index.array")

Get the actual data stored within.

[`DataFrame.to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy "pandas.DataFrame.to_numpy")

Similar method for DataFrame.

Notes

The returned array will be the same up to equality (values equal in self will be equal in the returned array; likewise for values that are not equal). When self contains an ExtensionArray, the dtype may be different. For example, for a category-dtype Series, `to_numpy()` will return a NumPy array and the categorical dtype will be lost.

For NumPy dtypes, this will be a reference to the actual data stored in this Series or Index (assuming `copy=False`). Modifying the result in place will modify the data stored in the Series or Index (not that we recommend doing that).

For extension types, `to_numpy()` _may_ require copying data and coercing the result to a NumPy type (possibly object), which may be expensive. When you need a no-copy reference to the underlying data, [`Series.array`](https://pandas.pydata.org/docs/reference/api/pandas.Series.array.html#pandas.Series.array "pandas.Series.array")
 should be used instead.

This table lays out the different dtypes and default return types of `to_numpy()` for various dtypes within pandas.

| dtype | array type |
| --- | --- |
| category\[T\] | ndarray\[T\] (same dtype as input) |
| period | ndarray\[object\] (Periods) |
| interval | ndarray\[object\] (Intervals) |
| IntegerNA | ndarray\[object\] |
| datetime64\[ns\] | datetime64\[ns\] |
| datetime64\[ns, tz\] | ndarray\[object\] (Timestamps) |

For timezone-aware datetime data, calling `to_numpy()` without specifying `dtype` produces an object-dtype array of [`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")
 objects. This is significantly slower and uses more memory than a native `datetime64` array. To avoid this, pass an explicit `dtype`:

*   `dtype="datetime64[ns]"` converts to UTC and drops the timezone, returning a native `datetime64[ns]` array.
    
*   `dtype=object` explicitly requests Timestamp objects when you need to preserve per-element timezone information.
    

Examples

\>>> ser \= pd.Series(pd.Categorical(\["a", "b", "a"\]))
\>>> ser.to\_numpy()
array(\['a', 'b', 'a'\], dtype=object)

Copy to clipboard

Specify the dtype to control how datetime-aware data is represented. Use `dtype=object` to return an ndarray of pandas [`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")
 objects, each with the correct `tz`.

\>>> ser \= pd.Series(pd.date\_range("2000", periods\=2, tz\="CET"))
\>>> ser.to\_numpy(dtype\=object)
array(\[Timestamp('2000-01-01 00:00:00+0100', tz='CET'),\
       Timestamp('2000-01-02 00:00:00+0100', tz='CET')\],
      dtype=object)

Copy to clipboard

Or `dtype='datetime64[ns]'` to return an ndarray of native datetime64 values. The values are converted to UTC and the timezone info is dropped.

\>>> ser.to\_numpy(dtype\="datetime64\[ns\]")
...
array(\['1999-12-31T23:00:00.000000000', '2000-01-01T23:00:00...'\],
      dtype='datetime64\[ns\]')

Copy to clipboard

On this page