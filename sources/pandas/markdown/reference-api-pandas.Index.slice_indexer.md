[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.slice_indexer.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.slice_indexer.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.slice_indexer.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.slice_indexer.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.slice_indexer.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.slice_indexer.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.slice_indexer.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.slice_indexer.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.slice_indexer.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.slice_indexer.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.slice_indexer.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.slice_indexer.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.slice_indexer.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.slice_indexer.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.slice\_indexer[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.slice_indexer.html#pandas-index-slice-indexer "Link to this heading")

===============================================================================================================================================================

Index.slice\_indexer(_start\=None_, _end\=None_, _step\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L7085-L7144)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.slice_indexer.html#pandas.Index.slice_indexer "Link to this definition")

Compute the slice indexer for input labels and step.

Index needs to be ordered and unique.

Parameters:

**start**label, default None

If None, defaults to the beginning.

**end**label, default None

If None, defaults to the end.

**step**int, default None

If None, defaults to 1.

Returns:

slice

A slice object.

Raises:

**KeyError**If key does not exist, or key is not unique and index is

not ordered.

See also

[`Index.slice_locs`](https://pandas.pydata.org/docs/reference/api/pandas.Index.slice_locs.html#pandas.Index.slice_locs "pandas.Index.slice_locs")

Computes slice locations for input labels.

[`Index.get_slice_bound`](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_slice_bound.html#pandas.Index.get_slice_bound "pandas.Index.get_slice_bound")

Retrieves slice bound that corresponds to given label.

Notes

This function assumes that the data is sorted, so use at your own peril.

Examples

This is a method on all index types. For example you can do:

\>>> idx \= pd.Index(list("abcd"))
\>>> idx.slice\_indexer(start\="b", end\="c")
slice(1, 3, None)

Copy to clipboard

\>>> idx \= pd.MultiIndex.from\_arrays(\[list("abcd"), list("efgh")\])
\>>> idx.slice\_indexer(start\="b", end\=("c", "g"))
slice(1, 3, None)

Copy to clipboard

On this page