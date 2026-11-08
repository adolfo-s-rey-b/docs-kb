[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.struct.field.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.struct.field.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.struct.field.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.struct.field.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.struct.field.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.struct.field.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.struct.field.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.struct.field.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.struct.field.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.struct.field.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.struct.field.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.struct.field.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.struct.field.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.struct.field.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.struct.field[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.struct.field.html#pandas-series-struct-field "Link to this heading")

==============================================================================================================================================================

Series.struct.field(_name\_or\_index_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/arrow/accessors.py#L330-L493)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.struct.field.html#pandas.Series.struct.field "Link to this definition")

Extract a child field of a struct as a Series.

This method accesses individual child fields of an Arrow struct column by name, index, expression, or a list of those for nested structs.

Parameters:

**name\_or\_index**str | bytes | int | expression | list

Name or index of the child field to extract.

For list-like inputs, this will index into a nested struct.

Returns:

pandas.Series

The data corresponding to the selected child field.

See also

[`Series.struct.explode`](https://pandas.pydata.org/docs/reference/api/pandas.Series.struct.explode.html#pandas.Series.struct.explode "pandas.Series.struct.explode")

Return all child fields as a DataFrame.

Notes

The name of the resulting Series will be set using the following rules:

*   For string, bytes, or integer name\_or\_index (or a list of these, for a nested selection), the Series name is set to the selected field’s name.
    
*   For a `pyarrow.compute.Expression`, this is set to the string form of the expression.
    
*   For list-like name\_or\_index, the name will be set to the name of the final field selected.
    

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

Extract by field name.

\>>> s.struct.field("project")
0    pandas
1    pandas
2     numpy
Name: project, dtype: string\[pyarrow\]

Copy to clipboard

Extract by field index.

\>>> s.struct.field(0)
0    1
1    2
2    1
Name: version, dtype: int64\[pyarrow\]

Copy to clipboard

Or an expression

\>>> import pyarrow.compute as pc
\>>> s.struct.field(pc.field("project"))
0    pandas
1    pandas
2     numpy
Name: project, dtype: string\[pyarrow\]

Copy to clipboard

For nested struct types, you can pass a list of values to index multiple levels:

\>>> version\_type \= pa.struct(
...     \[\
...         ("major", pa.int64()),\
...         ("minor", pa.int64()),\
...     \]
... )
\>>> s \= pd.Series(
...     \[\
...         {"version": {"major": 1, "minor": 5}, "project": "pandas"},\
...         {"version": {"major": 2, "minor": 1}, "project": "pandas"},\
...         {"version": {"major": 1, "minor": 26}, "project": "numpy"},\
...     \],
...     dtype\=pd.ArrowDtype(
...         pa.struct(\[("version", version\_type), ("project", pa.string())\])
...     ),
... )
\>>> s.struct.field(\["version", "minor"\])
0     5
1     1
2    26
Name: minor, dtype: int64\[pyarrow\]
\>>> s.struct.field(\[0, 0\])
0    1
1    2
2    1
Name: major, dtype: int64\[pyarrow\]

Copy to clipboard

On this page