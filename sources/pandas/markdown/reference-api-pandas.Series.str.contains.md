[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.contains.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.contains.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.contains.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.contains.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.contains.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.contains.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.contains.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.contains.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.contains.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.contains.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.contains.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.contains.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.contains.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.contains.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.contains[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.contains.html#pandas-series-str-contains "Link to this heading")

==============================================================================================================================================================

Series.str.contains(_pat_, _case\=True_, _flags\=0_, _na\=<no\_default>_, _regex\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L1417-L1552)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.contains.html#pandas.Series.str.contains "Link to this definition")

Test if pattern or regex is contained within a string of a Series or Index.

Return boolean Series or Index based on whether a given pattern or regex is contained within a string of a Series or Index.

Parameters:

**pat**str

Character sequence or regular expression.

**case**bool, default True

If True, case sensitive.

**flags**int, default 0 (no flags)

Flags to pass through to the re module, e.g. re.IGNORECASE.

**na**scalar, optional

Fill value for missing values. The default depends on dtype of the array. For the `"str"` dtype, `False` is used. For object dtype, `numpy.nan` is used. For the nullable `StringDtype`, `pandas.NA` is used.

**regex**bool, default True

If True, assumes the pat is a regular expression.

If False, treats the pat as a literal string.

Returns:

Series or Index of boolean values

A Series or Index of boolean values indicating whether the given pattern is contained within the string of each element of the Series or Index.

See also

[`match`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.match.html#pandas.Series.str.match "pandas.Series.str.match")

Analogous, but stricter, relying on re.match instead of re.search.

[`Series.str.startswith`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.startswith.html#pandas.Series.str.startswith "pandas.Series.str.startswith")

Test if the start of each string element matches a pattern.

[`Series.str.endswith`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.endswith.html#pandas.Series.str.endswith "pandas.Series.str.endswith")

Same as startswith, but tests the end of string.

Examples

Returning a Series of booleans using only a literal pattern.

\>>> s1 \= pd.Series(\["Mouse", "dog", "house and parrot", "23", np.nan\])
\>>> s1.str.contains("og", regex\=False)
0    False
1     True
2    False
3    False
4    False
dtype: bool

Copy to clipboard

Returning an Index of booleans using only a literal pattern.

\>>> ind \= pd.Index(\["Mouse", "dog", "house and parrot", "23.0", np.nan\])
\>>> ind.str.contains("23", regex\=False)
array(\[False, False, False,  True, False\])

Copy to clipboard

Specifying case sensitivity using case.

\>>> s1.str.contains("oG", case\=True, regex\=True)
0    False
1    False
2    False
3    False
4    False
dtype: bool

Copy to clipboard

Returning ‘house’ or ‘dog’ when either expression occurs in a string.

\>>> s1.str.contains("house|dog", regex\=True)
0    False
1     True
2     True
3    False
4    False
dtype: bool

Copy to clipboard

Ignoring case sensitivity using flags with regex.

\>>> import re
\>>> s1.str.contains("PARROT", flags\=re.IGNORECASE, regex\=True)
0    False
1    False
2     True
3    False
4    False
dtype: bool

Copy to clipboard

Returning any digit using regular expression.

\>>> s1.str.contains("\\\\d", regex\=True)
0    False
1    False
2    False
3     True
4    False
dtype: bool

Copy to clipboard

Ensure pat is a not a literal pattern when regex is set to True. Note in the following example one might expect only s2\[1\] and s2\[3\] to return True. However, ‘.0’ as a regex matches any character followed by a 0.

\>>> s2 \= pd.Series(\["40", "40.0", "41", "41.0", "35"\])
\>>> s2.str.contains(".0", regex\=True)
0     True
1     True
2    False
3     True
4    False
dtype: bool

Copy to clipboard

On this page