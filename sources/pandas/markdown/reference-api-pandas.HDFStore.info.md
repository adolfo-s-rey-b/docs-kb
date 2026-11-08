[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.info.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.HDFStore.info.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.info.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.HDFStore.info.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.HDFStore.info.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.HDFStore.info.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.HDFStore.info.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.HDFStore.info.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.HDFStore.info.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.HDFStore.info.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.HDFStore.info.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.HDFStore.info.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.HDFStore.info.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.HDFStore.info.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.HDFStore.info[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.info.html#pandas-hdfstore-info "Link to this heading")

============================================================================================================================================

HDFStore.info()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/pytables.py#L2188-L2248)
[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.info.html#pandas.HDFStore.info "Link to this definition")

Print detailed information on the store.

The information includes the file path, class name, and a listing of all stored object keys with their types and shapes.

Returns:

str

A String containing the python pandas class name, filepath to the HDF5 file and all the object keys along with their respective dataframe shapes.

See also

[`HDFStore.get_storer`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.get_storer.html#pandas.HDFStore.get_storer "pandas.HDFStore.get_storer")

Returns the storer object for a key.

Examples

\>>> df1 \= pd.DataFrame(\[\[1, 2\], \[3, 4\]\], columns\=\["A", "B"\])
\>>> df2 \= pd.DataFrame(\[\[5, 6\], \[7, 8\]\], columns\=\["C", "D"\])
\>>> store \= pd.HDFStore("store.h5", "w")
\>>> store.put("data1", df1)
\>>> store.put("data2", df2)
\>>> print(store.info())
\>>> store.close()
<class 'pandas.io.pytables.HDFStore'>
File path: store.h5
/data1            frame        (shape->\[2,2\])
/data2            frame        (shape->\[2,2\])

Copy to clipboard

On this page