[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.CategoricalIndex[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.html#pandas-categoricalindex "Link to this heading")

=====================================================================================================================================================

class pandas.CategoricalIndex(_data\=None_, _categories\=None_, _ordered\=None_, _dtype\=None_, _copy\=False_, _name\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/category.py#L56-L1110)
[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.html#pandas.CategoricalIndex "Link to this definition")

Index based on an underlying [`Categorical`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html#pandas.Categorical "pandas.Categorical")
.

CategoricalIndex, like Categorical, can only take on a limited, and usually fixed, number of possible values (categories). Also, like Categorical, it might have an order, but numerical operations (additions, divisions, …) are not possible.

Parameters:

**data**array-like (1-dimensional)

The values of the categorical. If categories are given, values not in categories will be replaced with NaN.

**categories**index-like, optional

The categories for the categorical. Items need to be unique. If the categories are not given here (and also not in dtype), they will be inferred from the data.

**ordered**bool, optional

Whether or not this categorical is treated as an ordered categorical. If not given here or in dtype, the resulting categorical will be unordered.

**dtype**CategoricalDtype or “category”, optional

If [`CategoricalDtype`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.html#pandas.CategoricalDtype "pandas.CategoricalDtype")
, cannot be used together with categories or ordered.

**copy**bool, default False

Make a copy of input ndarray.

**name**object, optional

Name to be stored in the index.

Attributes

|     |     |
| --- | --- |
| [`codes`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.codes.html#pandas.CategoricalIndex.codes "pandas.CategoricalIndex.codes") | The category codes of this categorical index. |
| [`categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.categories.html#pandas.CategoricalIndex.categories "pandas.CategoricalIndex.categories") | The categories of this CategoricalIndex. |
| [`ordered`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.ordered.html#pandas.CategoricalIndex.ordered "pandas.CategoricalIndex.ordered") | Whether the categories have an ordered relationship. |

Methods

|     |     |
| --- | --- |
| [`rename_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.rename_categories.html#pandas.CategoricalIndex.rename_categories "pandas.CategoricalIndex.rename_categories")<br>(new\_categories) | Rename categories. |
| [`reorder_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.reorder_categories.html#pandas.CategoricalIndex.reorder_categories "pandas.CategoricalIndex.reorder_categories")<br>(new\_categories\[, ordered\]) | Reorder categories as specified in new\_categories. |
| [`add_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.add_categories.html#pandas.CategoricalIndex.add_categories "pandas.CategoricalIndex.add_categories")<br>(new\_categories) | Add new categories. |
| [`remove_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.remove_categories.html#pandas.CategoricalIndex.remove_categories "pandas.CategoricalIndex.remove_categories")<br>(removals) | Remove the specified categories. |
| [`remove_unused_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.remove_unused_categories.html#pandas.CategoricalIndex.remove_unused_categories "pandas.CategoricalIndex.remove_unused_categories")<br>() | Remove categories which are not used. |
| [`set_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.set_categories.html#pandas.CategoricalIndex.set_categories "pandas.CategoricalIndex.set_categories")<br>(new\_categories\[, ordered, rename\]) | Set the categories to the specified new categories. |
| [`as_ordered`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.as_ordered.html#pandas.CategoricalIndex.as_ordered "pandas.CategoricalIndex.as_ordered")<br>() | Set the CategoricalIndex to be ordered. |
| [`as_unordered`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.as_unordered.html#pandas.CategoricalIndex.as_unordered "pandas.CategoricalIndex.as_unordered")<br>() | Set the CategoricalIndex to be unordered. |
| [`map`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.map.html#pandas.CategoricalIndex.map "pandas.CategoricalIndex.map")<br>(mapper\[, na\_action\]) | Map values using input an input mapping or function. |

Raises:

ValueError

If the categories do not validate.

TypeError

If an explicit `ordered=True` is given but no categories and the values are not sortable.

See also

[`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")

The base pandas Index type.

[`Categorical`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html#pandas.Categorical "pandas.Categorical")

A categorical array.

[`CategoricalDtype`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.html#pandas.CategoricalDtype "pandas.CategoricalDtype")

Type for categorical data.

Notes

See the [user guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#categoricalindex)
 for more.

Examples

\>>> pd.CategoricalIndex(\["a", "b", "c", "a", "b", "c"\])
CategoricalIndex(\['a', 'b', 'c', 'a', 'b', 'c'\],
                 categories=\['a', 'b', 'c'\], ordered=False, dtype='category')

Copy to clipboard

`CategoricalIndex` can also be instantiated from a `Categorical`:

\>>> c \= pd.Categorical(\["a", "b", "c", "a", "b", "c"\])
\>>> pd.CategoricalIndex(c)
CategoricalIndex(\['a', 'b', 'c', 'a', 'b', 'c'\],
                 categories=\['a', 'b', 'c'\], ordered=False, dtype='category')

Copy to clipboard

Ordered `CategoricalIndex` can have a min and max value.

\>>> ci \= pd.CategoricalIndex(
...     \["a", "b", "c", "a", "b", "c"\], ordered\=True, categories\=\["c", "b", "a"\]
... )
\>>> ci
CategoricalIndex(\['a', 'b', 'c', 'a', 'b', 'c'\],
                 categories=\['c', 'b', 'a'\], ordered=True, dtype='category')
\>>> ci.min()
'c'

Copy to clipboard

On this page