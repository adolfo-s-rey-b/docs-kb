[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.walk.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.HDFStore.walk[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.walk.html#pandas-hdfstore-walk "Link to this heading")

============================================================================================================================================

HDFStore.walk(_where\='/'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/pytables.py#L1973-L2035)
[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.walk.html#pandas.HDFStore.walk "Link to this definition")

Walk the pytables group hierarchy for pandas objects.

This generator will yield the group path, subgroups and pandas object names for each group.

Any non-pandas PyTables objects that are not a group will be ignored.

The where group itself is listed first (preorder), then each of its child groups (following an alphanumerical order) is also traversed, following the same procedure.

Parameters:

**where**str, default “/”

Group where to start walking.

Yields:

**path**str

Full path to a group (without trailing ‘/’).

**groups**list

Names (strings) of the groups contained in path.

**leaves**list

Names (strings) of the pandas objects contained in path.

See also

[`HDFStore.info`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.info.html#pandas.HDFStore.info "pandas.HDFStore.info")

Prints detailed information on the store.

Examples

\>>> df1 \= pd.DataFrame(\[\[1, 2\], \[3, 4\]\], columns\=\["A", "B"\])
\>>> store \= pd.HDFStore("store.h5", "w")
\>>> store.put("data", df1, format\="table")
\>>> df2 \= pd.DataFrame(\[\[5, 6\], \[7, 8\]\], columns\=\["A", "B"\])
\>>> store.append("data", df2)
\>>> store.close()
\>>> for group in store.walk():
...     print(group)
\>>> store.close()

Copy to clipboard

On this page