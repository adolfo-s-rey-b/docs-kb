[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_dtype_equal.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.types.is_dtype_equal.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_dtype_equal.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.types.is_dtype_equal.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.types.is_dtype_equal.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.types.is_dtype_equal.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.types.is_dtype_equal.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.types.is_dtype_equal.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.types.is_dtype_equal.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.types.is_dtype_equal.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.types.is_dtype_equal.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.types.is_dtype_equal.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.types.is_dtype_equal.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.types.is_dtype_equal.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_dtype\_equal[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_dtype_equal.html#pandas-api-types-is-dtype-equal "Link to this heading")

===============================================================================================================================================================================

pandas.api.types.is\_dtype\_equal(_source_, _target_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/common.py#L713-L779)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_dtype_equal.html#pandas.api.types.is_dtype_equal "Link to this definition")

Check if two dtypes are equal.

This function compares two dtype specifications, handling both NumPy dtypes and pandas ExtensionDtypes. String representations of dtypes are also supported and will be resolved before comparison.

Parameters:

**source**type or str

The first dtype to compare.

**target**type or str

The second dtype to compare.

Returns:

boolean

Whether or not the two dtypes are equal.

See also

`api.types.is_categorical_dtype`

Check whether the provided array or dtype is of the Categorical dtype.

`api.types.is_string_dtype`

Check whether the provided array or dtype is of the string dtype.

`api.types.is_object_dtype`

Check whether an array-like or dtype is of the object dtype.

Examples

\>>> from pandas.api.types import is\_dtype\_equal
\>>> is\_dtype\_equal(int, float)
False
\>>> is\_dtype\_equal("int", int)
True
\>>> is\_dtype\_equal(object, "category")
False
\>>> from pandas.api.types import CategoricalDtype
\>>> is\_dtype\_equal(CategoricalDtype(), "category")
True
\>>> from pandas.api.types import DatetimeTZDtype
\>>> is\_dtype\_equal(DatetimeTZDtype(tz\="UTC"), "datetime64")
False

Copy to clipboard

On this page