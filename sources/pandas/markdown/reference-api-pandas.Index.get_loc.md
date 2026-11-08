[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_loc.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.get_loc.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_loc.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.get_loc.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.get_loc.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.get_loc.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.get_loc.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.get_loc.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.get_loc.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.get_loc.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.get_loc.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.get_loc.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.get_loc.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.get_loc.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.get\_loc[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_loc.html#pandas-index-get-loc "Link to this heading")

=============================================================================================================================================

Index.get\_loc(_key_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L3771-L3829)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_loc.html#pandas.Index.get_loc "Link to this definition")

Get integer location, slice or boolean mask for requested label.

The return type depends on the characteristics of the index: an integer for a unique index, a slice for a monotonic index with duplicate entries, or a boolean mask for a non-monotonic index with duplicates.

Parameters:

**key**label

The key to check its location if it is present in the index.

Returns:

int if unique index, slice if monotonic index, else mask

Integer location, slice or boolean mask.

See also

[`Index.get_slice_bound`](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_slice_bound.html#pandas.Index.get_slice_bound "pandas.Index.get_slice_bound")

Calculate slice bound that corresponds to given label.

[`Index.get_indexer`](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_indexer.html#pandas.Index.get_indexer "pandas.Index.get_indexer")

Computes indexer and mask for new index given the current index.

`Index.get_non_unique`

Returns indexer and masks for new index given the current index.

[`Index.get_indexer_for`](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_indexer_for.html#pandas.Index.get_indexer_for "pandas.Index.get_indexer_for")

Returns an indexer even when non-unique.

Examples

\>>> unique\_index \= pd.Index(list("abc"))
\>>> unique\_index.get\_loc("b")
1

Copy to clipboard

\>>> monotonic\_index \= pd.Index(list("abbc"))
\>>> monotonic\_index.get\_loc("b")
slice(1, 3, None)

Copy to clipboard

\>>> non\_monotonic\_index \= pd.Index(list("abcb"))
\>>> non\_monotonic\_index.get\_loc("b")
array(\[False,  True, False,  True\])

Copy to clipboard

On this page