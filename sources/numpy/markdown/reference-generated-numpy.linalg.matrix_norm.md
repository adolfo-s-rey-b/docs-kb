[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_norm.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.matrix_norm.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_norm.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.matrix_norm.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.matrix_norm.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.matrix_norm.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.matrix_norm.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.matrix_norm.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.matrix_norm.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.matrix_norm.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.matrix_norm.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.matrix_norm.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.matrix_norm.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.matrix_norm.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.matrix_norm.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.matrix_norm.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.matrix_norm.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.matrix_norm.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.matrix_norm.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.matrix_norm.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.matrix_norm.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.matrix_norm.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.matrix\_norm[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_norm.html#numpy-linalg-matrix-norm "Link to this heading")

=============================================================================================================================================================

linalg.matrix\_norm(_x_, _/_, _\*_, _keepdims\=False_, _ord\='fro'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L3438-L3493)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_norm.html#numpy.linalg.matrix_norm "Link to this definition")

Computes the matrix norm of a matrix (or a stack of matrices) `x`.

This function is Array API compatible.

Parameters:

**x**array\_like

Input array having shape (…, M, N) and whose two innermost dimensions form `MxN` matrices.

**keepdims**bool, optional

If this is set to True, the axes which are normed over are left in the result as dimensions with size one. Default: False.

**ord**{1, -1, 2, -2, inf, -inf, ‘fro’, ‘nuc’}, optional

The order of the norm. For details see the table under `Notes` in [`numpy.linalg.norm`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html#numpy.linalg.norm "numpy.linalg.norm")
.

See also

[`numpy.linalg.norm`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html#numpy.linalg.norm "numpy.linalg.norm")

Generic norm function

Examples

Try it in your browser!

\>>> from numpy import linalg as LA
\>>> a \= np.arange(9) \- 4
\>>> a
array(\[-4, -3, -2, ...,  2,  3,  4\])
\>>> b \= a.reshape((3, 3))
\>>> b
array(\[\[-4, -3, -2\],\
       \[-1,  0,  1\],\
       \[ 2,  3,  4\]\])

Copy to clipboard

\>>> LA.matrix\_norm(b)
7.745966692414834
\>>> LA.matrix\_norm(b, ord\='fro')
7.745966692414834
\>>> LA.matrix\_norm(b, ord\=np.inf)
9.0
\>>> LA.matrix\_norm(b, ord\=-np.inf)
2.0

Copy to clipboard

\>>> LA.matrix\_norm(b, ord\=1)
7.0
\>>> LA.matrix\_norm(b, ord\=-1)
6.0
\>>> LA.matrix\_norm(b, ord\=2)
7.3484692283495345
\>>> LA.matrix\_norm(b, ord\=-2)
1.8570331885190563e-016 # may vary

Copy to clipboard

Go BackOpen In Tab

On this page