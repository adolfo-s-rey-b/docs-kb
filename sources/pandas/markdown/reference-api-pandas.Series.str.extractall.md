[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.extractall.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.extractall.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.extractall.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.extractall.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.extractall.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.extractall.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.extractall.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.extractall.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.extractall.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.extractall.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.extractall.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.extractall.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.extractall.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.extractall.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.extractall[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.extractall.html#pandas-series-str-extractall "Link to this heading")

====================================================================================================================================================================

Series.str.extractall(_pat_, _flags\=0_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L3532-L3608)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.extractall.html#pandas.Series.str.extractall "Link to this definition")

Extract capture groups in the regex pat as columns in DataFrame.

For each subject string in the Series, extract groups from all matches of regular expression pat. When each subject string in the Series has exactly one match, extractall(pat).xs(0, level=’match’) is the same as extract(pat).

Parameters:

**pat**str

Regular expression pattern with capturing groups.

**flags**int, default 0 (no flags)

A `re` module flag, for example `re.IGNORECASE`. These allow to modify regular expression matching for things like case, spaces, etc. Multiple flags can be combined with the bitwise OR operator, for example `re.IGNORECASE | re.MULTILINE`.

Returns:

DataFrame

A `DataFrame` with one row for each match, and one column for each group. Its rows have a `MultiIndex` with first levels that come from the subject `Series`. The last level is named ‘match’ and indexes the matches in each item of the `Series`. Any capture group names in regular expression pat will be used for column names; otherwise capture group numbers will be used.

See also

[`extract`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.extract.html#pandas.Series.str.extract "pandas.Series.str.extract")

Returns first match only (not all matches).

Examples

A pattern with one group will return a DataFrame with one column. Indices with no matches will not appear in the result.

\>>> s \= pd.Series(\["a1a2", "b1", "c1"\], index\=\["A", "B", "C"\])
\>>> s.str.extractall(r"\[ab\](\\d)")
        0
match
A 0      1
  1      2
B 0      1

Copy to clipboard

Capture group names are used for column names of the result.

\>>> s.str.extractall(r"\[ab\](?P<digit>\\d)")
        digit
match
A 0         1
  1         2
B 0         1

Copy to clipboard

A pattern with two groups will return a DataFrame with two columns.

\>>> s.str.extractall(r"(?P<letter>\[ab\])(?P<digit>\\d)")
        letter digit
match
A 0          a     1
  1          a     2
B 0          b     1

Copy to clipboard

Optional groups that do not match are NaN in the result.

\>>> s.str.extractall(r"(?P<letter>\[ab\])?(?P<digit>\\d)")
        letter digit
match
A 0          a     1
  1          a     2
B 0          b     1
C 0        NaN     1

Copy to clipboard

On this page