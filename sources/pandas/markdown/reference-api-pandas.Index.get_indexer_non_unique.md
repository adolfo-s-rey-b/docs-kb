[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_indexer_non_unique.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.get_indexer_non_unique.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_indexer_non_unique.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.get_indexer_non_unique.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.get_indexer_non_unique.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.get_indexer_non_unique.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.get_indexer_non_unique.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.get_indexer_non_unique.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.get_indexer_non_unique.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.get_indexer_non_unique.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.get_indexer_non_unique.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.get_indexer_non_unique.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.get_indexer_non_unique.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.get_indexer_non_unique.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.get\_indexer\_non\_unique[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_indexer_non_unique.html#pandas-index-get-indexer-non-unique "Link to this heading")

============================================================================================================================================================================================

Index.get\_indexer\_non\_unique(_target_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L6386-L6475)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_indexer_non_unique.html#pandas.Index.get_indexer_non_unique "Link to this definition")

Compute indexer and mask for new index given the current index.

The indexer should be then used as an input to ndarray.take to align the current data to the new index.

Parameters:

**target**Index

An iterable containing the values to be used for computing indexer.

Returns:

**indexer**np.ndarray\[np.intp\]

Integers from 0 to n - 1 indicating that the index at these positions matches the corresponding target values. Missing values in the target are marked by -1.

**missing**np.ndarray\[np.intp\]

An indexer into the target of the values not found. These correspond to the -1 in the indexer array.

See also

[`Index.get_indexer`](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_indexer.html#pandas.Index.get_indexer "pandas.Index.get_indexer")

Computes indexer and mask for new index given the current index.

[`Index.get_indexer_for`](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_indexer_for.html#pandas.Index.get_indexer_for "pandas.Index.get_indexer_for")

Returns an indexer even when non-unique.

Examples

\>>> index \= pd.Index(\["c", "b", "a", "b", "b"\])
\>>> index.get\_indexer\_non\_unique(\["b", "b"\])
(array(\[1, 3, 4, 1, 3, 4\]), array(\[\], dtype=int64))

Copy to clipboard

In the example below there are no matched values.

\>>> index \= pd.Index(\["c", "b", "a", "b", "b"\])
\>>> index.get\_indexer\_non\_unique(\["q", "r", "t"\])
(array(\[-1, -1, -1\]), array(\[0, 1, 2\]))

Copy to clipboard

For this reason, the returned `indexer` contains only integers equal to -1. It demonstrates that there’s no match between the index and the `target` values at these positions. The mask \[0, 1, 2\] in the return value shows that the first, second, and third elements are missing.

Notice that the return value is a tuple contains two items. In the example below the first item is an array of locations in `index`. The second item is a mask shows that the first and third elements are missing.

\>>> index \= pd.Index(\["c", "b", "a", "b", "b"\])
\>>> index.get\_indexer\_non\_unique(\["f", "b", "s"\])
(array(\[-1,  1,  3,  4, -1\]), array(\[0, 2\]))

Copy to clipboard

On this page