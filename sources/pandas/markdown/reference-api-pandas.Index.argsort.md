[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.argsort.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.argsort[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.argsort.html#pandas-index-argsort "Link to this heading")

============================================================================================================================================

Index.argsort(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L6325-L6366)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.argsort.html#pandas.Index.argsort "Link to this definition")

Return the integer indices that would sort the index.

This method returns an array of indices that indicate the order in which elements of the index should be arranged to produce a sorted index. It delegates to the underlying array’s `argsort` method.

Parameters:

**\*args**

Passed to numpy.ndarray.argsort.

**\*\*kwargs**

Passed to numpy.ndarray.argsort.

Returns:

np.ndarray\[np.intp\]

Integer indices that would sort the index if used as an indexer.

See also

[`numpy.argsort`](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "(in NumPy v2.5)")

Similar method for NumPy arrays.

[`Index.sort_values`](https://pandas.pydata.org/docs/reference/api/pandas.Index.sort_values.html#pandas.Index.sort_values "pandas.Index.sort_values")

Return sorted copy of Index.

Examples

\>>> idx \= pd.Index(\["b", "a", "d", "c"\])
\>>> idx
Index(\['b', 'a', 'd', 'c'\], dtype='str')

Copy to clipboard

\>>> order \= idx.argsort()
\>>> order
array(\[1, 0, 3, 2\])

Copy to clipboard

\>>> idx\[order\]
Index(\['a', 'b', 'c', 'd'\], dtype='str')

Copy to clipboard

On this page