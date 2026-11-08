[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.findall.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.findall.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.findall.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.findall.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.findall.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.findall.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.findall.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.findall.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.findall.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.findall.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.findall.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.findall.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.findall.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.findall.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.findall[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.findall.html#pandas-series-str-findall "Link to this heading")

===========================================================================================================================================================

Series.str.findall(_pat_, _flags\=0_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L3311-L3402)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.findall.html#pandas.Series.str.findall "Link to this definition")

Find all occurrences of pattern or regular expression in the Series/Index.

Equivalent to applying [`re.findall()`](https://docs.python.org/3/library/re.html#re.findall "(in Python v3.15)")
 to all the elements in the Series/Index.

Parameters:

**pat**str

Pattern or regular expression.

**flags**int, default 0

Flags from `re` module, e.g. re.IGNORECASE (default is 0, which means no flags).

Returns:

Series/Index of lists of strings

All non-overlapping matches of pattern or regular expression in each string of this Series/Index.

See also

[`count`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.count.html#pandas.Series.str.count "pandas.Series.str.count")

Count occurrences of pattern or regular expression in each string of the Series/Index.

[`extractall`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.extractall.html#pandas.Series.str.extractall "pandas.Series.str.extractall")

For each string in the Series, extract groups from all matches of regular expression and return a DataFrame with one row for each match and one column for each group.

[`re.findall`](https://docs.python.org/3/library/re.html#re.findall "(in Python v3.15)")

The equivalent `re` function to all non-overlapping matches of pattern or regular expression in string, as a list of strings.

Examples

\>>> s \= pd.Series(\["Lion", "Monkey", "Rabbit"\])

Copy to clipboard

The search for the pattern ‘Monkey’ returns one match:

\>>> s.str.findall("Monkey")
0          \[\]
1    \[Monkey\]
2          \[\]
dtype: object

Copy to clipboard

On the other hand, the search for the pattern ‘MONKEY’ doesn’t return any match:

\>>> s.str.findall("MONKEY")
0    \[\]
1    \[\]
2    \[\]
dtype: object

Copy to clipboard

Flags can be added to the pattern or regular expression. For instance, to find the pattern ‘MONKEY’ ignoring the case:

\>>> import re
\>>> s.str.findall("MONKEY", flags\=re.IGNORECASE)
0          \[\]
1    \[Monkey\]
2          \[\]
dtype: object

Copy to clipboard

When the pattern matches more than one string in the Series, all matches are returned:

\>>> s.str.findall("on")
0    \[on\]
1    \[on\]
2      \[\]
dtype: object

Copy to clipboard

Regular expressions are supported too. For instance, the search for all the strings ending with the word ‘on’ is shown next:

\>>> s.str.findall("on$")
0    \[on\]
1      \[\]
2      \[\]
dtype: object

Copy to clipboard

If the pattern is found more than once in the same string, then a list of multiple strings is returned:

\>>> s.str.findall("b")
0        \[\]
1        \[\]
2    \[b, b\]
dtype: object

Copy to clipboard

On this page