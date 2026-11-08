[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Categorical.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Categorical.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Categorical.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Categorical.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Categorical.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Categorical.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Categorical.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Categorical.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Categorical.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Categorical.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Categorical.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Categorical.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Categorical[#](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html#pandas-categorical "Link to this heading")

======================================================================================================================================

class pandas.Categorical(_values_, _categories\=None_, _ordered\=None_, _dtype\=None_, _copy\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/categorical.py#L258-L3062)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html#pandas.Categorical "Link to this definition")

Represent a categorical variable in classic R / S-plus fashion.

Categoricals can only take on a limited, and usually fixed, number of possible values (categories). In contrast to statistical categorical variables, a Categorical might have an order, but numerical operations (additions, divisions, …) are not possible.

All values of the Categorical are either in categories or np.nan. Assigning values outside of categories will raise a ValueError. Order is defined by the order of the categories, not lexical order of the values.

Parameters:

**values**list-like

The values of the categorical. If categories are given, values not in categories will be replaced with NaN.

**categories**Index-like (unique), optional

The unique categories for this categorical. If not given, the categories are assumed to be the unique values of values (sorted, if possible, otherwise in the order in which they appear).

**ordered**bool, default False

Whether or not this categorical is treated as an ordered categorical. If True, the resulting categorical will be ordered. An ordered categorical respects, when sorted, the order of its categories attribute (which in turn is the categories argument, if provided).

**dtype**CategoricalDtype

An instance of `CategoricalDtype` to use for this categorical.

**copy**bool, default True

Whether to copy if the codes are unchanged.

Attributes

|     |     |
| --- | --- |
| [`categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.categories.html#pandas.Categorical.categories "pandas.Categorical.categories") | The categories of this categorical. |
| [`codes`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.codes.html#pandas.Categorical.codes "pandas.Categorical.codes") | The category codes of this categorical index. |
| [`ordered`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.ordered.html#pandas.Categorical.ordered "pandas.Categorical.ordered") | Whether the categories have an ordered relationship. |
| [`dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.dtype.html#pandas.Categorical.dtype "pandas.Categorical.dtype") | The `CategoricalDtype` for this instance. |

Methods

|     |     |
| --- | --- |
| [`from_codes`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.from_codes.html#pandas.Categorical.from_codes "pandas.Categorical.from_codes")<br>(codes\[, categories, ordered, ...\]) | Make a Categorical type from codes and categories or dtype. |
| [`as_ordered`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.as_ordered.html#pandas.Categorical.as_ordered "pandas.Categorical.as_ordered")<br>() | Set the Categorical to be ordered. |
| [`as_unordered`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.as_unordered.html#pandas.Categorical.as_unordered "pandas.Categorical.as_unordered")<br>() | Set the Categorical to be unordered. |
| [`set_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.set_categories.html#pandas.Categorical.set_categories "pandas.Categorical.set_categories")<br>(new\_categories\[, ordered, rename\]) | Set the categories to the specified new categories. |
| [`rename_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.rename_categories.html#pandas.Categorical.rename_categories "pandas.Categorical.rename_categories")<br>(new\_categories) | Rename categories. |
| [`reorder_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.reorder_categories.html#pandas.Categorical.reorder_categories "pandas.Categorical.reorder_categories")<br>(new\_categories\[, ordered\]) | Reorder categories as specified in new\_categories. |
| [`add_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.add_categories.html#pandas.Categorical.add_categories "pandas.Categorical.add_categories")<br>(new\_categories) | Add new categories. |
| [`remove_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.remove_categories.html#pandas.Categorical.remove_categories "pandas.Categorical.remove_categories")<br>(removals) | Remove the specified categories. |
| [`remove_unused_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.remove_unused_categories.html#pandas.Categorical.remove_unused_categories "pandas.Categorical.remove_unused_categories")<br>() | Remove categories which are not used. |
| [`map`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.map.html#pandas.Categorical.map "pandas.Categorical.map")<br>(mapper\[, na\_action\]) | Map categories using an input mapping or function. |
| [`__array__`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.__array__.html#pandas.Categorical.__array__ "pandas.Categorical.__array__")<br>(\[dtype, copy\]) | The numpy array interface. |

Raises:

ValueError

If the categories do not validate.

TypeError

If an explicit `ordered=True` is given but no categories and the values are not sortable.

See also

[`CategoricalDtype`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.html#pandas.CategoricalDtype "pandas.CategoricalDtype")

Type for categorical data.

[`CategoricalIndex`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.html#pandas.CategoricalIndex "pandas.CategoricalIndex")

An Index with an underlying `Categorical`.

Notes

See the [user guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html)
 for more.

Examples

\>>> pd.Categorical(\[1, 2, 3, 1, 2, 3\])
\[1, 2, 3, 1, 2, 3\]
Categories (3, int64): \[1, 2, 3\]

Copy to clipboard

\>>> pd.Categorical(\["a", "b", "c", "a", "b", "c"\])
\['a', 'b', 'c', 'a', 'b', 'c'\]
Categories (3, str): \['a', 'b', 'c'\]

Copy to clipboard

Missing values are not included as a category.

\>>> c \= pd.Categorical(\[1, 2, 3, 1, 2, 3, np.nan\])
\>>> c
\[1, 2, 3, 1, 2, 3, NaN\]
Categories (3, int64): \[1, 2, 3\]

Copy to clipboard

However, their presence is indicated in the codes attribute by code \-1.

\>>> c.codes
array(\[ 0,  1,  2,  0,  1,  2, -1\], dtype=int8)

Copy to clipboard

Ordered Categoricals can be sorted according to the custom order of the categories and can have a min and max value.

\>>> c \= pd.Categorical(
...     \["a", "b", "c", "a", "b", "c"\], ordered\=True, categories\=\["c", "b", "a"\]
... )
\>>> c
\['a', 'b', 'c', 'a', 'b', 'c'\]
Categories (3, str): \['c' < 'b' < 'a'\]
\>>> c.min()
'c'

Copy to clipboard

On this page