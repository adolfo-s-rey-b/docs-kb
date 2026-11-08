[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.testing.overrides.allows_array_function_override.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.testing.overrides.allows\_array\_function\_override[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.overrides.allows_array_function_override.html#numpy-testing-overrides-allows-array-function-override "Link to this heading")

=========================================================================================================================================================================================================================================================

testing.overrides.allows\_array\_function\_override(_func_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/testing/overrides.py#L70-L84)
[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.overrides.allows_array_function_override.html#numpy.testing.overrides.allows_array_function_override "Link to this definition")

Determine if a Numpy function can be overridden via _\_\_array\_function\_\__

Parameters:

**func**callable

Function that may be overridable via _\_\_array\_function\_\__

Returns:

bool

_True_ if _func_ is a function in the Numpy API that is overridable via _\_\_array\_function\_\__ and _False_ otherwise.

On this page