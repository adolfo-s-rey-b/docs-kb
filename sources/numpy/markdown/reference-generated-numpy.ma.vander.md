[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.vander.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.vander.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.vander.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.vander.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.vander.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.vander.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.vander.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.vander.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.vander.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.vander.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.vander.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.vander.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.vander.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.vander.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.vander.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.vander.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.vander.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.vander.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.vander.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.vander.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.vander.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.vander.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.vander[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.vander.html#numpy-ma-vander "Link to this heading")

=================================================================================================================================

ma.vander(_x_, _n\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/extras.py#L2216-L2225)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.vander.html#numpy.ma.vander "Link to this definition")

Generate a Vandermonde matrix.

The columns of the output matrix are powers of the input vector. The order of the powers is determined by the _increasing_ boolean argument. Specifically, when _increasing_ is False, the _i_\-th output column is the input vector raised element-wise to the power of `N - i - 1`. Such a matrix with a geometric progression in each row is named for Alexandre- Theophile Vandermonde.

Parameters:

**x**array\_like

1-D input array.

**N**int, optional

Number of columns in the output. If _N_ is not specified, a square array is returned (`N = len(x)`).

**increasing**bool, optional

Order of the powers of the columns. If True, the powers increase from left to right, if False (the default) they are reversed.

Returns:

**out**ndarray

Vandermonde matrix. If _increasing_ is False, the first column is `x^(N-1)`, the second `x^(N-2)` and so forth. If _increasing_ is True, the columns are `x^0, x^1, ..., x^(N-1)`.

See also

[`polynomial.polynomial.polyvander`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvander.html#numpy.polynomial.polynomial.polyvander "numpy.polynomial.polynomial.polyvander")

Notes

Masked values in the input array result in rows of zeros.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array(\[1, 2, 3, 5\])
\>>> N \= 3
\>>> np.vander(x, N)
array(\[\[ 1,  1,  1\],\
       \[ 4,  2,  1\],\
       \[ 9,  3,  1\],\
       \[25,  5,  1\]\])

Copy to clipboard

\>>> np.column\_stack(\[x\*\*(N\-1\-i) for i in range(N)\])
array(\[\[ 1,  1,  1\],\
       \[ 4,  2,  1\],\
       \[ 9,  3,  1\],\
       \[25,  5,  1\]\])

Copy to clipboard

\>>> x \= np.array(\[1, 2, 3, 5\])
\>>> np.vander(x)
array(\[\[  1,   1,   1,   1\],\
       \[  8,   4,   2,   1\],\
       \[ 27,   9,   3,   1\],\
       \[125,  25,   5,   1\]\])
\>>> np.vander(x, increasing\=True)
array(\[\[  1,   1,   1,   1\],\
       \[  1,   2,   4,   8\],\
       \[  1,   3,   9,  27\],\
       \[  1,   5,  25, 125\]\])

Copy to clipboard

The determinant of a square Vandermonde matrix is the product of the differences between the values of the input vector:

\>>> np.linalg.det(np.vander(x))
48.000000000000043 # may vary
\>>> (5\-3)\*(5\-2)\*(5\-1)\*(3\-2)\*(3\-1)\*(2\-1)
48

Copy to clipboard

Go BackOpen In Tab

On this page