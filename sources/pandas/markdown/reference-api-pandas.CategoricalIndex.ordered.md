[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.ordered.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.CategoricalIndex.ordered.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.ordered.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.CategoricalIndex.ordered.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.CategoricalIndex.ordered.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.CategoricalIndex.ordered.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.CategoricalIndex.ordered.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.CategoricalIndex.ordered.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.CategoricalIndex.ordered.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.CategoricalIndex.ordered.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.CategoricalIndex.ordered.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.CategoricalIndex.ordered.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.CategoricalIndex.ordered.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.CategoricalIndex.ordered.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.CategoricalIndex.ordered[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.ordered.html#pandas-categoricalindex-ordered "Link to this heading")

=============================================================================================================================================================================

property CategoricalIndex.ordered[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/category.py#L228-L251)
[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.ordered.html#pandas.CategoricalIndex.ordered "Link to this definition")

Whether the categories have an ordered relationship.

This property returns True if the categories are ordered, meaning they have a meaningful order that allows comparison operations.

See also

[`CategoricalIndex.as_ordered`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.as_ordered.html#pandas.CategoricalIndex.as_ordered "pandas.CategoricalIndex.as_ordered")

Set the CategoricalIndex to be ordered.

[`CategoricalIndex.as_unordered`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.as_unordered.html#pandas.CategoricalIndex.as_unordered "pandas.CategoricalIndex.as_unordered")

Set the CategoricalIndex to be unordered.

Examples

\>>> ci \= pd.CategoricalIndex(\["a", "b"\], ordered\=True)
\>>> ci.ordered
True

Copy to clipboard

\>>> ci \= pd.CategoricalIndex(\["a", "b"\], ordered\=False)
\>>> ci.ordered
False

Copy to clipboard

On this page