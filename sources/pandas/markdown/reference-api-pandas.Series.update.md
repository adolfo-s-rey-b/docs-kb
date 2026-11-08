[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.update.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.update.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.update.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.update.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.update.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.update.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.update.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.update.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.update.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.update.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.update.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.update.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.update.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.update.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.update[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.update.html#pandas-series-update "Link to this heading")

============================================================================================================================================

Series.update(_other_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L3918-L4008)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.update.html#pandas.Series.update "Link to this definition")

Modify Series in place using values from passed Series.

Uses non-NA values from passed Series to make updates. Aligns on index.

Parameters:

**other**Series, or object coercible into Series

Other Series that provides values to update the current Series.

See also

[`Series.combine`](https://pandas.pydata.org/docs/reference/api/pandas.Series.combine.html#pandas.Series.combine "pandas.Series.combine")

Perform element-wise operation on two Series using a given function.

[`Series.transform`](https://pandas.pydata.org/docs/reference/api/pandas.Series.transform.html#pandas.Series.transform "pandas.Series.transform")

Modify a Series using a function.

Examples

\>>> s \= pd.Series(\[1, 2, 3\])
\>>> s.update(pd.Series(\[4, 5, 6\]))
\>>> s
0    4
1    5
2    6
dtype: int64

Copy to clipboard

\>>> s \= pd.Series(\["a", "b", "c"\])
\>>> s.update(pd.Series(\["d", "e"\], index\=\[0, 2\]))
\>>> s
0    d
1    b
2    e
dtype: str

Copy to clipboard

\>>> s \= pd.Series(\[1, 2, 3\])
\>>> s.update(pd.Series(\[4, 5, 6, 7, 8\]))
\>>> s
0    4
1    5
2    6
dtype: int64

Copy to clipboard

If `other` contains NaNs the corresponding values are not updated in the original Series.

\>>> s \= pd.Series(\[1, 2, 3\])
\>>> s.update(pd.Series(\[4, np.nan, 6\]))
\>>> s
0    4
1    2
2    6
dtype: int64

Copy to clipboard

`other` can also be a non-Series object type that is coercible into a Series

\>>> s \= pd.Series(\[1, 2, 3\])
\>>> s.update(\[4, np.nan, 6\])
\>>> s
0    4
1    2
2    6
dtype: int64

Copy to clipboard

\>>> s \= pd.Series(\[1, 2, 3\])
\>>> s.update({1: 9})
\>>> s
0    1
1    9
2    3
dtype: int64

Copy to clipboard

On this page