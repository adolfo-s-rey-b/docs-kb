[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.remove_categories.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.CategoricalIndex.remove_categories.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.remove_categories.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.CategoricalIndex.remove_categories.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.CategoricalIndex.remove_categories.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.CategoricalIndex.remove_categories.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.CategoricalIndex.remove_categories.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.CategoricalIndex.remove_categories.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.CategoricalIndex.remove_categories.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.CategoricalIndex.remove_categories.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.CategoricalIndex.remove_categories.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.CategoricalIndex.remove_categories.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.CategoricalIndex.remove_categories.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.CategoricalIndex.remove_categories.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.CategoricalIndex.remove\_categories[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.remove_categories.html#pandas-categoricalindex-remove-categories "Link to this heading")

============================================================================================================================================================================================================

CategoricalIndex.remove\_categories(_removals_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/category.py#L424-L468)
[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.remove_categories.html#pandas.CategoricalIndex.remove_categories "Link to this definition")

Remove the specified categories.

The `removals` argument must be a subset of the current categories. Any values that were part of the removed categories will be set to NaN.

Parameters:

**removals**category or list of categories

The categories which should be removed.

Returns:

CategoricalIndex

CategoricalIndex with removed categories.

Raises:

ValueError

If the removals are not contained in the categories

See also

[`CategoricalIndex.rename_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.rename_categories.html#pandas.CategoricalIndex.rename_categories "pandas.CategoricalIndex.rename_categories")

Rename categories.

[`CategoricalIndex.reorder_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.reorder_categories.html#pandas.CategoricalIndex.reorder_categories "pandas.CategoricalIndex.reorder_categories")

Reorder categories.

[`CategoricalIndex.add_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.add_categories.html#pandas.CategoricalIndex.add_categories "pandas.CategoricalIndex.add_categories")

Add new categories.

[`CategoricalIndex.remove_unused_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.remove_unused_categories.html#pandas.CategoricalIndex.remove_unused_categories "pandas.CategoricalIndex.remove_unused_categories")

Remove categories which are not used.

[`CategoricalIndex.set_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.set_categories.html#pandas.CategoricalIndex.set_categories "pandas.CategoricalIndex.set_categories")

Set the categories to the specified ones.

Examples

\>>> ci \= pd.CategoricalIndex(\["a", "c", "b", "c", "d"\])
\>>> ci
CategoricalIndex(\['a', 'c', 'b', 'c', 'd'\], categories=\['a', 'b', 'c', 'd'\],
                 ordered=False, dtype='category')

Copy to clipboard

\>>> ci.remove\_categories(\["d", "a"\])
CategoricalIndex(\[nan, 'c', 'b', 'c', nan\], categories=\['b', 'c'\],
                 ordered=False, dtype='category')

Copy to clipboard

On this page