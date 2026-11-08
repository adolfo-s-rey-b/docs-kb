[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.nunique.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.nunique[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.nunique.html#pandas-index-nunique "Link to this heading")

============================================================================================================================================

Index.nunique(_dropna\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/base.py#L1218-L1257)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.nunique.html#pandas.Index.nunique "Link to this definition")

Return number of unique elements in the object.

Excludes NA values by default.

Parameters:

**dropna**bool, default True

Don’t include NaN in the count.

Returns:

int

An integer indicating the number of unique elements in the object.

See also

[`DataFrame.nunique`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nunique.html#pandas.DataFrame.nunique "pandas.DataFrame.nunique")

Method nunique for DataFrame.

[`Series.count`](https://pandas.pydata.org/docs/reference/api/pandas.Series.count.html#pandas.Series.count "pandas.Series.count")

Count non-NA/null observations in the Series.

Examples

\>>> s \= pd.Series(\[1, 3, 5, 7, 7\])
\>>> s
0    1
1    3
2    5
3    7
4    7
dtype: int64

Copy to clipboard

\>>> s.nunique()
4

Copy to clipboard

On this page