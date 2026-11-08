[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_markdown.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.to\_markdown[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_markdown.html#pandas-dataframe-to-markdown "Link to this heading")

=====================================================================================================================================================================

DataFrame.to\_markdown(_buf\=None_, _\*_, _mode\='wt'_, _index\=True_, _storage\_options\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L2753-L2840)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_markdown.html#pandas.DataFrame.to_markdown "Link to this definition")

Print DataFrame in Markdown-friendly format.

Generates a Markdown table representation of the DataFrame using the `tabulate` library. The result can be written to a file or returned as a string for embedding in Markdown documents.

Parameters:

**buf**str, Path or StringIO-like, optional, default None

Buffer to write to. If None, the output is returned as a string.

**mode**str, optional

Mode in which file is opened, “wt” by default.

**index**bool, optional, default True

Add index (row) labels.

**storage\_options**dict, optional

Extra options that make sense for a particular storage connection, e.g. host, port, username, password, etc. For HTTP(S) URLs the key-value pairs are forwarded to `urllib.request.Request` as header options. For other URLs (e.g. starting with “s3://”, and “gcs://”) the key-value pairs are forwarded to `fsspec.open`. Please see `fsspec` and `urllib` for more details, and for more examples on storage options refer [here](https://pandas.pydata.org/docs/user_guide/io.html?highlight=storage_options#reading-writing-remote-files)
.

**\*\*kwargs**

These parameters will be passed to [tabulate](https://pypi.org/project/tabulate)
.

Returns:

str

DataFrame in Markdown-friendly format.

See also

[`DataFrame.to_html`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_html.html#pandas.DataFrame.to_html "pandas.DataFrame.to_html")

Render DataFrame to HTML-formatted table.

[`DataFrame.to_latex`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_latex.html#pandas.DataFrame.to_latex "pandas.DataFrame.to_latex")

Render DataFrame to LaTeX-formatted table.

Notes

Requires the [tabulate](https://pypi.org/project/tabulate)
 package.

Examples

\>>> df \= pd.DataFrame(
...     data\={"animal\_1": \["elk", "pig"\], "animal\_2": \["dog", "quetzal"\]}
... )
\>>> print(df.to\_markdown())
|    | animal\_1   | animal\_2   |
|---:|:-----------|:-----------|
|  0 | elk        | dog        |
|  1 | pig        | quetzal    |

Copy to clipboard

Output markdown with a tabulate option.

\>>> print(df.to\_markdown(tablefmt\="grid"))
+----+------------+------------+
|    | animal\_1   | animal\_2   |
+====+============+============+
|  0 | elk        | dog        |
+----+------------+------------+
|  1 | pig        | quetzal    |
+----+------------+------------+

Copy to clipboard

On this page