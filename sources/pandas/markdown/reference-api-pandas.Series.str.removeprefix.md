[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.removeprefix.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.removeprefix.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.removeprefix.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.removeprefix.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.removeprefix.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.removeprefix.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.removeprefix.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.removeprefix.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.removeprefix.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.removeprefix.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.removeprefix.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.removeprefix.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.removeprefix.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.removeprefix.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.removeprefix[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.removeprefix.html#pandas-series-str-removeprefix "Link to this heading")

==========================================================================================================================================================================

Series.str.removeprefix(_prefix_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L2783-L2831)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.removeprefix.html#pandas.Series.str.removeprefix "Link to this definition")

Remove a prefix from an object series.

If the prefix is not present, the original string will be returned.

Parameters:

**prefix**str

Remove the prefix of the string.

Returns:

Series/Index: object

The Series or Index with given prefix removed.

See also

[`Series.str.removesuffix`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.removesuffix.html#pandas.Series.str.removesuffix "pandas.Series.str.removesuffix")

Remove a suffix from an object series.

Examples

\>>> s \= pd.Series(\["str\_foo", "str\_bar", "no\_prefix"\])
\>>> s
0    str\_foo
1    str\_bar
2    no\_prefix
dtype: str
\>>> s.str.removeprefix("str\_")
0    foo
1    bar
2    no\_prefix
dtype: str

Copy to clipboard

\>>> s \= pd.Series(\["foo\_str", "bar\_str", "no\_suffix"\])
\>>> s
0    foo\_str
1    bar\_str
2    no\_suffix
dtype: str
\>>> s.str.removesuffix("\_str")
0    foo
1    bar
2    no\_suffix
dtype: str

Copy to clipboard

On this page