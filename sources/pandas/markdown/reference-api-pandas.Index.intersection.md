[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.intersection.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.intersection.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.intersection.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.intersection.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.intersection.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.intersection.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.intersection.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.intersection.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.intersection.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.intersection.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.intersection.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.intersection.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.intersection.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.intersection.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.intersection[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.intersection.html#pandas-index-intersection "Link to this heading")

===========================================================================================================================================================

final Index.intersection(_other_, _sort\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L3401-L3495)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.intersection.html#pandas.Index.intersection "Link to this definition")

Form the intersection of two Index objects.

This returns a new Index with elements common to the index and other.

Parameters:

**other**Index or array-like

An Index or an array-like object containing elements to form the intersection with the original Index.

**sort**True, False or None, default False

Whether to sort the resulting index.

*   None : sort the result, except when self and other are equal or when the values cannot be compared.
    
*   False : do not sort the result.
    
*   True : Sort the result (which may raise TypeError).
    

Returns:

Index

Returns a new Index object with elements common to both the original Index and the other Index.

See also

[`Index.union`](https://pandas.pydata.org/docs/reference/api/pandas.Index.union.html#pandas.Index.union "pandas.Index.union")

Form the union of two Index objects.

[`Index.difference`](https://pandas.pydata.org/docs/reference/api/pandas.Index.difference.html#pandas.Index.difference "pandas.Index.difference")

Return a new Index with elements of index not in other.

[`Index.isin`](https://pandas.pydata.org/docs/reference/api/pandas.Index.isin.html#pandas.Index.isin "pandas.Index.isin")

Return a boolean array where the index values are in values.

Examples

\>>> idx1 \= pd.Index(\[1, 2, 3, 4\])
\>>> idx2 \= pd.Index(\[3, 4, 5, 6\])
\>>> idx1.intersection(idx2)
Index(\[3, 4\], dtype='int64')

Copy to clipboard

On this page