[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.rename_categories.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.CategoricalIndex.rename_categories.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.rename_categories.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.CategoricalIndex.rename_categories.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.CategoricalIndex.rename_categories.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.CategoricalIndex.rename_categories.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.CategoricalIndex.rename_categories.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.CategoricalIndex.rename_categories.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.CategoricalIndex.rename_categories.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.CategoricalIndex.rename_categories.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.CategoricalIndex.rename_categories.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.CategoricalIndex.rename_categories.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.CategoricalIndex.rename_categories.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.CategoricalIndex.rename_categories.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.CategoricalIndex.rename\_categories[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.rename_categories.html#pandas-categoricalindex-rename-categories "Link to this heading")

============================================================================================================================================================================================================

CategoricalIndex.rename\_categories(_new\_categories_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/category.py#L256-L324)
[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.rename_categories.html#pandas.CategoricalIndex.rename_categories "Link to this definition")

Rename categories.

This method is commonly used to re-label or adjust the category names in categorical data without changing the underlying data. It is useful in situations where you want to modify the labels used for clarity, consistency, or readability.

Parameters:

**new\_categories**list-like, dict-like or callable

New categories which will replace old categories.

*   list-like: all items must be unique and the number of items in the new categories must match the existing number of categories.
    
*   dict-like: specifies a mapping from old categories to new. Categories not contained in the mapping are passed through and extra categories in the mapping are ignored.
    
*   callable : a callable that is called on all items in the old categories and whose return values comprise the new categories.
    

Returns:

CategoricalIndex

CategoricalIndex with renamed categories.

Raises:

ValueError

If new categories are list-like and do not have the same number of items as the current categories or do not validate as categories

See also

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

\>>> ci \= pd.CategoricalIndex(\["a", "a", "b"\])
\>>> ci.rename\_categories(\[0, 1\])
CategoricalIndex(\[0, 0, 1\], categories=\[0, 1\], ordered=False, dtype='category')

Copy to clipboard

For dict-like `new_categories`, extra keys are ignored and categories not in the dictionary are passed through

\>>> ci.rename\_categories({"a": "A", "c": "C"})
CategoricalIndex(\['A', 'A', 'b'\], categories=\['A', 'b'\], ordered=False,
                 dtype='category')

Copy to clipboard

You may also provide a callable to create the new categories

\>>> ci.rename\_categories(lambda x: x.upper())
CategoricalIndex(\['A', 'A', 'B'\], categories=\['A', 'B'\], ordered=False,
                 dtype='category')

Copy to clipboard

On this page