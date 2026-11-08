[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.count.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.count.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.count.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.count.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.count.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.count.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.count.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.count.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.count.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.count.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.count.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.count.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.count.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.count.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.count[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.count.html#pandas-series-str-count "Link to this heading")

=====================================================================================================================================================

Series.str.count(_pat_, _flags\=0_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L3121-L3185)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.count.html#pandas.Series.str.count "Link to this definition")

Count occurrences of pattern in each string of the Series/Index.

This function is used to count the number of times a particular regex pattern is repeated in each of the string elements of the [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
.

Parameters:

**pat**str

Valid regular expression.

**flags**int, default 0, meaning no flags

Flags for the re module. For a complete list, [see here](https://docs.python.org/3/howto/regex.html#compilation-flags)
.

Returns:

Series or Index

Same type as the calling object containing the integer counts.

See also

[`re`](https://docs.python.org/3/library/re.html#module-re "(in Python v3.15)")

Standard library module for regular expressions.

[`str.count`](https://docs.python.org/3/builtins/stdtypes.html#str.count "(in Python v3.15)")

Standard library version, without regular expression support.

Notes

Some characters need to be escaped when passing in pat. eg. `'$'` has a special meaning in regex and must be escaped when finding this literal character.

Examples

\>>> s \= pd.Series(\["A", "B", "Aaba", "Baca", np.nan, "CABA", "cat"\])
\>>> s.str.count("a")
0    0.0
1    0.0
2    2.0
3    2.0
4    NaN
5    0.0
6    1.0
dtype: float64

Copy to clipboard

Escape `'$'` to find the literal dollar sign.

\>>> s \= pd.Series(\["$", "B", "Aab$", "$$ca", "C$B$", "cat"\])
\>>> s.str.count("\\\\$")
0    1
1    0
2    1
3    2
4    2
5    0
dtype: int64

Copy to clipboard

This is also available on Index

\>>> pd.Index(\["A", "A", "Aaba", "cat"\]).str.count("a")
Index(\[0, 0, 2, 1\], dtype='int64')

Copy to clipboard

On this page