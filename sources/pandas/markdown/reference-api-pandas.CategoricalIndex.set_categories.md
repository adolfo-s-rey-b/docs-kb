[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.set_categories.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.CategoricalIndex.set_categories.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.set_categories.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.CategoricalIndex.set_categories.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.CategoricalIndex.set_categories.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.CategoricalIndex.set_categories.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.CategoricalIndex.set_categories.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.CategoricalIndex.set_categories.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.CategoricalIndex.set_categories.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.CategoricalIndex.set_categories.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.CategoricalIndex.set_categories.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.CategoricalIndex.set_categories.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.CategoricalIndex.set_categories.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.CategoricalIndex.set_categories.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.CategoricalIndex.set\_categories[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.set_categories.html#pandas-categoricalindex-set-categories "Link to this heading")

===================================================================================================================================================================================================

CategoricalIndex.set\_categories(_new\_categories_, _ordered\=None_, _rename\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/category.py#L511-L583)
[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.set_categories.html#pandas.CategoricalIndex.set_categories "Link to this definition")

Set the categories to the specified new categories.

`new_categories` can include new categories (which will result in unused categories) or remove old categories (which results in values set to `NaN`). If `rename=True`, the categories will simply be renamed (less or more items than in old categories will result in values set to `NaN` or in unused categories respectively).

This method can be used to perform more than one action of adding, removing, and reordering simultaneously and is therefore faster than performing the individual steps via the more specialised methods.

On the other hand this method does not check whether the old categories are included in the new categories on a reorder, which can result in surprising changes.

Parameters:

**new\_categories**Index-like

The categories in new order.

**ordered**bool, default None

Whether or not the categorical is treated as an ordered categorical. If not given, do not change the ordered information.

**rename**bool, default False

Whether or not the new\_categories should be considered as a rename of the old categories or as reordered categories.

Returns:

CategoricalIndex

CategoricalIndex with the new categories.

Raises:

ValueError

If new\_categories does not validate as categories

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

Examples

\>>> ci \= pd.CategoricalIndex(
...     \["a", "b", "c", None\], categories\=\["a", "b", "c"\], ordered\=True
... )
\>>> ci
CategoricalIndex(\['a', 'b', 'c', nan\], categories=\['a', 'b', 'c'\],
                 ordered=True, dtype='category')

Copy to clipboard

\>>> ci.set\_categories(\["A", "b", "c"\])
CategoricalIndex(\[nan, 'b', 'c', nan\], categories=\['A', 'b', 'c'\],
                 ordered=True, dtype='category')
\>>> ci.set\_categories(\["A", "b", "c"\], rename\=True)
CategoricalIndex(\['A', 'b', 'c', nan\], categories=\['A', 'b', 'c'\],
                 ordered=True, dtype='category')

Copy to clipboard

On this page