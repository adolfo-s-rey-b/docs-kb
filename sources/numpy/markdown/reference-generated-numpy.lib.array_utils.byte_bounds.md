[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.array_utils.byte_bounds.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.lib.array_utils.byte_bounds.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.lib.array_utils.byte_bounds.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.lib.array_utils.byte_bounds.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.lib.array_utils.byte_bounds.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.lib.array_utils.byte_bounds.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.lib.array_utils.byte_bounds.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.lib.array_utils.byte_bounds.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.lib.array_utils.byte_bounds.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.lib.array_utils.byte_bounds.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.lib.array_utils.byte_bounds.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.lib.array_utils.byte_bounds.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.lib.array_utils.byte_bounds.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.lib.array_utils.byte_bounds.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.lib.array_utils.byte_bounds.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.lib.array_utils.byte_bounds.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.lib.array_utils.byte_bounds.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.lib.array_utils.byte_bounds.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.lib.array_utils.byte_bounds.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.lib.array_utils.byte_bounds.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.lib.array_utils.byte_bounds.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.lib.array_utils.byte_bounds.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.array\_utils.byte\_bounds[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.array_utils.byte_bounds.html#numpy-lib-array-utils-byte-bounds "Link to this heading")

=========================================================================================================================================================================================

lib.array\_utils.byte\_bounds(_a_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_array_utils_impl.py#L11-L62)
[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.array_utils.byte_bounds.html#numpy.lib.array_utils.byte_bounds "Link to this definition")

Returns pointers to the end-points of an array.

Parameters:

**a**ndarray

Input array. It must conform to the Python-side of the array interface.

Returns:

**(low, high)**tuple of 2 integers

The first integer is the first byte of the array, the second integer is just past the last byte of the array. If _a_ is not contiguous it will not use every byte between the (_low_, _high_) values.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> I \= np.eye(2, dtype\=np.float32); I.dtype
dtype('float32')
\>>> low, high \= np.lib.array\_utils.byte\_bounds(I)
\>>> high \- low \== I.size\*I.itemsize
True
\>>> I \= np.eye(2); I.dtype
dtype('float64')
\>>> low, high \= np.lib.array\_utils.byte\_bounds(I)
\>>> high \- low \== I.size\*I.itemsize
True

Copy to clipboard

Go BackOpen In Tab

On this page