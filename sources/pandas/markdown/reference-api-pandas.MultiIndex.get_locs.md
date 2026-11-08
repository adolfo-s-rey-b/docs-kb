[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_locs.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.MultiIndex.get_locs.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_locs.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.MultiIndex.get_locs.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.MultiIndex.get_locs.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.MultiIndex.get_locs.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.MultiIndex.get_locs.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.MultiIndex.get_locs.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.MultiIndex.get_locs.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.MultiIndex.get_locs.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.MultiIndex.get_locs.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.MultiIndex.get_locs.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.MultiIndex.get_locs.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.MultiIndex.get_locs.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex.get\_locs[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_locs.html#pandas-multiindex-get-locs "Link to this heading")

===============================================================================================================================================================

MultiIndex.get\_locs(_seq_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/multi.py#L4149-L4458)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_locs.html#pandas.MultiIndex.get_locs "Link to this definition")

Get location for a sequence of labels.

This method returns the integer positions in the index that match the given sequence of per-level keys, slices, or boolean masks.

Parameters:

**seq**label, slice, list, mask or a sequence of such

You should use one of the above for each level. If a level should not be used, set it to `slice(None)`.

Returns:

numpy.ndarray

NumPy array of integers suitable for passing to iloc.

See also

[`MultiIndex.get_loc`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_loc.html#pandas.MultiIndex.get_loc "pandas.MultiIndex.get_loc")

Get location for a label or a tuple of labels.

`MultiIndex.slice_locs`

Get slice location given start label(s) and end label(s).

Examples

\>>> mi \= pd.MultiIndex.from\_arrays(\[list("abb"), list("def")\])

Copy to clipboard

\>>> mi.get\_locs("b")
array(\[1, 2\], dtype=int64)

Copy to clipboard

\>>> mi.get\_locs(\[slice(None), \["e", "f"\]\])
array(\[1, 2\], dtype=int64)

Copy to clipboard

\>>> mi.get\_locs(\[\[True, False, True\], slice("e", "f")\])
array(\[2\], dtype=int64)

Copy to clipboard

On this page