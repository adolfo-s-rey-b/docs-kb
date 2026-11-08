[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.center.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.center.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.center.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.center.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.center.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.center.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.center.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.center.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.center.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.center.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.center.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.center.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.center.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.center.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.center[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.center.html#pandas-series-str-center "Link to this heading")

========================================================================================================================================================

Series.str.center(_width_, _fillchar\=' '_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L2034-L2094)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.center.html#pandas.Series.str.center "Link to this definition")

Pad left and right side of strings in the Series/Index.

Equivalent to [`str.center()`](https://docs.python.org/3/builtins/stdtypes.html#str.center "(in Python v3.15)")
.

Parameters:

**width**int

Minimum width of resulting string; additional characters will be filled with `fillchar`.

**fillchar**str

Additional character for filling, default is whitespace.

Returns:

Series/Index of objects.

A Series or Index where the strings are modified by [`str.center()`](https://docs.python.org/3/builtins/stdtypes.html#str.center "(in Python v3.15)")
.

See also

[`Series.str.rjust`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.rjust.html#pandas.Series.str.rjust "pandas.Series.str.rjust")

Fills the left side of strings with an arbitrary character.

[`Series.str.ljust`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.ljust.html#pandas.Series.str.ljust "pandas.Series.str.ljust")

Fills the right side of strings with an arbitrary character.

[`Series.str.center`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.center.html#pandas.Series.str.center "pandas.Series.str.center")

Fills both sides of strings with an arbitrary character.

[`Series.str.zfill`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.zfill.html#pandas.Series.str.zfill "pandas.Series.str.zfill")

Pad strings in the Series/Index by prepending ‘0’ character.

Examples

For Series.str.center:

\>>> ser \= pd.Series(\["dog", "bird", "mouse"\])
\>>> ser.str.center(8, fillchar\=".")
0   ..dog...
1   ..bird..
2   .mouse..
dtype: str

Copy to clipboard

For Series.str.ljust:

\>>> ser \= pd.Series(\["dog", "bird", "mouse"\])
\>>> ser.str.ljust(8, fillchar\=".")
0   dog.....
1   bird....
2   mouse...
dtype: str

Copy to clipboard

For Series.str.rjust:

\>>> ser \= pd.Series(\["dog", "bird", "mouse"\])
\>>> ser.str.rjust(8, fillchar\=".")
0   .....dog
1   ....bird
2   ...mouse
dtype: str

Copy to clipboard

On this page