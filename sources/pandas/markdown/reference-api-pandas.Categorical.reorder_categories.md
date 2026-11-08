[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.reorder_categories.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Categorical.reorder_categories.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.reorder_categories.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Categorical.reorder_categories.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Categorical.reorder_categories.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Categorical.reorder_categories.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Categorical.reorder_categories.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Categorical.reorder_categories.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Categorical.reorder_categories.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Categorical.reorder_categories.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Categorical.reorder_categories.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Categorical.reorder_categories.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Categorical.reorder_categories.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Categorical.reorder_categories.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Categorical.reorder\_categories[#](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.reorder_categories.html#pandas-categorical-reorder-categories "Link to this heading")

================================================================================================================================================================================================

Categorical.reorder\_categories(_new\_categories_, _ordered\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/categorical.py#L1437-L1510)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.reorder_categories.html#pandas.Categorical.reorder_categories "Link to this definition")

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

[`rename_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.rename_categories.html#pandas.Categorical.rename_categories "pandas.Categorical.rename_categories")

Rename categories.

[`add_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.add_categories.html#pandas.Categorical.add_categories "pandas.Categorical.add_categories")

Add new categories.

[`remove_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.remove_categories.html#pandas.Categorical.remove_categories "pandas.Categorical.remove_categories")

Remove the specified categories.

[`remove_unused_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.remove_unused_categories.html#pandas.Categorical.remove_unused_categories "pandas.Categorical.remove_unused_categories")

Remove categories which are not used.

[`set_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.set_categories.html#pandas.Categorical.set_categories "pandas.Categorical.set_categories")

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