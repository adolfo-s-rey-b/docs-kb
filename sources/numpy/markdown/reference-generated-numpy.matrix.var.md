[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matrix.var.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.matrix.var.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.matrix.var.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.matrix.var.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.matrix.var.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.matrix.var.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.matrix.var.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.matrix.var.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.matrix.var.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.matrix.var.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.matrix.var.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.matrix.var.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.matrix.var.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.matrix.var.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.matrix.var.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.matrix.var.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.matrix.var.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.matrix.var.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.matrix.var.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.matrix.var.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.matrix.var.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.matrix.var.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matrix.var[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.var.html#numpy-matrix-var "Link to this heading")

====================================================================================================================================

method

matrix.var(_axis\=None_, _dtype\=None_, _out\=None_, _ddof\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/matrixlib/defmatrix.py#L486-L519)
[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.var.html#numpy.matrix.var "Link to this definition")

Returns the variance of the matrix elements, along the given axis.

Refer to [`numpy.var`](https://numpy.org/doc/stable/reference/generated/numpy.var.html#numpy.var "numpy.var")
 for full documentation.

See also

[`numpy.var`](https://numpy.org/doc/stable/reference/generated/numpy.var.html#numpy.var "numpy.var")

Notes

This is the same as [`ndarray.var`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.var.html#numpy.ndarray.var "numpy.ndarray.var")
, except that where an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 would be returned, a [`matrix`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy.matrix "numpy.matrix")
 object is returned instead.

Examples

Try it in your browser!

\>>> x \= np.matrix(np.arange(12).reshape((3, 4)))
\>>> x
matrix(\[\[ 0,  1,  2,  3\],\
        \[ 4,  5,  6,  7\],\
        \[ 8,  9, 10, 11\]\])
\>>> x.var()
11.916666666666666
\>>> x.var(0)
matrix(\[\[ 10.66666667,  10.66666667,  10.66666667,  10.66666667\]\]) # may vary
\>>> x.var(1)
matrix(\[\[1.25\],\
        \[1.25\],\
        \[1.25\]\])

Copy to clipboard

Go BackOpen In Tab

On this page