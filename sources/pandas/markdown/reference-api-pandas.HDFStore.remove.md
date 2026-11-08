[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.remove.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.HDFStore.remove[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.remove.html#pandas-hdfstore-remove "Link to this heading")

==================================================================================================================================================

HDFStore.remove(_key_, _where\=None_, _start\=None_, _stop\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/pytables.py#L1495-L1570)
[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.remove.html#pandas.HDFStore.remove "Link to this definition")

Remove pandas object partially by specifying the where condition.

If `where` is not provided, the entire object stored at `key` (and any of its child nodes) is removed. When `where` is given, only matching rows are deleted, which requires the object to be in `table` format.

Parameters:

**key**str

Node to remove or delete rows from.

**where**list of Term (or convertible) objects, optional

Conditions selecting which rows to remove.

**start**int, optional

Row number to start selection.

**stop**int, optional

Row number to stop selection.

Returns:

int or None

Number of rows removed (or `None` if the object is not a Table).

Raises:

KeyError

If `key` is not a valid store.

See also

[`HDFStore.append`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.append.html#pandas.HDFStore.append "pandas.HDFStore.append")

Append data to an existing table.

[`HDFStore.put`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.put.html#pandas.HDFStore.put "pandas.HDFStore.put")

Store an object in the file.

Examples

\>>> df \= pd.DataFrame(\[\[1, 2\], \[3, 4\]\], columns\=\["A", "B"\])
\>>> store \= pd.HDFStore("store.h5", "w")
\>>> store.put("data", df)
\>>> store.remove("data")
\>>> store.close()

Copy to clipboard

On this page