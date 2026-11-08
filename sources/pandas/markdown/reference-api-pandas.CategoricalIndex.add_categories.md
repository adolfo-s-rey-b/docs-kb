[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.add_categories.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.CategoricalIndex.add\_categories[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.add_categories.html#pandas-categoricalindex-add-categories "Link to this heading")

===================================================================================================================================================================================================

CategoricalIndex.add\_categories(_new\_categories_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/category.py#L377-L422)
[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.add_categories.html#pandas.CategoricalIndex.add_categories "Link to this definition")

Add new categories.

new\_categories will be included at the last/highest place in the categories and will be unused directly after this call.

Parameters:

**new\_categories**category or list-like of category

The new categories to be included.

Returns:

CategoricalIndex

CategoricalIndex with new categories added.

Raises:

ValueError

If the new categories include old categories or do not validate as categories

See also

[`CategoricalIndex.rename_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.rename_categories.html#pandas.CategoricalIndex.rename_categories "pandas.CategoricalIndex.rename_categories")

Rename categories.

[`CategoricalIndex.reorder_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.reorder_categories.html#pandas.CategoricalIndex.reorder_categories "pandas.CategoricalIndex.reorder_categories")

Reorder categories.

[`CategoricalIndex.remove_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.remove_categories.html#pandas.CategoricalIndex.remove_categories "pandas.CategoricalIndex.remove_categories")

Remove the specified categories.

[`CategoricalIndex.remove_unused_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.remove_unused_categories.html#pandas.CategoricalIndex.remove_unused_categories "pandas.CategoricalIndex.remove_unused_categories")

Remove categories which are not used.

[`CategoricalIndex.set_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.set_categories.html#pandas.CategoricalIndex.set_categories "pandas.CategoricalIndex.set_categories")

Set the categories to the specified ones.

Examples

\>>> ci \= pd.CategoricalIndex(\["c", "b", "c"\])
\>>> ci
CategoricalIndex(\['c', 'b', 'c'\], categories=\['b', 'c'\], ordered=False,
                 dtype='category')

Copy to clipboard

\>>> ci.add\_categories(\["d", "a"\])
CategoricalIndex(\['c', 'b', 'c'\], categories=\['b', 'c', 'd', 'a'\],
                 ordered=False, dtype='category')

Copy to clipboard

On this page