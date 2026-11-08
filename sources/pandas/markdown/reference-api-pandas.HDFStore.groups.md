[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.groups.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.HDFStore.groups[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.groups.html#pandas-hdfstore-groups "Link to this heading")

==================================================================================================================================================

HDFStore.groups()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/pytables.py#L1930-L1971)
[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.groups.html#pandas.HDFStore.groups "Link to this definition")

Return a list of all the top-level nodes.

Each node returned is not a pandas storage object.

Returns:

list

List of objects.

See also

`HDFStore.get_node`

Returns the node with the key.

Examples

\>>> df \= pd.DataFrame(\[\[1, 2\], \[3, 4\]\], columns\=\["A", "B"\])
\>>> store \= pd.HDFStore("store.h5", "w")
\>>> store.put("data", df)
\>>> print(store.groups())
\>>> store.close()
\[/data (Group) ''\
  children := \['axis0' (Array), 'axis1' (Array), 'block0\_values' (Array),\
  'block0\_items' (Array)\]\]

Copy to clipboard

On this page