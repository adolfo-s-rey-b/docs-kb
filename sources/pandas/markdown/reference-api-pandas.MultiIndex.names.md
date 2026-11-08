[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.names.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.MultiIndex.names.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.names.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.MultiIndex.names.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.MultiIndex.names.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.MultiIndex.names.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.MultiIndex.names.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.MultiIndex.names.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.MultiIndex.names.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.MultiIndex.names.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.MultiIndex.names.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.MultiIndex.names.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.MultiIndex.names.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.MultiIndex.names.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex.names[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.names.html#pandas-multiindex-names "Link to this heading")

=====================================================================================================================================================

property MultiIndex.names[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/multi.py#L1718-L1719)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.names.html#pandas.MultiIndex.names "Link to this definition")

Names of levels in MultiIndex.

This attribute provides access to the names of the levels in a MultiIndex. The names are stored as a FrozenList, which is an immutable list-like container. Each name corresponds to a level in the MultiIndex, and can be used to identify or manipulate the levels individually.

See also

`MultiIndex.set_names`

Set Index or MultiIndex name.

`MultiIndex.rename`

Rename specific levels in a MultiIndex.

[`Index.names`](https://pandas.pydata.org/docs/reference/api/pandas.Index.names.html#pandas.Index.names "pandas.Index.names")

Get names on index.

Examples

\>>> mi \= pd.MultiIndex.from\_arrays(
...     \[\[1, 2\], \[3, 4\], \[5, 6\]\], names\=\['x', 'y', 'z'\]
... )
\>>> mi
MultiIndex(\[(1, 3, 5),\
            (2, 4, 6)\],
           names=\['x', 'y', 'z'\])
\>>> mi.names
FrozenList(\['x', 'y', 'z'\])

Copy to clipboard

On this page