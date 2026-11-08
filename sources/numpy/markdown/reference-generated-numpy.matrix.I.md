[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matrix.I.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matrix.I[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.I.html#numpy-matrix-i "Link to this heading")

==============================================================================================================================

property

_property_ matrix.I[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.I.html#numpy.matrix.I "Link to this definition")

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