[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.unravel_index.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.unravel_index.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.unravel_index.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.unravel_index.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.unravel_index.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.unravel_index.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.unravel_index.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.unravel_index.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.unravel_index.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.unravel_index.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.unravel_index.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.unravel_index.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.unravel_index.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.unravel_index.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.unravel_index.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.unravel_index.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.unravel_index.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.unravel_index.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.unravel_index.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.unravel_index.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.unravel_index.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.unravel_index.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.unravel\_index[#](https://numpy.org/doc/stable/reference/generated/numpy.unravel_index.html#numpy-unravel-index "Link to this heading")

==============================================================================================================================================

numpy.unravel\_index(_indices_, _shape_, _order\='C'_)[#](https://numpy.org/doc/stable/reference/generated/numpy.unravel_index.html#numpy.unravel_index "Link to this definition")

Converts a flat index or array of flat indices into a tuple of coordinate arrays.

Parameters:

**indices**array\_like

An integer array whose elements are indices into the flattened version of an array of dimensions `shape`. Before version 1.6.0, this function accepted just one index value.

**shape**tuple of ints

The shape of the array to use for unraveling `indices`.

**order**{‘C’, ‘F’}, optional

Determines whether the indices should be viewed as indexing in row-major (C-style) or column-major (Fortran-style) order.

Returns:

**unraveled\_coords**tuple of ndarray

Each array in the tuple has the same shape as the `indices` array.

See also

[`ravel_multi_index`](https://numpy.org/doc/stable/reference/generated/numpy.ravel_multi_index.html#numpy.ravel_multi_index "numpy.ravel_multi_index")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.unravel\_index(\[22, 41, 37\], (7,6))
(array(\[3, 6, 6\]), array(\[4, 5, 1\]))
\>>> np.unravel\_index(\[31, 41, 13\], (7,6), order\='F')
(array(\[3, 6, 6\]), array(\[4, 5, 1\]))

Copy to clipboard

\>>> np.unravel\_index(1621, (6,7,8,9))
(3, 1, 4, 1)

Copy to clipboard

Go BackOpen In Tab

On this page