[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.memory_usage.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.memory_usage.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.memory_usage.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.memory_usage.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.memory_usage.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.memory_usage.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.memory_usage.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.memory_usage.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.memory_usage.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.memory_usage.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.memory_usage.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.memory_usage.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.memory_usage.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.memory_usage.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.memory\_usage[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.memory_usage.html#pandas-series-memory-usage "Link to this heading")

===============================================================================================================================================================

Series.memory\_usage(_index\=True_, _deep\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L6482-L6536)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.memory_usage.html#pandas.Series.memory_usage "Link to this definition")

Return the memory usage of the Series.

The memory usage can optionally include the contribution of the index and of elements of object dtype.

Parameters:

**index**bool, default True

Specifies whether to include the memory usage of the Series index.

**deep**bool, default False

If True, introspect the data deeply by interrogating object dtypes for system-level memory consumption, and include it in the returned value.

Returns:

int

Bytes of memory consumed.

See also

[`numpy.ndarray.nbytes`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.nbytes.html#numpy.ndarray.nbytes "(in NumPy v2.5)")

Total bytes consumed by the elements of the array.

[`DataFrame.memory_usage`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.memory_usage.html#pandas.DataFrame.memory_usage "pandas.DataFrame.memory_usage")

Bytes consumed by a DataFrame.

Examples

\>>> s \= pd.Series(range(3))
\>>> s.memory\_usage()
156

Copy to clipboard

Not including the index gives the size of the rest of the data, which is necessarily smaller:

\>>> s.memory\_usage(index\=False)
24

Copy to clipboard

The memory footprint of object values is ignored by default:

\>>> s \= pd.Series(\["a", "b"\])
\>>> s.values
<ArrowStringArray>
\['a', 'b'\]
Length: 2, dtype: str
\>>> s.memory\_usage()
150
\>>> s.memory\_usage(deep\=True)
150

Copy to clipboard

On this page