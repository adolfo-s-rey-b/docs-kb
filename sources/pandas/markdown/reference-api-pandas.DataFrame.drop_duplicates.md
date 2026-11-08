[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.drop\_duplicates[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html#pandas-dataframe-drop-duplicates "Link to this heading")

=================================================================================================================================================================================

DataFrame.drop\_duplicates(_subset\=None_, _\*_, _keep\='first'_, _inplace\=<no\_default>_, _ignore\_index\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L8792-L8916)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html#pandas.DataFrame.drop_duplicates "Link to this definition")

Return DataFrame with duplicate rows removed.

Considering certain columns is optional. Indexes, including time indexes are ignored.

Parameters:

**subset**column label or iterable of labels, optional

Only consider certain columns for identifying duplicates, by default use all of the columns.

**keep**{‘first’, ‘last’, `False`}, default ‘first’

Determines which duplicates (if any) to keep.

*   ‘first’ : Drop duplicates except for the first occurrence.
    
*   ‘last’ : Drop duplicates except for the last occurrence.
    
*   `False` : Drop all duplicates.
    

**inplace**bool, default `False`

Whether to modify the DataFrame rather than creating a new one.

Deprecated since version 3.1.0: This keyword is deprecated and will be removed in pandas 4.0. See the [whatsnew note on PDEP-8](https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace)
 for more details.

**ignore\_index**bool, default `False`

If `True`, the resulting axis will be labeled 0, 1, …, n - 1.

Returns:

DataFrame or None

DataFrame with duplicates removed or None if `inplace=True`.

See also

[`DataFrame.value_counts`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html#pandas.DataFrame.value_counts "pandas.DataFrame.value_counts")

Count unique combinations of columns.

[`Index.duplicated`](https://pandas.pydata.org/docs/reference/api/pandas.Index.duplicated.html#pandas.Index.duplicated "pandas.Index.duplicated")

Indicate duplicate index values.

Notes

This method requires columns specified by `subset` to be of hashable type. Passing unhashable columns will raise a `TypeError`.

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

By default, it removes duplicate rows based on all columns.

\>>> df.drop\_duplicates()
    brand style  rating
0  Yum Yum   cup     4.0
2  Indomie   cup     3.5
3  Indomie  pack    15.0
4  Indomie  pack     5.0

Copy to clipboard

To remove duplicates on specific column(s), use `subset`.

\>>> df.drop\_duplicates(subset\=\["brand"\])
    brand style  rating
0  Yum Yum   cup     4.0
2  Indomie   cup     3.5

Copy to clipboard

To remove duplicates and keep last occurrences, use `keep`.

\>>> df.drop\_duplicates(subset\=\["brand", "style"\], keep\="last")
    brand style  rating
1  Yum Yum   cup     4.0
2  Indomie   cup     3.5
4  Indomie  pack     5.0

Copy to clipboard

Duplicates in the index are not considered. To drop rows with a duplicate index label, use [`Index.duplicated()`](https://pandas.pydata.org/docs/reference/api/pandas.Index.duplicated.html#pandas.Index.duplicated "pandas.Index.duplicated")
 with boolean indexing.

\>>> indexed \= df.set\_index("brand")
\>>> indexed\[~indexed.index.duplicated(keep\="first")\]
        style  rating
brand
Yum Yum   cup     4.0
Indomie   cup     3.5

Copy to clipboard

On this page