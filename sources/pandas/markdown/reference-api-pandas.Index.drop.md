[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.drop.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.drop[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.drop.html#pandas-index-drop "Link to this heading")

===================================================================================================================================

Index.drop(_labels_, _errors\='raise'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L7576-L7628)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.drop.html#pandas.Index.drop "Link to this definition")

Make new Index with passed list of labels deleted.

Unlike [`Index.delete()`](https://pandas.pydata.org/docs/reference/api/pandas.Index.delete.html#pandas.Index.delete "pandas.Index.delete")
, which accepts positional indices, this method removes entries by their label values. The original Index is not modified.

Parameters:

**labels**array-like or scalar

Array-like object or a scalar value, representing the labels to be removed from the Index.

**errors**{‘ignore’, ‘raise’}, default ‘raise’

If ‘ignore’, suppress error and existing labels are dropped.

Returns:

Index

Will be same type as self, except for RangeIndex.

Raises:

KeyError

If not all of the labels are found in the selected axis

See also

[`Index.dropna`](https://pandas.pydata.org/docs/reference/api/pandas.Index.dropna.html#pandas.Index.dropna "pandas.Index.dropna")

Return Index without NA/NaN values.

[`Index.drop_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.Index.drop_duplicates.html#pandas.Index.drop_duplicates "pandas.Index.drop_duplicates")

Return Index with duplicate values removed.

Examples

\>>> idx \= pd.Index(\["a", "b", "c"\])
\>>> idx.drop(\["a"\])
Index(\['b', 'c'\], dtype='str')

Copy to clipboard

On this page