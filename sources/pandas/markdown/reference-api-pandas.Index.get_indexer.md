[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_indexer.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.get\_indexer[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_indexer.html#pandas-index-get-indexer "Link to this heading")

=========================================================================================================================================================

final Index.get\_indexer(_target_, _method\=None_, _limit\=None_, _tolerance\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L3831-L3973)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_indexer.html#pandas.Index.get_indexer "Link to this definition")

Compute indexer and mask for new index given the current index.

The indexer should be then used as an input to ndarray.take to align the current data to the new index.

Parameters:

**target**Index

An iterable containing the values to be used for computing indexer.

**method**{None, ‘pad’/’ffill’, ‘backfill’/’bfill’, ‘nearest’}, optional

*   default: exact matches only.
    
*   pad / ffill: find the PREVIOUS index value if no exact match.
    
*   backfill / bfill: use NEXT index value if no exact match
    
*   nearest: use the NEAREST index value if no exact match. Tied distances are broken by preferring the larger index value.
    

**limit**int, optional

Maximum number of consecutive labels in `target` to match for inexact matches.

**tolerance**optional

Maximum distance between original and new labels for inexact matches. The values of the index at the matching locations must satisfy the equation `abs(index[indexer] - target) <= tolerance`.

Tolerance may be a scalar value, which applies the same tolerance to all values, or list-like, which applies variable tolerance per element. List-like includes list, tuple, array, Series, and must be the same size as the index and its dtype must exactly match the index’s type.

Returns:

np.ndarray\[np.intp\]

Integers from 0 to n - 1 indicating that the index at these positions matches the corresponding target values. Missing values in the target are marked by -1.

See also

[`Index.get_indexer_for`](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_indexer_for.html#pandas.Index.get_indexer_for "pandas.Index.get_indexer_for")

Returns an indexer even when non-unique.

`Index.get_non_unique`

Returns indexer and masks for new index given the current index.

Notes

Returns -1 for unmatched values, for further explanation see the example below.

Examples

\>>> index \= pd.Index(\["c", "a", "b"\])
\>>> index.get\_indexer(\["a", "b", "x"\])
array(\[ 1,  2, -1\])

Copy to clipboard

Notice that the return value is an array of locations in `index` and `x` is marked by -1, as it is not in `index`.

On this page