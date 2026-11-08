[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.ParserWarning.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.errors.ParserWarning.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.errors.ParserWarning.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.errors.ParserWarning.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.errors.ParserWarning.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.errors.ParserWarning.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.errors.ParserWarning.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.errors.ParserWarning.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.errors.ParserWarning.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.errors.ParserWarning.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.errors.ParserWarning.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.errors.ParserWarning.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.errors.ParserWarning.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.errors.ParserWarning.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.ParserWarning[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.ParserWarning.html#pandas-errors-parserwarning "Link to this heading")

=================================================================================================================================================================

exception pandas.errors.ParserWarning[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py#L416-L453)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.ParserWarning.html#pandas.errors.ParserWarning "Link to this definition")

Warning raised when reading a file that doesn’t use the default ‘c’ parser.

Raised by pd.read\_csv and pd.read\_table when it is necessary to change parsers, generally from the default ‘c’ parser to ‘python’.

It happens due to a lack of support or functionality for parsing a particular attribute of a CSV file with the requested engine.

Currently, ‘c’ unsupported options include the following parameters:

1.  sep other than a single character (e.g. regex separators)
    
2.  skipfooter higher than 0
    

The warning can be avoided by adding engine=’python’ as a parameter in pd.read\_csv and pd.read\_table methods.

See also

`pd.read_csv`

Read CSV (comma-separated) file into DataFrame.

`pd.read_table`

Read general delimited file into DataFrame.

Examples

Using a sep in pd.read\_csv other than a single character:

\>>> import io
\>>> csv \= '''a;b;c
...           1;1,8
...           1;2,1'''
\>>> df \= pd.read\_csv(io.StringIO(csv), sep\="\[;,\]")
... \# ParserWarning: Falling back to the 'python' engine...

Copy to clipboard

Adding engine=’python’ to pd.read\_csv removes the Warning:

\>>> df \= pd.read\_csv(io.StringIO(csv), sep\="\[;,\]", engine\="python")

Copy to clipboard

On this page