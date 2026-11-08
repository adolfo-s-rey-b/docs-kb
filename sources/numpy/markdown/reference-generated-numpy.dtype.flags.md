[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.dtype.flags.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.dtype.flags.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.dtype.flags.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.dtype.flags.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.dtype.flags.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.dtype.flags.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.dtype.flags.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.dtype.flags.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.dtype.flags.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.dtype.flags.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.dtype.flags.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.dtype.flags.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.dtype.flags.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.dtype.flags.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.dtype.flags.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.dtype.flags.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.dtype.flags.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.dtype.flags.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.dtype.flags.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.dtype.flags.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.dtype.flags.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.dtype.flags.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.dtype.flags[#](https://numpy.org/doc/stable/reference/generated/numpy.dtype.flags.html#numpy-dtype-flags "Link to this heading")

=======================================================================================================================================

attribute

dtype.flags[#](https://numpy.org/doc/stable/reference/generated/numpy.dtype.flags.html#numpy.dtype.flags "Link to this definition")

Bit-flags describing how this data type is to be interpreted.

Bit-masks are in `numpy._core.multiarray` as the constants _ITEM\_HASOBJECT_, _LIST\_PICKLE_, _ITEM\_IS\_POINTER_, _NEEDS\_INIT_, _NEEDS\_PYAPI_, _USE\_GETITEM_, _USE\_SETITEM_. A full explanation of these flags is in C-API documentation; they are largely useful for user-defined data-types.

The following example demonstrates that operations on this particular dtype requires Python C-API.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.dtype(\[('a', np.int32, 8), ('b', np.float64, 6)\])
\>>> x.flags
16
\>>> np.\_core.multiarray.NEEDS\_PYAPI
16

Copy to clipboard

Go BackOpen In Tab

On this page