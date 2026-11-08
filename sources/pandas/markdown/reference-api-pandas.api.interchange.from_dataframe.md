[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.interchange.from_dataframe.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.interchange.from_dataframe.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.interchange.from_dataframe.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.interchange.from_dataframe.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.interchange.from_dataframe.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.interchange.from_dataframe.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.interchange.from_dataframe.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.interchange.from_dataframe.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.interchange.from_dataframe.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.interchange.from_dataframe.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.interchange.from_dataframe.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.interchange.from_dataframe.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.interchange.from_dataframe.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.interchange.from_dataframe.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.interchange.from\_dataframe[#](https://pandas.pydata.org/docs/reference/api/pandas.api.interchange.from_dataframe.html#pandas-api-interchange-from-dataframe "Link to this heading")

================================================================================================================================================================================================

pandas.api.interchange.from\_dataframe(_df_, _allow\_copy\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/interchange/from_dataframe.py#L41-L139)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.interchange.from_dataframe.html#pandas.api.interchange.from_dataframe "Link to this definition")

Build a `pd.DataFrame` from any DataFrame supporting the interchange protocol.

Note

For new development, we highly recommend using the Arrow C Data Interface alongside the Arrow PyCapsule Interface instead of the interchange protocol. From pandas 3.0 onwards, from\_dataframe uses the PyCapsule Interface, only falling back to the interchange protocol if that fails.

From pandas 4.0 onwards, that fallback will no longer be available and only the PyCapsule Interface will be used.

Warning

Due to severe implementation issues, we recommend only considering using the interchange protocol in the following cases:

*   converting to pandas: for pandas >= 2.0.3
    
*   converting from pandas: for pandas >= 3.0.0
    

Parameters:

**df**ArrowStreamExportable or DataFrameXchg

Object supporting the Arrow PyCapsule Interface, i.e. an \_\_arrow\_c\_stream\_\_ method (`ArrowStreamExportable`), or an object supporting the interchange protocol, i.e. a \_\_dataframe\_\_ method (`DataFrameXchg`).

**allow\_copy**bool, default: True

Whether to allow copying the memory to perform the conversion (if false then zero-copy approach is requested).

Returns:

pd.DataFrame

A pandas DataFrame built from the provided interchange protocol object.

See also

`pd.DataFrame`

DataFrame class which can be created from various input data formats, including objects that support the interchange protocol.

Examples

\>>> df\_not\_necessarily\_pandas \= pd.DataFrame({"A": \[1, 2\], "B": \[3, 4\]})
\>>> interchange\_object \= df\_not\_necessarily\_pandas.\_\_dataframe\_\_()
\>>> interchange\_object.column\_names()
Index(\['A', 'B'\], dtype='str')
\>>> df\_pandas \= pd.api.interchange.from\_dataframe(
...     interchange\_object.select\_columns\_by\_name(\["A"\])
... )
\>>> df\_pandas
     A
0    1
1    2

Copy to clipboard

These methods (`column_names`, `select_columns_by_name`) should work for any dataframe library which implements the interchange protocol.

On this page