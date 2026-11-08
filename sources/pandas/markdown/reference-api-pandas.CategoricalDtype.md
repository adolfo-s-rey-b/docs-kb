[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.CategoricalDtype.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.CategoricalDtype.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.CategoricalDtype.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.CategoricalDtype.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.CategoricalDtype.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.CategoricalDtype.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.CategoricalDtype.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.CategoricalDtype.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.CategoricalDtype.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.CategoricalDtype.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.CategoricalDtype.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.CategoricalDtype.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.CategoricalDtype[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.html#pandas-categoricaldtype "Link to this heading")

=====================================================================================================================================================

class pandas.CategoricalDtype(_categories\=None_, _ordered\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/dtypes.py#L164-L719)
[#](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.html#pandas.CategoricalDtype "Link to this definition")

Type for categorical data with the categories and orderedness.

It is a dtype representation for categorical data, which allows users to define a fixed set of values and optionally impose an ordering. This is particularly useful for handling categorical variables efficiently, as it can significantly reduce memory usage compared to using object dtypes.

Parameters:

**categories**sequence, optional

Must be unique, and must not contain any nulls. The categories are stored in an Index, and if an index is provided the dtype of that index will be used.

**ordered**bool or None, default False

Whether or not this categorical is treated as an ordered categorical. None can be used to maintain the ordered value of existing categoricals when used in operations that combine categoricals, e.g. astype, and will resolve to False if there is no existing ordered to maintain.

Attributes

|     |     |
| --- | --- |
| [`categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.categories.html#pandas.CategoricalDtype.categories "pandas.CategoricalDtype.categories") | An `Index` containing the unique categories allowed. |
| [`ordered`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.ordered.html#pandas.CategoricalDtype.ordered "pandas.CategoricalDtype.ordered") | Whether the categories have an ordered relationship. |

See also

[`Categorical`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html#pandas.Categorical "pandas.Categorical")

Represent a categorical variable in classic R / S-plus fashion.

Notes

This class is useful for specifying the type of a `Categorical` independent of the values. See [CategoricalDtype](https://pandas.pydata.org/docs/user_guide/categorical.html#categorical-categoricaldtype)
 for more.

Examples

\>>> t \= pd.CategoricalDtype(categories\=\["b", "a"\], ordered\=True)
\>>> pd.Series(\["a", "b", "a", None\], dtype\=t)
0      a
1      b
2      a
3    NaN
dtype: category
Categories (2, str): \['b' < 'a'\]

Copy to clipboard

An empty CategoricalDtype with a specific dtype can be created by providing an empty index. As follows,

\>>> pd.CategoricalDtype(pd.DatetimeIndex(\[\])).categories.dtype
dtype('<M8\[s\]')

Copy to clipboard

On this page