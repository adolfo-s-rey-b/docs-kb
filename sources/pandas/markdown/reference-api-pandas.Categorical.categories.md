[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.categories.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Categorical.categories.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.categories.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Categorical.categories.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Categorical.categories.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Categorical.categories.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Categorical.categories.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Categorical.categories.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Categorical.categories.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Categorical.categories.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Categorical.categories.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Categorical.categories.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Categorical.categories.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Categorical.categories.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Categorical.categories[#](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.categories.html#pandas-categorical-categories "Link to this heading")

=======================================================================================================================================================================

property Categorical.categories[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/categorical.py#L951-L1007)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.categories.html#pandas.Categorical.categories "Link to this definition")

The categories of this categorical.

Setting assigns new values to each category (effectively a rename of each individual category).

The assigned value has to be a list-like object. All items must be unique and the number of items in the new categories must be the same as the number of items in the old categories.

Raises:

ValueError

If the new categories do not validate as categories or if the number of new categories is unequal the number of old categories

See also

[`rename_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.rename_categories.html#pandas.Categorical.rename_categories "pandas.Categorical.rename_categories")

Rename categories.

[`reorder_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.reorder_categories.html#pandas.Categorical.reorder_categories "pandas.Categorical.reorder_categories")

Reorder categories.

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
\>>> ser.cat.categories
Index(\['a', 'b', 'c'\], dtype='str')

Copy to clipboard

\>>> raw\_cat \= pd.Categorical(\[None, "b", "c", None\], categories\=\["b", "c", "d"\])
\>>> ser \= pd.Series(raw\_cat)
\>>> ser.cat.categories
Index(\['b', 'c', 'd'\], dtype='str')

Copy to clipboard

For [`pandas.Categorical`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html#pandas.Categorical "pandas.Categorical")
:

\>>> cat \= pd.Categorical(\["a", "b"\], ordered\=True)
\>>> cat.categories
Index(\['a', 'b'\], dtype='str')

Copy to clipboard

For [`pandas.CategoricalIndex`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.html#pandas.CategoricalIndex "pandas.CategoricalIndex")
:

\>>> ci \= pd.CategoricalIndex(\["a", "c", "b", "a", "c", "b"\])
\>>> ci.categories
Index(\['a', 'b', 'c'\], dtype='str')

Copy to clipboard

\>>> ci \= pd.CategoricalIndex(\["a", "c"\], categories\=\["c", "b", "a"\])
\>>> ci.categories
Index(\['c', 'b', 'a'\], dtype='str')

Copy to clipboard

On this page