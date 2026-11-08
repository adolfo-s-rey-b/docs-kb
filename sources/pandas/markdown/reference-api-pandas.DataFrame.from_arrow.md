[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_arrow.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.from\_arrow[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_arrow.html#pandas-dataframe-from-arrow "Link to this heading")

==================================================================================================================================================================

classmethod DataFrame.from\_arrow(_data_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L1628-L1689)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_arrow.html#pandas.DataFrame.from_arrow "Link to this definition")

Construct a DataFrame from a tabular Arrow object.

This function accepts any Arrow-compatible tabular object implementing the [Arrow PyCapsule Protocol](https://arrow.apache.org/docs/format/CDataInterface/PyCapsuleInterface.html)
 (i.e. having an `__arrow_c_array__` or `__arrow_c_stream__` method).

This function currently relies on `pyarrow` to convert the tabular object in Arrow format to pandas.

Added in version 3.0.

Parameters:

**data**pyarrow.Table or Arrow-compatible table

Any tabular object implementing the Arrow PyCapsule Protocol (i.e. has an `__arrow_c_array__` or `__arrow_c_stream__` method).

Returns:

DataFrame

See also

[`Series.from_arrow`](https://pandas.pydata.org/docs/reference/api/pandas.Series.from_arrow.html#pandas.Series.from_arrow "pandas.Series.from_arrow")

Construct a Series from an Arrow object.

Examples

\>>> import pyarrow as pa
\>>> table \= pa.table({"a": \[1, 2, 3\], "b": \["x", "y", "z"\]})
\>>> pd.DataFrame.from\_arrow(table)
   a  b
0  1  x
1  2  y
2  3  z

Copy to clipboard

On this page