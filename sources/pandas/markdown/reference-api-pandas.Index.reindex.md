[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.reindex.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.reindex[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.reindex.html#pandas-index-reindex "Link to this heading")

============================================================================================================================================

Index.reindex(_target_, _method\=None_, _level\=None_, _limit\=None_, _tolerance\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L4339-L4455)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.reindex.html#pandas.Index.reindex "Link to this definition")

Create index with target’s values.

Optionally provides an indexer that maps the new labels back to the original positions, and supports filling methods for non-exact matches.

Parameters:

**target**an iterable

An iterable containing the values to be used for creating the new index.

**method**{None, ‘pad’/’ffill’, ‘backfill’/’bfill’, ‘nearest’}, optional

*   default: exact matches only.
    
*   pad / ffill: find the PREVIOUS index value if no exact match.
    
*   backfill / bfill: use NEXT index value if no exact match
    
*   nearest: use the NEAREST index value if no exact match. Tied distances are broken by preferring the larger index value.
    

**level**int, optional

Level of multiindex.

**limit**int, optional

Maximum number of consecutive labels in `target` to match for inexact matches.

**tolerance**int, float, or list-like, optional

Maximum distance between original and new labels for inexact matches. The values of the index at the matching locations must satisfy the equation `abs(index[indexer] - target) <= tolerance`.

Tolerance may be a scalar value, which applies the same tolerance to all values, or list-like, which applies variable tolerance per element. List-like includes list, tuple, array, Series, and must be the same size as the index and its dtype must exactly match the index’s type.

Returns:

**new\_index**pd.Index

Resulting index.

**indexer**np.ndarray\[np.intp\] or None

Indices of output values in original index.

Raises:

TypeError

If `method` passed along with `level`.

ValueError

If non-unique multi-index

ValueError

If non-unique index and `method` or `limit` passed.

See also

[`Series.reindex`](https://pandas.pydata.org/docs/reference/api/pandas.Series.reindex.html#pandas.Series.reindex "pandas.Series.reindex")

Conform Series to new index with optional filling logic.

[`DataFrame.reindex`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex.html#pandas.DataFrame.reindex "pandas.DataFrame.reindex")

Conform DataFrame to new index with optional filling logic.

Examples

\>>> idx \= pd.Index(\["car", "bike", "train", "tractor"\])
\>>> idx
Index(\['car', 'bike', 'train', 'tractor'\], dtype='str')
\>>> idx.reindex(\["car", "bike"\])
(Index(\['car', 'bike'\], dtype='str'), array(\[0, 1\]))

Copy to clipboard

On this page