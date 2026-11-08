[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.pop.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.pop.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.pop.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.pop.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.pop.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.pop.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.pop.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.pop.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.pop.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.pop.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.pop.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.pop.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.pop.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.pop.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.pop[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.pop.html#pandas-series-pop "Link to this heading")

===================================================================================================================================

Series.pop(_item_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L6323-L6357)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.pop.html#pandas.Series.pop "Link to this definition")

Return item and drops from series. Raise KeyError if not found.

The Series is modified in place, and the value corresponding to the given label is removed and returned.

Parameters:

**item**label

Index of the element that needs to be removed.

Returns:

scalar

Value that is popped from series.

See also

[`Series.drop`](https://pandas.pydata.org/docs/reference/api/pandas.Series.drop.html#pandas.Series.drop "pandas.Series.drop")

Drop specified values from Series.

[`Series.drop_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.Series.drop_duplicates.html#pandas.Series.drop_duplicates "pandas.Series.drop_duplicates")

Return Series with duplicate values removed.

Examples

\>>> ser \= pd.Series(\[1, 2, 3\])

Copy to clipboard

\>>> ser.pop(0)
1

Copy to clipboard

\>>> ser
1    2
2    3
dtype: int64

Copy to clipboard

On this page