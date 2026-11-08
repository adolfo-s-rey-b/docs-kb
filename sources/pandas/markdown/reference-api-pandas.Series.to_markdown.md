[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_markdown.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.to_markdown.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_markdown.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.to_markdown.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.to_markdown.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.to_markdown.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.to_markdown.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.to_markdown.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.to_markdown.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.to_markdown.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.to_markdown.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.to_markdown.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.to_markdown.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.to_markdown.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.to\_markdown[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_markdown.html#pandas-series-to-markdown "Link to this heading")

============================================================================================================================================================

Series.to\_markdown(_buf\=None_, _\*_, _mode\='wt'_, _index\=True_, _storage\_options\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L1780-L1863)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_markdown.html#pandas.Series.to_markdown "Link to this definition")

Print Series in Markdown-friendly format.

Converts the Series to a Markdown table representation using the [tabulate](https://pypi.org/project/tabulate)
 package. The output can be written to a buffer or returned as a string.

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

Series in Markdown-friendly format.

See also

[`Series.to_frame`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_frame.html#pandas.Series.to_frame "pandas.Series.to_frame")

Rrite a text representation of object to the system clipboard.

[`Series.to_latex`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_latex.html#pandas.Series.to_latex "pandas.Series.to_latex")

Render Series to LaTeX-formatted table.

Notes

Requires the [tabulate](https://pypi.org/project/tabulate)
 package.

Examples

\>>> s \= pd.Series(\["elk", "pig", "dog", "quetzal"\], name\="animal")
\>>> print(s.to\_markdown())
|    | animal   |
|---:|:---------|
|  0 | elk      |
|  1 | pig      |
|  2 | dog      |
|  3 | quetzal  |

Copy to clipboard

Output markdown with a tabulate option.

\>>> print(s.to\_markdown(tablefmt\="grid"))
+----+----------+
|    | animal   |
+====+==========+
|  0 | elk      |
+----+----------+
|  1 | pig      |
+----+----------+
|  2 | dog      |
+----+----------+
|  3 | quetzal  |
+----+----------+

Copy to clipboard

On this page