[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.reorder_levels.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.MultiIndex.reorder_levels.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.reorder_levels.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.MultiIndex.reorder_levels.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.MultiIndex.reorder_levels.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.MultiIndex.reorder_levels.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.MultiIndex.reorder_levels.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.MultiIndex.reorder_levels.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.MultiIndex.reorder_levels.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.MultiIndex.reorder_levels.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.MultiIndex.reorder_levels.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.MultiIndex.reorder_levels.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.MultiIndex.reorder_levels.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.MultiIndex.reorder_levels.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex.reorder\_levels[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.reorder_levels.html#pandas-multiindex-reorder-levels "Link to this heading")

=================================================================================================================================================================================

MultiIndex.reorder\_levels(_order_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/multi.py#L3117-L3165)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.reorder_levels.html#pandas.MultiIndex.reorder_levels "Link to this definition")

Rearrange levels using input order. May not drop or duplicate levels.

reorder\_levels is useful when you need to change the order of levels in a MultiIndex, such as when reordering levels for hierarchical indexing. It maintains the integrity of the MultiIndex, ensuring that all existing levels are present and no levels are duplicated. This method is helpful for aligning the index structure with other data structures or for optimizing the order for specific data operations.

Parameters:

**order**list of int or list of str

List representing new level order. Reference level by number (position) or by key (label).

Returns:

MultiIndex

A new MultiIndex with levels rearranged according to the specified order.

See also

[`MultiIndex.swaplevel`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.swaplevel.html#pandas.MultiIndex.swaplevel "pandas.MultiIndex.swaplevel")

Swap two levels of the MultiIndex.

`MultiIndex.set_names`

Set names for the MultiIndex levels.

[`DataFrame.reorder_levels`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reorder_levels.html#pandas.DataFrame.reorder_levels "pandas.DataFrame.reorder_levels")

Reorder levels in a DataFrame with a MultiIndex.

Examples

\>>> mi \= pd.MultiIndex.from\_arrays(\[\[1, 2\], \[3, 4\]\], names\=\["x", "y"\])
\>>> mi
MultiIndex(\[(1, 3),\
            (2, 4)\],
           names=\['x', 'y'\])

Copy to clipboard

\>>> mi.reorder\_levels(order\=\[1, 0\])
MultiIndex(\[(3, 1),\
            (4, 2)\],
           names=\['y', 'x'\])

Copy to clipboard

\>>> mi.reorder\_levels(order\=\["y", "x"\])
MultiIndex(\[(3, 1),\
            (4, 2)\],
           names=\['y', 'x'\])

Copy to clipboard

On this page