[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.as_unordered.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.CategoricalIndex.as_unordered.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.as_unordered.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.CategoricalIndex.as_unordered.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.CategoricalIndex.as_unordered.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.CategoricalIndex.as_unordered.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.CategoricalIndex.as_unordered.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.CategoricalIndex.as_unordered.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.CategoricalIndex.as_unordered.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.CategoricalIndex.as_unordered.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.CategoricalIndex.as_unordered.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.CategoricalIndex.as_unordered.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.CategoricalIndex.as_unordered.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.CategoricalIndex.as_unordered.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.CategoricalIndex.as\_unordered[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.as_unordered.html#pandas-categoricalindex-as-unordered "Link to this heading")

=============================================================================================================================================================================================

CategoricalIndex.as\_unordered()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/category.py#L613-L639)
[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.as_unordered.html#pandas.CategoricalIndex.as_unordered "Link to this definition")

Set the CategoricalIndex to be unordered.

This method returns a new CategoricalIndex with the ordered attribute set to False, disabling comparison operations between categories.

Returns:

CategoricalIndex

Unordered CategoricalIndex.

See also

[`CategoricalIndex.as_ordered`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.as_ordered.html#pandas.CategoricalIndex.as_ordered "pandas.CategoricalIndex.as_ordered")

Set the CategoricalIndex to be ordered.

Examples

\>>> ci \= pd.CategoricalIndex(\["a", "b", "c", "a"\], ordered\=True)
\>>> ci.ordered
True
\>>> ci \= ci.as\_unordered()
\>>> ci.ordered
False

Copy to clipboard

On this page