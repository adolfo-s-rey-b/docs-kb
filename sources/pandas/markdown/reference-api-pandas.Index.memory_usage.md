[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.memory_usage.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.memory_usage.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.memory_usage.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.memory_usage.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.memory_usage.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.memory_usage.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.memory_usage.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.memory_usage.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.memory_usage.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.memory_usage.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.memory_usage.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.memory_usage.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.memory_usage.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.memory_usage.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.memory\_usage[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.memory_usage.html#pandas-index-memory-usage "Link to this heading")

============================================================================================================================================================

Index.memory\_usage(_deep\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L5465-L5505)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.memory_usage.html#pandas.Index.memory_usage "Link to this definition")

Memory usage of the values.

Returns the number of bytes consumed by the Index. When `deep=True`, the memory consumption of underlying objects referencing this Index (e.g., the characters of object-dtype values) is included.

Parameters:

**deep**bool, default False

Introspect the data deeply, interrogate object dtypes for system-level memory consumption.

Returns:

bytes used

Returns memory usage of the values in the Index in bytes.

See also

[`numpy.ndarray.nbytes`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.nbytes.html#numpy.ndarray.nbytes "(in NumPy v2.5)")

Total bytes consumed by the elements of the array.

Notes

Memory usage does not include memory consumed by elements that are not components of the array if deep=False or if used on PyPy

Examples

\>>> idx \= pd.Index(\[1, 2, 3\])
\>>> idx.memory\_usage()
24

Copy to clipboard

On this page