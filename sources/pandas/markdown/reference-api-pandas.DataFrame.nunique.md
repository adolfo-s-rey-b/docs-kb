[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nunique.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.nunique[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nunique.html#pandas-dataframe-nunique "Link to this heading")

========================================================================================================================================================

DataFrame.nunique(_axis\=0_, _dropna\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L19248-L19287)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nunique.html#pandas.DataFrame.nunique "Link to this definition")

Count number of distinct elements in specified axis.

Return Series with number of distinct elements. Can ignore NaN values.

Parameters:

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

The axis to use. 0 or ‘index’ for row-wise, 1 or ‘columns’ for column-wise.

**dropna**bool, default True

Don’t include NaN in the counts.

Returns:

Series

Series with counts of unique values per row or column, depending on axis.

See also

[`Series.nunique`](https://pandas.pydata.org/docs/reference/api/pandas.Series.nunique.html#pandas.Series.nunique "pandas.Series.nunique")

Method nunique for Series.

[`DataFrame.count`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html#pandas.DataFrame.count "pandas.DataFrame.count")

Count non-NA cells for each column or row.

Examples

\>>> df \= pd.DataFrame({"A": \[4, 5, 6\], "B": \[4, 1, 1\]})
\>>> df.nunique()
A    3
B    2
dtype: int64

Copy to clipboard

\>>> df.nunique(axis\=1)
0    1
1    2
2    2
dtype: int64

Copy to clipboard

On this page