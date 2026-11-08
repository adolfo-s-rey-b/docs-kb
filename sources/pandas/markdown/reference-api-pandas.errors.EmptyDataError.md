[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.EmptyDataError.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.errors.EmptyDataError.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.errors.EmptyDataError.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.errors.EmptyDataError.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.errors.EmptyDataError.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.errors.EmptyDataError.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.errors.EmptyDataError.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.errors.EmptyDataError.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.errors.EmptyDataError.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.errors.EmptyDataError.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.errors.EmptyDataError.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.errors.EmptyDataError.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.errors.EmptyDataError.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.errors.EmptyDataError.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.EmptyDataError[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.EmptyDataError.html#pandas-errors-emptydataerror "Link to this heading")

====================================================================================================================================================================

exception pandas.errors.EmptyDataError[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py#L391-L413)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.EmptyDataError.html#pandas.errors.EmptyDataError "Link to this definition")

Exception raised in `pd.read_csv` when empty data or header is encountered.

This error is typically encountered when attempting to read an empty file or an invalid file where no data or headers are present.

See also

`read_csv`

Read a comma-separated values (CSV) file into DataFrame.

`errors.ParserError`

Exception that is raised by an error encountered in parsing file contents.

`errors.DtypeWarning`

Warning raised when reading different dtypes in a column from a file.

Examples

\>>> from io import StringIO
\>>> empty \= StringIO()
\>>> pd.read\_csv(empty)
Traceback (most recent call last):
EmptyDataError: No columns to parse from file

Copy to clipboard

On this page