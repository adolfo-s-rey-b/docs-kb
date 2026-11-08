[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ravel.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ravel.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ravel.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ravel.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ravel.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ravel.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ravel.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ravel.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ravel.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ravel.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ravel.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ravel.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ravel.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ravel.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ravel.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ravel.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ravel.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ravel.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ravel.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ravel.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ravel[#](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html#numpy-ravel "Link to this heading")

=====================================================================================================================

numpy.ravel(_a_, _order\='C'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L1917-L2024)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html#numpy.ravel "Link to this definition")

Return a contiguous flattened array.

A 1-D array, containing the elements of the input, is returned. A copy is made only if needed.

As of NumPy 1.10, the returned array will have the same type as the input array. (for example, a masked array will be returned for a masked array input)

Parameters:

**a**array\_like

Input array. The elements in _a_ are read in the order specified by _order_, and packed as a 1-D array.

**order**{‘C’,’F’, ‘A’, ‘K’}, optional

The elements of _a_ are read using this index order. ‘C’ means to index the elements in row-major, C-style order, with the last axis index changing fastest, back to the first axis index changing slowest. ‘F’ means to index the elements in column-major, Fortran-style order, with the first index changing fastest, and the last index changing slowest. Note that the ‘C’ and ‘F’ options take no account of the memory layout of the underlying array, and only refer to the order of axis indexing. ‘A’ means to read the elements in Fortran-like index order if _a_ is Fortran _contiguous_ in memory, C-like order otherwise. ‘K’ means to read the elements in the order they occur in memory, except for reversing the data when strides are negative. By default, ‘C’ index order is used.

Returns:

**y**array\_like

y is a contiguous 1-D array of the same subtype as _a_, with shape `(a.size,)`. Note that matrices are special cased for backward compatibility, if _a_ is a matrix, then y is a 1-D ndarray.

See also

[`ndarray.flat`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flat.html#numpy.ndarray.flat "numpy.ndarray.flat")

1-D iterator over an array.

[`ndarray.flatten`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html#numpy.ndarray.flatten "numpy.ndarray.flatten")

1-D array copy of the elements of an array in row-major order.

[`ndarray.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.reshape.html#numpy.ndarray.reshape "numpy.ndarray.reshape")

Change the shape of an array without changing its data.

Notes

In row-major, C-style order, in two dimensions, the row index varies the slowest, and the column index the quickest. This can be generalized to multiple dimensions, where row-major order implies that the index along the first axis varies slowest, and the index along the last quickest. The opposite holds for column-major, Fortran-style index ordering.

When a view is desired in as many cases as possible, `arr.reshape(-1)` may be preferable. However, `ravel` supports `K` in the optional `order` argument while `reshape` does not.

Examples

Try it in your browser!

It is equivalent to `reshape(-1, order=order)`.

\>>> import numpy as np
\>>> x \= np.array(\[\[1, 2, 3\], \[4, 5, 6\]\])
\>>> np.ravel(x)
array(\[1, 2, 3, 4, 5, 6\])

Copy to clipboard

\>>> x.reshape(\-1)
array(\[1, 2, 3, 4, 5, 6\])

Copy to clipboard

\>>> np.ravel(x, order\='F')
array(\[1, 4, 2, 5, 3, 6\])

Copy to clipboard

When `order` is ‘A’, it will preserve the array’s ‘C’ or ‘F’ ordering:

\>>> np.ravel(x.T)
array(\[1, 4, 2, 5, 3, 6\])
\>>> np.ravel(x.T, order\='A')
array(\[1, 2, 3, 4, 5, 6\])

Copy to clipboard

When `order` is ‘K’, it will preserve orderings that are neither ‘C’ nor ‘F’, but won’t reverse axes:

\>>> a \= np.arange(3)\[::\-1\]; a
array(\[2, 1, 0\])
\>>> a.ravel(order\='C')
array(\[2, 1, 0\])
\>>> a.ravel(order\='K')
array(\[2, 1, 0\])

Copy to clipboard

\>>> a \= np.arange(12).reshape(2,3,2).swapaxes(1,2); a
array(\[\[\[ 0,  2,  4\],\
        \[ 1,  3,  5\]\],\
       \[\[ 6,  8, 10\],\
        \[ 7,  9, 11\]\]\])
\>>> a.ravel(order\='C')
array(\[ 0,  2,  4,  1,  3,  5,  6,  8, 10,  7,  9, 11\])
\>>> a.ravel(order\='K')
array(\[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11\])

Copy to clipboard

Go BackOpen In Tab

On this page