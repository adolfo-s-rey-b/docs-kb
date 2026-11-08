[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select_column.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.HDFStore.select\_column[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select_column.html#pandas-hdfstore-select-column "Link to this heading")

========================================================================================================================================================================

HDFStore.select\_column(_key_, _column_, _start\=None_, _stop\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/pytables.py#L1119-L1183)
[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select_column.html#pandas.HDFStore.select_column "Link to this definition")

Return a single column from the table.

This is generally only useful to select an indexable.

Warning

Pandas uses PyTables for reading and writing HDF5 files, which allows serializing object-dtype data with pickle when using the “fixed” format. Loading pickled data received from untrusted sources can be unsafe.

See: [https://docs.python.org/3/library/pickle.html](https://docs.python.org/3/library/pickle.html)
 for more.

Parameters:

**key**str

Object being retrieved from file.

**column**str

The column of interest.

**start**int or None, default None

Row number to start selection.

**stop**int or None, default None

Row number to stop selection.

Returns:

Series

A `Series` of the column’s values.

Raises:

KeyError

If the column is not found, or `key` is not a valid store.

ValueError

If the column cannot be extracted individually (not an indexable or a data column).

See also

[`HDFStore.select`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select.html#pandas.HDFStore.select "pandas.HDFStore.select")

Retrieve a stored object, optionally filtered by `where`.

[`HDFStore.select_as_coordinates`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select_as_coordinates.html#pandas.HDFStore.select_as_coordinates "pandas.HDFStore.select_as_coordinates")

Return the matching row coordinates as an Index.

Examples

\>>> df \= pd.DataFrame(\[\[1, 2\], \[3, 4\]\], columns\=\["A", "B"\])
\>>> store \= pd.HDFStore("store.h5", "w")
\>>> store.append(
...     "data", df, format\="table", data\_columns\=\["A"\]
... )
\>>> store.select\_column("data", "A")
\>>> store.close()

Copy to clipboard

On this page