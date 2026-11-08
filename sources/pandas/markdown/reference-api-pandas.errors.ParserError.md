[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.ParserError.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.errors.ParserError.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.errors.ParserError.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.errors.ParserError.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.errors.ParserError.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.errors.ParserError.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.errors.ParserError.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.errors.ParserError.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.errors.ParserError.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.errors.ParserError.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.errors.ParserError.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.errors.ParserError.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.errors.ParserError.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.errors.ParserError.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.ParserError[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.ParserError.html#pandas-errors-parsererror "Link to this heading")

===========================================================================================================================================================

exception pandas.errors.ParserError[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py#L308-L330)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.ParserError.html#pandas.errors.ParserError "Link to this definition")

Exception that is raised by an error encountered in parsing file contents.

This is a generic error raised for errors encountered when functions like read\_csv or read\_html are parsing contents of a file.

See also

`read_csv`

Read CSV (comma-separated) file into a DataFrame.

`read_html`

Read HTML table into a DataFrame.

Examples

\>>> data \= '''a,b,c
... cat,foo,bar
... dog,foo,"baz'''
\>>> from io import StringIO
\>>> pd.read\_csv(StringIO(data), skipfooter\=1, engine\="python")
Traceback (most recent call last):
ParserError: ',' expected after '"'. Error could possibly be due
to parsing errors in the skipped footer rows

Copy to clipboard

On this page