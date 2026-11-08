[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.remove_categories.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.cat.remove_categories.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.remove_categories.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.cat.remove_categories.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.cat.remove_categories.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.cat.remove_categories.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.cat.remove_categories.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.cat.remove_categories.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.cat.remove_categories.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.cat.remove_categories.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.cat.remove_categories.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.cat.remove_categories.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.cat.remove_categories.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.cat.remove_categories.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.cat.remove\_categories[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.remove_categories.html#pandas-series-cat-remove-categories "Link to this heading")

==========================================================================================================================================================================================

Series.cat.remove\_categories(_removals_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/categorical.py#L1581-L1639)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.remove_categories.html#pandas.Series.cat.remove_categories "Link to this definition")

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

[`rename_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.rename_categories.html#pandas.Series.cat.rename_categories "pandas.Series.cat.rename_categories")

Rename categories.

[`reorder_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.reorder_categories.html#pandas.Series.cat.reorder_categories "pandas.Series.cat.reorder_categories")

Reorder categories.

[`add_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.add_categories.html#pandas.Series.cat.add_categories "pandas.Series.cat.add_categories")

Add new categories.

[`remove_unused_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.remove_unused_categories.html#pandas.Series.cat.remove_unused_categories "pandas.Series.cat.remove_unused_categories")

Remove categories which are not used.

[`set_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.set_categories.html#pandas.Series.cat.set_categories "pandas.Series.cat.set_categories")

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