[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.struct.dtypes.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.struct.dtypes.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.struct.dtypes.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.struct.dtypes.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.struct.dtypes.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.struct.dtypes.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.struct.dtypes.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.struct.dtypes.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.struct.dtypes.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.struct.dtypes.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.struct.dtypes.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.struct.dtypes.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.struct.dtypes.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.struct.dtypes.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.struct.dtypes[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.struct.dtypes.html#pandas-series-struct-dtypes "Link to this heading")

=================================================================================================================================================================

Series.struct.dtypes[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/arrow/accessors.py#L285-L328)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.struct.dtypes.html#pandas.Series.struct.dtypes "Link to this definition")

Return the dtype object of each child field of the struct.

The returned Series is indexed by the field names of the struct and contains the corresponding [`ArrowDtype`](https://pandas.pydata.org/docs/reference/api/pandas.ArrowDtype.html#pandas.ArrowDtype "pandas.ArrowDtype")
 for each field.

Returns:

pandas.Series

The data type of each child field.

See also

[`Series.dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dtype.html#pandas.Series.dtype "pandas.Series.dtype")

Return the dtype object of the underlying data.

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
\>>> s.struct.dtypes
version     int64\[pyarrow\]
project    string\[pyarrow\]
dtype: object

Copy to clipboard

On this page