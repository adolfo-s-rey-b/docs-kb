[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.copy.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.MultiIndex.copy.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.copy.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.MultiIndex.copy.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.MultiIndex.copy.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.MultiIndex.copy.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.MultiIndex.copy.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.MultiIndex.copy.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.MultiIndex.copy.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.MultiIndex.copy.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.MultiIndex.copy.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.MultiIndex.copy.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.MultiIndex.copy.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.MultiIndex.copy.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex.copy[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.copy.html#pandas-multiindex-copy "Link to this heading")

==================================================================================================================================================

MultiIndex.copy(_names\=None_, _deep\=False_, _name\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/multi.py#L1381-L1460)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.copy.html#pandas.MultiIndex.copy "Link to this definition")

Make a copy of this object. Names, dtype, levels and codes can be passed and will be set on new copy.

The copy method provides a mechanism to create a duplicate of an existing MultiIndex object. This is particularly useful in scenarios where modifications are required on an index, but the original MultiIndex should remain unchanged. By specifying the deep parameter, users can control whether the copy should be a deep or shallow copy, providing flexibility depending on the size and complexity of the MultiIndex.

Parameters:

**names**sequence, optional

Names to set on the new MultiIndex object.

**deep**bool, default False

If False, the new object will be a shallow copy. If True, a deep copy will be attempted. Deep copying can be potentially expensive for large MultiIndex objects.

**name**Label

Kept for compatibility with 1-dimensional Index. Should not be used.

Returns:

MultiIndex

A new MultiIndex object with the specified modifications.

See also

[`MultiIndex.from_arrays`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_arrays.html#pandas.MultiIndex.from_arrays "pandas.MultiIndex.from_arrays")

Convert arrays to MultiIndex.

[`MultiIndex.from_tuples`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_tuples.html#pandas.MultiIndex.from_tuples "pandas.MultiIndex.from_tuples")

Convert list of tuples to MultiIndex.

[`MultiIndex.from_frame`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_frame.html#pandas.MultiIndex.from_frame "pandas.MultiIndex.from_frame")

Convert DataFrame to MultiIndex.

Notes

In most cases, there should be no functional difference from using `deep`, but if `deep` is passed it will attempt to deepcopy. This could be potentially expensive on large MultiIndex objects.

Examples

\>>> mi \= pd.MultiIndex.from\_arrays(\[\["a"\], \["b"\], \["c"\]\])
\>>> mi
MultiIndex(\[('a', 'b', 'c')\],
           )
\>>> mi.copy()
MultiIndex(\[('a', 'b', 'c')\],
           )

Copy to clipboard

On this page