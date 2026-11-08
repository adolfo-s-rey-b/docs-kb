[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.droplevel.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex.droplevel[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.droplevel.html#pandas-multiindex-droplevel "Link to this heading")

=================================================================================================================================================================

MultiIndex.droplevel(_level\=0_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L2359-L2416)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.droplevel.html#pandas.MultiIndex.droplevel "Link to this definition")

Return index with requested level(s) removed.

If resulting index has only 1 level left, the result will be of Index type, not MultiIndex. The original index is not modified inplace.

Parameters:

**level**int, str, or list-like, default 0

If a string is given, must be the name of a level If list-like, elements must be names or indexes of levels.

Returns:

Index or MultiIndex

Returns an Index or MultiIndex object, depending on the resulting index after removing the requested level(s).

See also

[`Index.dropna`](https://pandas.pydata.org/docs/reference/api/pandas.Index.dropna.html#pandas.Index.dropna "pandas.Index.dropna")

Return Index without NA/NaN values.

Examples

\>>> mi \= pd.MultiIndex.from\_arrays(
...     \[\[1, 2\], \[3, 4\], \[5, 6\]\], names\=\["x", "y", "z"\]
... )
\>>> mi
MultiIndex(\[(1, 3, 5),\
            (2, 4, 6)\],
           names=\['x', 'y', 'z'\])

Copy to clipboard

\>>> mi.droplevel()
MultiIndex(\[(3, 5),\
            (4, 6)\],
           names=\['y', 'z'\])

Copy to clipboard

\>>> mi.droplevel(2)
MultiIndex(\[(1, 3),\
            (2, 4)\],
           names=\['x', 'y'\])

Copy to clipboard

\>>> mi.droplevel("z")
MultiIndex(\[(1, 3),\
            (2, 4)\],
           names=\['x', 'y'\])

Copy to clipboard

\>>> mi.droplevel(\["x", "y"\])
Index(\[5, 6\], dtype='int64', name='z')

Copy to clipboard

On this page