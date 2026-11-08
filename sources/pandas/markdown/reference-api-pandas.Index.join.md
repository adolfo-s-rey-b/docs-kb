[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.join.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.join.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.join.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.join.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.join.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.join.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.join.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.join.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.join.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.join.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.join.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.join.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.join.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.join.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.join[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.join.html#pandas-index-join "Link to this heading")

===================================================================================================================================

final Index.join(_other_, _\*_, _how\='left'_, _level\=None_, _return\_indexers\=False_, _sort\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L4579-L4732)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.join.html#pandas.Index.join "Link to this definition")

Compute join\_index and indexers to conform data structures to the new index.

This method computes the result of a join between two Index objects using the specified join type, and optionally returns integer indexers that map each original index to the new joined index.

Parameters:

**other**Index

The other index on which join is performed.

**how**{‘left’, ‘right’, ‘inner’, ‘outer’}

**level**int or level name, default None

It is either the integer position or the name of the level.

**return\_indexers**bool, default False

Whether to return the indexers or not for both the index objects.

**sort**bool, default False

Sort the join keys lexicographically in the result Index. If False, the order of the join keys depends on the join type (how keyword).

Returns:

join\_index, (left\_indexer, right\_indexer)

The new index.

See also

[`DataFrame.join`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html#pandas.DataFrame.join "pandas.DataFrame.join")

Join columns with other DataFrame either on index or on a key.

[`DataFrame.merge`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html#pandas.DataFrame.merge "pandas.DataFrame.merge")

Merge DataFrame or named Series objects with a database-style join.

Examples

\>>> idx1 \= pd.Index(\[1, 2, 3\])
\>>> idx2 \= pd.Index(\[4, 5, 6\])
\>>> idx1.join(idx2, how\="outer")
Index(\[1, 2, 3, 4, 5, 6\], dtype='int64')
\>>> idx1.join(other\=idx2, how\="outer", return\_indexers\=True)
(Index(\[1, 2, 3, 4, 5, 6\], dtype='int64'),
array(\[ 0,  1,  2, -1, -1, -1\]), array(\[-1, -1, -1,  0,  1,  2\]))

Copy to clipboard

On this page