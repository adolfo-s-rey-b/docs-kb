[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.item.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.item.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.item.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.item.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.item.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.item.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.item.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.item.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.item.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.item.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.item.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.item.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.item.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.item.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.item[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.item.html#pandas-index-item "Link to this heading")

===================================================================================================================================

Index.item()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/base.py#L417-L455)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.item.html#pandas.Index.item "Link to this definition")

Return the first element of the underlying data as a Python scalar.

This method extracts the single element from a length-1 Series or Index and returns it as a native Python scalar type (e.g., `int`, `float`, `str`).

Returns:

scalar

The first element of Series or Index.

Raises:

ValueError

If the data is not length = 1.

See also

[`Index.values`](https://pandas.pydata.org/docs/reference/api/pandas.Index.values.html#pandas.Index.values "pandas.Index.values")

Returns an array representing the data in the Index.

[`Series.head`](https://pandas.pydata.org/docs/reference/api/pandas.Series.head.html#pandas.Series.head "pandas.Series.head")

Returns the first n rows.

Examples

\>>> s \= pd.Series(\[1\])
\>>> s.item()
1

Copy to clipboard

For an index:

\>>> s \= pd.Series(\[1\], index\=\["a"\])
\>>> s.index.item()
'a'

Copy to clipboard

On this page