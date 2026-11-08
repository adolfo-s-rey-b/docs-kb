[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.inferred_type.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.inferred_type.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.inferred_type.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.inferred_type.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.inferred_type.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.inferred_type.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.inferred_type.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.inferred_type.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.inferred_type.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.inferred_type.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.inferred_type.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.inferred_type.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.inferred_type.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.inferred_type.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.inferred\_type[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.inferred_type.html#pandas-index-inferred-type "Link to this heading")

===============================================================================================================================================================

Index.inferred\_type[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L2641-L2662)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.inferred_type.html#pandas.Index.inferred_type "Link to this definition")

Return a string of the type inferred from the values.

This inspects the actual values in the Index to determine their type, which may differ from the stored [`dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Index.dtype.html#pandas.Index.dtype "pandas.Index.dtype")
. For example, an object-dtype Index containing only integers returns `'integer'`.

See also

[`Index.dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Index.dtype.html#pandas.Index.dtype "pandas.Index.dtype")

Return the dtype object of the underlying data.

Examples

\>>> idx \= pd.Index(\[1, 2, 3\])
\>>> idx
Index(\[1, 2, 3\], dtype='int64')
\>>> idx.inferred\_type
'integer'

Copy to clipboard

On this page