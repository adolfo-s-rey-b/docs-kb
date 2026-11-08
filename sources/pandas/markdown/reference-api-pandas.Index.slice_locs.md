[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.slice_locs.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.slice_locs.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.slice_locs.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.slice_locs.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.slice_locs.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.slice_locs.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.slice_locs.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.slice_locs.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.slice_locs.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.slice_locs.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.slice_locs.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.slice_locs.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.slice_locs.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.slice_locs.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.slice\_locs[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.slice_locs.html#pandas-index-slice-locs "Link to this heading")

======================================================================================================================================================

Index.slice\_locs(_start\=None_, _end\=None_, _step\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L7335-L7450)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.slice_locs.html#pandas.Index.slice_locs "Link to this definition")

Compute slice locations for input labels.

This method determines the integer start and end positions for a label-based slice, which is useful for translating label-based slicing into positional slicing on the underlying data.

Parameters:

**start**label, default None

If None, defaults to the beginning.

**end**label, default None

If None, defaults to the end.

**step**int, defaults None

If None, defaults to 1.

Returns:

tuple\[int, int\]

Returns a tuple of two integers representing the slice locations for the input labels within the index.

See also

[`Index.get_loc`](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_loc.html#pandas.Index.get_loc "pandas.Index.get_loc")

Get location for a single label.

[`Index.get_slice_bound`](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_slice_bound.html#pandas.Index.get_slice_bound "pandas.Index.get_slice_bound")

Calculate the slice bound for a single label; used internally by `slice_locs` for each of `start` and `end`.

Notes

This method only works if the index is monotonic or unique.

If `start` or `end` is not present in a monotonic index, the returned position is the insertion point that preserves ordering (analogous to [`numpy.searchsorted()`](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html#numpy.searchsorted "(in NumPy v2.5)")
); no error is raised. If the index is not monotonic and the label is missing, a `KeyError` is raised.

Examples

\>>> idx \= pd.Index(list("abcd"))
\>>> idx.slice\_locs(start\="b", end\="c")
(1, 3)

Copy to clipboard

`start` and `end` need not be present in the index; for a monotonic index they are mapped to the appropriate insertion positions:

\>>> idx \= pd.Index(list("bcde"))
\>>> idx.slice\_locs(start\="a", end\="c")
(0, 2)

Copy to clipboard

On this page