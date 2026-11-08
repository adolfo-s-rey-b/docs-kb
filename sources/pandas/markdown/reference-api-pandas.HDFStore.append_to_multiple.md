[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.append_to_multiple.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.HDFStore.append\_to\_multiple[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.append_to_multiple.html#pandas-hdfstore-append-to-multiple "Link to this heading")

========================================================================================================================================================================================

HDFStore.append\_to\_multiple(_d_, _value_, _selector_, _data\_columns\=None_, _axes\=None_, _dropna\=<no\_default>_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/pytables.py#L1732-L1866)
[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.append_to_multiple.html#pandas.HDFStore.append_to_multiple "Link to this definition")

Append to multiple tables.

Splits `value` column-wise according to `d` and appends each slice to the corresponding table. The `selector` table is the one you query against; its columns are made data\_columns so they can be used in `where` clauses.

Parameters:

**d**dict

Mapping of table\_name to table\_columns. `None` is acceptable as the values for one node (that table will get all the remaining columns).

**value**DataFrame or Series

Pandas object to split across the tables.

**selector**str

Designates the indexable table; all of its columns will be made data\_columns unless `data_columns` is passed, in which case those are used.

**data\_columns**list of str or True, optional

Columns to create as data columns, or `True` to use all columns.

**axes**default None

This parameter is currently not accepted.

**dropna**bool, default False

If `True`, drop rows from all tables if any single row in each table has all NaN.

Deprecated since version 3.1.0: The `dropna` keyword is deprecated and will be removed in a future version. Use [`DataFrame.dropna()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html#pandas.DataFrame.dropna "pandas.DataFrame.dropna")
 before writing instead.

**\*\*kwargs**

Additional keyword arguments forwarded to [`HDFStore.append()`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.append.html#pandas.HDFStore.append "pandas.HDFStore.append")
.

See also

[`HDFStore.append`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.append.html#pandas.HDFStore.append "pandas.HDFStore.append")

Append to a single table.

[`HDFStore.select_as_multiple`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.select_as_multiple.html#pandas.HDFStore.select_as_multiple "pandas.HDFStore.select_as_multiple")

Read from multiple tables with a single `where`.

Examples

\>>> df \= pd.DataFrame({"A": \[1, 2\], "B": \[3, 4\], "C": \[5, 6\]})
\>>> store \= pd.HDFStore("store.h5", "w")
\>>> store.append\_to\_multiple(
...     {"t1": \["A", "B"\], "t2": None}, df, selector\="t1"
... )
\>>> store.close()

Copy to clipboard

On this page