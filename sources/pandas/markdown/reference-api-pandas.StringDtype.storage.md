[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.StringDtype.storage.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.StringDtype.storage[#](https://pandas.pydata.org/docs/reference/api/pandas.StringDtype.storage.html#pandas-stringdtype-storage "Link to this heading")

==============================================================================================================================================================

property StringDtype.storage[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/string_.py#L173-L192)
[#](https://pandas.pydata.org/docs/reference/api/pandas.StringDtype.storage.html#pandas.StringDtype.storage "Link to this definition")

The storage backend for this dtype.

Can be either “pyarrow” or “python”.

See also

[`StringDtype.na_value`](https://pandas.pydata.org/docs/reference/api/pandas.StringDtype.na_value.html#pandas.StringDtype.na_value "pandas.StringDtype.na_value")

The missing value for this dtype.

Examples

\>>> ser \= pd.Series(\["a", "b"\])
\>>> ser.dtype
<StringDtype(na\_value=nan)>
\>>> ser.dtype.storage
'pyarrow'

Copy to clipboard

On this page