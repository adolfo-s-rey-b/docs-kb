[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select_as_multiple.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.HDFStore.select_as_multiple.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select_as_multiple.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.HDFStore.select_as_multiple.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.HDFStore.select_as_multiple.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.HDFStore.select_as_multiple.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.HDFStore.select_as_multiple.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.HDFStore.select_as_multiple.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.HDFStore.select_as_multiple.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.HDFStore.select_as_multiple.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.HDFStore.select_as_multiple.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.HDFStore.select_as_multiple.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.HDFStore.select_as_multiple.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.HDFStore.select_as_multiple.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.HDFStore.select\_as\_multiple[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select_as_multiple.html#pandas-hdfstore-select-as-multiple "Link to this heading")

========================================================================================================================================================================================

HDFStore.select\_as\_multiple(_keys_, _where\=None_, _selector\=None_, _columns\=None_, _start\=None_, _stop\=None_, _iterator\=False_, _chunksize\=None_, _auto\_close\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/pytables.py#L1185-L1341)
[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select_as_multiple.html#pandas.HDFStore.select_as_multiple "Link to this definition")

Retrieve pandas objects from multiple tables.

Warning

Pandas uses PyTables for reading and writing HDF5 files, which allows serializing object-dtype data with pickle when using the “fixed” format. Loading pickled data received from untrusted sources can be unsafe.

See: [https://docs.python.org/3/library/pickle.html](https://docs.python.org/3/library/pickle.html)
 for more.

Parameters:

**keys**list of str

Names of the tables to read.

**where**list, optional

List of Term (or convertible) objects.

**selector**str, optional

The table to apply the where criteria to. Defaults to `keys[0]`.

**columns**list, optional

Columns to return.

**start**int, optional

Row number to start selection. Applied to each table before `where` is evaluated.

**stop**int, optional

Row number to stop selection. Applied to each table before `where` is evaluated.

**iterator**bool, default False

Return an iterator.

**chunksize**int, optional

Number of rows to include in each iteration; implies `iterator=True`.

**auto\_close**bool, default False

Should automatically close the store when finished.

Returns:

DataFrame or TableIterator

Concatenated result from the selected tables. A `TableIterator` is returned instead when `iterator=True` or `chunksize` is given.

Raises:

KeyError

If `keys` or `selector` is not found, or `keys` is empty.

TypeError

If `keys` is not a list or tuple.

ValueError

If the tables do not all have the same number of rows.

See also

[`HDFStore.append_to_multiple`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.append_to_multiple.html#pandas.HDFStore.append_to_multiple "pandas.HDFStore.append_to_multiple")

Append to multiple tables, splitting a single object into a dict of column groups.

[`HDFStore.select`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select.html#pandas.HDFStore.select "pandas.HDFStore.select")

Retrieve a single stored object.

Examples

\>>> df1 \= pd.DataFrame(\[\[1, 2\], \[3, 4\]\], columns\=\["A", "B"\])
\>>> df2 \= pd.DataFrame(\[\[5, 6\], \[7, 8\]\], columns\=\["C", "D"\])
\>>> store \= pd.HDFStore("store.h5", "w")
\>>> store.append("t1", df1, format\="table")
\>>> store.append("t2", df2, format\="table")
\>>> store.select\_as\_multiple(\["t1", "t2"\])
\>>> store.close()

Copy to clipboard

On this page