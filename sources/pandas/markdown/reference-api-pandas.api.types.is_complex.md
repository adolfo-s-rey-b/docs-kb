[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_complex.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_complex[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_complex.html#pandas-api-types-is-complex "Link to this heading")

==================================================================================================================================================================

pandas.api.types.is\_complex(_obj_)[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_complex.html#pandas.api.types.is_complex "Link to this definition")

Return True if given object is complex.

This function checks whether `obj` is an instance of Python’s built-in `complex` type or numpy’s complex type (e.g., `numpy.complex128`).

Parameters:

**obj**object

Object to check.

Returns:

bool

See also

`api.types.is_complex_dtype`

Check whether the provided array or dtype is of a complex dtype.

`api.types.is_number`

Check if the object is a number.

`api.types.is_integer`

Return True if given object is integer.

Examples

\>>> pd.api.types.is\_complex(1 + 1j)
True

Copy to clipboard

\>>> pd.api.types.is\_complex(1)
False

Copy to clipboard

On this page