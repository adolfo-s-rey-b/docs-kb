[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.putmask.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.putmask.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.putmask.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.putmask.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.putmask.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.putmask.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.putmask.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.putmask.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.putmask.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.putmask.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.putmask.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.putmask.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.putmask.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.putmask.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.putmask[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.putmask.html#pandas-index-putmask "Link to this heading")

============================================================================================================================================

Index.putmask(_mask_, _value_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L5817-L5852)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.putmask.html#pandas.Index.putmask "Link to this definition")

Return a new Index of the values set with the mask.

Replaces elements of the Index where the corresponding mask entry is `True`, returning a new Index rather than modifying in place.

Parameters:

**mask**array-like of bool

Array of booleans denoting where values should be replaced.

**value**scalar

Scalar value to use to fill holes (e.g. 0). This value cannot be a list-likes.

Returns:

Index

A new Index of the values set with the mask.

See also

[`numpy.putmask`](https://numpy.org/doc/stable/reference/generated/numpy.putmask.html#numpy.putmask "(in NumPy v2.5)")

Changes elements of an array based on conditional and input values.

Examples

\>>> idx1 \= pd.Index(\[1, 2, 3\])
\>>> idx2 \= pd.Index(\[5, 6, 7\])
\>>> idx1.putmask(\[True, False, False\], idx2)
Index(\[5, 2, 3\], dtype='int64')

Copy to clipboard

On this page