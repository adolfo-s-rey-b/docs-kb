[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select_as_coordinates.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.HDFStore.select\_as\_coordinates[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select_as_coordinates.html#pandas-hdfstore-select-as-coordinates "Link to this heading")

=================================================================================================================================================================================================

HDFStore.select\_as\_coordinates(_key_, _where\=None_, _start\=None_, _stop\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/pytables.py#L1060-L1117)
[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select_as_coordinates.html#pandas.HDFStore.select_as_coordinates "Link to this definition")

Return the selection as an Index.

Warning

Pandas uses PyTables for reading and writing HDF5 files, which allows serializing object-dtype data with pickle when using the “fixed” format. Loading pickled data received from untrusted sources can be unsafe.

See: [https://docs.python.org/3/library/pickle.html](https://docs.python.org/3/library/pickle.html)
 for more.

Parameters:

**key**str

Object being retrieved from file.

**where**list of Term (or convertible) objects, optional

Conditions to apply to the selection. `start` and `stop` are applied to the table before `where`.

**start**int, optional

Row number to start selection.

**stop**int, optional

Row number to stop selection.

Returns:

Index

Integer positions of the matching rows; can be passed as `where` to a subsequent `select`.

See also

[`HDFStore.select`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select.html#pandas.HDFStore.select "pandas.HDFStore.select")

Retrieve a stored object, optionally filtered by `where`.

[`HDFStore.select_as_multiple`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select_as_multiple.html#pandas.HDFStore.select_as_multiple "pandas.HDFStore.select_as_multiple")

Retrieve pandas objects from multiple tables.

Examples

\>>> df \= pd.DataFrame(\[\[1, 2\], \[3, 4\]\], columns\=\["A", "B"\])
\>>> store \= pd.HDFStore("store.h5", "w")
\>>> store.append(
...     "data", df, format\="table", data\_columns\=\["A"\]
... )
\>>> store.select\_as\_coordinates("data", "A>1")
\>>> store.close()

Copy to clipboard

On this page