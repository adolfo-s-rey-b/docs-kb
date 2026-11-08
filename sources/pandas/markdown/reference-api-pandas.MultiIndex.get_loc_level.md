[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_loc_level.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.MultiIndex.get_loc_level.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_loc_level.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.MultiIndex.get_loc_level.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.MultiIndex.get_loc_level.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.MultiIndex.get_loc_level.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.MultiIndex.get_loc_level.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.MultiIndex.get_loc_level.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.MultiIndex.get_loc_level.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.MultiIndex.get_loc_level.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.MultiIndex.get_loc_level.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.MultiIndex.get_loc_level.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.MultiIndex.get_loc_level.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.MultiIndex.get_loc_level.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex.get\_loc\_level[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_loc_level.html#pandas-multiindex-get-loc-level "Link to this heading")

===============================================================================================================================================================================

MultiIndex.get\_loc\_level(_key_, _level\=0_, _drop\_level\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/multi.py#L3768-L3831)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_loc_level.html#pandas.MultiIndex.get_loc_level "Link to this definition")

Get location and sliced index for requested label(s)/level(s).

The get\_loc\_level method is a more advanced form of get\_loc, allowing users to specify not just a label or sequence of labels, but also the level(s) in which to search. This method is useful when you need to isolate particular sections of a MultiIndex, either for further analysis or for slicing and dicing the data. The method provides flexibility in terms of maintaining or dropping levels from the resulting index based on the drop\_level parameter.

Parameters:

**key**label or sequence of labels

The label(s) for which to get the location.

**level**int/level name or list thereof, optional

The level(s) in the MultiIndex to consider. If not provided, defaults to the first level.

**drop\_level**bool, default True

If `False`, the resulting index will not drop any level.

Returns:

tuple

A 2-tuple where the elements :

Element 0: int, slice object or boolean array.

Element 1: The resulting sliced multiindex/index. If the key contains all levels, this will be `None`.

See also

[`MultiIndex.get_loc`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_loc.html#pandas.MultiIndex.get_loc "pandas.MultiIndex.get_loc")

Get location for a label or a tuple of labels.

[`MultiIndex.get_locs`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_locs.html#pandas.MultiIndex.get_locs "pandas.MultiIndex.get_locs")

Get location for a label/slice/list/mask or a sequence of such.

Examples

\>>> mi \= pd.MultiIndex.from\_arrays(\[list("abb"), list("def")\], names\=\["A", "B"\])

Copy to clipboard

\>>> mi.get\_loc\_level("b")
(slice(1, 3, None), Index(\['e', 'f'\], dtype='str', name='B'))

Copy to clipboard

\>>> mi.get\_loc\_level("e", level\="B")
(array(\[False,  True, False\]), Index(\['b'\], dtype='str', name='A'))

Copy to clipboard

\>>> mi.get\_loc\_level(\["b", "e"\])
(1, None)

Copy to clipboard

On this page