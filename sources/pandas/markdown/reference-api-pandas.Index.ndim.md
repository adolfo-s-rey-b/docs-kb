[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.ndim.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.ndim[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.ndim.html#pandas-index-ndim "Link to this heading")

===================================================================================================================================

property Index.ndim[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/base.py#L381-L415)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.ndim.html#pandas.Index.ndim "Link to this definition")

Number of dimensions of the underlying data, by definition 1.

Series and Index are one-dimensional; this property always returns 1 for compatibility with array-like interfaces.

See also

[`Series.size`](https://pandas.pydata.org/docs/reference/api/pandas.Series.size.html#pandas.Series.size "pandas.Series.size")

Return the number of elements in the underlying data.

[`Series.shape`](https://pandas.pydata.org/docs/reference/api/pandas.Series.shape.html#pandas.Series.shape "pandas.Series.shape")

Return a tuple of the shape of the underlying data.

[`Series.dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dtype.html#pandas.Series.dtype "pandas.Series.dtype")

Return the dtype object of the underlying data.

[`Series.values`](https://pandas.pydata.org/docs/reference/api/pandas.Series.values.html#pandas.Series.values "pandas.Series.values")

Return Series as ndarray or ndarray-like depending on the dtype.

Examples

\>>> s \= pd.Series(\["Ant", "Bear", "Cow"\])
\>>> s
0     Ant
1    Bear
2     Cow
dtype: str
\>>> s.ndim
1

Copy to clipboard

For Index:

\>>> idx \= pd.Index(\[1, 2, 3\])
\>>> idx
Index(\[1, 2, 3\], dtype='int64')
\>>> idx.ndim
1

Copy to clipboard

On this page