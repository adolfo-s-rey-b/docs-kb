[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.remove_unused_levels.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex.remove\_unused\_levels[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.remove_unused_levels.html#pandas-multiindex-remove-unused-levels "Link to this heading")

====================================================================================================================================================================================================

MultiIndex.remove\_unused\_levels()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/multi.py#L2435-L2531)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.remove_unused_levels.html#pandas.MultiIndex.remove_unused_levels "Link to this definition")

Create new MultiIndex from current that removes unused levels.

Unused level(s) means levels that are not expressed in the labels. The resulting MultiIndex will have the same outward appearance, meaning the same .values and ordering. It will also be .equals() to the original.

The remove\_unused\_levels method is useful in cases where you have a MultiIndex with hierarchical levels, but some of these levels are no longer needed due to filtering or subsetting operations. By removing the unused levels, the resulting MultiIndex becomes more compact and efficient, which can improve performance in subsequent operations.

Returns:

MultiIndex

A new MultiIndex with unused levels removed.

See also

[`MultiIndex.droplevel`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.droplevel.html#pandas.MultiIndex.droplevel "pandas.MultiIndex.droplevel")

Remove specified levels from a MultiIndex.

[`MultiIndex.reorder_levels`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.reorder_levels.html#pandas.MultiIndex.reorder_levels "pandas.MultiIndex.reorder_levels")

Rearrange levels of a MultiIndex.

[`MultiIndex.set_levels`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.set_levels.html#pandas.MultiIndex.set_levels "pandas.MultiIndex.set_levels")

Set new levels on a MultiIndex.

Examples

\>>> mi \= pd.MultiIndex.from\_product(\[range(2), list("ab")\])
\>>> mi
MultiIndex(\[(0, 'a'),\
            (0, 'b'),\
            (1, 'a'),\
            (1, 'b')\],
           )

Copy to clipboard

\>>> mi\[2:\]
MultiIndex(\[(1, 'a'),\
            (1, 'b')\],
           )

Copy to clipboard

The 0 from the first level is not represented and can be removed

\>>> mi2 \= mi\[2:\].remove\_unused\_levels()
\>>> mi2.levels
FrozenList(\[\[1\], \['a', 'b'\]\])

Copy to clipboard

On this page