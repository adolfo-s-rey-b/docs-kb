[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.list.flatten.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.list.flatten.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.list.flatten.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.list.flatten.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.list.flatten.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.list.flatten.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.list.flatten.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.list.flatten.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.list.flatten.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.list.flatten.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.list.flatten.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.list.flatten.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.list.flatten.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.list.flatten.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.list.flatten[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.list.flatten.html#pandas-series-list-flatten "Link to this heading")

==============================================================================================================================================================

Series.list.flatten()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/arrow/accessors.py#L216-L260)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.list.flatten.html#pandas.Series.list.flatten "Link to this definition")

Flatten list values.

Each list element is expanded into separate rows, preserving the original index. The resulting Series may have a longer length than the original if lists contain more than one element.

Returns:

pandas.Series

The data from all lists in the series flattened.

See also

`ListAccessor.__getitem__`

Index or slice values in the Series.

Examples

\>>> import pyarrow as pa
\>>> s \= pd.Series(
...     \[\
...         \[1, 2, 3\],\
...         \[3\],\
...     \],
...     dtype\=pd.ArrowDtype(pa.list\_(pa.int64())),
... )
\>>> s.list.flatten()
0    1
0    2
0    3
1    3
dtype: int64\[pyarrow\]

Copy to clipboard

On this page