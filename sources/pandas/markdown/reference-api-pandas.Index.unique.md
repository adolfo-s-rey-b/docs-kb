[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.unique.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.unique[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.unique.html#pandas-index-unique "Link to this heading")

=========================================================================================================================================

Index.unique(_level\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L2963-L2998)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.unique.html#pandas.Index.unique "Link to this definition")

Return unique values in the index.

Unique values are returned in order of appearance, this does NOT sort.

Parameters:

**level**int or hashable, optional

Only return values from specified level (for MultiIndex). If int, gets the level by integer position, else by level name.

Returns:

Index

Unique values in the index.

See also

[`unique`](https://pandas.pydata.org/docs/reference/api/pandas.unique.html#pandas.unique "pandas.unique")

Numpy array of unique values in that column.

[`Series.unique`](https://pandas.pydata.org/docs/reference/api/pandas.Series.unique.html#pandas.Series.unique "pandas.Series.unique")

Return unique values of Series object.

Examples

\>>> idx \= pd.Index(\[1, 1, 2, 3, 3\])
\>>> idx.unique()
Index(\[1, 2, 3\], dtype='int64')

Copy to clipboard

On this page