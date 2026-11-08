[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_transpose.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.matrix_transpose.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_transpose.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.matrix_transpose.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.matrix_transpose.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.matrix_transpose.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.matrix_transpose.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.matrix_transpose.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.matrix_transpose.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.matrix_transpose.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.matrix_transpose.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.matrix_transpose.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.matrix_transpose.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.matrix_transpose.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.matrix_transpose.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.matrix_transpose.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.matrix_transpose.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.matrix_transpose.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.matrix_transpose.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.matrix_transpose.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.matrix_transpose.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.matrix_transpose.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.matrix\_transpose[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_transpose.html#numpy-linalg-matrix-transpose "Link to this heading")

============================================================================================================================================================================

linalg.matrix\_transpose(_x_, _/_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L3420-L3422)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_transpose.html#numpy.linalg.matrix_transpose "Link to this definition")

Transposes a matrix (or a stack of matrices) `x`.

This function is Array API compatible.

Parameters:

**x**array\_like

Input array having shape (…, M, N) and whose two innermost dimensions form `MxN` matrices.

Returns:

**out**ndarray

An array containing the transpose for each matrix and having shape (…, N, M).

See also

[`transpose`](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html#numpy.transpose "numpy.transpose")

Generic transpose method.

Notes

This function is an alias of [`numpy.matrix_transpose`](https://numpy.org/doc/stable/reference/generated/numpy.matrix_transpose.html#numpy.matrix_transpose "numpy.matrix_transpose")
.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.matrix\_transpose(\[\[1, 2\], \[3, 4\]\])
array(\[\[1, 3\],\
       \[2, 4\]\])

Copy to clipboard

\>>> np.matrix\_transpose(\[\[\[1, 2\], \[3, 4\]\], \[\[5, 6\], \[7, 8\]\]\])
array(\[\[\[1, 3\],\
        \[2, 4\]\],\
       \[\[5, 7\],\
        \[6, 8\]\]\])

Copy to clipboard

Go BackOpen In Tab

On this page