[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.keys.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.keys.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.keys.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.keys.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.keys.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.keys.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.keys.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.keys.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.keys.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.keys.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.keys.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.keys.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.keys.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.keys.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.keys[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.keys.html#pandas-series-keys "Link to this heading")

======================================================================================================================================

Series.keys()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L1899-L1921)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.keys.html#pandas.Series.keys "Link to this definition")

Return alias for index.

This method provides dictionary-like compatibility by returning the index of the Series, analogous to the keys of a dictionary.

Returns:

Index

Index of the Series.

See also

[`Series.index`](https://pandas.pydata.org/docs/reference/api/pandas.Series.index.html#pandas.Series.index "pandas.Series.index")

The index (axis labels) of the Series.

Examples

\>>> s \= pd.Series(\[1, 2, 3\], index\=\[0, 1, 2\])
\>>> s.keys()
Index(\[0, 1, 2\], dtype='int64')

Copy to clipboard

On this page