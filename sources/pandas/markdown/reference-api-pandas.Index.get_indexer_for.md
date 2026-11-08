[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_indexer_for.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.get_indexer_for.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_indexer_for.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.get_indexer_for.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.get_indexer_for.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.get_indexer_for.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.get_indexer_for.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.get_indexer_for.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.get_indexer_for.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.get_indexer_for.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.get_indexer_for.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.get_indexer_for.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.get_indexer_for.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.get_indexer_for.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.get\_indexer\_for[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_indexer_for.html#pandas-index-get-indexer-for "Link to this heading")

======================================================================================================================================================================

final Index.get\_indexer\_for(_target_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L6477-L6511)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_indexer_for.html#pandas.Index.get_indexer_for "Link to this definition")

Guaranteed return of an indexer even when non-unique.

This dispatches to get\_indexer or get\_indexer\_non\_unique as appropriate.

Parameters:

**target**Index

An iterable containing the values to be used for computing indexer.

Returns:

np.ndarray\[np.intp\]

List of indices.

See also

[`Index.get_indexer`](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_indexer.html#pandas.Index.get_indexer "pandas.Index.get_indexer")

Computes indexer and mask for new index given the current index.

`Index.get_non_unique`

Returns indexer and masks for new index given the current index.

Examples

\>>> idx \= pd.Index(\[np.nan, "var1", np.nan\])
\>>> idx.get\_indexer\_for(\[np.nan\])
array(\[0, 2\])

Copy to clipboard

On this page