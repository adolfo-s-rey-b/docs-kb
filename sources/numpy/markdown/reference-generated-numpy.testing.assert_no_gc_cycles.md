[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_no_gc_cycles.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.testing.assert\_no\_gc\_cycles[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_no_gc_cycles.html#numpy-testing-assert-no-gc-cycles "Link to this heading")

==========================================================================================================================================================================================

testing.assert\_no\_gc\_cycles(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/testing/_private/utils.py#L2632-L2662)
[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_no_gc_cycles.html#numpy.testing.assert_no_gc_cycles "Link to this definition")

Fail if the given callable produces any reference cycles.

If called with all arguments omitted, may be used as a context manager:

with assert\_no\_gc\_cycles():
    do\_something()

Copy to clipboard

Parameters:

**func**callable

The callable to test.

**\*args**Arguments

Arguments passed to _func_.

**\*\*kwargs**Kwargs

Keyword arguments passed to _func_.

Returns:

Nothing. The result is deliberately discarded to ensure that all cycles

are found.

On this page