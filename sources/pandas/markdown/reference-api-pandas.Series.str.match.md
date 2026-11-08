[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.match.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.match.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.match.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.match.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.match.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.match.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.match.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.match.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.match.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.match.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.match.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.match.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.match.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.match.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.match[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.match.html#pandas-series-str-match "Link to this heading")

=====================================================================================================================================================

Series.str.match(_pat_, _case\=<no\_default>_, _flags\=<no\_default>_, _na\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L1554-L1658)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.match.html#pandas.Series.str.match "Link to this definition")

Determine if each string starts with a match of a regular expression.

Determines whether each string in the Series or Index starts with a match to a specified regular expression. This function is especially useful for validating prefixes, such as ensuring that codes, tags, or identifiers begin with a specific pattern.

Parameters:

**pat**str or compiled regex

Character sequence or regular expression.

**case**bool, default True

If True, case sensitive.

**flags**int, default 0 (no flags)

Regex module flags, e.g. re.IGNORECASE.

**na**scalar, optional

Fill value for missing values. The default depends on dtype of the array. For the `"str"` dtype, `False` is used. For object dtype, `numpy.nan` is used. For the nullable `StringDtype`, `pandas.NA` is used.

Returns:

Series/Index/array of boolean values

A Series, Index, or array of boolean values indicating whether the start of each string matches the pattern. The result will be of the same type as the input.

See also

[`fullmatch`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.fullmatch.html#pandas.Series.str.fullmatch "pandas.Series.str.fullmatch")

Stricter matching that requires the entire string to match.

[`contains`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.contains.html#pandas.Series.str.contains "pandas.Series.str.contains")

Analogous, but less strict, relying on re.search instead of re.match.

[`extract`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.extract.html#pandas.Series.str.extract "pandas.Series.str.extract")

Extract matched groups.

Examples

\>>> ser \= pd.Series(\["horse", "eagle", "donkey"\])
\>>> ser.str.match("e")
0   False
1   True
2   False
dtype: bool

Copy to clipboard

On this page