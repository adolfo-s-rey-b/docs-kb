[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_number.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_number[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_number.html#pandas-api-types-is-number "Link to this heading")

===============================================================================================================================================================

pandas.api.types.is\_number(_obj_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/inference.py#L40-L79)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_number.html#pandas.api.types.is_number "Link to this definition")

Check if the object is a number.

Returns True when the object is a number, and False if is not.

Parameters:

**obj**any type

The object to check if is a number.

Returns:

bool

Whether obj is a number or not.

See also

`api.types.is_integer`

Checks a subgroup of numbers.

Examples

\>>> from pandas.api.types import is\_number
\>>> is\_number(1)
True
\>>> is\_number(7.15)
True

Copy to clipboard

Booleans are valid because they are int subclass.

\>>> is\_number(False)
True

Copy to clipboard

\>>> is\_number("foo")
False
\>>> is\_number("5")
False

Copy to clipboard

On this page