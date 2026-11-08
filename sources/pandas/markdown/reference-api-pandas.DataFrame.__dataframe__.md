[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.__dataframe__.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.__dataframe__.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.__dataframe__.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.__dataframe__.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.__dataframe__.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.__dataframe__.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.__dataframe__.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.__dataframe__.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.__dataframe__.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.__dataframe__.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.__dataframe__.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.__dataframe__.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.__dataframe__.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.__dataframe__.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.\_\_dataframe\_\_[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.__dataframe__.html#pandas-dataframe-dataframe "Link to this heading")

==========================================================================================================================================================================

DataFrame.\_\_dataframe\_\_(_nan\_as\_null\=False_, _allow\_copy\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L673-L751)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.__dataframe__.html#pandas.DataFrame.__dataframe__ "Link to this definition")

Return the dataframe interchange object implementing the interchange protocol.

Deprecated since version 3.0.0: The Dataframe Interchange Protocol is deprecated. For dataframe-agnostic code, you may want to look into:

*   [Arrow PyCapsule Interface](https://arrow.apache.org/docs/format/CDataInterface/PyCapsuleInterface.html)
    
*   [Narwhals](https://github.com/narwhals-dev/narwhals)
    

Note

For new development, we highly recommend using the Arrow C Data Interface alongside the Arrow PyCapsule Interface instead of the interchange protocol

Warning

Due to severe implementation issues, we recommend only considering using the interchange protocol in the following cases:

*   converting to pandas: for pandas >= 2.0.3
    
*   converting from pandas: for pandas >= 3.0.0
    

Parameters:

**nan\_as\_null**bool, default False

nan\_as\_null is DEPRECATED and has no effect. Please avoid using it; it will be removed in a future release.

**allow\_copy**bool, default True

Whether to allow memory copying when exporting. If set to False it would cause non-zero-copy exports to fail.

Returns:

DataFrame interchange object

The object which consuming library can use to ingress the dataframe.

See also

[`DataFrame.from_records`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_records.html#pandas.DataFrame.from_records "pandas.DataFrame.from_records")

Constructor from tuples, also record arrays.

[`DataFrame.from_dict`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html#pandas.DataFrame.from_dict "pandas.DataFrame.from_dict")

From dicts of Series, arrays, or dicts.

Notes

Details on the interchange protocol: [https://data-apis.org/dataframe-protocol/latest/index.html](https://data-apis.org/dataframe-protocol/latest/index.html)

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