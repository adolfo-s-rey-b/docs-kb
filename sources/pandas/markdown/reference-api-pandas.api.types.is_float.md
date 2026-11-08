[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_float.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.types.is_float.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_float.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.types.is_float.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.types.is_float.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.types.is_float.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.types.is_float.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.types.is_float.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.types.is_float.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.types.is_float.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.types.is_float.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.types.is_float.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.types.is_float.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.types.is_float.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_float[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_float.html#pandas-api-types-is-float "Link to this heading")

============================================================================================================================================================

pandas.api.types.is\_float(_obj_)[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_float.html#pandas.api.types.is_float "Link to this definition")

Return True if given object is float.

This method checks whether the passed object is a float type. It returns True if the object is a float, and False otherwise.

Parameters:

**obj**object

The object to check for float type.

Returns:

bool

True if the object is of float type, otherwise False.

See also

`api.types.is_integer`

Check if an object is of integer type.

`api.types.is_numeric_dtype`

Check if an object is of numeric type.

Examples

\>>> pd.api.types.is\_float(1.0)
True

Copy to clipboard

\>>> pd.api.types.is\_float(1)
False

Copy to clipboard

On this page