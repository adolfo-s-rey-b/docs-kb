[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.extract.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.extract.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.extract.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.extract.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.extract.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.extract.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.extract.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.extract.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.extract.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.extract.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.extract.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.extract.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.extract.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.extract.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.extract[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.extract.html#pandas-series-str-extract "Link to this heading")

===========================================================================================================================================================

Series.str.extract(_pat_, _flags\=0_, _expand\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L3404-L3530)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.extract.html#pandas.Series.str.extract "Link to this definition")

Extract capture groups in the regex pat as columns in a DataFrame.

For each subject string in the Series, extract groups from the first match of regular expression pat.

Parameters:

**pat**str

Regular expression pattern with capturing groups.

**flags**int, default 0 (no flags)

Flags from the `re` module, e.g. `re.IGNORECASE`, that modify regular expression matching for things like case, spaces, etc. For more details, see [`re`](https://docs.python.org/3/library/re.html#module-re "(in Python v3.15)")
.

**expand**bool, default True

If True, return DataFrame with one column per capture group. If False, return a Series/Index if there is one capture group or DataFrame if there are multiple capture groups.

Returns:

DataFrame or Series or Index

A DataFrame with one row for each subject string, and one column for each group. Any capture group names in regular expression pat will be used for column names; otherwise capture group numbers will be used. The dtype of each result column is always object, even when no match is found. If `expand=False` and pat has only one capture group, then return a Series (if subject is a Series) or Index (if subject is an Index).

See also

[`extractall`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.extractall.html#pandas.Series.str.extractall "pandas.Series.str.extractall")

Returns all matches (not just the first match).

Examples

A pattern with two groups will return a DataFrame with two columns. Non-matches will be NaN.

\>>> s \= pd.Series(\["a1", "b2", "c3"\])
\>>> s.str.extract(r"(\[ab\])(\\d)")
    0    1
0    a    1
1    b    2
2  NaN  NaN

Copy to clipboard

A pattern may contain optional groups.

\>>> s.str.extract(r"(\[ab\])?(\\d)")
    0  1
0    a  1
1    b  2
2  NaN  3

Copy to clipboard

Named groups will become column names in the result.

\>>> s.str.extract(r"(?P<letter>\[ab\])(?P<digit>\\d)")
letter digit
0      a     1
1      b     2
2    NaN   NaN

Copy to clipboard

A pattern with one group will return a DataFrame with one column if expand=True.

\>>> s.str.extract(r"\[ab\](\\d)", expand\=True)
     0
0    1
1    2
2  NaN

Copy to clipboard

A pattern with one group will return a Series if expand=False.

\>>> s.str.extract(r"\[ab\](\\d)", expand\=False)
0      1
1      2
2    NaN
dtype: str

Copy to clipboard

On this page