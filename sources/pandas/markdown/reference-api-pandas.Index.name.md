[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.name.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.name.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.name.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.name.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.name.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.name.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.name.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.name.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.name.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.name.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.name.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.name.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.name.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.name.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.name[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.name.html#pandas-index-name "Link to this heading")

===================================================================================================================================

property Index.name[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L1836-L1863)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.name.html#pandas.Index.name "Link to this definition")

Return Index or MultiIndex name.

The name (or label) of an Index provides metadata that can be used to identify the axis in DataFrames and Series.

Returns:

label (hashable object)

The name of the Index.

See also

[`Index.set_names`](https://pandas.pydata.org/docs/reference/api/pandas.Index.set_names.html#pandas.Index.set_names "pandas.Index.set_names")

Able to set new names partially and by level.

[`Index.rename`](https://pandas.pydata.org/docs/reference/api/pandas.Index.rename.html#pandas.Index.rename "pandas.Index.rename")

Able to set new names partially and by level.

[`Series.name`](https://pandas.pydata.org/docs/reference/api/pandas.Series.name.html#pandas.Series.name "pandas.Series.name")

Corresponding Series property.

Examples

\>>> idx \= pd.Index(\[1, 2, 3\], name\="x")
\>>> idx
Index(\[1, 2, 3\], dtype='int64',  name='x')
\>>> idx.name
'x'

Copy to clipboard

On this page