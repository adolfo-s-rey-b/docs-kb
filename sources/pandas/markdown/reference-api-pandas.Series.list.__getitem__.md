[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.list.__getitem__.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.list.__getitem__.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.list.__getitem__.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.list.__getitem__.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.list.__getitem__.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.list.__getitem__.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.list.__getitem__.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.list.__getitem__.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.list.__getitem__.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.list.__getitem__.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.list.__getitem__.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.list.__getitem__.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.list.__getitem__.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.list.__getitem__.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.list.\_\_getitem\_\_[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.list.__getitem__.html#pandas-series-list-getitem "Link to this heading")

==========================================================================================================================================================================

Series.list.\_\_getitem\_\_(_key_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/arrow/accessors.py#L138-L211)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.list.__getitem__.html#pandas.Series.list.__getitem__ "Link to this definition")

Index or slice lists in the Series.

Retrieves elements at the given integer index or slice from each list in the Series, returning a new Series with the selected values.

Parameters:

**key**int | slice

Index or slice of indices to access from each list.

Returns:

pandas.Series

The list at requested index.

See also

`ListAccessor.flatten`

Flatten list values.

Examples

\>>> import pyarrow as pa
\>>> s \= pd.Series(
...     \[\
...         \[1, 2, 3\],\
...         \[3\],\
...     \],
...     dtype\=pd.ArrowDtype(pa.list\_(pa.int64())),
... )
\>>> s.list\[0\]
0    1
1    3
dtype: int64\[pyarrow\]

Copy to clipboard

On this page