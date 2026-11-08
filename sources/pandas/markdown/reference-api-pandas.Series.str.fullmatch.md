[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.fullmatch.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.fullmatch.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.fullmatch.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.fullmatch.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.fullmatch.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.fullmatch.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.fullmatch.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.fullmatch.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.fullmatch.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.fullmatch.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.fullmatch.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.fullmatch.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.fullmatch.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.fullmatch.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.fullmatch[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.fullmatch.html#pandas-series-str-fullmatch "Link to this heading")

=================================================================================================================================================================

Series.str.fullmatch(_pat_, _case\=True_, _flags\=0_, _na\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L1660-L1707)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.fullmatch.html#pandas.Series.str.fullmatch "Link to this definition")

Determine if each string entirely matches a regular expression.

Checks if each string in the Series or Index fully matches the specified regular expression pattern. This function is useful when the requirement is for an entire string to conform to a pattern, such as validating formats like phone numbers or email addresses.

Parameters:

**pat**str

Character sequence or regular expression.

**case**bool, default True

If True, case sensitive.

**flags**int, default 0 (no flags)

Regex module flags, e.g. re.IGNORECASE.

**na**scalar, optional

Fill value for missing values. The default depends on dtype of the array. For the `"str"` dtype, `False` is used. For object dtype, `numpy.nan` is used. For the nullable `StringDtype`, `pandas.NA` is used.

Returns:

Series/Index/array of boolean values

The function returns a Series, Index, or array of boolean values, where True indicates that the entire string matches the regular expression pattern and False indicates that it does not.

See also

[`match`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.match.html#pandas.Series.str.match "pandas.Series.str.match")

Similar, but also returns True when only a _prefix_ of the string matches the regular expression.

[`extract`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.extract.html#pandas.Series.str.extract "pandas.Series.str.extract")

Extract matched groups.

Examples

\>>> ser \= pd.Series(\["cat", "duck", "dove"\])
\>>> ser.str.fullmatch(r"d.+")
0   False
1    True
2    True
dtype: bool

Copy to clipboard

On this page