[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.vecdot.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.vecdot.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.vecdot.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.vecdot.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.vecdot.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.vecdot.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.vecdot.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.vecdot.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.vecdot.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.vecdot.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.vecdot.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.vecdot.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.vecdot.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.vecdot.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.vecdot.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.vecdot.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.vecdot.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.vecdot.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.vecdot.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.vecdot.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.vecdot.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.vecdot.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.vecdot[#](https://numpy.org/doc/stable/reference/generated/numpy.vecdot.html#numpy-vecdot "Link to this heading")

========================================================================================================================

numpy.vecdot(_x1_, _x2_, _/_, _out=None_, _\*_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_, _axes_, _axis_\]) _\= <ufunc 'vecdot'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.vecdot.html#numpy.vecdot "Link to this definition")

Vector dot product of two arrays.

Let be a vector in _x1_ and \\mathbf{b} be a corresponding vector in _x2_. The dot product is defined as:

\\mathbf{a} \\cdot \\mathbf{b} = \\sum\_{i=0}^{n-1} \\overline{a\_i}b\_i

where the sum is over the last dimension (unless _axis_ is specified) and where \\overline{a\_i} denotes the complex conjugate if a\_i is complex and the identity otherwise.

New in version 2.0.0.

Parameters:

**x1, x2**array\_like

Input arrays, scalars not allowed.

**out**ndarray, optional

A location into which the result is stored. If provided, it must have the broadcasted shape of _x1_ and _x2_ with the last axis removed. If not provided or None, a freshly-allocated array is used.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**y**ndarray

The vector dot product of the inputs. This is a scalar only when both x1, x2 are 1-d vectors.

Raises:

ValueError

If the last dimension of _x1_ is not the same size as the last dimension of _x2_.

If a scalar value is passed in.

See also

[`vdot`](https://numpy.org/doc/stable/reference/generated/numpy.vdot.html#numpy.vdot "numpy.vdot")

same but flattens arguments first

[`matmul`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html#numpy.matmul "numpy.matmul")

Matrix-matrix product.

[`vecmat`](https://numpy.org/doc/stable/reference/generated/numpy.vecmat.html#numpy.vecmat "numpy.vecmat")

Vector-matrix product.

[`matvec`](https://numpy.org/doc/stable/reference/generated/numpy.matvec.html#numpy.matvec "numpy.matvec")

Matrix-vector product.

[`einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum "numpy.einsum")

Einstein summation convention.

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

Get the projected size along a given normal for an array of vectors.

\>>> v \= np.array(\[\[0., 5., 0.\], \[0., 0., 10.\], \[0., 6., 8.\]\])
\>>> n \= np.array(\[0., 0.6, 0.8\])
\>>> np.vecdot(v, n)
array(\[ 3.,  8., 10.\])

Copy to clipboard

Go BackOpen In Tab

On this page