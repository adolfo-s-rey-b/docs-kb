[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.__array__.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.__array__.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.__array__.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.__array__.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.__array__.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.__array__.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.__array__.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.__array__.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.__array__.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.__array__.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.__array__.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.__array__.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.__array__.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.__array__.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.\_\_array\_\_[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.__array__.html#pandas-series-array "Link to this heading")

=====================================================================================================================================================

Series.\_\_array\_\_(_dtype\=None_, _copy\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L984-L1048)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.__array__.html#pandas.Series.__array__ "Link to this definition")

Return the values as a NumPy array.

Users should not call this directly. Rather, it is invoked by [`numpy.array()`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "(in NumPy v2.5)")
 and [`numpy.asarray()`](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "(in NumPy v2.5)")
.

Parameters:

**dtype**str or numpy.dtype, optional

The dtype to use for the resulting NumPy array. By default, the dtype is inferred from the data.

**copy**bool or None, optional

See [`numpy.asarray()`](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "(in NumPy v2.5)")
.

Returns:

numpy.ndarray

The values in the series converted to a [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
 with the specified dtype.

See also

[`array`](https://pandas.pydata.org/docs/reference/api/pandas.array.html#pandas.array "pandas.array")

Create a new array from data.

[`Series.array`](https://pandas.pydata.org/docs/reference/api/pandas.Series.array.html#pandas.Series.array "pandas.Series.array")

Zero-copy view to the array backing the Series.

[`Series.to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy "pandas.Series.to_numpy")

Series method for similar behavior.

Examples

\>>> ser \= pd.Series(\[1, 2, 3\])
\>>> np.asarray(ser)
array(\[1, 2, 3\])

Copy to clipboard

For timezone-aware data, the timezones may be retained with `dtype='object'`

\>>> tzser \= pd.Series(pd.date\_range("2000", periods\=2, tz\="CET"))
\>>> np.asarray(tzser, dtype\="object")
array(\[Timestamp('2000-01-01 00:00:00+0100', tz='CET'),\
       Timestamp('2000-01-02 00:00:00+0100', tz='CET')\],
      dtype=object)

Copy to clipboard

Or the values may be localized to UTC and the tzinfo discarded with `dtype='datetime64[ns]'`

\>>> np.asarray(tzser, dtype\="datetime64\[ns\]")
array(\['1999-12-31T23:00:00.000000000', ...\],
      dtype='datetime64\[ns\]')

Copy to clipboard

On this page