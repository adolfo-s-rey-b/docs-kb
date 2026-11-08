[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.zfill.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.zfill.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.zfill.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.zfill.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.zfill.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.zfill.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.zfill.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.zfill.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.zfill.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.zfill.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.zfill.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.zfill.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.zfill.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.zfill.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.zfill[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.zfill.html#pandas-series-str-zfill "Link to this heading")

=====================================================================================================================================================

Series.str.zfill(_width_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L2220-L2288)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.zfill.html#pandas.Series.str.zfill "Link to this definition")

Pad strings in the Series/Index by prepending ‘0’ characters.

Strings in the Series/Index are padded with ‘0’ characters on the left of the string to reach a total string length width. Strings in the Series/Index with length greater or equal to width are unchanged.

Parameters:

**width**int

Minimum length of resulting string; strings with length less than width be prepended with ‘0’ characters.

Returns:

Series/Index of objects.

A Series or Index where the strings are prepended with ‘0’ characters.

See also

[`Series.str.rjust`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.rjust.html#pandas.Series.str.rjust "pandas.Series.str.rjust")

Fills the left side of strings with an arbitrary character.

[`Series.str.ljust`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.ljust.html#pandas.Series.str.ljust "pandas.Series.str.ljust")

Fills the right side of strings with an arbitrary character.

[`Series.str.pad`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.pad.html#pandas.Series.str.pad "pandas.Series.str.pad")

Fills the specified sides of strings with an arbitrary character.

[`Series.str.center`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.center.html#pandas.Series.str.center "pandas.Series.str.center")

Fills both sides of strings with an arbitrary character.

Notes

Follows the same rules as [`str.zfill()`](https://docs.python.org/3/builtins/stdtypes.html#str.zfill "(in Python v3.15)")
: a leading sign character (‘+’/’-’) is kept at the front of the string and the ‘0’ padding is inserted after it.

Examples

\>>> s \= pd.Series(\["-1", "1", "1000", 10, np.nan\])
\>>> s
0      -1
1       1
2    1000
3      10
4     NaN
dtype: object

Copy to clipboard

Note that `10` and `NaN` are not strings, therefore they are converted to `NaN`. The minus sign in `'-1'` is kept at the front of the string and the ‘0’ padding is inserted after it, the same as [`str.zfill()`](https://docs.python.org/3/builtins/stdtypes.html#str.zfill "(in Python v3.15)")
. `1000` remains unchanged as it is longer than width.

\>>> s.str.zfill(3)
0     -01
1     001
2    1000
3     NaN
4     NaN
dtype: object

Copy to clipboard

On this page