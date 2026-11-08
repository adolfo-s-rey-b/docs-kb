[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.reorder_categories.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.CategoricalIndex.reorder\_categories[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.reorder_categories.html#pandas-categoricalindex-reorder-categories "Link to this heading")

===============================================================================================================================================================================================================

CategoricalIndex.reorder\_categories(_new\_categories_, _ordered\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/category.py#L326-L375)
[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.reorder_categories.html#pandas.CategoricalIndex.reorder_categories "Link to this definition")

Reorder categories as specified in new\_categories.

`new_categories` need to include all old categories and no new category items.

Parameters:

**new\_categories**Index-like

The categories in new order.

**ordered**bool, optional

Whether or not the categorical is treated as an ordered categorical. If not given, do not change the ordered information.

Returns:

CategoricalIndex

CategoricalIndex with reordered categories.

Raises:

ValueError

If the new categories do not contain all old category items or any new ones

See also

[`CategoricalIndex.rename_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.rename_categories.html#pandas.CategoricalIndex.rename_categories "pandas.CategoricalIndex.rename_categories")

Rename categories.

[`CategoricalIndex.add_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.add_categories.html#pandas.CategoricalIndex.add_categories "pandas.CategoricalIndex.add_categories")

Add new categories.

[`CategoricalIndex.remove_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.remove_categories.html#pandas.CategoricalIndex.remove_categories "pandas.CategoricalIndex.remove_categories")

Remove the specified categories.

[`CategoricalIndex.remove_unused_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.remove_unused_categories.html#pandas.CategoricalIndex.remove_unused_categories "pandas.CategoricalIndex.remove_unused_categories")

Remove categories which are not used.

[`CategoricalIndex.set_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.set_categories.html#pandas.CategoricalIndex.set_categories "pandas.CategoricalIndex.set_categories")

Set the categories to the specified ones.

Examples

\>>> ci \= pd.CategoricalIndex(\["a", "b", "c", "a"\])
\>>> ci
CategoricalIndex(\['a', 'b', 'c', 'a'\], categories=\['a', 'b', 'c'\],
                 ordered=False, dtype='category')
\>>> ci.reorder\_categories(\["c", "b", "a"\], ordered\=True)
CategoricalIndex(\['a', 'b', 'c', 'a'\], categories=\['c', 'b', 'a'\],
                 ordered=True, dtype='category')

Copy to clipboard

On this page