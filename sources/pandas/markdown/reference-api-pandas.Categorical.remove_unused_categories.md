[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.remove_unused_categories.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Categorical.remove_unused_categories.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.remove_unused_categories.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Categorical.remove_unused_categories.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Categorical.remove_unused_categories.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Categorical.remove_unused_categories.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Categorical.remove_unused_categories.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Categorical.remove_unused_categories.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Categorical.remove_unused_categories.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Categorical.remove_unused_categories.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Categorical.remove_unused_categories.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Categorical.remove_unused_categories.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Categorical.remove_unused_categories.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Categorical.remove_unused_categories.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Categorical.remove\_unused\_categories[#](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.remove_unused_categories.html#pandas-categorical-remove-unused-categories "Link to this heading")

===================================================================================================================================================================================================================

Categorical.remove\_unused\_categories()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/categorical.py#L1641-L1692)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.remove_unused_categories.html#pandas.Categorical.remove_unused_categories "Link to this definition")

Remove categories which are not used.

This method is useful when working with datasets that undergo dynamic changes where categories may no longer be relevant, allowing to maintain a clean, efficient data structure.

Returns:

Categorical

Categorical with unused categories dropped.

See also

[`rename_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.rename_categories.html#pandas.Categorical.rename_categories "pandas.Categorical.rename_categories")

Rename categories.

[`reorder_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.reorder_categories.html#pandas.Categorical.reorder_categories "pandas.Categorical.reorder_categories")

Reorder categories.

[`add_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.add_categories.html#pandas.Categorical.add_categories "pandas.Categorical.add_categories")

Add new categories.

[`remove_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.remove_categories.html#pandas.Categorical.remove_categories "pandas.Categorical.remove_categories")

Remove the specified categories.

[`set_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.set_categories.html#pandas.Categorical.set_categories "pandas.Categorical.set_categories")

Set the categories to the specified ones.

Examples

\>>> c \= pd.Categorical(\["a", "c", "b", "c", "d"\])
\>>> c
\['a', 'c', 'b', 'c', 'd'\]
Categories (4, str): \['a', 'b', 'c', 'd'\]

Copy to clipboard

\>>> c\[2\] \= "a"
\>>> c\[4\] \= "c"
\>>> c
\['a', 'c', 'a', 'c', 'c'\]
Categories (4, str): \['a', 'b', 'c', 'd'\]

Copy to clipboard

\>>> c.remove\_unused\_categories()
\['a', 'c', 'a', 'c', 'c'\]
Categories (2, str): \['a', 'c'\]

Copy to clipboard

On this page