[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.union.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.union.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.union.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.union.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.union.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.union.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.union.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.union.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.union.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.union.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.union.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.union.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.union.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.union.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.union[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.union.html#pandas-index-union "Link to this heading")

======================================================================================================================================

final Index.union(_other_, _sort\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L3173-L3313)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.union.html#pandas.Index.union "Link to this definition")

Form the union of two Index objects.

If the Index objects are incompatible, both Index objects will be cast to dtype(‘object’) first.

Parameters:

**other**Index or array-like

Index or an array-like object containing elements to form the union with the original Index.

**sort**bool or None, default None

Whether to sort the resulting Index.

*   None : Sort the result, except when
    
    1.  self and other are equal.
        
    2.  self or other has length 0.
        
    3.  Some values in self or other cannot be compared. A RuntimeWarning is issued in this case.
        
*   False : do not sort the result.
    
*   True : Sort the result (which may raise TypeError).
    

Returns:

Index

Returns a new Index object with elements from both the original Index and the `other` Index.

If either index contains duplicate entries, the result preserves duplicates up to the maximum number of occurrences in either index.

See also

[`Index.unique`](https://pandas.pydata.org/docs/reference/api/pandas.Index.unique.html#pandas.Index.unique "pandas.Index.unique")

Return unique values in the index.

[`Index.intersection`](https://pandas.pydata.org/docs/reference/api/pandas.Index.intersection.html#pandas.Index.intersection "pandas.Index.intersection")

Form the intersection of two Index objects.

[`Index.difference`](https://pandas.pydata.org/docs/reference/api/pandas.Index.difference.html#pandas.Index.difference "pandas.Index.difference")

Return a new Index with elements of index not in other.

Examples

Union matching dtypes

\>>> idx1 \= pd.Index(\[1, 2, 3, 4\])
\>>> idx2 \= pd.Index(\[3, 4, 5, 6\])
\>>> idx1.union(idx2)
Index(\[1, 2, 3, 4, 5, 6\], dtype='int64')

Copy to clipboard

Union mismatched dtypes

\>>> idx1 \= pd.Index(\["a", "b", "c", "d"\])
\>>> idx2 \= pd.Index(\[1, 2, 3, 4\])
\>>> idx1.union(idx2)
Index(\['a', 'b', 'c', 'd', 1, 2, 3, 4\], dtype='object')

Copy to clipboard

Union with duplicate values

\>>> idx1 \= pd.Index(\[1, 2, 2, 3\])
\>>> idx2 \= pd.Index(\[3, 3, 4\])
\>>> idx1.union(idx2)
Index(\[1, 2, 2, 3, 3, 4\], dtype='int64')

Copy to clipboard

MultiIndex case

\>>> idx1 \= pd.MultiIndex.from\_arrays(
...     \[\[1, 1, 2, 2\], \["Red", "Blue", "Red", "Blue"\]\]
... )
\>>> idx1
MultiIndex(\[(1,  'Red'),\
    (1, 'Blue'),\
    (2,  'Red'),\
    (2, 'Blue')\],
   )
\>>> idx2 \= pd.MultiIndex.from\_arrays(
...     \[\[3, 3, 2, 2\], \["Red", "Green", "Red", "Green"\]\]
... )
\>>> idx2
MultiIndex(\[(3,   'Red'),\
    (3, 'Green'),\
    (2,   'Red'),\
    (2, 'Green')\],
   )
\>>> idx1.union(idx2)
MultiIndex(\[(1,  'Blue'),\
    (1,   'Red'),\
    (2,  'Blue'),\
    (2, 'Green'),\
    (2,   'Red'),\
    (3, 'Green'),\
    (3,   'Red')\],
   )
\>>> idx1.union(idx2, sort\=False)
MultiIndex(\[(1,   'Red'),\
    (1,  'Blue'),\
    (2,   'Red'),\
    (2,  'Blue'),\
    (3,   'Red'),\
    (3, 'Green'),\
    (2, 'Green')\],
   )

Copy to clipboard

On this page