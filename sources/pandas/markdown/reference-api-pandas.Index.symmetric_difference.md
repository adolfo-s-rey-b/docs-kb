[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.symmetric_difference.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.symmetric\_difference[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.symmetric_difference.html#pandas-index-symmetric-difference "Link to this heading")

====================================================================================================================================================================================

Index.symmetric\_difference(_other_, _result\_name\=None_, _sort\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L3652-L3752)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.symmetric_difference.html#pandas.Index.symmetric_difference "Link to this definition")

Compute the symmetric difference of two Index objects.

The result contains elements that are in either of the two Index objects but not in their intersection. This is the set-theoretic symmetric difference, analogous to the `^` operator on Python sets.

Parameters:

**other**Index or array-like

Index or an array-like object with elements to compute the symmetric difference with the original Index.

**result\_name**str

A string representing the name of the resulting Index, if desired.

**sort**bool or None, default None

Whether to sort the resulting index. By default, the values are attempted to be sorted, but any TypeError from incomparable elements is caught by pandas.

*   None : Attempt to sort the result, but catch any TypeErrors from comparing incomparable elements.
    
*   False : Do not sort the result.
    
*   True : Sort the result (which may raise TypeError).
    

Returns:

Index

Returns a new Index object containing elements that appear in either the original Index or the other Index, but not both.

See also

[`Index.difference`](https://pandas.pydata.org/docs/reference/api/pandas.Index.difference.html#pandas.Index.difference "pandas.Index.difference")

Return a new Index with elements of index not in other.

[`Index.union`](https://pandas.pydata.org/docs/reference/api/pandas.Index.union.html#pandas.Index.union "pandas.Index.union")

Form the union of two Index objects.

[`Index.intersection`](https://pandas.pydata.org/docs/reference/api/pandas.Index.intersection.html#pandas.Index.intersection "pandas.Index.intersection")

Form the intersection of two Index objects.

Notes

`symmetric_difference` contains elements that appear in either `idx1` or `idx2` but not both. Equivalent to the Index created by `idx1.difference(idx2) | idx2.difference(idx1)` with duplicates dropped.

Examples

\>>> idx1 \= pd.Index(\[1, 2, 3, 4\])
\>>> idx2 \= pd.Index(\[2, 3, 4, 5\])
\>>> idx1.symmetric\_difference(idx2)
Index(\[1, 5\], dtype='int64')

Copy to clipboard

On this page