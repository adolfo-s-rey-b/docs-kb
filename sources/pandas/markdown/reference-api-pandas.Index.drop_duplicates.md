[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.drop_duplicates.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.drop\_duplicates[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.drop_duplicates.html#pandas-index-drop-duplicates "Link to this heading")

=====================================================================================================================================================================

Index.drop\_duplicates(_\*_, _keep\='first'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L3000-L3053)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.drop_duplicates.html#pandas.Index.drop_duplicates "Link to this definition")

Return Index with duplicate values removed.

The `keep` parameter controls which duplicate values are removed. The original Index is not modified.

Parameters:

**keep**{‘first’, ‘last’, `False`}, default ‘first’

*   ‘first’ : Drop duplicates except for the first occurrence.
    
*   ‘last’ : Drop duplicates except for the last occurrence.
    
*   `False` : Drop all duplicates.
    

Returns:

Index

A new Index object with the duplicate values removed.

See also

[`Series.drop_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.Series.drop_duplicates.html#pandas.Series.drop_duplicates "pandas.Series.drop_duplicates")

Equivalent method on Series.

[`DataFrame.drop_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html#pandas.DataFrame.drop_duplicates "pandas.DataFrame.drop_duplicates")

Equivalent method on DataFrame.

[`Index.duplicated`](https://pandas.pydata.org/docs/reference/api/pandas.Index.duplicated.html#pandas.Index.duplicated "pandas.Index.duplicated")

Related method on Index, indicating duplicate Index values.

Examples

Generate a pandas.Index with duplicate values.

\>>> idx \= pd.Index(\["llama", "cow", "llama", "beetle", "llama", "hippo"\])

Copy to clipboard

The keep parameter controls which duplicate values are removed. The value ‘first’ keeps the first occurrence for each set of duplicated entries. The default value of keep is ‘first’.

\>>> idx.drop\_duplicates(keep\="first")
Index(\['llama', 'cow', 'beetle', 'hippo'\], dtype='str')

Copy to clipboard

The value ‘last’ keeps the last occurrence for each set of duplicated entries.

\>>> idx.drop\_duplicates(keep\="last")
Index(\['cow', 'beetle', 'llama', 'hippo'\], dtype='str')

Copy to clipboard

The value `False` discards all sets of duplicated entries.

\>>> idx.drop\_duplicates(keep\=False)
Index(\['cow', 'beetle', 'hippo'\], dtype='str')

Copy to clipboard

On this page