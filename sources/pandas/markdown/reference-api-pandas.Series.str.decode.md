[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.decode.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.decode.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.decode.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.decode.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.decode.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.decode.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.decode.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.decode.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.decode.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.decode.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.decode.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.decode.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.decode.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.decode.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.decode[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.decode.html#pandas-series-str-decode "Link to this heading")

========================================================================================================================================================

Series.str.decode(_encoding_, _errors\='strict'_, _dtype\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L2451-L2507)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.decode.html#pandas.Series.str.decode "Link to this definition")

Decode character string in the Series/Index using indicated encoding.

Equivalent to `str.decode()` in python2 and [`bytes.decode()`](https://docs.python.org/3/builtins/stdtypes.html#bytes.decode "(in Python v3.15)")
 in python3.

Parameters:

**encoding**str

Specifies the encoding to be used.

**errors**str, optional

Specifies the error handling scheme. Possible values are those supported by [`bytes.decode()`](https://docs.python.org/3/builtins/stdtypes.html#bytes.decode "(in Python v3.15)")
.

**dtype**str or dtype, optional

The dtype of the result. When not `None`, must be either a string or object dtype. When `None`, the dtype of the result is determined by `pd.options.future.infer_string`.

Added in version 2.3.0.

Returns:

Series or Index

A Series or Index with decoded strings.

See also

[`Series.str.encode`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.encode.html#pandas.Series.str.encode "pandas.Series.str.encode")

Encodes strings into bytes in a Series/Index.

Examples

For Series:

\>>> ser \= pd.Series(\[b"cow", b"123", b"()"\])
\>>> ser.str.decode("ascii")
0   cow
1   123
2   ()
dtype: str

Copy to clipboard

On this page