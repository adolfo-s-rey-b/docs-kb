[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.reshape.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ndarray.reshape[#](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.reshape.html#numpy-ndarray-reshape "Link to this heading")

===================================================================================================================================================

method

ndarray.reshape(_shape_, _/_, _\*_, _order='C'_, _copy=None) a.reshape(\*shape_, _order='C'_, _copy=None_)[#](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.reshape.html#numpy.ndarray.reshape "Link to this definition")

ndarray.reshape(_\*shape_, _order\='C'_, _copy\=None_) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")

Returns an array containing the same data with a new shape.

Refer to [`numpy.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape")
 for full documentation.

See also

[`numpy.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape")

equivalent function

Notes

Unlike the free function [`numpy.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape")
, this method on [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 allows the elements of the shape parameter to be passed in as separate arguments. For example, `a.reshape(4, 2)` is equivalent to `a.reshape((4, 2))`.

On this page