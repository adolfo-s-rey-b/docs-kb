[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.identical.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.identical.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.identical.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.identical.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.identical.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.identical.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.identical.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.identical.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.identical.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.identical.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.identical.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.identical.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.identical.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.identical.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.identical[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.identical.html#pandas-index-identical "Link to this heading")

==================================================================================================================================================

final Index.identical(_other_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L5956-L6002)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.identical.html#pandas.Index.identical "Link to this definition")

Similar to equals, but checks that object attributes and types are also equal.

While [`Index.equals()`](https://pandas.pydata.org/docs/reference/api/pandas.Index.equals.html#pandas.Index.equals "pandas.Index.equals")
 only checks that the elements are the same, this method additionally verifies that the Index objects have matching types and attributes (e.g., `name`).

Parameters:

**other**Index

The Index object you want to compare with the current Index object.

Returns:

bool

If two Index objects have equal elements and same type True, otherwise False.

See also

[`Index.equals`](https://pandas.pydata.org/docs/reference/api/pandas.Index.equals.html#pandas.Index.equals "pandas.Index.equals")

Determine if two Index object are equal.

[`Index.has_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.Index.has_duplicates.html#pandas.Index.has_duplicates "pandas.Index.has_duplicates")

Check if the Index has duplicate values.

[`Index.is_unique`](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_unique.html#pandas.Index.is_unique "pandas.Index.is_unique")

Return if the index has unique values.

Examples

\>>> idx1 \= pd.Index(\["1", "2", "3"\])
\>>> idx2 \= pd.Index(\["1", "2", "3"\])
\>>> idx2.identical(idx1)
True

Copy to clipboard

\>>> idx1 \= pd.Index(\["1", "2", "3"\], name\="A")
\>>> idx2 \= pd.Index(\["1", "2", "3"\], name\="B")
\>>> idx2.identical(idx1)
False

Copy to clipboard

On this page