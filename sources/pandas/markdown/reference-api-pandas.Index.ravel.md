[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.ravel.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.ravel.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.ravel.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.ravel.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.ravel.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.ravel.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.ravel.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.ravel.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.ravel.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.ravel.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.ravel.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.ravel.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.ravel.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.ravel.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.ravel[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.ravel.html#pandas-index-ravel "Link to this heading")

======================================================================================================================================

final Index.ravel(_order\='C'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L1040-L1069)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.ravel.html#pandas.Index.ravel "Link to this definition")

Return a view on self.

Since Index objects are one-dimensional, this simply returns a view of the original Index unchanged.

Parameters:

**order**{‘K’, ‘A’, ‘C’, ‘F’}, default ‘C’

Specify the memory layout of the view. This parameter is not implemented currently.

Returns:

Index

A view on self.

See also

[`numpy.ndarray.ravel`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.ravel.html#numpy.ndarray.ravel "(in NumPy v2.5)")

Return a flattened array.

Examples

\>>> s \= pd.Series(\[1, 2, 3\], index\=\["a", "b", "c"\])
\>>> s.index.ravel()
Index(\['a', 'b', 'c'\], dtype='str')

Copy to clipboard

On this page