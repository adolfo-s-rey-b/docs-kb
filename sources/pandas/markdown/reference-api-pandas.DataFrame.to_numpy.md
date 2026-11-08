[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.to_numpy.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.to_numpy.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.to_numpy.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.to_numpy.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.to_numpy.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.to_numpy.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.to_numpy.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.to_numpy.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.to_numpy.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.to_numpy.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.to_numpy.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.to_numpy.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.to\_numpy[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html#pandas-dataframe-to-numpy "Link to this heading")

============================================================================================================================================================

DataFrame.to\_numpy(_dtype\=None_, _copy\=False_, _na\_value\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L1840-L1905)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy "Link to this definition")

Convert the DataFrame to a NumPy array.

By default, the dtype of the returned array will be the common NumPy dtype of all types in the DataFrame. For example, if the dtypes are `float16` and `float32`, the results dtype will be `float32`. This may require copying data and coercing values, which may be expensive.

Parameters:

**dtype**str or numpy.dtype, optional

The dtype to pass to `numpy.asarray()`.

**copy**bool, default False

Whether to ensure that the returned value is not a view on another array. Note that `copy=False` does not _ensure_ that `to_numpy()` is no-copy. Rather, `copy=True` ensure that a copy is made, even if not strictly necessary.

**na\_value**Any, optional

The value to use for missing values. The default value depends on dtype and the dtypes of the DataFrame columns.

Returns:

numpy.ndarray

The NumPy array representing the values in the DataFrame.

See also

[`Series.to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy "pandas.Series.to_numpy")

Similar method for Series.

Examples

\>>> pd.DataFrame({"A": \[1, 2\], "B": \[3, 4\]}).to\_numpy()
array(\[\[1, 3\],\
       \[2, 4\]\])

Copy to clipboard

With heterogeneous data, the lowest common type will have to be used.

\>>> df \= pd.DataFrame({"A": \[1, 2\], "B": \[3.0, 4.5\]})
\>>> df.to\_numpy()
array(\[\[1. , 3. \],\
       \[2. , 4.5\]\])

Copy to clipboard

For a mix of numeric and non-numeric types, the output array will have object dtype.

\>>> df\["C"\] \= pd.date\_range("2000", periods\=2)
\>>> df.to\_numpy()
array(\[\[1, 3.0, Timestamp('2000-01-01 00:00:00')\],\
       \[2, 4.5, Timestamp('2000-01-02 00:00:00')\]\], dtype=object)

Copy to clipboard

On this page