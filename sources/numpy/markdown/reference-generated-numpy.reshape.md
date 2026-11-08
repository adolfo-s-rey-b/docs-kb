[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.reshape.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.reshape.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.reshape.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.reshape.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.reshape.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.reshape.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.reshape.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.reshape.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.reshape.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.reshape.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.reshape.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.reshape.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.reshape.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.reshape.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.reshape.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.reshape.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.reshape.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.reshape.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.reshape.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.reshape.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.reshape[#](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy-reshape "Link to this heading")

===========================================================================================================================

numpy.reshape(_a_, _/_, _shape_, _order\='C'_, _\*_, _copy\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L207-L299)
[#](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape "Link to this definition")

Returns a reshaped ndarray without changing data.

Parameters:

**a**array\_like

Array to be reshaped.

**shape**int or tuple of ints

The new shape should be compatible with the original shape. If an integer, then the result will be a 1-D array of that length. One shape dimension can be -1. In this case, the value is inferred from the length of the array and remaining dimensions.

**order**{‘C’, ‘F’, ‘A’}, optional

Read the elements of `a` using this index order, and place the elements into the reshaped array using this index order. ‘C’ means to read / write the elements using C-like index order, with the last axis index changing fastest, back to the first axis index changing slowest. ‘F’ means to read / write the elements using Fortran-like index order, with the first index changing fastest, and the last index changing slowest. Note that the ‘C’ and ‘F’ options take no account of the memory layout of the underlying array, and only refer to the order of indexing. ‘A’ means to read / write the elements in Fortran-like index order if `a` is Fortran _contiguous_ in memory, C-like order otherwise.

**copy**bool, optional

If `True`, then the array data is copied. If `None`, a copy will only be made if it’s required by `order`. For `False` it raises a `ValueError` if a copy cannot be avoided. Default: `None`.

Returns:

**reshaped\_array**ndarray

This will be a new view object if possible; otherwise, it will be a copy. Note there is no guarantee of the _memory layout_ (C- or Fortran- contiguous) of the returned array.

See also

[`ndarray.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.reshape.html#numpy.ndarray.reshape "numpy.ndarray.reshape")

Equivalent method.

Notes

It is not always possible to change the shape of an array without copying the data.

The `order` keyword gives the index ordering both for _fetching_ the values from `a`, and then _placing_ the values into the output array. For example, let’s say you have an array:

\>>> a \= np.arange(6).reshape((3, 2))
\>>> a
array(\[\[0, 1\],\
       \[2, 3\],\
       \[4, 5\]\])

Copy to clipboard

You can think of reshaping as first raveling the array (using the given index order), then inserting the elements from the raveled array into the new array using the same kind of index ordering as was used for the raveling.

\>>> np.reshape(a, (2, 3)) \# C-like index ordering
array(\[\[0, 1, 2\],\
       \[3, 4, 5\]\])
\>>> np.reshape(np.ravel(a), (2, 3)) \# equivalent to C ravel then C reshape
array(\[\[0, 1, 2\],\
       \[3, 4, 5\]\])
\>>> np.reshape(a, (2, 3), order\='F') \# Fortran-like index ordering
array(\[\[0, 4, 3\],\
       \[2, 1, 5\]\])
\>>> np.reshape(np.ravel(a, order\='F'), (2, 3), order\='F')
array(\[\[0, 4, 3\],\
       \[2, 1, 5\]\])

Copy to clipboard

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[\[1,2,3\], \[4,5,6\]\])
\>>> np.reshape(a, 6)
array(\[1, 2, 3, 4, 5, 6\])
\>>> np.reshape(a, 6, order\='F')
array(\[1, 4, 2, 5, 3, 6\])

Copy to clipboard

\>>> np.reshape(a, (3,\-1))       \# the unspecified value is inferred to be 2
array(\[\[1, 2\],\
       \[3, 4\],\
       \[5, 6\]\])

Copy to clipboard

Go BackOpen In Tab

On this page