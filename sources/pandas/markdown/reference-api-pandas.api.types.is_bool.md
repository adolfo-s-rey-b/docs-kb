[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_bool.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.types.is_bool.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_bool.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.types.is_bool.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.types.is_bool.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.types.is_bool.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.types.is_bool.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.types.is_bool.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.types.is_bool.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.types.is_bool.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.types.is_bool.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.types.is_bool.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.types.is_bool.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.types.is_bool.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_bool[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_bool.html#pandas-api-types-is-bool "Link to this heading")

=========================================================================================================================================================

pandas.api.types.is\_bool(_obj_)[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_bool.html#pandas.api.types.is_bool "Link to this definition")

Return True if given object is boolean.

This function checks whether `obj` is an instance of Python’s built-in `bool` type. It does not return True for numeric values like `0` or `1` that can evaluate as booleans.

Parameters:

**obj**object

Object to check.

Returns:

bool

See also

`api.types.is_scalar`

Check if the input is a scalar.

`api.types.is_integer`

Check if the input is an integer.

`api.types.is_float`

Check if the input is a float.

Examples

\>>> pd.api.types.is\_bool(True)
True

Copy to clipboard

\>>> pd.api.types.is\_bool(1)
False

Copy to clipboard

On this page