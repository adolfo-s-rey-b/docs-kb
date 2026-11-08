[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_interval_dtype.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_interval\_dtype[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_interval_dtype.html#pandas-api-types-is-interval-dtype "Link to this heading")

========================================================================================================================================================================================

pandas.api.types.is\_interval\_dtype(_arr\_or\_dtype_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/common.py#L539-L595)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_interval_dtype.html#pandas.api.types.is_interval_dtype "Link to this definition")

Check whether an array-like or dtype is of the Interval dtype.

Deprecated since version 2.2.0: Use isinstance(dtype, pd.IntervalDtype) instead.

Parameters:

**arr\_or\_dtype**array-like or dtype

The array-like or dtype to check.

Returns:

boolean

Whether or not the array-like or dtype is of the Interval dtype.

See also

`api.types.is_object_dtype`

Check whether an array-like or dtype is of the object dtype.

`api.types.is_numeric_dtype`

Check whether the provided array or dtype is of a numeric dtype.

`api.types.is_categorical_dtype`

Check whether an array-like or dtype is of the Categorical dtype.

Examples

\>>> from pandas.api.types import is\_interval\_dtype
\>>> is\_interval\_dtype(object)
False
\>>> is\_interval\_dtype(pd.IntervalDtype())
True
\>>> is\_interval\_dtype(\[1, 2, 3\])
False
\>>>
\>>> interval \= pd.Interval(1, 2, closed\="right")
\>>> is\_interval\_dtype(interval)
False
\>>> is\_interval\_dtype(pd.IntervalIndex(\[interval\]))
True

Copy to clipboard

On this page