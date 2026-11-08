[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.copy.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.HDFStore.copy.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.copy.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.HDFStore.copy.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.HDFStore.copy.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.HDFStore.copy.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.HDFStore.copy.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.HDFStore.copy.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.HDFStore.copy.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.HDFStore.copy.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.HDFStore.copy.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.HDFStore.copy.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.HDFStore.copy.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.HDFStore.copy.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.HDFStore.copy[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.copy.html#pandas-hdfstore-copy "Link to this heading")

============================================================================================================================================

HDFStore.copy(_file_, _mode\='w'_, _propindexes\=True_, _keys\=None_, _complib\=None_, _complevel\=None_, _fletcher32\=False_, _overwrite\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/pytables.py#L2099-L2186)
[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.copy.html#pandas.HDFStore.copy "Link to this definition")

Copy the existing store to a new file, updating in place.

Each object stored in the current `HDFStore` is read and re-written to the destination file, which can be useful for repacking (to reclaim space after deletes), changing compression options, or cloning a subset of keys.

Parameters:

**file**str or path-like

Destination file to write to.

**mode**str, default ‘w’

File mode for the destination, see `HDFStore`.

**propindexes**bool, default True

Restore indexes in copied file.

**keys**list, optional

List of keys to include in the copy (defaults to all).

**complib**str, optional

Compression library, see `HDFStore`.

**complevel**int, optional

Compression level, see `HDFStore`.

**fletcher32**bool, default False

Whether to use the Fletcher32 checksum, see `HDFStore`.

**overwrite**bool, default True

Whether to overwrite (remove and replace) existing nodes in the new store.

Returns:

HDFStore

Open file handle of the new store.

See also

[`HDFStore.put`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.put.html#pandas.HDFStore.put "pandas.HDFStore.put")

Write an object to the store.

[`HDFStore.append`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.append.html#pandas.HDFStore.append "pandas.HDFStore.append")

Append to an existing table.

Examples

\>>> df \= pd.DataFrame(\[\[1, 2\], \[3, 4\]\], columns\=\["A", "B"\])
\>>> store \= pd.HDFStore("store.h5", "w")
\>>> store.put("data", df)
\>>> new\_store \= store.copy("store\_copy.h5")
\>>> new\_store.close()
\>>> store.close()

Copy to clipboard

On this page