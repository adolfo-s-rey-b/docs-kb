[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.encode.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.encode[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.encode.html#pandas-series-str-encode "Link to this heading")

========================================================================================================================================================

Series.str.encode(_encoding_, _errors\='strict'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L2509-L2543)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.encode.html#pandas.Series.str.encode "Link to this definition")

Encode character string in the Series/Index using indicated encoding.

Equivalent to [`str.encode()`](https://docs.python.org/3/builtins/stdtypes.html#str.encode "(in Python v3.15)")
.

Parameters:

**encoding**str

Specifies the encoding to be used.

**errors**str, optional

Specifies the error handling scheme. Possible values are those supported by [`str.encode()`](https://docs.python.org/3/builtins/stdtypes.html#str.encode "(in Python v3.15)")
.

Returns:

Series/Index of objects

A Series or Index with strings encoded into bytes.

See also

[`Series.str.decode`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.decode.html#pandas.Series.str.decode "pandas.Series.str.decode")

Decodes bytes into strings in a Series/Index.

Examples

\>>> ser \= pd.Series(\["cow", "123", "()"\])
\>>> ser.str.encode(encoding\="ascii")
0     b'cow'
1     b'123'
2      b'()'
dtype: object

Copy to clipboard

On this page