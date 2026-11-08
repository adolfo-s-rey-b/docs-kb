[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_loc.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.MultiIndex.get_loc.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_loc.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.MultiIndex.get_loc.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.MultiIndex.get_loc.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.MultiIndex.get_loc.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.MultiIndex.get_loc.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.MultiIndex.get_loc.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.MultiIndex.get_loc.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.MultiIndex.get_loc.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.MultiIndex.get_loc.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.MultiIndex.get_loc.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.MultiIndex.get_loc.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.MultiIndex.get_loc.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex.get\_loc[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_loc.html#pandas-multiindex-get-loc "Link to this heading")

============================================================================================================================================================

MultiIndex.get\_loc(_key_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/multi.py#L3633-L3766)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_loc.html#pandas.MultiIndex.get_loc "Link to this definition")

Get location for a label or a tuple of labels. The location is returned as an integer/slice or boolean mask.

This method returns the integer location, slice object, or boolean mask corresponding to the specified key, which can be a single label or a tuple of labels. The key represents a position in the MultiIndex, and the location indicates where the key is found within the index.

Parameters:

**key**label or tuple of labels (one for each level)

A label or tuple of labels that correspond to the levels of the MultiIndex. The key must match the structure of the MultiIndex.

Returns:

int, slice object or boolean mask

If the key is past the lexsort depth, the return may be a boolean mask array, otherwise it is always a slice or int.

See also

[`Index.get_loc`](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_loc.html#pandas.Index.get_loc "pandas.Index.get_loc")

The get\_loc method for (single-level) index.

`MultiIndex.slice_locs`

Get slice location given start label(s) and end label(s).

[`MultiIndex.get_locs`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_locs.html#pandas.MultiIndex.get_locs "pandas.MultiIndex.get_locs")

Get location for a label/slice/list/mask or a sequence of such.

Notes

The key cannot be a slice, list of same-level labels, a boolean mask, or a sequence of such. If you want to use those, use [`MultiIndex.get_locs()`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_locs.html#pandas.MultiIndex.get_locs "pandas.MultiIndex.get_locs")
 instead.

Examples

\>>> mi \= pd.MultiIndex.from\_arrays(\[list("abb"), list("def")\])

Copy to clipboard

\>>> mi.get\_loc("b")
slice(1, 3, None)

Copy to clipboard

\>>> mi.get\_loc(("b", "e"))
1

Copy to clipboard

On this page