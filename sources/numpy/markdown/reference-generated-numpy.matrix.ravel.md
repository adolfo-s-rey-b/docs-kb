[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matrix.ravel.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.matrix.ravel.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.matrix.ravel.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.matrix.ravel.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.matrix.ravel.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.matrix.ravel.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.matrix.ravel.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.matrix.ravel.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.matrix.ravel.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.matrix.ravel.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.matrix.ravel.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.matrix.ravel.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.matrix.ravel.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.matrix.ravel.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.matrix.ravel.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.matrix.ravel.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.matrix.ravel.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.matrix.ravel.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.matrix.ravel.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.matrix.ravel.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.matrix.ravel.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.matrix.ravel.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matrix.ravel[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.ravel.html#numpy-matrix-ravel "Link to this heading")

==========================================================================================================================================

method

matrix.ravel(_order\='C'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/matrixlib/defmatrix.py#L902-L938)
[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.ravel.html#numpy.matrix.ravel "Link to this definition")

Return a flattened matrix.

Refer to [`numpy.ravel`](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html#numpy.ravel "numpy.ravel")
 for more documentation.

Parameters:

**order**{‘C’, ‘F’, ‘A’, ‘K’}, optional

The elements of _m_ are read using this index order. ‘C’ means to index the elements in C-like order, with the last axis index changing fastest, back to the first axis index changing slowest. ‘F’ means to index the elements in Fortran-like index order, with the first index changing fastest, and the last index changing slowest. Note that the ‘C’ and ‘F’ options take no account of the memory layout of the underlying array, and only refer to the order of axis indexing. ‘A’ means to read the elements in Fortran-like index order if _m_ is Fortran _contiguous_ in memory, C-like order otherwise. ‘K’ means to read the elements in the order they occur in memory, except for reversing the data when strides are negative. By default, ‘C’ index order is used.

Returns:

**ret**matrix

Return the matrix flattened to shape _(1, N)_ where _N_ is the number of elements in the original matrix. A copy is made only if necessary.

See also

[`matrix.flatten`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.flatten.html#numpy.matrix.flatten "numpy.matrix.flatten")

returns a similar output matrix but always a copy

[`matrix.flat`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.flat.html#numpy.matrix.flat "numpy.matrix.flat")

a flat iterator on the array.

[`numpy.ravel`](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html#numpy.ravel "numpy.ravel")

related function which returns an ndarray

On this page