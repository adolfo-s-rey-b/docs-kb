[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.strip.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.strip[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.strip.html#pandas-series-str-strip "Link to this heading")

=====================================================================================================================================================

Series.str.strip(_to\_strip\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L2545-L2623)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.strip.html#pandas.Series.str.strip "Link to this definition")

Remove leading and trailing characters.

Strip whitespaces (including newlines) or a set of specified characters from each string in the Series/Index from left and right sides. Replaces any non-strings in Series with NaNs. Equivalent to [`str.strip()`](https://docs.python.org/3/builtins/stdtypes.html#str.strip "(in Python v3.15)")
.

Parameters:

**to\_strip**str or None, default None

Specifying the set of characters to be removed. All combinations of this set of characters will be stripped. If None then whitespaces are removed.

Returns:

Series or Index of object

Series or Index with the strings being stripped from the left and right sides.

See also

[`Series.str.strip`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.strip.html#pandas.Series.str.strip "pandas.Series.str.strip")

Remove leading and trailing characters in Series/Index.

[`Series.str.lstrip`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.lstrip.html#pandas.Series.str.lstrip "pandas.Series.str.lstrip")

Remove leading characters in Series/Index.

[`Series.str.rstrip`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.rstrip.html#pandas.Series.str.rstrip "pandas.Series.str.rstrip")

Remove trailing characters in Series/Index.

Examples

\>>> s \= pd.Series(\["1. Ant.  ", "2. Bee!\\n", "3. Cat?\\t", np.nan, 10, True\])
\>>> s
0    1. Ant.
1    2. Bee!\\n
2    3. Cat?\\t
3          NaN
4           10
5         True
dtype: object

Copy to clipboard

\>>> s.str.strip()
0    1. Ant.
1    2. Bee!
2    3. Cat?
3        NaN
4        NaN
5        NaN
dtype: object

Copy to clipboard

\>>> s.str.lstrip("123.")
0    Ant.
1    Bee!\\n
2    Cat?\\t
3       NaN
4       NaN
5       NaN
dtype: object

Copy to clipboard

\>>> s.str.rstrip(".!? \\n\\t")
0    1. Ant
1    2. Bee
2    3. Cat
3       NaN
4       NaN
5       NaN
dtype: object

Copy to clipboard

\>>> s.str.strip("123.!? \\n\\t")
0    Ant
1    Bee
2    Cat
3    NaN
4    NaN
5    NaN
dtype: object

Copy to clipboard

On this page