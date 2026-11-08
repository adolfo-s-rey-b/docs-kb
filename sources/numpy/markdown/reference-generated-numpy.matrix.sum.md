[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matrix.sum.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.matrix.sum.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.matrix.sum.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.matrix.sum.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.matrix.sum.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.matrix.sum.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.matrix.sum.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.matrix.sum.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.matrix.sum.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.matrix.sum.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.matrix.sum.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.matrix.sum.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.matrix.sum.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.matrix.sum.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.matrix.sum.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.matrix.sum.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.matrix.sum.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.matrix.sum.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.matrix.sum.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.matrix.sum.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.matrix.sum.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.matrix.sum.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matrix.sum[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.sum.html#numpy-matrix-sum "Link to this heading")

====================================================================================================================================

method

matrix.sum(_axis\=None_, _dtype\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/matrixlib/defmatrix.py#L293-L325)
[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.sum.html#numpy.matrix.sum "Link to this definition")

Returns the sum of the matrix elements, along the given axis.

Refer to [`numpy.sum`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
 for full documentation.

See also

[`numpy.sum`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")

Notes

This is the same as [`ndarray.sum`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.sum.html#numpy.ndarray.sum "numpy.ndarray.sum")
, except that where an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 would be returned, a [`matrix`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy.matrix "numpy.matrix")
 object is returned instead.

Examples

Try it in your browser!

\>>> x \= np.matrix(\[\[1, 2\], \[4, 3\]\])
\>>> x.sum()
10
\>>> x.sum(axis\=1)
matrix(\[\[3\],\
        \[7\]\])
\>>> x.sum(axis\=1, dtype\=np.float64)
matrix(\[\[3.\],\
        \[7.\]\])
\>>> out \= np.zeros((2, 1), dtype\=np.float64)
\>>> x.sum(axis\=1, dtype\=np.float64, out\=np.asmatrix(out))
matrix(\[\[3.\],\
        \[7.\]\])

Copy to clipboard

Go BackOpen In Tab

On this page