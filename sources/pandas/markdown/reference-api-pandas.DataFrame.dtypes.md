[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.dtypes[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html#pandas-dataframe-dtypes "Link to this heading")

=====================================================================================================================================================

property DataFrame.dtypes[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L6549-L6589)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html#pandas.DataFrame.dtypes "Link to this definition")

Return the dtypes in the DataFrame.

This returns a Series with the data type of each column. The result’s index is the original DataFrame’s columns. Columns with mixed types are stored with the `object` dtype. See [the User Guide](https://pandas.pydata.org/docs/user_guide/basics.html#basics-dtypes)
 for more.

Returns:

pandas.Series

The data type of each column.

See also

[`Series.dtypes`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dtypes.html#pandas.Series.dtypes "pandas.Series.dtypes")

Return the dtype object of the underlying data.

Examples

\>>> df \= pd.DataFrame(
...     {
...         "float": \[1.0\],
...         "int": \[1\],
...         "datetime": \[pd.Timestamp("20180310")\],
...         "string": \["foo"\],
...     }
... )
\>>> df.dtypes
float              float64
int                  int64
datetime    datetime64\[us\]
string              str
dtype: object

Copy to clipboard

On this page