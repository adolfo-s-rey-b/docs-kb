[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_no_warnings.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.testing.assert\_no\_warnings[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_no_warnings.html#numpy-testing-assert-no-warnings "Link to this heading")

======================================================================================================================================================================================

testing.assert\_no\_warnings(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/testing/_private/utils.py#L2080-L2111)
[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_no_warnings.html#numpy.testing.assert_no_warnings "Link to this definition")

Fail if the given callable produces any warnings.

If called with all arguments omitted, may be used as a context manager:

with assert\_no\_warnings():
    do\_something()

Copy to clipboard

The ability to be used as a context manager is new in NumPy v1.11.0.

Parameters:

**func**callable

The callable to test.

**\*args**Arguments

Arguments passed to _func_.

**\*\*kwargs**Kwargs

Keyword arguments passed to _func_.

Returns:

The value returned by _func_.

On this page