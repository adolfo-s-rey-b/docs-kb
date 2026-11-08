[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.drop_duplicates.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.drop\_duplicates[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.drop_duplicates.html#pandas-series-drop-duplicates "Link to this heading")

========================================================================================================================================================================

Series.drop\_duplicates(_\*_, _keep\='first'_, _inplace\=<no\_default>_, _ignore\_index\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L2539-L2660)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.drop_duplicates.html#pandas.Series.drop_duplicates "Link to this definition")

Return Series with duplicate values removed.

This method identifies and removes duplicate values from the Series, keeping the first, last, or none of the duplicate occurrences based on the `keep` parameter.

Parameters:

**keep**{‘first’, ‘last’, `False`}, default ‘first’

Method to handle dropping duplicates:

*   ‘first’ : Drop duplicates except for the first occurrence.
    
*   ‘last’ : Drop duplicates except for the last occurrence.
    
*   `False` : Drop all duplicates.
    

**inplace**bool, default `False`

If `True`, performs operation inplace and returns None.

Deprecated since version 3.1.0: This keyword is deprecated and will be removed in pandas 4.0. See the [whatsnew note on PDEP-8](https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace)
 for more details.

**ignore\_index**bool, default `False`

If `True`, the resulting axis will be labeled 0, 1, …, n - 1.

Added in version 2.0.0.

Returns:

Series or None

Series with duplicates dropped or None if `inplace=True`.

See also

[`Index.drop_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.Index.drop_duplicates.html#pandas.Index.drop_duplicates "pandas.Index.drop_duplicates")

Equivalent method on Index.

[`DataFrame.drop_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html#pandas.DataFrame.drop_duplicates "pandas.DataFrame.drop_duplicates")

Equivalent method on DataFrame.

[`Series.duplicated`](https://pandas.pydata.org/docs/reference/api/pandas.Series.duplicated.html#pandas.Series.duplicated "pandas.Series.duplicated")

Related method on Series, indicating duplicate Series values.

[`Series.unique`](https://pandas.pydata.org/docs/reference/api/pandas.Series.unique.html#pandas.Series.unique "pandas.Series.unique")

Return unique values as an array.

[`Index.duplicated`](https://pandas.pydata.org/docs/reference/api/pandas.Index.duplicated.html#pandas.Index.duplicated "pandas.Index.duplicated")

Indicate duplicate index values.

Examples

Generate a Series with duplicated entries.

\>>> s \= pd.Series(
...     \["llama", "cow", "llama", "beetle", "llama", "hippo"\], name\="animal"
... )
\>>> s
0     llama
1       cow
2     llama
3    beetle
4     llama
5     hippo
Name: animal, dtype: str

Copy to clipboard

With the ‘keep’ parameter, the selection behavior of duplicated values can be changed. The value ‘first’ keeps the first occurrence for each set of duplicated entries. The default value of keep is ‘first’.

\>>> s.drop\_duplicates()
0     llama
1       cow
3    beetle
5     hippo
Name: animal, dtype: str

Copy to clipboard

The value ‘last’ for parameter ‘keep’ keeps the last occurrence for each set of duplicated entries.

\>>> s.drop\_duplicates(keep\="last")
1       cow
3    beetle
4     llama
5     hippo
Name: animal, dtype: str

Copy to clipboard

The value `False` for parameter ‘keep’ discards all sets of duplicated entries.

\>>> s.drop\_duplicates(keep\=False)
1       cow
3    beetle
5     hippo
Name: animal, dtype: str

Copy to clipboard

Only the values are considered, not the index. To drop entries with a duplicate index label, use [`Index.duplicated()`](https://pandas.pydata.org/docs/reference/api/pandas.Index.duplicated.html#pandas.Index.duplicated "pandas.Index.duplicated")
 with boolean indexing.

\>>> s.index \= \["a", "b", "b", "c", "c", "d"\]
\>>> s\[~s.index.duplicated(keep\="first")\]
a     llama
b       cow
c    beetle
d     hippo
Name: animal, dtype: str

Copy to clipboard

On this page