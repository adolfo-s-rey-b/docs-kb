[Skip to main content](https://numpy.org/doc/stable/reference/routines.matlib.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Matrix library ([`numpy.matlib`](https://numpy.org/doc/stable/reference/routines.matlib.html#module-numpy.matlib "numpy.matlib")
)[#](https://numpy.org/doc/stable/reference/routines.matlib.html#matrix-library-numpy-matlib "Link to this heading")

======================================================================================================================================================================================================================================================

This module contains all functions in the [`numpy`](https://numpy.org/doc/stable/reference/index.html#module-numpy "numpy")
 namespace, with the following replacement functions that return [`matrices`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy.matrix "numpy.matrix")
 instead of [`ndarrays`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.

Functions that are also in the numpy namespace and return matrices

|     |     |
| --- | --- |
| [`matrix`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy.matrix "numpy.matrix")<br>(data\[, dtype, copy\]) | Returns a matrix from an array-like object, or from a string of data. |
| [`asmatrix`](https://numpy.org/doc/stable/reference/generated/numpy.asmatrix.html#numpy.asmatrix "numpy.asmatrix")<br>(data\[, dtype\]) | Interpret the input as a matrix. |
| [`bmat`](https://numpy.org/doc/stable/reference/generated/numpy.bmat.html#numpy.bmat "numpy.bmat")<br>(obj\[, ldict, gdict\]) | Build a matrix object from a string, nested sequence, or array. |

Replacement functions in [`matlib`](https://numpy.org/doc/stable/reference/routines.matlib.html#module-numpy.matlib "numpy.matlib")

|     |     |
| --- | --- |
| [`empty`](https://numpy.org/doc/stable/reference/generated/numpy.matlib.empty.html#numpy.matlib.empty "numpy.matlib.empty")<br>(shape\[, dtype, order\]) | Return a new matrix of given shape and type, without initializing entries. |
| [`zeros`](https://numpy.org/doc/stable/reference/generated/numpy.matlib.zeros.html#numpy.matlib.zeros "numpy.matlib.zeros")<br>(shape\[, dtype, order\]) | Return a matrix of given shape and type, filled with zeros. |
| [`ones`](https://numpy.org/doc/stable/reference/generated/numpy.matlib.ones.html#numpy.matlib.ones "numpy.matlib.ones")<br>(shape\[, dtype, order\]) | Matrix of ones. |
| [`eye`](https://numpy.org/doc/stable/reference/generated/numpy.matlib.eye.html#numpy.matlib.eye "numpy.matlib.eye")<br>(n\[, M, k, dtype, order\]) | Return a matrix with ones on the diagonal and zeros elsewhere. |
| [`identity`](https://numpy.org/doc/stable/reference/generated/numpy.matlib.identity.html#numpy.matlib.identity "numpy.matlib.identity")<br>(n\[, dtype\]) | Returns the square identity matrix of given size. |
| [`repmat`](https://numpy.org/doc/stable/reference/generated/numpy.matlib.repmat.html#numpy.matlib.repmat "numpy.matlib.repmat")<br>(a, m, n) | Repeat a 0-D to 2-D array or matrix MxN times. |
| [`rand`](https://numpy.org/doc/stable/reference/generated/numpy.matlib.rand.html#numpy.matlib.rand "numpy.matlib.rand")<br>(\*args) | Return a matrix of random values with given shape. |
| [`randn`](https://numpy.org/doc/stable/reference/generated/numpy.matlib.randn.html#numpy.matlib.randn "numpy.matlib.randn")<br>(\*args) | Return a random matrix with data from the "standard normal" distribution. |