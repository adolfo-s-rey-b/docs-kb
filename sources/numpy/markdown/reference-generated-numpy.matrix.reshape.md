[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matrix.reshape.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.matrix.reshape.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.matrix.reshape.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.matrix.reshape.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.matrix.reshape.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.matrix.reshape.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.matrix.reshape.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.matrix.reshape.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.matrix.reshape.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.matrix.reshape.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.matrix.reshape.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.matrix.reshape.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.matrix.reshape.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.matrix.reshape.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.matrix.reshape.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.matrix.reshape.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.matrix.reshape.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.matrix.reshape.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.matrix.reshape.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.matrix.reshape.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.matrix.reshape.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.matrix.reshape.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matrix.reshape[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.reshape.html#numpy-matrix-reshape "Link to this heading")

================================================================================================================================================

method

matrix.reshape(_shape_, _/_, _\*_, _order='C'_, _copy=None) a.reshape(\*shape_, _order='C'_, _copy=None_)[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.reshape.html#numpy.matrix.reshape "Link to this definition")

matrix.reshape(_\*shape_, _order\='C'_, _copy\=None_) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")

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