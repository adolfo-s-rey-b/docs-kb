[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.rename_categories.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.cat.rename_categories.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.rename_categories.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.cat.rename_categories.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.cat.rename_categories.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.cat.rename_categories.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.cat.rename_categories.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.cat.rename_categories.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.cat.rename_categories.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.cat.rename_categories.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.cat.rename_categories.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.cat.rename_categories.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.cat.rename_categories.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.cat.rename_categories.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.cat.rename\_categories[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.rename_categories.html#pandas-series-cat-rename-categories "Link to this heading")

==========================================================================================================================================================================================

Series.cat.rename\_categories(_new\_categories_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/categorical.py#L1358-L1435)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.rename_categories.html#pandas.Series.cat.rename_categories "Link to this definition")

Rename categories.

This method is commonly used to re-label or adjust the category names in categorical data without changing the underlying data. It is useful in situations where you want to modify the labels used for clarity, consistency, or readability.

Parameters:

**new\_categories**list-like, dict-like or callable

New categories which will replace old categories.

*   list-like: all items must be unique and the number of items in the new categories must match the existing number of categories.
    
*   dict-like: specifies a mapping from old categories to new. Categories not contained in the mapping are passed through and extra categories in the mapping are ignored.
    
*   callable : a callable that is called on all items in the old categories and whose return values comprise the new categories.
    

Returns:

Categorical

Categorical with renamed categories.

Raises:

ValueError

If new categories are list-like and do not have the same number of items than the current categories or do not validate as categories

See also

[`reorder_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.reorder_categories.html#pandas.Series.cat.reorder_categories "pandas.Series.cat.reorder_categories")

Reorder categories.

[`add_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.add_categories.html#pandas.Series.cat.add_categories "pandas.Series.cat.add_categories")

Add new categories.

[`remove_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.remove_categories.html#pandas.Series.cat.remove_categories "pandas.Series.cat.remove_categories")

Remove the specified categories.

[`remove_unused_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.remove_unused_categories.html#pandas.Series.cat.remove_unused_categories "pandas.Series.cat.remove_unused_categories")

Remove categories which are not used.

[`set_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.set_categories.html#pandas.Series.cat.set_categories "pandas.Series.cat.set_categories")

Set the categories to the specified ones.

[`Series.replace`](https://pandas.pydata.org/docs/reference/api/pandas.Series.replace.html#pandas.Series.replace "pandas.Series.replace")

Replace values, e.g. to merge several categories into one.

Examples

\>>> c \= pd.Categorical(\["a", "a", "b"\])
\>>> c.rename\_categories(\[0, 1\])
\[0, 0, 1\]
Categories (2, int64): \[0, 1\]

Copy to clipboard

For dict-like `new_categories`, extra keys are ignored and categories not in the dictionary are passed through

\>>> c.rename\_categories({"a": "A", "c": "C"})
\['A', 'A', 'b'\]
Categories (2, str): \['A', 'b'\]

Copy to clipboard

You may also provide a callable to create the new categories

\>>> c.rename\_categories(lambda x: x.upper())
\['A', 'A', 'B'\]
Categories (2, str): \['A', 'B'\]

Copy to clipboard

On this page