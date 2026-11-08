[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Int32Dtype.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Int32Dtype[#](https://pandas.pydata.org/docs/reference/api/pandas.Int32Dtype.html#pandas-int32dtype "Link to this heading")

===================================================================================================================================

class pandas.Int32Dtype[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/integer.py#L241-L246)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Int32Dtype.html#pandas.Int32Dtype "Link to this definition")

An ExtensionDtype for int32 integer data.

Uses [`pandas.NA`](https://pandas.pydata.org/docs/reference/api/pandas.NA.html#pandas.NA "pandas.NA")
 as its missing value, rather than `numpy.nan`.

See also

[`Int8Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Int8Dtype.html#pandas.Int8Dtype "pandas.Int8Dtype")

8-bit nullable integer type.

[`Int16Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Int16Dtype.html#pandas.Int16Dtype "pandas.Int16Dtype")

16-bit nullable integer type.

[`Int32Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Int32Dtype.html#pandas.Int32Dtype "pandas.Int32Dtype")

32-bit nullable integer type.

[`Int64Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Int64Dtype.html#pandas.Int64Dtype "pandas.Int64Dtype")

64-bit nullable integer type.

Examples

For Int8Dtype:

\>>> ser \= pd.Series(\[2, pd.NA\], dtype\=pd.Int8Dtype())
\>>> ser.dtype
Int8Dtype()

Copy to clipboard

For Int16Dtype:

\>>> ser \= pd.Series(\[2, pd.NA\], dtype\=pd.Int16Dtype())
\>>> ser.dtype
Int16Dtype()

Copy to clipboard

For Int32Dtype:

\>>> ser \= pd.Series(\[2, pd.NA\], dtype\=pd.Int32Dtype())
\>>> ser.dtype
Int32Dtype()

Copy to clipboard

For Int64Dtype:

\>>> ser \= pd.Series(\[2, pd.NA\], dtype\=pd.Int64Dtype())
\>>> ser.dtype
Int64Dtype()

Copy to clipboard

For UInt8Dtype:

\>>> ser \= pd.Series(\[2, pd.NA\], dtype\=pd.UInt8Dtype())
\>>> ser.dtype
UInt8Dtype()

Copy to clipboard

For UInt16Dtype:

\>>> ser \= pd.Series(\[2, pd.NA\], dtype\=pd.UInt16Dtype())
\>>> ser.dtype
UInt16Dtype()

Copy to clipboard

For UInt32Dtype:

\>>> ser \= pd.Series(\[2, pd.NA\], dtype\=pd.UInt32Dtype())
\>>> ser.dtype
UInt32Dtype()

Copy to clipboard

For UInt64Dtype:

\>>> ser \= pd.Series(\[2, pd.NA\], dtype\=pd.UInt64Dtype())
\>>> ser.dtype
UInt64Dtype()

Copy to clipboard

On this page