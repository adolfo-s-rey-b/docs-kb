[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.shape.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.shape.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.shape.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.shape.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.shape.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.shape.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.shape.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.shape.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.shape.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.shape.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.shape.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.shape.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.shape.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.shape.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.shape[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.shape.html#pandas-index-shape "Link to this heading")

======================================================================================================================================

property Index.shape[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L8226-L8251)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.shape.html#pandas.Index.shape "Link to this definition")

Return a tuple of the shape of the underlying data.

Since an Index is always one-dimensional, this returns a tuple with a single element equal to the number of elements in the Index.

See also

[`Index.size`](https://pandas.pydata.org/docs/reference/api/pandas.Index.size.html#pandas.Index.size "pandas.Index.size")

Return the number of elements in the underlying data.

[`Index.ndim`](https://pandas.pydata.org/docs/reference/api/pandas.Index.ndim.html#pandas.Index.ndim "pandas.Index.ndim")

Number of dimensions of the underlying data, by definition 1.

[`Index.dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Index.dtype.html#pandas.Index.dtype "pandas.Index.dtype")

Return the dtype object of the underlying data.

[`Index.values`](https://pandas.pydata.org/docs/reference/api/pandas.Index.values.html#pandas.Index.values "pandas.Index.values")

Return an array representing the data in the Index.

Examples

\>>> idx \= pd.Index(\[1, 2, 3\])
\>>> idx
Index(\[1, 2, 3\], dtype='int64')
\>>> idx.shape
(3,)

Copy to clipboard

On this page