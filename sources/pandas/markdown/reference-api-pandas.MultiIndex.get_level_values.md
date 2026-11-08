[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_level_values.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex.get\_level\_values[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_level_values.html#pandas-multiindex-get-level-values "Link to this heading")

========================================================================================================================================================================================

MultiIndex.get\_level\_values(_level_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/multi.py#L2077-L2144)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_level_values.html#pandas.MultiIndex.get_level_values "Link to this definition")

Return vector of label values for requested level.

Length of returned vector is equal to the length of the index. The get\_level\_values method is a crucial utility for extracting specific level values from a MultiIndex. This function is particularly useful when working with multi-level data, allowing you to isolate and manipulate individual levels without having to deal with the complexity of the entire MultiIndex structure. It seamlessly handles both integer and string-based level access, providing flexibility in how you can interact with the data. Additionally, this method ensures that the returned Index maintains the integrity of the original data, even when missing values are present, by appropriately casting the result to a suitable data type.

Parameters:

**level**int or str

`level` is either the integer position of the level in the MultiIndex, or the name of the level.

Returns:

Index

Values is a level of this MultiIndex converted to a single [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
 (or subclass thereof).

See also

[`MultiIndex`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex")

A multi-level, or hierarchical, index object for pandas objects.

[`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")

Immutable sequence used for indexing and alignment.

[`MultiIndex.remove_unused_levels`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.remove_unused_levels.html#pandas.MultiIndex.remove_unused_levels "pandas.MultiIndex.remove_unused_levels")

Create new MultiIndex from current that removes unused levels.

Notes

If the level contains missing values, the result may be casted to `float` with missing values specified as `NaN`. This is because the level is converted to a regular `Index`.

Examples

Create a MultiIndex:

\>>> mi \= pd.MultiIndex.from\_arrays((list("abc"), list("def")))
\>>> mi.names \= \["level\_1", "level\_2"\]

Copy to clipboard

Get level values by supplying level as either integer or name:

\>>> mi.get\_level\_values(0)
Index(\['a', 'b', 'c'\], dtype='str', name='level\_1')
\>>> mi.get\_level\_values("level\_2")
Index(\['d', 'e', 'f'\], dtype='str', name='level\_2')

Copy to clipboard

If a level contains missing values, the return type of the level may be cast to `float`.

\>>> pd.MultiIndex.from\_arrays(\[\[1, None, 2\], \[3, 4, 5\]\]).dtypes
level\_0    int64
level\_1    int64
dtype: object
\>>> pd.MultiIndex.from\_arrays(\[\[1, None, 2\], \[3, 4, 5\]\]).get\_level\_values(0)
Index(\[1.0, nan, 2.0\], dtype='float64')

Copy to clipboard

On this page