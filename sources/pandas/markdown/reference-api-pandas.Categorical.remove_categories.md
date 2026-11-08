[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.remove_categories.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Categorical.remove\_categories[#](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.remove_categories.html#pandas-categorical-remove-categories "Link to this heading")

=============================================================================================================================================================================================

Categorical.remove\_categories(_removals_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/categorical.py#L1581-L1639)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.remove_categories.html#pandas.Categorical.remove_categories "Link to this definition")

Remove the specified categories.

The `removals` argument must be a subset of the current categories. Any values that were part of the removed categories will be set to NaN.

Parameters:

**removals**category or list of categories

The categories which should be removed.

Returns:

Categorical

Categorical with removed categories.

Raises:

ValueError

If the removals are not contained in the categories

See also

[`rename_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.rename_categories.html#pandas.Categorical.rename_categories "pandas.Categorical.rename_categories")

Rename categories.

[`reorder_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.reorder_categories.html#pandas.Categorical.reorder_categories "pandas.Categorical.reorder_categories")

Reorder categories.

[`add_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.add_categories.html#pandas.Categorical.add_categories "pandas.Categorical.add_categories")

Add new categories.

[`remove_unused_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.remove_unused_categories.html#pandas.Categorical.remove_unused_categories "pandas.Categorical.remove_unused_categories")

Remove categories which are not used.

[`set_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.set_categories.html#pandas.Categorical.set_categories "pandas.Categorical.set_categories")

Set the categories to the specified ones.

Examples

\>>> c \= pd.Categorical(\["a", "c", "b", "c", "d"\])
\>>> c
\['a', 'c', 'b', 'c', 'd'\]
Categories (4, str): \['a', 'b', 'c', 'd'\]

Copy to clipboard

\>>> c.remove\_categories(\["d", "a"\])
\[NaN, 'c', 'b', 'c', NaN\]
Categories (2, str): \['b', 'c'\]

Copy to clipboard

On this page