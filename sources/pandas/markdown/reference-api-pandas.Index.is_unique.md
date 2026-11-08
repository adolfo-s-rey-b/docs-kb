[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_unique.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.is_unique.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_unique.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.is_unique.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.is_unique.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.is_unique.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.is_unique.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.is_unique.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.is_unique.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.is_unique.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.is_unique.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.is_unique.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.is_unique.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.is_unique.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.is\_unique[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_unique.html#pandas-index-is-unique "Link to this heading")

===================================================================================================================================================

Index.is\_unique[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L2563-L2599)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_unique.html#pandas.Index.is_unique "Link to this definition")

Return if the index has unique values.

The uniqueness check is based on exact equality of values. An index with no repeated values returns `True`, otherwise `False`.

Returns:

bool

See also

[`Index.has_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.Index.has_duplicates.html#pandas.Index.has_duplicates "pandas.Index.has_duplicates")

Inverse method that checks if it has duplicate values.

Examples

\>>> idx \= pd.Index(\[1, 5, 7, 7\])
\>>> idx.is\_unique
False

Copy to clipboard

\>>> idx \= pd.Index(\[1, 5, 7\])
\>>> idx.is\_unique
True

Copy to clipboard

\>>> idx \= pd.Index(\["Watermelon", "Orange", "Apple", "Watermelon"\]).astype(
...     "category"
... )
\>>> idx.is\_unique
False

Copy to clipboard

\>>> idx \= pd.Index(\["Orange", "Apple", "Watermelon"\]).astype("category")
\>>> idx.is\_unique
True

Copy to clipboard

On this page