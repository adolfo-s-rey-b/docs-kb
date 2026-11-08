[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_integer.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.types.is_integer.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_integer.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.types.is_integer.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.types.is_integer.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.types.is_integer.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.types.is_integer.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.types.is_integer.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.types.is_integer.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.types.is_integer.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.types.is_integer.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.types.is_integer.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.types.is_integer.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.types.is_integer.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_integer[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_integer.html#pandas-api-types-is-integer "Link to this heading")

==================================================================================================================================================================

pandas.api.types.is\_integer(_obj_)[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_integer.html#pandas.api.types.is_integer "Link to this definition")

Return True if given object is integer.

This method checks whether the passed object is an integer type. It returns True if the object is an integer, and False otherwise.

Parameters:

**obj**object

The object to check for integer type.

Returns:

bool

True if the object is of integer type, otherwise False.

See also

`api.types.is_float`

Check if an object is of float type.

`api.types.is_numeric_dtype`

Check if an object is of numeric type.

Examples

\>>> pd.api.types.is\_integer(1)
True

Copy to clipboard

\>>> pd.api.types.is\_integer(1.0)
False

Copy to clipboard

On this page