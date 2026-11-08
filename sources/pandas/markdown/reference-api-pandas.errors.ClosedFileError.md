[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.ClosedFileError.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.ClosedFileError[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.ClosedFileError.html#pandas-errors-closedfileerror "Link to this heading")

=======================================================================================================================================================================

exception pandas.errors.ClosedFileError[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py#L880-L900)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.ClosedFileError.html#pandas.errors.ClosedFileError "Link to this definition")

Exception is raised when trying to perform an operation on a closed HDFStore file.

`ClosedFileError` is specific to operations on `HDFStore` objects. Once an HDFStore is closed, its resources are no longer available, and any further attempt to access data or perform file operations will raise this exception.

See also

`HDFStore.close`

Closes the PyTables file handle.

`HDFStore.open`

Opens the file in the specified mode.

`HDFStore.is_open`

Returns a boolean indicating whether the file is open.

Examples

\>>> store \= pd.HDFStore("my-store", "a")
\>>> store.close()
\>>> store.keys()
... \# ClosedFileError: my-store file is not open!

Copy to clipboard

On this page