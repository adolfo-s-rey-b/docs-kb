[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.struct.explode.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.struct.explode.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.struct.explode.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.struct.explode.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.struct.explode.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.struct.explode.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.struct.explode.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.struct.explode.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.struct.explode.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.struct.explode.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.struct.explode.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.struct.explode.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.struct.explode.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.struct.explode.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.struct.explode[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.struct.explode.html#pandas-series-struct-explode "Link to this heading")

====================================================================================================================================================================

Series.struct.explode()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/arrow/accessors.py#L495-L536)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.struct.explode.html#pandas.Series.struct.explode "Link to this definition")

Extract all child fields of a struct as a DataFrame.

Each child field of the struct becomes a column in the resulting DataFrame, with column names matching the struct field names.

Returns:

pandas.DataFrame

The data corresponding to all child fields.

See also

[`Series.struct.field`](https://pandas.pydata.org/docs/reference/api/pandas.Series.struct.field.html#pandas.Series.struct.field "pandas.Series.struct.field")

Return a single child field as a Series.

Examples

\>>> import pyarrow as pa
\>>> s \= pd.Series(
...     \[\
...         {"version": 1, "project": "pandas"},\
...         {"version": 2, "project": "pandas"},\
...         {"version": 1, "project": "numpy"},\
...     \],
...     dtype\=pd.ArrowDtype(
...         pa.struct(\[("version", pa.int64()), ("project", pa.string())\])
...     ),
... )

Copy to clipboard

\>>> s.struct.explode()
   version project
0        1  pandas
1        2  pandas
2        1   numpy

Copy to clipboard

On this page