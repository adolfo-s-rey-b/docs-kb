[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.PossibleDataLossError.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.errors.PossibleDataLossError.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.errors.PossibleDataLossError.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.errors.PossibleDataLossError.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.errors.PossibleDataLossError.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.errors.PossibleDataLossError.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.errors.PossibleDataLossError.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.errors.PossibleDataLossError.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.errors.PossibleDataLossError.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.errors.PossibleDataLossError.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.errors.PossibleDataLossError.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.errors.PossibleDataLossError.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.errors.PossibleDataLossError.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.errors.PossibleDataLossError.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.PossibleDataLossError[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.PossibleDataLossError.html#pandas-errors-possibledatalosserror "Link to this heading")

=========================================================================================================================================================================================

exception pandas.errors.PossibleDataLossError[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py#L860-L877)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.PossibleDataLossError.html#pandas.errors.PossibleDataLossError "Link to this definition")

Exception raised when trying to open an HDFStore file when already opened.

This error is triggered when there is a potential risk of data loss due to conflicting operations on an HDFStore file. It serves to prevent unintended overwrites or data corruption by enforcing exclusive access to the file.

See also

`HDFStore`

Dict-like IO interface for storing pandas objects in PyTables.

`HDFStore.open`

Open an HDFStore file in the specified mode.

Examples

\>>> store \= pd.HDFStore("my-store", "a")
\>>> store.open("w")

Copy to clipboard

On this page