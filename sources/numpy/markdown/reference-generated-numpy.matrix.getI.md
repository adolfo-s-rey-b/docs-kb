[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matrix.getI.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.matrix.getI.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.matrix.getI.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.matrix.getI.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.matrix.getI.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.matrix.getI.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.matrix.getI.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.matrix.getI.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.matrix.getI.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.matrix.getI.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.matrix.getI.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.matrix.getI.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.matrix.getI.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.matrix.getI.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.matrix.getI.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.matrix.getI.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.matrix.getI.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.matrix.getI.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.matrix.getI.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.matrix.getI.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.matrix.getI.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.matrix.getI.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matrix.getI[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.getI.html#numpy-matrix-geti "Link to this heading")

=======================================================================================================================================

method

matrix.getI()[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/matrixlib/defmatrix.py#L798-L841)
[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.getI.html#numpy.matrix.getI "Link to this definition")

Returns the (multiplicative) inverse of invertible _self_.

Parameters:

**None**

Returns:

**ret**matrix object

If _self_ is non-singular, _ret_ is such that `ret * self` == `self * ret` == `np.matrix(np.eye(self[0,:].size))` all return `True`.

Raises:

numpy.linalg.LinAlgError: Singular matrix

If _self_ is singular.

See also

[`linalg.inv`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.inv.html#numpy.linalg.inv "numpy.linalg.inv")

Examples

Try it in your browser!

\>>> m \= np.matrix('\[1, 2; 3, 4\]'); m
matrix(\[\[1, 2\],\
        \[3, 4\]\])
\>>> m.getI()
matrix(\[\[-2. ,  1. \],\
        \[ 1.5, -0.5\]\])
\>>> m.getI() \* m
matrix(\[\[ 1.,  0.\], # may vary\
        \[ 0.,  1.\]\])

Copy to clipboard

Go BackOpen In Tab

On this page