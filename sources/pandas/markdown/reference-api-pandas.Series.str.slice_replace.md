[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.slice_replace.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.slice_replace.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.slice_replace.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.slice_replace.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.slice_replace.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.slice_replace.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.slice_replace.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.slice_replace.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.slice_replace.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.slice_replace.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.slice_replace.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.slice_replace.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.slice_replace.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.slice_replace.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.slice\_replace[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.slice_replace.html#pandas-series-str-slice-replace "Link to this heading")

==============================================================================================================================================================================

Series.str.slice\_replace(_start\=None_, _stop\=None_, _repl\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L2370-L2449)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.slice_replace.html#pandas.Series.str.slice_replace "Link to this definition")

Replace a positional slice of a string with another value.

This function allows replacing specific parts of a string in a Series or Index by specifying start and stop positions. It is useful for modifying substrings in a controlled way, such as updating sections of text based on their positions or patterns.

Parameters:

**start**int, optional

Left index position to use for the slice. If not specified (None), the slice is unbounded on the left, i.e. slice from the start of the string.

**stop**int, optional

Right index position to use for the slice. If not specified (None), the slice is unbounded on the right, i.e. slice until the end of the string.

**repl**str, optional

String for replacement. If not specified (None), the sliced region is replaced with an empty string.

Returns:

Series or Index

Same type as the original object.

See also

[`Series.str.slice`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.slice.html#pandas.Series.str.slice "pandas.Series.str.slice")

Just slicing without replacement.

Examples

\>>> s \= pd.Series(\["a", "ab", "abc", "abdc", "abcde"\])
\>>> s
0        a
1       ab
2      abc
3     abdc
4    abcde
dtype: str

Copy to clipboard

Specify just start, meaning replace start until the end of the string with repl.

\>>> s.str.slice\_replace(1, repl\="X")
0    aX
1    aX
2    aX
3    aX
4    aX
dtype: str

Copy to clipboard

Specify just stop, meaning the start of the string to stop is replaced with repl, and the rest of the string is included.

\>>> s.str.slice\_replace(stop\=2, repl\="X")
0       X
1       X
2      Xc
3     Xdc
4    Xcde
dtype: str

Copy to clipboard

Specify start and stop, meaning the slice from start to stop is replaced with repl. Everything before or after start and stop is included as is.

\>>> s.str.slice\_replace(start\=1, stop\=3, repl\="X")
0      aX
1      aX
2      aX
3     aXc
4    aXde
dtype: str

Copy to clipboard

On this page