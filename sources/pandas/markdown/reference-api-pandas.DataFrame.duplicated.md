[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.duplicated[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html#pandas-dataframe-duplicated "Link to this heading")

=================================================================================================================================================================

DataFrame.duplicated(_subset\=None_, _keep\='first'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L8918-L9053)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html#pandas.DataFrame.duplicated "Link to this definition")

Return boolean Series denoting duplicate rows.

Rows are considered duplicated when the same values appear more than once across the requested columns. Considering certain columns is optional.

Parameters:

**subset**column label or iterable of labels, optional

Only consider certain columns for identifying duplicates, by default use all of the columns.

**keep**{‘first’, ‘last’, False}, default ‘first’

Determines which duplicates (if any) to mark.

*   `first` : Mark duplicates as `True` except for the first occurrence.
    
*   `last` : Mark duplicates as `True` except for the last occurrence.
    
*   False : Mark all duplicates as `True`.
    

Returns:

Series

Boolean Series indicating whether each row is a duplicated row according to `keep`.

See also

[`Index.duplicated`](https://pandas.pydata.org/docs/reference/api/pandas.Index.duplicated.html#pandas.Index.duplicated "pandas.Index.duplicated")

Equivalent method on index.

[`Series.duplicated`](https://pandas.pydata.org/docs/reference/api/pandas.Series.duplicated.html#pandas.Series.duplicated "pandas.Series.duplicated")

Equivalent method on Series.

[`Series.drop_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.Series.drop_duplicates.html#pandas.Series.drop_duplicates "pandas.Series.drop_duplicates")

Remove duplicate values from Series.

[`DataFrame.drop_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html#pandas.DataFrame.drop_duplicates "pandas.DataFrame.drop_duplicates")

Remove duplicate values from DataFrame.

Examples

Consider dataset containing ramen rating.

\>>> df \= pd.DataFrame(
...     {
...         "brand": \["Yum Yum", "Yum Yum", "Indomie", "Indomie", "Indomie"\],
...         "style": \["cup", "cup", "cup", "pack", "pack"\],
...         "rating": \[4, 4, 3.5, 15, 5\],
...     }
... )
\>>> df
    brand style  rating
0  Yum Yum   cup     4.0
1  Yum Yum   cup     4.0
2  Indomie   cup     3.5
3  Indomie  pack    15.0
4  Indomie  pack     5.0

Copy to clipboard

By default, for each set of duplicated values, the first occurrence is set on False and all others on True.

\>>> df.duplicated()
0    False
1     True
2    False
3    False
4    False
dtype: bool

Copy to clipboard

By using ‘last’, the last occurrence of each set of duplicated values is set on False and all others on True.

\>>> df.duplicated(keep\="last")
0     True
1    False
2    False
3    False
4    False
dtype: bool

Copy to clipboard

By setting `keep` on False, all duplicates are True.

\>>> df.duplicated(keep\=False)
0     True
1     True
2    False
3    False
4    False
dtype: bool

Copy to clipboard

To find duplicates on specific column(s), use `subset`.

\>>> df.duplicated(subset\=\["brand"\])
0    False
1     True
2    False
3     True
4     True
dtype: bool

Copy to clipboard

On this page