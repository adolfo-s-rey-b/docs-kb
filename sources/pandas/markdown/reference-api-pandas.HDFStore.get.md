[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.get.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.HDFStore.get.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.get.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.HDFStore.get.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.HDFStore.get.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.HDFStore.get.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.HDFStore.get.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.HDFStore.get.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.HDFStore.get.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.HDFStore.get.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.HDFStore.get.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.HDFStore.get.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.HDFStore.get.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.HDFStore.get.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.HDFStore.get[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.get.html#pandas-hdfstore-get "Link to this heading")

=========================================================================================================================================

HDFStore.get(_key_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/pytables.py#L923-L959)
[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.get.html#pandas.HDFStore.get "Link to this definition")

Retrieve pandas object stored in file.

The object is read from the HDF5 file and returned as the same type that was stored (e.g., DataFrame, Series).

Parameters:

**key**str

Object to retrieve from file. Raises KeyError if not found.

Returns:

object

Same type as object stored in file.

See also

`HDFStore.get_node`

Returns the node with the key.

[`HDFStore.get_storer`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.get_storer.html#pandas.HDFStore.get_storer "pandas.HDFStore.get_storer")

Returns the storer object for a key.

Examples

\>>> df \= pd.DataFrame(\[\[1, 2\], \[3, 4\]\], columns\=\["A", "B"\])
\>>> store \= pd.HDFStore("store.h5", "w")
\>>> store.put("data", df)
\>>> store.get("data")
\>>> store.close()

Copy to clipboard

On this page