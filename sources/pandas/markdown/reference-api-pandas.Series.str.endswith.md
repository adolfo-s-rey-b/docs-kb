[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.endswith.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.endswith.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.endswith.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.endswith.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.endswith.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.endswith.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.endswith.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.endswith.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.endswith.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.endswith.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.endswith.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.endswith.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.endswith.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.endswith.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.endswith[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.endswith.html#pandas-series-str-endswith "Link to this heading")

==============================================================================================================================================================

Series.str.endswith(_pat_, _na\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L3249-L3309)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.endswith.html#pandas.Series.str.endswith "Link to this definition")

Test if the end of each string element matches a pattern.

Equivalent to [`str.endswith()`](https://docs.python.org/3/builtins/stdtypes.html#str.endswith "(in Python v3.15)")
.

Parameters:

**pat**str or tuple\[str, …\]

Character sequence or tuple of strings. Regular expressions are not accepted.

**na**scalar, optional

Object shown if element tested is not a string. The default depends on dtype of the array. For the `"str"` dtype, `False` is used. For object dtype, `numpy.nan` is used. For the nullable `StringDtype`, `pandas.NA` is used.

Returns:

Series or Index of bool

A Series of booleans indicating whether the given pattern matches the end of each string element.

See also

[`str.endswith`](https://docs.python.org/3/builtins/stdtypes.html#str.endswith "(in Python v3.15)")

Python standard library string method.

[`Series.str.startswith`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.startswith.html#pandas.Series.str.startswith "pandas.Series.str.startswith")

Same as endswith, but tests the start of string.

[`Series.str.contains`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.contains.html#pandas.Series.str.contains "pandas.Series.str.contains")

Tests if string element contains a pattern.

Examples

\>>> s \= pd.Series(\["bat", "bear", "caT", np.nan\])
\>>> s
0     bat
1    bear
2     caT
3     NaN
dtype: str

Copy to clipboard

\>>> s.str.endswith("t")
0     True
1    False
2    False
3    False
dtype: bool

Copy to clipboard

\>>> s.str.endswith(("t", "T"))
0     True
1    False
2     True
3    False
dtype: bool

Copy to clipboard

On this page