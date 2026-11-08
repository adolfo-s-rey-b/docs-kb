[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.memory_usage.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.memory_usage.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.memory_usage.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.memory_usage.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.memory_usage.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.memory_usage.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.memory_usage.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.memory_usage.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.memory_usage.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.memory_usage.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.memory_usage.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.memory_usage.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.memory_usage.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.memory_usage.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.memory\_usage[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.memory_usage.html#pandas-dataframe-memory-usage "Link to this heading")

========================================================================================================================================================================

DataFrame.memory\_usage(_index\=True_, _deep\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L3918-L4016)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.memory_usage.html#pandas.DataFrame.memory_usage "Link to this definition")

Return the memory usage of each column in bytes.

The memory usage can optionally include the contribution of the index and elements of object dtype.

This value is displayed in DataFrame.info by default. This can be suppressed by setting `pandas.options.display.memory_usage` to False.

Parameters:

**index**bool, default True

Specifies whether to include the memory usage of the DataFrame’s index in returned Series. If `index=True`, the memory usage of the index is the first item in the output.

**deep**bool, default False

If True, introspect the data deeply by interrogating object dtypes for system-level memory consumption, and include it in the returned values.

Returns:

Series

A Series whose index is the original column names and whose values is the memory usage of each column in bytes.

See also

[`numpy.ndarray.nbytes`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.nbytes.html#numpy.ndarray.nbytes "(in NumPy v2.5)")

Total bytes consumed by the elements of an ndarray.

[`Series.memory_usage`](https://pandas.pydata.org/docs/reference/api/pandas.Series.memory_usage.html#pandas.Series.memory_usage "pandas.Series.memory_usage")

Bytes consumed by a Series.

[`Categorical`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html#pandas.Categorical "pandas.Categorical")

Memory-efficient array for string values with many repeated values.

[`DataFrame.info`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html#pandas.DataFrame.info "pandas.DataFrame.info")

Concise summary of a DataFrame.

Notes

See the [Frequently Asked Questions](https://pandas.pydata.org/docs/user_guide/gotchas.html#df-memory-usage)
 for more details.

Examples

\>>> dtypes \= \["int64", "float64", "complex128", "object", "bool"\]
\>>> data \= dict(\[(t, np.ones(shape\=5000, dtype\=int).astype(t)) for t in dtypes\])
\>>> df \= pd.DataFrame(data)
\>>> df.head()
   int64  float64            complex128  object  bool
0      1      1.0              1.0+0.0j       1  True
1      1      1.0              1.0+0.0j       1  True
2      1      1.0              1.0+0.0j       1  True
3      1      1.0              1.0+0.0j       1  True
4      1      1.0              1.0+0.0j       1  True

Copy to clipboard

\>>> df.memory\_usage()
Index           132
int64         40000
float64       40000
complex128    80000
object        40000
bool           5000
dtype: int64

Copy to clipboard

\>>> df.memory\_usage(index\=False)
int64         40000
float64       40000
complex128    80000
object        40000
bool           5000
dtype: int64

Copy to clipboard

The memory footprint of object dtype columns is ignored by default:

\>>> df.memory\_usage(deep\=True)
Index            132
int64          40000
float64        40000
complex128     80000
object        180000
bool            5000
dtype: int64

Copy to clipboard

Use a Categorical for efficient storage of an object-dtype column with many repeated values.

\>>> df\["object"\].astype("category").memory\_usage(deep\=True)
5140

Copy to clipboard

On this page