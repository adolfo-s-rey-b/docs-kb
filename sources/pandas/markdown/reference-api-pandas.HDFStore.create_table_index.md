[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.create_table_index.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.HDFStore.create\_table\_index[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.create_table_index.html#pandas-hdfstore-create-table-index "Link to this heading")

========================================================================================================================================================================================

HDFStore.create\_table\_index(_key_, _columns\=None_, _optlevel\=None_, _kind\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/pytables.py#L1868-L1928)
[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.create_table_index.html#pandas.HDFStore.create_table_index "Link to this definition")

Create a pytables index on the table.

Indexes are automatically created on indexable axes and `data_columns` during `append`/`put` when `index=True` (the default). This method lets you add or rebuild indexes after the fact, which is **highly encouraged** because it greatly speeds up `select` calls that filter on the indexed dimension.

Parameters:

**key**str

Object stored in the file to index.

**columns**None, bool, or listlike\[str\]

Indicate which columns to create an index on.

*   False : Do not create any indexes.
    
*   True : Create indexes on all columns.
    
*   None : Create indexes on all columns.
    
*   listlike : Create indexes on the given columns.
    

**optlevel**int or None, default None

Optimization level, if None, pytables defaults to 6.

**kind**str or None, default None

Kind of index, if None, pytables defaults to “medium”.

Raises:

TypeError

If the node is not a table.

See also

[`HDFStore.append`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.append.html#pandas.HDFStore.append "pandas.HDFStore.append")

Append data to an existing table; columns are indexed automatically by default.

[`HDFStore.select`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select.html#pandas.HDFStore.select "pandas.HDFStore.select")

Filter on indexed columns for fast retrieval.

Examples

\>>> df \= pd.DataFrame(\[\[1, 2\], \[3, 4\]\], columns\=\["A", "B"\])
\>>> store \= pd.HDFStore("store.h5", "w")
\>>> store.append("data", df, format\="table", index\=False)
\>>> store.create\_table\_index("data", columns\=\["A"\])
\>>> store.close()

Copy to clipboard

On this page