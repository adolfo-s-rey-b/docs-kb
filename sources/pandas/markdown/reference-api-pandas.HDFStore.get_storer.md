[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.get_storer.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.HDFStore.get\_storer[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.get_storer.html#pandas-hdfstore-get-storer "Link to this heading")

===============================================================================================================================================================

HDFStore.get\_storer(_key_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/pytables.py#L2053-L2097)
[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.get_storer.html#pandas.HDFStore.get_storer "Link to this definition")

Return the storer object for a key.

The storer is the low-level wrapper around the stored pandas object. It exposes implementation details such as `nrows` (the row count on disk) and `table` (the underlying PyTables `Table`), which can be useful for inspecting a store without loading its data.

Parameters:

**key**str

Object stored in the file.

Returns:

GenericFixed or Table

The storer wrapping the stored object. `Table` instances expose attributes such as `nrows` and `table`.

Raises:

KeyError

If `key` is not in the file.

See also

[`HDFStore.get`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.get.html#pandas.HDFStore.get "pandas.HDFStore.get")

Read the stored object back into pandas.

[`HDFStore.info`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.info.html#pandas.HDFStore.info "pandas.HDFStore.info")

Print a summary of the store’s contents.

Examples

\>>> df \= pd.DataFrame(\[\[1, 2\], \[3, 4\]\], columns\=\["A", "B"\])
\>>> store \= pd.HDFStore("store.h5", "w")
\>>> store.append("data", df, format\="table")
\>>> store.get\_storer("data").nrows
\>>> store.close()

Copy to clipboard

On this page