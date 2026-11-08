[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.categories.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.CategoricalIndex.categories[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.categories.html#pandas-categoricalindex-categories "Link to this heading")

======================================================================================================================================================================================

property CategoricalIndex.categories[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/category.py#L197-L226)
[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.categories.html#pandas.CategoricalIndex.categories "Link to this definition")

The categories of this CategoricalIndex.

These are the unique values the index may hold, in category order. Use the `*_categories` methods to return an index with changed categories.

See also

[`CategoricalIndex.rename_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.rename_categories.html#pandas.CategoricalIndex.rename_categories "pandas.CategoricalIndex.rename_categories")

Rename categories.

[`CategoricalIndex.reorder_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.reorder_categories.html#pandas.CategoricalIndex.reorder_categories "pandas.CategoricalIndex.reorder_categories")

Reorder categories.

[`CategoricalIndex.add_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.add_categories.html#pandas.CategoricalIndex.add_categories "pandas.CategoricalIndex.add_categories")

Add new categories.

[`CategoricalIndex.remove_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.remove_categories.html#pandas.CategoricalIndex.remove_categories "pandas.CategoricalIndex.remove_categories")

Remove the specified categories.

[`CategoricalIndex.remove_unused_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.remove_unused_categories.html#pandas.CategoricalIndex.remove_unused_categories "pandas.CategoricalIndex.remove_unused_categories")

Remove categories which are not used.

[`CategoricalIndex.set_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.set_categories.html#pandas.CategoricalIndex.set_categories "pandas.CategoricalIndex.set_categories")

Set the categories to the specified ones.

Examples

\>>> ci \= pd.CategoricalIndex(\["a", "c", "b", "a", "c", "b"\])
\>>> ci.categories
Index(\['a', 'b', 'c'\], dtype='str')

Copy to clipboard

\>>> ci \= pd.CategoricalIndex(\["a", "c"\], categories\=\["c", "b", "a"\])
\>>> ci.categories
Index(\['c', 'b', 'a'\], dtype='str')

Copy to clipboard

On this page