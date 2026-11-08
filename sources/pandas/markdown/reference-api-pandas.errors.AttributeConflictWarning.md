[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.AttributeConflictWarning.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.errors.AttributeConflictWarning.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.errors.AttributeConflictWarning.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.errors.AttributeConflictWarning.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.errors.AttributeConflictWarning.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.errors.AttributeConflictWarning.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.errors.AttributeConflictWarning.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.errors.AttributeConflictWarning.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.errors.AttributeConflictWarning.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.errors.AttributeConflictWarning.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.errors.AttributeConflictWarning.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.errors.AttributeConflictWarning.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.errors.AttributeConflictWarning.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.errors.AttributeConflictWarning.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.AttributeConflictWarning[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.AttributeConflictWarning.html#pandas-errors-attributeconflictwarning "Link to this heading")

==================================================================================================================================================================================================

exception pandas.errors.AttributeConflictWarning[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py#L909-L933)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.AttributeConflictWarning.html#pandas.errors.AttributeConflictWarning "Link to this definition")

Warning raised when index attributes conflict when using HDFStore.

Occurs when attempting to append an index with a different name than the existing index on an HDFStore or attempting to append an index with a different frequency than the existing index on an HDFStore.

See also

`HDFStore`

Dict-like IO interface for storing pandas objects in PyTables.

`DataFrame.to_hdf`

Write the contained data to an HDF5 file using HDFStore.

`read_hdf`

Read from an HDF5 file into a DataFrame.

Examples

\>>> idx1 \= pd.Index(\["a", "b"\], name\="name1")
\>>> df1 \= pd.DataFrame(\[\[1, 2\], \[3, 4\]\], index\=idx1)
\>>> df1.to\_hdf("file", "data", "w", append\=True)
\>>> idx2 \= pd.Index(\["c", "d"\], name\="name2")
\>>> df2 \= pd.DataFrame(\[\[5, 6\], \[7, 8\]\], index\=idx2)
\>>> df2.to\_hdf("file", "data", "a", append\=True)
AttributeConflictWarning: the \[index\_name\] attribute of the existing index is
\[name1\] which conflicts with the new \[name2\]...

Copy to clipboard

On this page