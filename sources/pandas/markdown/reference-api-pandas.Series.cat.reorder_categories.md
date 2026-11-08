[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.reorder_categories.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.cat.reorder\_categories[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.reorder_categories.html#pandas-series-cat-reorder-categories "Link to this heading")

=============================================================================================================================================================================================

Series.cat.reorder\_categories(_new\_categories_, _ordered\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/categorical.py#L1437-L1510)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.reorder_categories.html#pandas.Series.cat.reorder_categories "Link to this definition")

Reorder categories as specified in new\_categories.

`new_categories` need to include all old categories and no new category items.

Parameters:

**new\_categories**Index-like

The categories in new order.

**ordered**bool, optional

Whether or not the categorical is treated as an ordered categorical. If not given, do not change the ordered information.

Returns:

Categorical

Categorical with reordered categories.

Raises:

ValueError

If the new categories do not contain all old category items or any new ones

See also

[`rename_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.rename_categories.html#pandas.Series.cat.rename_categories "pandas.Series.cat.rename_categories")

Rename categories.

[`add_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.add_categories.html#pandas.Series.cat.add_categories "pandas.Series.cat.add_categories")

Add new categories.

[`remove_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.remove_categories.html#pandas.Series.cat.remove_categories "pandas.Series.cat.remove_categories")

Remove the specified categories.

[`remove_unused_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.remove_unused_categories.html#pandas.Series.cat.remove_unused_categories "pandas.Series.cat.remove_unused_categories")

Remove categories which are not used.

[`set_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.set_categories.html#pandas.Series.cat.set_categories "pandas.Series.cat.set_categories")

Set the categories to the specified ones.

Examples

For [`pandas.Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
:

\>>> ser \= pd.Series(\["a", "b", "c", "a"\], dtype\="category")
\>>> ser \= ser.cat.reorder\_categories(\["c", "b", "a"\], ordered\=True)
\>>> ser
0   a
1   b
2   c
3   a
dtype: category
Categories (3, str): \['c' < 'b' < 'a'\]

Copy to clipboard

\>>> ser.sort\_values()
2   c
1   b
0   a
3   a
dtype: category
Categories (3, str): \['c' < 'b' < 'a'\]

Copy to clipboard

For [`pandas.CategoricalIndex`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.html#pandas.CategoricalIndex "pandas.CategoricalIndex")
:

\>>> ci \= pd.CategoricalIndex(\["a", "b", "c", "a"\])
\>>> ci
CategoricalIndex(\['a', 'b', 'c', 'a'\], categories=\['a', 'b', 'c'\],
                 ordered=False, dtype='category')
\>>> ci.reorder\_categories(\["c", "b", "a"\], ordered\=True)
CategoricalIndex(\['a', 'b', 'c', 'a'\], categories=\['c', 'b', 'a'\],
                 ordered=True, dtype='category')

Copy to clipboard

On this page