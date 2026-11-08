[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.matmul.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.matmul.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.matmul.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.matmul.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.matmul.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.matmul.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.matmul.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.matmul.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.matmul.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.matmul.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.matmul.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.matmul.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.matmul.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.matmul.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.matmul.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.matmul.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.matmul.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.matmul.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.matmul.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.matmul.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matmul[#](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html#numpy-matmul "Link to this heading")

========================================================================================================================

numpy.matmul(_x1_, _x2_, _/_, _out=None_, _\*_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_, _axes_, _axis_\]) _\= <ufunc 'matmul'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html#numpy.matmul "Link to this definition")

Matrix product of two arrays.

Parameters:

**x1, x2**array\_like

Input arrays, scalars not allowed.

**out**ndarray, optional

A location into which the result is stored. If provided, it must have a shape that matches the signature _(n,k),(k,m)->(n,m)_. If not provided or None, a freshly-allocated array is returned.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**y**ndarray

The matrix product of the inputs. This is a scalar only when both x1, x2 are 1-d vectors.

Raises:

ValueError

If the last dimension of _x1_ is not the same size as the second-to-last dimension of _x2_.

If a scalar value is passed in.

See also

[`vecdot`](https://numpy.org/doc/stable/reference/generated/numpy.vecdot.html#numpy.vecdot "numpy.vecdot")

Complex-conjugating dot product for stacks of vectors.

[`matvec`](https://numpy.org/doc/stable/reference/generated/numpy.matvec.html#numpy.matvec "numpy.matvec")

Matrix-vector product for stacks of matrices and vectors.

[`vecmat`](https://numpy.org/doc/stable/reference/generated/numpy.vecmat.html#numpy.vecmat "numpy.vecmat")

Vector-matrix product for stacks of vectors and matrices.

[`tensordot`](https://numpy.org/doc/stable/reference/generated/numpy.tensordot.html#numpy.tensordot "numpy.tensordot")

Sum products over arbitrary axes.

[`einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum "numpy.einsum")

Einstein summation convention.

[`dot`](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")

alternative matrix product with different broadcasting rules.

Notes

The behavior depends on the arguments in the following way.

*   If both arguments are 2-D they are multiplied like conventional matrices.
    
*   If either argument is N-D, N > 2, it is treated as a stack of matrices residing in the last two indexes and broadcast accordingly.
    
*   If the first argument is 1-D, it is promoted to a matrix by prepending a 1 to its dimensions. After matrix multiplication the prepended 1 is removed. (For stacks of vectors, use `vecmat`.)
    
*   If the second argument is 1-D, it is promoted to a matrix by appending a 1 to its dimensions. After matrix multiplication the appended 1 is removed. (For stacks of vectors, use `matvec`.)
    

`matmul` differs from `dot` in two important ways:

*   Multiplication by scalars is not allowed, use `*` instead.
    
*   Stacks of matrices are broadcast together as if the matrices were elements, respecting the signature `(n,k),(k,m)->(n,m)`:
    
    \>>> a \= np.ones(\[9, 5, 7, 4\])
    \>>> c \= np.ones(\[9, 5, 4, 3\])
    \>>> np.dot(a, c).shape
    (9, 5, 7, 9, 5, 3)
    \>>> np.matmul(a, c).shape
    (9, 5, 7, 3)
    \>>> \# n is 7, k is 4, m is 3
    
    Copy to clipboard
    

The matmul function implements the semantics of the `@` operator defined in [**PEP 465**](https://peps.python.org/pep-0465/)
.

It uses an optimized BLAS library when possible (see [`numpy.linalg`](https://numpy.org/doc/stable/reference/routines.linalg.html#module-numpy.linalg "numpy.linalg")
).

Examples

Try it in your browser!

For 2-D arrays it is the matrix product:

\>>> import numpy as np
\>>> a \= np.array(\[\[1, 0\],\
...               \[0, 1\]\])
\>>> b \= np.array(\[\[4, 1\],\
...               \[2, 2\]\])
\>>> np.matmul(a, b)
array(\[\[4, 1\],\
       \[2, 2\]\])

Copy to clipboard

For 2-D mixed with 1-D, the result is the usual.

\>>> a \= np.array(\[\[1, 0\],\
...               \[0, 1\]\])
\>>> b \= np.array(\[1, 2\])
\>>> np.matmul(a, b)
array(\[1, 2\])
\>>> np.matmul(b, a)
array(\[1, 2\])

Copy to clipboard

Broadcasting is conventional for stacks of arrays

\>>> a \= np.arange(2 \* 2 \* 4).reshape((2, 2, 4))
\>>> b \= np.arange(2 \* 2 \* 4).reshape((2, 4, 2))
\>>> np.matmul(a,b).shape
(2, 2, 2)
\>>> np.matmul(a, b)\[0, 1, 1\]
98
\>>> sum(a\[0, 1, :\] \* b\[0 , :, 1\])
98

Copy to clipboard

Vector, vector returns the scalar inner product, but neither argument is complex-conjugated:

\>>> np.matmul(\[2j, 3j\], \[2j, 3j\])
(-13+0j)

Copy to clipboard

Scalar multiplication raises an error.

\>>> np.matmul(\[1,2\], 3)
Traceback (most recent call last):
...
ValueError: matmul: Input operand 1 does not have enough dimensions ...

Copy to clipboard

The `@` operator can be used as a shorthand for `np.matmul` on ndarrays.

\>>> x1 \= np.array(\[2j, 3j\])
\>>> x2 \= np.array(\[2j, 3j\])
\>>> x1 @ x2
(-13+0j)

Copy to clipboard

Go BackOpen In Tab

On this page