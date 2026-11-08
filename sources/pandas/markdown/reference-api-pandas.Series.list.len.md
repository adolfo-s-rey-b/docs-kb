[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.list.len.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.list.len[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.list.len.html#pandas-series-list-len "Link to this heading")

==================================================================================================================================================

Series.list.len()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/arrow/accessors.py#L95-L136)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.list.len.html#pandas.Series.list.len "Link to this definition")

Return the length of each list in the Series.

Computes the number of elements in each list entry. The result is a Series of integers with the same index as the original Series.

Returns:

pandas.Series

The length of each list.

See also

`str.len`

Python built-in function returning the length of an object.

[`Series.size`](https://pandas.pydata.org/docs/reference/api/pandas.Series.size.html#pandas.Series.size "pandas.Series.size")

Returns the length of the Series.

`StringMethods.len`

Compute the length of each element in the Series/Index.

Examples

\>>> import pyarrow as pa
\>>> s \= pd.Series(
...     \[\
...         \[1, 2, 3\],\
...         \[3\],\
...     \],
...     dtype\=pd.ArrowDtype(pa.list\_(pa.int64())),
... )
\>>> s.list.len()
0    3
1    1
dtype: int32\[pyarrow\]

Copy to clipboard

On this page