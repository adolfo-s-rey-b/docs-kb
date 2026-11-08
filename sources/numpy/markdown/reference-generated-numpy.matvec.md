[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matvec.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.matvec.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.matvec.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.matvec.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.matvec.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.matvec.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.matvec.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.matvec.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.matvec.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.matvec.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.matvec.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.matvec.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.matvec.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.matvec.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.matvec.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.matvec.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.matvec.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.matvec.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.matvec.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.matvec.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.matvec.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.matvec.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matvec[#](https://numpy.org/doc/stable/reference/generated/numpy.matvec.html#numpy-matvec "Link to this heading")

========================================================================================================================

numpy.matvec(_x1_, _x2_, _/_, _out=None_, _\*_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_, _axes_, _axis_\]) _\= <ufunc 'matvec'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.matvec.html#numpy.matvec "Link to this definition")

Matrix-vector dot product of two arrays.

Given a matrix (or stack of matrices) \\(\\mathbf{A}\\) in `x1` and a vector (or stack of vectors) \\(\\mathbf{v}\\) in `x2`, the matrix-vector product is defined as:

\\\[\\mathbf{A} \\cdot \\mathbf{v} = \\sum\_{j=0}^{n-1} A\_{ij} v\_j\\\]

where the sum is over the last dimensions in `x1` and `x2` (unless `axes` is specified). (For a matrix-vector product with the vector conjugated, use `np.vecmat(x2, x1.mT)`.)

New in version 2.2.0.

Parameters:

**x1, x2**array\_like

Input arrays, scalars not allowed.

**out**ndarray, optional

A location into which the result is stored. If provided, it must have the broadcasted shape of `x1` and `x2` with the summation axis removed. If not provided or None, a freshly-allocated array is used.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**y**ndarray

The matrix-vector product of the inputs.

Raises:

ValueError

If the last dimensions of `x1` and `x2` are not the same size.

If a scalar value is passed in.

See also

[`vecdot`](https://numpy.org/doc/stable/reference/generated/numpy.vecdot.html#numpy.vecdot "numpy.vecdot")

Vector-vector product.

[`vecmat`](https://numpy.org/doc/stable/reference/generated/numpy.vecmat.html#numpy.vecmat "numpy.vecmat")

Vector-matrix product.

[`matmul`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html#numpy.matmul "numpy.matmul")

Matrix-matrix product.

[`einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum "numpy.einsum")

Einstein summation convention.

Examples

Try it in your browser!

Rotate a set of vectors from Y to X along Z.

\>>> a \= np.array(\[\[0., 1., 0.\],\
...               \[\-1., 0., 0.\],\
...               \[0., 0., 1.\]\])
\>>> v \= np.array(\[\[1., 0., 0.\],\
...               \[0., 1., 0.\],\
...               \[0., 0., 1.\],\
...               \[0., 6., 8.\]\])
\>>> np.matvec(a, v)
array(\[\[ 0., -1.,  0.\],\
       \[ 1.,  0.,  0.\],\
       \[ 0.,  0.,  1.\],\
       \[ 6.,  0.,  8.\]\])

Copy to clipboard

Go BackOpen In Tab

On this page