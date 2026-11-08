[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matrix.prod.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.matrix.prod.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.matrix.prod.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.matrix.prod.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.matrix.prod.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.matrix.prod.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.matrix.prod.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.matrix.prod.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.matrix.prod.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.matrix.prod.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.matrix.prod.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.matrix.prod.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.matrix.prod.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.matrix.prod.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.matrix.prod.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.matrix.prod.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.matrix.prod.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.matrix.prod.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.matrix.prod.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.matrix.prod.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.matrix.prod.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.matrix.prod.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matrix.prod[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.prod.html#numpy-matrix-prod "Link to this heading")

=======================================================================================================================================

method

matrix.prod(_axis\=None_, _dtype\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/matrixlib/defmatrix.py#L521-L552)
[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.prod.html#numpy.matrix.prod "Link to this definition")

Return the product of the array elements over the given axis.

Refer to [`prod`](https://numpy.org/doc/stable/reference/generated/numpy.prod.html#numpy.prod "numpy.prod")
 for full documentation.

See also

[`prod`](https://numpy.org/doc/stable/reference/generated/numpy.prod.html#numpy.prod "numpy.prod")
, [`ndarray.prod`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.prod.html#numpy.ndarray.prod "numpy.ndarray.prod")

Notes

Same as [`ndarray.prod`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.prod.html#numpy.ndarray.prod "numpy.ndarray.prod")
, except, where that returns an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, this returns a [`matrix`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy.matrix "numpy.matrix")
 object instead.

Examples

Try it in your browser!

\>>> x \= np.matrix(np.arange(12).reshape((3,4))); x
matrix(\[\[ 0,  1,  2,  3\],\
        \[ 4,  5,  6,  7\],\
        \[ 8,  9, 10, 11\]\])
\>>> x.prod()
0
\>>> x.prod(0)
matrix(\[\[  0,  45, 120, 231\]\])
\>>> x.prod(1)
matrix(\[\[   0\],\
        \[ 840\],\
        \[7920\]\])

Copy to clipboard

Go BackOpen In Tab

On this page