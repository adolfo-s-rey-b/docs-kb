[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.case_when.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.case_when.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.case_when.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.case_when.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.case_when.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.case_when.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.case_when.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.case_when.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.case_when.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.case_when.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.case_when.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.case_when.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.case_when.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.case_when.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.case\_when[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.case_when.html#pandas-series-case-when "Link to this heading")

======================================================================================================================================================

Series.case\_when(_caselist_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L6708-L6831)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.case_when.html#pandas.Series.case_when "Link to this definition")

Replace values where the conditions are True.

Replacement is performed in order; for each element, the first condition that evaluates to True determines the value used. This mirrors the semantics of a SQL `CASE WHEN` expression. If no condition matches, the original value is kept.

Added in version 2.2.0.

Parameters:

**caselist**A list of tuples of conditions and expected replacements

Takes the form: `(condition0, replacement0)`, `(condition1, replacement1)`, … . `condition` should be a 1-D boolean array-like object or a callable. If `condition` is a callable, it is computed on the Series and should return a boolean Series or array. The callable must not change the input Series (though pandas doesn\`t check it). `replacement` should be a 1-D array-like object, a scalar or a callable. If `replacement` is a callable, it is computed on the Series and should return a scalar or Series. The callable must not change the input Series (though pandas doesn\`t check it).

Returns:

Series

A new Series with values replaced based on the provided conditions.

See also

[`Series.mask`](https://pandas.pydata.org/docs/reference/api/pandas.Series.mask.html#pandas.Series.mask "pandas.Series.mask")

Replace values where the condition is True.

Examples

\>>> c \= pd.Series(\[6, 7, 8, 9\], name\="c")
\>>> a \= pd.Series(\[0, 0, 1, 2\])
\>>> b \= pd.Series(\[0, 3, 4, 5\])

Copy to clipboard

\>>> c.case\_when(
...     caselist\=\[\
...         (a.gt(0), a),  \# condition, replacement\
...         (b.gt(0), b),\
...     \]
... )
0    6
1    3
2    1
3    2
Name: c, dtype: int64

Copy to clipboard

On this page