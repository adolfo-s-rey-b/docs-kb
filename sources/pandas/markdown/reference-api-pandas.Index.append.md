[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.append.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.append.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.append.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.append.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.append.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.append.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.append.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.append.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.append.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.append.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.append.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.append.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.append.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.append.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.append[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.append.html#pandas-index-append "Link to this heading")

=========================================================================================================================================

Index.append(_other_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L5760-L5805)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.append.html#pandas.Index.append "Link to this definition")

Append a collection of Index options together.

This method concatenates one or more Index objects to the current index, returning a new Index containing all elements in order.

Parameters:

**other**Index or list/tuple of indices

Single Index or a collection of indices, which can be either a list or a tuple.

Returns:

Index

Returns a new Index object resulting from appending the provided other indices to the original Index.

See also

[`Index.insert`](https://pandas.pydata.org/docs/reference/api/pandas.Index.insert.html#pandas.Index.insert "pandas.Index.insert")

Make new Index inserting new item at location.

Examples

\>>> idx \= pd.Index(\[1, 2, 3\])
\>>> idx.append(pd.Index(\[4\]))
Index(\[1, 2, 3, 4\], dtype='int64')

Copy to clipboard

On this page