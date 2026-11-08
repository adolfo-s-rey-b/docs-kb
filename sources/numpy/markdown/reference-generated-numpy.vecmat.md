[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.vecmat.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.vecmat.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.vecmat.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.vecmat.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.vecmat.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.vecmat.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.vecmat.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.vecmat.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.vecmat.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.vecmat.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.vecmat.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.vecmat.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.vecmat.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.vecmat.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.vecmat.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.vecmat.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.vecmat.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.vecmat.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.vecmat.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.vecmat.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.vecmat.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.vecmat.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.vecmat[#](https://numpy.org/doc/stable/reference/generated/numpy.vecmat.html#numpy-vecmat "Link to this heading")

========================================================================================================================

numpy.vecmat(_x1_, _x2_, _/_, _out=None_, _\*_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_, _axes_, _axis_\]) _\= <ufunc 'vecmat'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.vecmat.html#numpy.vecmat "Link to this definition")

Vector-matrix dot product of two arrays.

Given a vector (or stack of vector) \\(\\mathbf{v}\\) in `x1` and a matrix (or stack of matrices) \\(\\mathbf{A}\\) in `x2`, the vector-matrix product is defined as:

\\\[\\mathbf{v} \\cdot \\mathbf{A} = \\sum\_{i=0}^{n-1} \\overline{v\_i}A\_{ij}\\\]

where the sum is over the last dimension of `x1` and the one-but-last dimensions in `x2` (unless _axes_ is specified) and where \\(\\overline{v\_i}\\) denotes the complex conjugate if \\(v\\) is complex and the identity otherwise. (For a non-conjugated vector-matrix product, use `np.matvec(x2.mT, x1)`.)

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

The vector-matrix product of the inputs.

Raises:

ValueError

If the last dimensions of `x1` and the one-but-last dimension of `x2` are not the same size.

If a scalar value is passed in.

See also

[`vecdot`](https://numpy.org/doc/stable/reference/generated/numpy.vecdot.html#numpy.vecdot "numpy.vecdot")

Vector-vector product.

[`matvec`](https://numpy.org/doc/stable/reference/generated/numpy.matvec.html#numpy.matvec "numpy.matvec")

Matrix-vector product.

[`matmul`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html#numpy.matmul "numpy.matmul")

Matrix-matrix product.

[`einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum "numpy.einsum")

Einstein summation convention.

Examples

Try it in your browser!

Project a vector along X and Y.

\>>> v \= np.array(\[0., 4., 2.\])
\>>> a \= np.array(\[\[1., 0., 0.\],\
...               \[0., 1., 0.\],\
...               \[0., 0., 0.\]\])
\>>> np.vecmat(v, a)
array(\[ 0.,  4., 0.\])

Copy to clipboard

Go BackOpen In Tab

On this page