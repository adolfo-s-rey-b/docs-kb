[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.count[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html#pandas-dataframe-count "Link to this heading")

==================================================================================================================================================

DataFrame.count(_axis\=0_, _numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L16889-L16967)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html#pandas.DataFrame.count "Link to this definition")

Count non-NA cells for each column or row.

The values None, NaN, NaT, `pandas.NA` are considered NA.

Parameters:

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

If 0 or ‘index’ counts are generated for each column. If 1 or ‘columns’ counts are generated for each row.

**numeric\_only**bool, default False

Include only float, int or boolean data.

Returns:

Series

For each column/row the number of non-NA/null entries.

See also

[`Series.count`](https://pandas.pydata.org/docs/reference/api/pandas.Series.count.html#pandas.Series.count "pandas.Series.count")

Number of non-NA elements in a Series.

[`DataFrame.value_counts`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html#pandas.DataFrame.value_counts "pandas.DataFrame.value_counts")

Count unique combinations of columns.

[`DataFrame.shape`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html#pandas.DataFrame.shape "pandas.DataFrame.shape")

Number of DataFrame rows and columns (including NA elements).

[`DataFrame.isna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html#pandas.DataFrame.isna "pandas.DataFrame.isna")

Boolean same-sized DataFrame showing places of NA elements.

Examples

Constructing DataFrame from a dictionary:

\>>> df \= pd.DataFrame(
...     {
...         "Person": \["John", "Myla", "Lewis", "John", "Myla"\],
...         "Age": \[24.0, np.nan, 21.0, 33, 26\],
...         "Single": \[False, True, True, True, False\],
...     }
... )
\>>> df
   Person   Age  Single
0    John  24.0   False
1    Myla   NaN    True
2   Lewis  21.0    True
3    John  33.0    True
4    Myla  26.0   False

Copy to clipboard

Notice the uncounted NA values:

\>>> df.count()
Person    5
Age       4
Single    5
dtype: int64

Copy to clipboard

Counts for each **row**:

\>>> df.count(axis\="columns")
0    3
1    2
2    3
3    3
4    3
dtype: int64

Copy to clipboard

On this page