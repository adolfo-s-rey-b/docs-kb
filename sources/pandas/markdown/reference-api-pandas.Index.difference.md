[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.difference.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.difference.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.difference.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.difference.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.difference.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.difference.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.difference.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.difference.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.difference.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.difference.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.difference.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.difference.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.difference.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.difference.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.difference[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.difference.html#pandas-index-difference "Link to this heading")

=====================================================================================================================================================

final Index.difference(_other_, _sort\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L3563-L3633)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.difference.html#pandas.Index.difference "Link to this definition")

Return a new Index with elements of index not in other.

This is the set difference of two Index objects.

Parameters:

**other**Index or array-like

Index object or an array-like object containing elements to be compared with the elements of the original Index.

**sort**bool or None, default None

Whether to sort the resulting index. By default, the values are attempted to be sorted, but any TypeError from incomparable elements is caught by pandas.

*   None : Attempt to sort the result, but catch any TypeErrors from comparing incomparable elements.
    
*   False : Do not sort the result.
    
*   True : Sort the result (which may raise TypeError).
    

Returns:

Index

Returns a new Index object containing elements that are in the original Index but not in the other Index.

See also

[`Index.symmetric_difference`](https://pandas.pydata.org/docs/reference/api/pandas.Index.symmetric_difference.html#pandas.Index.symmetric_difference "pandas.Index.symmetric_difference")

Compute the symmetric difference of two Index objects.

[`Index.intersection`](https://pandas.pydata.org/docs/reference/api/pandas.Index.intersection.html#pandas.Index.intersection "pandas.Index.intersection")

Form the intersection of two Index objects.

Examples

\>>> idx1 \= pd.Index(\[2, 1, 3, 4\])
\>>> idx2 \= pd.Index(\[3, 4, 5, 6\])
\>>> idx1.difference(idx2)
Index(\[1, 2\], dtype='int64')
\>>> idx1.difference(idx2, sort\=False)
Index(\[2, 1\], dtype='int64')

Copy to clipboard

On this page