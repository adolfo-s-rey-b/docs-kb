[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.reorder_levels.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.reorder_levels.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.reorder_levels.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.reorder_levels.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.reorder_levels.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.reorder_levels.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.reorder_levels.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.reorder_levels.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.reorder_levels.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.reorder_levels.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.reorder_levels.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.reorder_levels.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.reorder_levels.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.reorder_levels.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.reorder\_levels[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.reorder_levels.html#pandas-series-reorder-levels "Link to this heading")

=====================================================================================================================================================================

Series.reorder\_levels(_order_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L4827-L4878)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.reorder_levels.html#pandas.Series.reorder_levels "Link to this definition")

Rearrange index levels using input order.

May not drop or duplicate levels.

Parameters:

**order**list of int representing new level order

Reference level by number or key.

Returns:

Series

Type of caller with index as MultiIndex (new object).

See also

[`DataFrame.reorder_levels`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reorder_levels.html#pandas.DataFrame.reorder_levels "pandas.DataFrame.reorder_levels")

Rearrange index or column levels using input `order`.

Examples

\>>> arrays \= \[\
...     np.array(\["dog", "dog", "cat", "cat", "bird", "bird"\]),\
...     np.array(\["white", "black", "white", "black", "white", "black"\]),\
... \]
\>>> s \= pd.Series(\[1, 2, 3, 3, 5, 2\], index\=arrays)
\>>> s
dog   white    1
      black    2
cat   white    3
      black    3
bird  white    5
      black    2
dtype: int64
\>>> s.reorder\_levels(\[1, 0\])
white  dog     1
black  dog     2
white  cat     3
black  cat     3
white  bird    5
black  bird    2
dtype: int64

Copy to clipboard

On this page