[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_categorical_dtype.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_categorical\_dtype[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_categorical_dtype.html#pandas-api-types-is-categorical-dtype "Link to this heading")

=================================================================================================================================================================================================

pandas.api.types.is\_categorical\_dtype(_arr\_or\_dtype_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/common.py#L598-L650)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_categorical_dtype.html#pandas.api.types.is_categorical_dtype "Link to this definition")

Check whether an array-like or dtype is of the Categorical dtype.

Deprecated since version 2.2.0: Use isinstance(dtype, pd.CategoricalDtype) instead.

Parameters:

**arr\_or\_dtype**array-like or dtype

The array-like or dtype to check.

Returns:

boolean

Whether or not the array-like or dtype is of the Categorical dtype.

See also

`api.types.is_list_like`

Check if the object is list-like.

`api.types.is_complex_dtype`

Check whether the provided array or dtype is of a complex dtype.

Examples

\>>> from pandas.api.types import is\_categorical\_dtype
\>>> from pandas import CategoricalDtype
\>>> is\_categorical\_dtype(object)
False
\>>> is\_categorical\_dtype(CategoricalDtype())
True
\>>> is\_categorical\_dtype(\[1, 2, 3\])
False
\>>> is\_categorical\_dtype(pd.Categorical(\[1, 2, 3\]))
True
\>>> is\_categorical\_dtype(pd.CategoricalIndex(\[1, 2, 3\]))
True

Copy to clipboard

On this page