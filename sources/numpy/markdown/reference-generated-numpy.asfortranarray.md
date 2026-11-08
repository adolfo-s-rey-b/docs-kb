[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.asfortranarray.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.asfortranarray.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.asfortranarray.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.asfortranarray.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.asfortranarray.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.asfortranarray.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.asfortranarray.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.asfortranarray.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.asfortranarray.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.asfortranarray.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.asfortranarray.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.asfortranarray.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.asfortranarray.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.asfortranarray.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.asfortranarray.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.asfortranarray.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.asfortranarray.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.asfortranarray.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.asfortranarray.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.asfortranarray.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.asfortranarray.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.asfortranarray.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.asfortranarray[#](https://numpy.org/doc/stable/reference/generated/numpy.asfortranarray.html#numpy-asfortranarray "Link to this heading")

================================================================================================================================================

numpy.asfortranarray(_a_, _dtype\=None_, _\*_, _like\=None_)[#](https://numpy.org/doc/stable/reference/generated/numpy.asfortranarray.html#numpy.asfortranarray "Link to this definition")

Return an array (ndim >= 1) laid out in Fortran order in memory.

Parameters:

**a**array\_like

Input array.

**dtype**str or dtype object, optional

By default, the data-type is inferred from the input data.

**like**array\_like, optional

Reference object to allow the creation of arrays which are not NumPy arrays. If an array-like passed in as `like` supports the `__array_function__` protocol, the result will be defined by it. In this case, it ensures the creation of an array object compatible with that passed in via this argument.

New in version 1.20.0.

Returns:

**out**ndarray

The input _a_ in Fortran, or column-major, order.

See also

[`ascontiguousarray`](https://numpy.org/doc/stable/reference/generated/numpy.ascontiguousarray.html#numpy.ascontiguousarray "numpy.ascontiguousarray")

Convert input to a contiguous (C order) array.

[`asanyarray`](https://numpy.org/doc/stable/reference/generated/numpy.asanyarray.html#numpy.asanyarray "numpy.asanyarray")

Convert input to an ndarray with either row or column-major memory order.

[`require`](https://numpy.org/doc/stable/reference/generated/numpy.require.html#numpy.require "numpy.require")

Return an ndarray that satisfies requirements.

[`ndarray.flags`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flags.html#numpy.ndarray.flags "numpy.ndarray.flags")

Information about the memory layout of the array.

Examples

Try it in your browser!

Starting with a C-contiguous array:

\>>> import numpy as np
\>>> x \= np.ones((2, 3), order\='C')
\>>> x.flags\['C\_CONTIGUOUS'\]
True

Copy to clipboard

Calling `asfortranarray` makes a Fortran-contiguous copy:

\>>> y \= np.asfortranarray(x)
\>>> y.flags\['F\_CONTIGUOUS'\]
True
\>>> np.may\_share\_memory(x, y)
False

Copy to clipboard

Now, starting with a Fortran-contiguous array:

\>>> x \= np.ones((2, 3), order\='F')
\>>> x.flags\['F\_CONTIGUOUS'\]
True

Copy to clipboard

Then, calling `asfortranarray` returns the same object:

\>>> y \= np.asfortranarray(x)
\>>> x is y
True

Copy to clipboard

Note: This function returns an array with at least one-dimension (1-d) so it will not preserve 0-d arrays.

Go BackOpen In Tab

On this page