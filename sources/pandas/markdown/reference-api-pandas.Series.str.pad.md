[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.pad.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.pad.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.pad.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.pad.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.pad.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.pad.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.pad.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.pad.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.pad.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.pad.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.pad.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.pad.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.pad.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.pad.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.pad[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.pad.html#pandas-series-str-pad "Link to this heading")

===============================================================================================================================================

Series.str.pad(_width_, _side\='left'_, _fillchar\=' '_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L1955-L2032)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.pad.html#pandas.Series.str.pad "Link to this definition")

Pad strings in the Series/Index up to width.

This function pads strings in a Series or Index to a specified width, filling the extra space with a character of your choice. It provides flexibility in positioning the padding, allowing it to be added to the left, right, or both sides. This is useful for formatting strings to align text or ensure consistent string lengths in data processing.

Parameters:

**width**int

Minimum width of resulting string; additional characters will be filled with character defined in fillchar.

**side**{‘left’, ‘right’, ‘both’}, default ‘left’

Side from which to fill resulting string.

**fillchar**str, default ‘ ‘

Additional character for filling, default is whitespace.

Returns:

Series or Index of object

Returns Series or Index with minimum number of char in object.

See also

[`Series.str.rjust`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.rjust.html#pandas.Series.str.rjust "pandas.Series.str.rjust")

Fills the left side of strings with an arbitrary character. Equivalent to `Series.str.pad(side='left')`.

[`Series.str.ljust`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.ljust.html#pandas.Series.str.ljust "pandas.Series.str.ljust")

Fills the right side of strings with an arbitrary character. Equivalent to `Series.str.pad(side='right')`.

[`Series.str.center`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.center.html#pandas.Series.str.center "pandas.Series.str.center")

Fills both sides of strings with an arbitrary character. Equivalent to `Series.str.pad(side='both')`.

[`Series.str.zfill`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.zfill.html#pandas.Series.str.zfill "pandas.Series.str.zfill")

Pad strings in the Series/Index by prepending ‘0’ character. Equivalent to `Series.str.pad(side='left', fillchar='0')`.

Examples

\>>> s \= pd.Series(\["caribou", "tiger"\])
\>>> s
0    caribou
1      tiger
dtype: str

Copy to clipboard

\>>> s.str.pad(width\=10)
0       caribou
1         tiger
dtype: str

Copy to clipboard

\>>> s.str.pad(width\=10, side\="right", fillchar\="-")
0    caribou---
1    tiger-----
dtype: str

Copy to clipboard

\>>> s.str.pad(width\=10, side\="both", fillchar\="-")
0    -caribou--
1    --tiger---
dtype: str

Copy to clipboard

On this page