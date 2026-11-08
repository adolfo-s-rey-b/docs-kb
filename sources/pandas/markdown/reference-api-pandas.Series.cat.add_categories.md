[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.add_categories.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.cat.add_categories.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.add_categories.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.cat.add_categories.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.cat.add_categories.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.cat.add_categories.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.cat.add_categories.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.cat.add_categories.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.cat.add_categories.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.cat.add_categories.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.cat.add_categories.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.cat.add_categories.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.cat.add_categories.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.cat.add_categories.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.cat.add\_categories[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.add_categories.html#pandas-series-cat-add-categories "Link to this heading")

=================================================================================================================================================================================

Series.cat.add\_categories(_new\_categories_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/categorical.py#L1512-L1579)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.add_categories.html#pandas.Series.cat.add_categories "Link to this definition")

Add new categories.

new\_categories will be included at the last/highest place in the categories and will be unused directly after this call.

Parameters:

**new\_categories**category or list-like of category

The new categories to be included.

Returns:

Categorical

Categorical with new categories added.

Raises:

ValueError

If the new categories include old categories or do not validate as categories

See also

[`rename_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.rename_categories.html#pandas.Series.cat.rename_categories "pandas.Series.cat.rename_categories")

Rename categories.

[`reorder_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.reorder_categories.html#pandas.Series.cat.reorder_categories "pandas.Series.cat.reorder_categories")

Reorder categories.

[`remove_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.remove_categories.html#pandas.Series.cat.remove_categories "pandas.Series.cat.remove_categories")

Remove the specified categories.

[`remove_unused_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.remove_unused_categories.html#pandas.Series.cat.remove_unused_categories "pandas.Series.cat.remove_unused_categories")

Remove categories which are not used.

[`set_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.set_categories.html#pandas.Series.cat.set_categories "pandas.Series.cat.set_categories")

Set the categories to the specified ones.

Examples

\>>> c \= pd.Categorical(\["c", "b", "c"\])
\>>> c
\['c', 'b', 'c'\]
Categories (2, str): \['b', 'c'\]

Copy to clipboard

\>>> c.add\_categories(\["d", "a"\])
\['c', 'b', 'c'\]
Categories (4, str): \['b', 'c', 'd', 'a'\]

Copy to clipboard

On this page