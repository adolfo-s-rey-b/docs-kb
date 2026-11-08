[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.read_clipboard.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.read_clipboard.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.read_clipboard.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.read_clipboard.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.read_clipboard.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.read_clipboard.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.read_clipboard.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.read_clipboard.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.read_clipboard.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.read_clipboard.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.read_clipboard.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.read_clipboard.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.read_clipboard.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.read_clipboard.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.read\_clipboard[#](https://pandas.pydata.org/docs/reference/api/pandas.read_clipboard.html#pandas-read-clipboard "Link to this heading")

================================================================================================================================================

pandas.read\_clipboard(_sep\='\\\\s+'_, _dtype\_backend\=<no\_default>_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/clipboards.py#L24-L131)
[#](https://pandas.pydata.org/docs/reference/api/pandas.read_clipboard.html#pandas.read_clipboard "Link to this definition")

Read text from clipboard and pass to [`read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")
.

Parses clipboard contents similar to how CSV files are parsed using [`read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")
.

Parameters:

**sep**str, default ‘\\s+’

A string or regex delimiter. The default of `'\\s+'` denotes one or more whitespace characters.

**dtype\_backend**{‘numpy\_nullable’, ‘pyarrow’}

Back-end data type applied to the resultant [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 (still experimental). If not specified, the default behavior is to not use nullable data types. If specified, the behavior is as follows:

*   `"numpy_nullable"`: returns nullable-dtype-backed [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
    
*   `"pyarrow"`: returns pyarrow-backed nullable [`ArrowDtype`](https://pandas.pydata.org/docs/reference/api/pandas.ArrowDtype.html#pandas.ArrowDtype "pandas.ArrowDtype")
     [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
    

Added in version 2.0.

**\*\*kwargs**

See [`read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")
 for the full argument list.

Returns:

DataFrame

A parsed [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 object.

See also

[`DataFrame.to_clipboard`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_clipboard.html#pandas.DataFrame.to_clipboard "pandas.DataFrame.to_clipboard")

Copy object to the system clipboard.

[`read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")

Read a comma-separated values (csv) file into DataFrame.

[`read_fwf`](https://pandas.pydata.org/docs/reference/api/pandas.read_fwf.html#pandas.read_fwf "pandas.read_fwf")

Read a table of fixed-width formatted lines into DataFrame.

Examples

\>>> df \= pd.DataFrame(\[\[1, 2, 3\], \[4, 5, 6\]\], columns\=\["A", "B", "C"\])
\>>> df.to\_clipboard()
\>>> pd.read\_clipboard()
     A  B  C
0    1  2  3
1    4  5  6

Copy to clipboard

On this page