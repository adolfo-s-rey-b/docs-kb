[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.rsplit.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.rsplit.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.rsplit.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.rsplit.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.rsplit.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.rsplit.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.rsplit.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.rsplit.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.rsplit.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.rsplit.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.rsplit.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.rsplit.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.rsplit.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.rsplit.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.rsplit[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.rsplit.html#pandas-series-str-rsplit "Link to this heading")

========================================================================================================================================================

Series.str.rsplit(_pat\=None_, _\*_, _n\=\-1_, _expand\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L948-L1083)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.rsplit.html#pandas.Series.str.rsplit "Link to this definition")

Split strings around given separator/delimiter.

Splits the string in the Series/Index from the end, at the specified delimiter string.

Parameters:

**pat**str, optional

String to split on. Does not support regex. If not specified, split on whitespace.

**n**int, default -1 (all)

Limit number of splits in output. `None`, 0 and -1 will be interpreted as return all splits.

**expand**bool, default False

Expand the split strings into separate columns.

*   If `True`, return DataFrame/MultiIndex expanding dimensionality.
    
*   If `False`, return Series/Index, containing lists of strings.
    

Returns:

Series, Index, DataFrame or MultiIndex

Type matches caller unless `expand=True` (see Notes).

See also

[`Series.str.split`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.split.html#pandas.Series.str.split "pandas.Series.str.split")

Split strings around given separator/delimiter or regular expression.

[`Series.str.join`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.join.html#pandas.Series.str.join "pandas.Series.str.join")

Join lists contained as elements in the Series/Index with passed delimiter.

[`re.split`](https://docs.python.org/3/library/re.html#re.split "(in Python v3.15)")

Standard library version for split with `regex=True`.

[`str.split`](https://docs.python.org/3/builtins/stdtypes.html#str.split "(in Python v3.15)")

Standard library version for split with `regex=False`.

[`str.rsplit`](https://docs.python.org/3/builtins/stdtypes.html#str.rsplit "(in Python v3.15)")

Standard library version for rsplit.

Notes

The handling of the n keyword depends on the number of found splits:

*   If found splits > n, make first n splits only
    
*   If found splits <= n, make all splits
    
*   If for a certain row the number of found splits is less than the maximum number of splits found across all rows, append None for padding if `expand=True`
    

If using `expand=True`, Series and Index callers return DataFrame and MultiIndex objects, respectively. The number of columns equals the maximum number of splits found in the data plus one and can be less than `n + 1`; n is an upper bound on the number of splits, not a guaranteed output width. To get a fixed number of columns, reindex the result, e.g. `.reindex(range(n + 1), axis=1)`.

Examples

\>>> s \= pd.Series(
...     \[\
...         "this is a regular sentence",\
...         "https://docs.python.org/3/tutorial/index.html",\
...         np.nan,\
...     \]
... )
\>>> s
0                       this is a regular sentence
1    https://docs.python.org/3/tutorial/index.html
2                                              NaN
dtype: str

Copy to clipboard

In the default setting, the string is split by whitespace.

\>>> s.str.split()
0                   \[this, is, a, regular, sentence\]
1    \[https://docs.python.org/3/tutorial/index.html\]
2                                                NaN
dtype: object

Copy to clipboard

Without the n parameter, the outputs of rsplit and split are identical.

\>>> s.str.rsplit()
0                   \[this, is, a, regular, sentence\]
1    \[https://docs.python.org/3/tutorial/index.html\]
2                                                NaN
dtype: object

Copy to clipboard

The n parameter can be used to limit the number of splits on the delimiter. The outputs of split and rsplit are different.

\>>> s.str.split(n\=2)
0                     \[this, is, a regular sentence\]
1    \[https://docs.python.org/3/tutorial/index.html\]
2                                                NaN
dtype: object

Copy to clipboard

\>>> s.str.rsplit(n\=2)
0                     \[this is a, regular, sentence\]
1    \[https://docs.python.org/3/tutorial/index.html\]
2                                                NaN
dtype: object

Copy to clipboard

The pat parameter can be used to split by other characters.

\>>> s.str.split(pat\="/")
0                         \[this is a regular sentence\]
1    \[https:, , docs.python.org, 3, tutorial, index...\
2                                                  NaN\
dtype: object\
\
Copy to clipboard\
\
When using `expand=True`, the split elements will expand out into separate columns. If NaN is present, it is propagated throughout the columns during the split.\
\
\>>> s.str.split(expand\=True)\
                                               0    1    2        3         4\
0                                           this   is    a  regular  sentence\
1  https://docs.python.org/3/tutorial/index.html  NaN  NaN      NaN       NaN\
2                                            NaN  NaN  NaN      NaN       NaN\
\
Copy to clipboard\
\
For slightly more complex use cases like splitting the html document name from a url, a combination of parameter settings can be used.\
\
\>>> s.str.rsplit("/", n\=1, expand\=True)\
                                    0           1\
0          this is a regular sentence         NaN\
1  https://docs.python.org/3/tutorial  index.html\
2                                 NaN         NaN\
\
Copy to clipboard\
\
On this page