[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.UInt64Dtype.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.UInt64Dtype.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.UInt64Dtype.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.UInt64Dtype.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.UInt64Dtype.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.UInt64Dtype.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.UInt64Dtype.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.UInt64Dtype.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.UInt64Dtype.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.UInt64Dtype.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.UInt64Dtype.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.UInt64Dtype.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.UInt64Dtype.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.UInt64Dtype.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.UInt64Dtype[#](https://pandas.pydata.org/docs/reference/api/pandas.UInt64Dtype.html#pandas-uint64dtype "Link to this heading")

======================================================================================================================================

class pandas.UInt64Dtype[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/integer.py#L281-L286)
[#](https://pandas.pydata.org/docs/reference/api/pandas.UInt64Dtype.html#pandas.UInt64Dtype "Link to this definition")

An ExtensionDtype for uint64 integer data.

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