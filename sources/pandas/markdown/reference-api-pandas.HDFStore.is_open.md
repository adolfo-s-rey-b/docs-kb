[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.is_open.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.HDFStore.is_open.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.is_open.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.HDFStore.is_open.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.HDFStore.is_open.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.HDFStore.is_open.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.HDFStore.is_open.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.HDFStore.is_open.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.HDFStore.is_open.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.HDFStore.is_open.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.HDFStore.is_open.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.HDFStore.is_open.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.HDFStore.is_open.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.HDFStore.is_open.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.HDFStore.is\_open[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.is_open.html#pandas-hdfstore-is-open "Link to this heading")

======================================================================================================================================================

property HDFStore.is\_open[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/pytables.py#L858-L883)
[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.is_open.html#pandas.HDFStore.is_open "Link to this definition")

Return a boolean indicating whether the file is open.

`HDFStore` instances open the underlying PyTables file in their constructor, but the file can be closed and reopened on the same instance via `close()` and `open()`.

See also

`HDFStore.open`

Open the underlying file in the specified mode.

`HDFStore.close`

Close the underlying PyTables file handle.

Examples

\>>> store \= pd.HDFStore("store.h5", "w")
\>>> store.is\_open
True
\>>> store.close()
\>>> store.is\_open
False

Copy to clipboard

On this page