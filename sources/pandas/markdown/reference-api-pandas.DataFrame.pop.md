[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pop.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.pop[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pop.html#pandas-dataframe-pop "Link to this heading")

============================================================================================================================================

DataFrame.pop(_item_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L7362-L7416)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pop.html#pandas.DataFrame.pop "Link to this definition")

Return item and drop it from DataFrame. Raise KeyError if not found.

The column is removed from the DataFrame and returned as a Series; the original DataFrame is modified in place unless it was a view.

Parameters:

**item**label

Label of column to be popped.

Returns:

Series

Series representing the item that is dropped.

See also

[`DataFrame.drop`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html#pandas.DataFrame.drop "pandas.DataFrame.drop")

Drop specified labels from rows or columns.

[`DataFrame.drop_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html#pandas.DataFrame.drop_duplicates "pandas.DataFrame.drop_duplicates")

Return DataFrame with duplicate rows removed.

Examples

\>>> df \= pd.DataFrame(
...     \[\
...         ("falcon", "bird", 389.0),\
...         ("parrot", "bird", 24.0),\
...         ("lion", "mammal", 80.5),\
...         ("monkey", "mammal", np.nan),\
...     \],
...     columns\=("name", "class", "max\_speed"),
... )
\>>> df
     name   class  max\_speed
0  falcon    bird      389.0
1  parrot    bird       24.0
2    lion  mammal       80.5
3  monkey  mammal        NaN

Copy to clipboard

\>>> df.pop("class")
0      bird
1      bird
2    mammal
3    mammal
Name: class, dtype: str

Copy to clipboard

\>>> df
     name  max\_speed
0  falcon      389.0
1  parrot       24.0
2    lion       80.5
3  monkey        NaN

Copy to clipboard

On this page