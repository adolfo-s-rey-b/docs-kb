[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.keys.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.HDFStore.keys[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.keys.html#pandas-hdfstore-keys "Link to this heading")

============================================================================================================================================

HDFStore.keys(_include\='pandas'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/pytables.py#L743-L793)
[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.keys.html#pandas.HDFStore.keys "Link to this definition")

Return a list of keys corresponding to objects stored in HDFStore.

The keys are absolute path-names within the HDF5 file hierarchy. By default only pandas objects are returned, but native HDF5 table objects can be included as well.

Parameters:

**include**str, default ‘pandas’

When kind equals ‘pandas’ return pandas objects. When kind equals ‘native’ return native HDF5 Table objects.

Returns:

list

List of ABSOLUTE path-names (e.g. have the leading ‘/’).

Raises:

raises ValueError if kind has an illegal value

See also

[`HDFStore.info`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.info.html#pandas.HDFStore.info "pandas.HDFStore.info")

Prints detailed information on the store.

`HDFStore.get_node`

Returns the node with the key.

[`HDFStore.get_storer`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.get_storer.html#pandas.HDFStore.get_storer "pandas.HDFStore.get_storer")

Returns the storer object for a key.

Examples

\>>> df \= pd.DataFrame(\[\[1, 2\], \[3, 4\]\], columns\=\["A", "B"\])
\>>> store \= pd.HDFStore("store.h5", "w")
\>>> store.put("data", df)
\>>> store.get("data")
\>>> print(store.keys())
\['/data1', '/data2'\]
\>>> store.close()

Copy to clipboard

On this page