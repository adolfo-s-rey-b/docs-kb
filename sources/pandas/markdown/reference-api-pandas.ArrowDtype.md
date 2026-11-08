[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.ArrowDtype.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.ArrowDtype[#](https://pandas.pydata.org/docs/reference/api/pandas.ArrowDtype.html#pandas-arrowdtype "Link to this heading")

===================================================================================================================================

class pandas.ArrowDtype(_pyarrow\_dtype_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/dtypes.py#L2222-L2591)
[#](https://pandas.pydata.org/docs/reference/api/pandas.ArrowDtype.html#pandas.ArrowDtype "Link to this definition")

An ExtensionDtype for PyArrow data types.

Warning

ArrowDtype is considered experimental. The implementation and parts of the API may change without warning.

While most `dtype` arguments can accept the “string” constructor, e.g. `"int64[pyarrow]"`, ArrowDtype is useful if the data type contains parameters like `pyarrow.timestamp`.

Parameters:

**pyarrow\_dtype**pa.DataType

An instance of a [pyarrow.DataType](https://arrow.apache.org/docs/python/api/datatypes.html#factory-functions)
.

Attributes

|     |     |
| --- | --- |
| **pyarrow\_dtype** |     |

Returns:

ArrowDtype

See also

[`DataFrame.convert_dtypes`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.convert_dtypes.html#pandas.DataFrame.convert_dtypes "pandas.DataFrame.convert_dtypes")

Convert columns to the best possible dtypes.

Examples

\>>> import pyarrow as pa
\>>> pd.ArrowDtype(pa.int64())
int64\[pyarrow\]

Copy to clipboard

Types with parameters must be constructed with ArrowDtype.

\>>> pd.ArrowDtype(pa.timestamp("s", tz\="America/New\_York"))
timestamp\[s, tz=America/New\_York\]\[pyarrow\]
\>>> pd.ArrowDtype(pa.list\_(pa.int64()))
list<item: int64>\[pyarrow\]

Copy to clipboard

On this page