[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.has_duplicates.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.has_duplicates.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.has_duplicates.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.has_duplicates.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.has_duplicates.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.has_duplicates.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.has_duplicates.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.has_duplicates.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.has_duplicates.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.has_duplicates.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.has_duplicates.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.has_duplicates.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.has_duplicates.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.has_duplicates.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.has\_duplicates[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.has_duplicates.html#pandas-index-has-duplicates "Link to this heading")

==================================================================================================================================================================

property Index.has\_duplicates[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L2601-L2639)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.has_duplicates.html#pandas.Index.has_duplicates "Link to this definition")

Check if the Index has duplicate values.

This is the inverse of [`is_unique`](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_unique.html#pandas.Index.is_unique "pandas.Index.is_unique")
. It returns `True` if any value appears more than once in the index, `False` otherwise.

Returns:

bool

Whether or not the Index has duplicate values.

See also

[`Index.is_unique`](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_unique.html#pandas.Index.is_unique "pandas.Index.is_unique")

Inverse method that checks if it has unique values.

Examples

\>>> idx \= pd.Index(\[1, 5, 7, 7\])
\>>> idx.has\_duplicates
True

Copy to clipboard

\>>> idx \= pd.Index(\[1, 5, 7\])
\>>> idx.has\_duplicates
False

Copy to clipboard

\>>> idx \= pd.Index(\["Watermelon", "Orange", "Apple", "Watermelon"\]).astype(
...     "category"
... )
\>>> idx.has\_duplicates
True

Copy to clipboard

\>>> idx \= pd.Index(\["Orange", "Apple", "Watermelon"\]).astype("category")
\>>> idx.has\_duplicates
False

Copy to clipboard

On this page