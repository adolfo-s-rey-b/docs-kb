[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.nunique.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.DataFrameGroupBy.nunique.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.nunique.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.DataFrameGroupBy.nunique.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.DataFrameGroupBy.nunique.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.DataFrameGroupBy.nunique.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.DataFrameGroupBy.nunique.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.DataFrameGroupBy.nunique.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.DataFrameGroupBy.nunique.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.DataFrameGroupBy.nunique.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.DataFrameGroupBy.nunique.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.DataFrameGroupBy.nunique.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.DataFrameGroupBy.nunique.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.DataFrameGroupBy.nunique.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.nunique[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.nunique.html#pandas-api-typing-dataframegroupby-nunique "Link to this heading")

==============================================================================================================================================================================================================

DataFrameGroupBy.nunique(_dropna\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L3092-L3147)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.nunique.html#pandas.api.typing.DataFrameGroupBy.nunique "Link to this definition")

Return DataFrame with counts of unique elements in each position.

This method counts the number of distinct values for each column within each group, optionally excluding NaN values.

Parameters:

**dropna**bool, default True

Don’t include NaN in the counts.

Returns:

nunique: DataFrame

Counts of unique elements in each position.

See also

`DataFrame.nunique`

Count number of distinct elements in specified axis.

Examples

\>>> df \= pd.DataFrame(
...     {
...         "id": \["spam", "egg", "egg", "spam", "ham", "ham"\],
...         "value1": \[1, 5, 5, 2, 5, 5\],
...         "value2": list("abbaxy"),
...     }
... )
\>>> df
     id  value1 value2
0  spam       1      a
1   egg       5      b
2   egg       5      b
3  spam       2      a
4   ham       5      x
5   ham       5      y

Copy to clipboard

\>>> df.groupby("id").nunique()
      value1  value2
id
egg        1       1
ham        1       2
spam       2       1

Copy to clipboard

Check for rows with the same id but conflicting values:

\>>> df.groupby("id").filter(lambda g: (g.nunique() \> 1).any())
     id  value1 value2
0  spam       1      a
3  spam       2      a
4   ham       5      x
5   ham       5      y

Copy to clipboard

On this page