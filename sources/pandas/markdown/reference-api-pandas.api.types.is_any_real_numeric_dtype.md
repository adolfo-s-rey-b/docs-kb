[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_any_real_numeric_dtype.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.types.is_any_real_numeric_dtype.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_any_real_numeric_dtype.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.types.is_any_real_numeric_dtype.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.types.is_any_real_numeric_dtype.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.types.is_any_real_numeric_dtype.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.types.is_any_real_numeric_dtype.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.types.is_any_real_numeric_dtype.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.types.is_any_real_numeric_dtype.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.types.is_any_real_numeric_dtype.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.types.is_any_real_numeric_dtype.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.types.is_any_real_numeric_dtype.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.types.is_any_real_numeric_dtype.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.types.is_any_real_numeric_dtype.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_any\_real\_numeric\_dtype[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_any_real_numeric_dtype.html#pandas-api-types-is-any-real-numeric-dtype "Link to this heading")

==================================================================================================================================================================================================================

pandas.api.types.is\_any\_real\_numeric\_dtype(_arr\_or\_dtype_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/common.py#L1396-L1441)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_any_real_numeric_dtype.html#pandas.api.types.is_any_real_numeric_dtype "Link to this definition")

Check whether the provided array or dtype is of a real number dtype.

Real number dtypes include integer and float types but exclude complex and boolean dtypes. This is useful when operations require real-valued numeric input only.

Parameters:

**arr\_or\_dtype**array-like or dtype

The array or dtype to check.

Returns:

boolean

Whether or not the array or dtype is of a real number dtype.

See also

[`is_numeric_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_numeric_dtype.html#pandas.api.types.is_numeric_dtype "pandas.api.types.is_numeric_dtype")

Check if a dtype is numeric.

[`is_complex_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_complex_dtype.html#pandas.api.types.is_complex_dtype "pandas.api.types.is_complex_dtype")

Check if a dtype is complex.

[`is_bool_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_bool_dtype.html#pandas.api.types.is_bool_dtype "pandas.api.types.is_bool_dtype")

Check if a dtype is boolean.

Examples

\>>> from pandas.api.types import is\_any\_real\_numeric\_dtype
\>>> is\_any\_real\_numeric\_dtype(int)
True
\>>> is\_any\_real\_numeric\_dtype(float)
True
\>>> is\_any\_real\_numeric\_dtype(object)
False
\>>> is\_any\_real\_numeric\_dtype(str)
False
\>>> is\_any\_real\_numeric\_dtype(complex(1, 2))
False
\>>> is\_any\_real\_numeric\_dtype(bool)
False

Copy to clipboard

On this page