[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.HDFStore.select.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.HDFStore.select.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.HDFStore.select.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.HDFStore.select.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.HDFStore.select.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.HDFStore.select.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.HDFStore.select.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.HDFStore.select.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.HDFStore.select.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.HDFStore.select.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.HDFStore.select.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.HDFStore.select.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.HDFStore.select[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select.html#pandas-hdfstore-select "Link to this heading")

==================================================================================================================================================

HDFStore.select(_key_, _where\=None_, _start\=None_, _stop\=None_, _columns\=None_, _iterator\=False_, _chunksize\=None_, _auto\_close\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/pytables.py#L961-L1058)
[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select.html#pandas.HDFStore.select "Link to this definition")

Retrieve pandas object stored in file, optionally based on where criteria.

Warning

Pandas uses PyTables for reading and writing HDF5 files, which allows serializing object-dtype data with pickle when using the “fixed” format. Loading pickled data received from untrusted sources can be unsafe.

See: [https://docs.python.org/3/library/pickle.html](https://docs.python.org/3/library/pickle.html)
 for more.

Parameters:

**key**str

Object being retrieved from file.

**where**list or None

List of Term (or convertible) objects, optional.

**start**int or None

Row number to start selection.

**stop**int, default None

Row number to stop selection.

**columns**list or None

A list of columns that if not None, will limit the return columns.

**iterator**bool or False

Returns an iterator.

**chunksize**int or None

Number or rows to include in iteration, return an iterator.

**auto\_close**bool or False

Should automatically close the store when finished.

Returns:

object

Retrieved object from file.

See also

[`HDFStore.select_as_coordinates`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select_as_coordinates.html#pandas.HDFStore.select_as_coordinates "pandas.HDFStore.select_as_coordinates")

Returns the selection as an index.

[`HDFStore.select_column`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select_column.html#pandas.HDFStore.select_column "pandas.HDFStore.select_column")

Returns a single column from the table.

[`HDFStore.select_as_multiple`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select_as_multiple.html#pandas.HDFStore.select_as_multiple "pandas.HDFStore.select_as_multiple")

Retrieves pandas objects from multiple tables.

Examples

\>>> df \= pd.DataFrame(\[\[1, 2\], \[3, 4\]\], columns\=\["A", "B"\])
\>>> store \= pd.HDFStore("store.h5", "w")
\>>> store.put("data", df)
\>>> store.get("data")
\>>> print(store.keys())
\['/data1', '/data2'\]
\>>> store.select("/data1")
   A  B
0  1  2
1  3  4
\>>> store.select("/data1", where\="columns == A")
   A
0  1
1  3
\>>> store.close()

Copy to clipboard

On this page