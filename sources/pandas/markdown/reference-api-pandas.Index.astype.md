[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.astype.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.astype.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.astype.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.astype.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.astype.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.astype.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.astype.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.astype.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.astype.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.astype.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.astype.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.astype.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.astype.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.astype.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.astype[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.astype.html#pandas-index-astype "Link to this heading")

=========================================================================================================================================

Index.astype(_dtype_, _copy\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L1149-L1216)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.astype.html#pandas.Index.astype "Link to this definition")

Create an Index with values cast to dtypes.

The class of a new Index is determined by dtype. When conversion is impossible, a TypeError exception is raised.

Parameters:

**dtype**numpy dtype or pandas type

Dtype for the result Index.

**copy**bool, default True

By default, astype always returns a newly allocated object. If copy is set to False and internal requirements on dtype are satisfied, the original data is used to create a new Index or the original Index is returned.

Returns:

Index

Index with values cast to specified dtype.

See also

[`Index.dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Index.dtype.html#pandas.Index.dtype "pandas.Index.dtype")

Return the dtype object of the underlying data.

`Index.dtypes`

Return the dtype object of the underlying data.

`Index.convert_dtypes`

Convert columns to the best possible dtypes.

Examples

\>>> idx \= pd.Index(\[1, 2, 3\])
\>>> idx
Index(\[1, 2, 3\], dtype='int64')
\>>> idx.astype("float")
Index(\[1.0, 2.0, 3.0\], dtype='float64')

Copy to clipboard

On this page