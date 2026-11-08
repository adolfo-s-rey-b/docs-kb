[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matrix.argmin.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.matrix.argmin.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.matrix.argmin.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.matrix.argmin.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.matrix.argmin.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.matrix.argmin.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.matrix.argmin.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.matrix.argmin.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.matrix.argmin.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.matrix.argmin.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.matrix.argmin.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.matrix.argmin.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.matrix.argmin.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.matrix.argmin.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.matrix.argmin.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.matrix.argmin.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.matrix.argmin.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.matrix.argmin.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.matrix.argmin.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.matrix.argmin.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.matrix.argmin.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.matrix.argmin.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matrix.argmin[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.argmin.html#numpy-matrix-argmin "Link to this heading")

=============================================================================================================================================

method

matrix.argmin(_axis\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/matrixlib/defmatrix.py#L726-L763)
[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.argmin.html#numpy.matrix.argmin "Link to this definition")

Indexes of the minimum values along an axis.

Return the indexes of the first occurrences of the minimum values along the specified axis. If axis is None, the index is for the flattened matrix.

Parameters:

**See \`numpy.argmin\` for complete descriptions.**

See also

[`numpy.argmin`](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html#numpy.argmin "numpy.argmin")

Notes

This is the same as [`ndarray.argmin`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.argmin.html#numpy.ndarray.argmin "numpy.ndarray.argmin")
, but returns a [`matrix`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy.matrix "numpy.matrix")
 object where [`ndarray.argmin`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.argmin.html#numpy.ndarray.argmin "numpy.ndarray.argmin")
 would return an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.

Examples

Try it in your browser!

\>>> x \= \-np.matrix(np.arange(12).reshape((3,4))); x
matrix(\[\[  0,  -1,  -2,  -3\],\
        \[ -4,  -5,  -6,  -7\],\
        \[ -8,  -9, -10, -11\]\])
\>>> x.argmin()
11
\>>> x.argmin(0)
matrix(\[\[2, 2, 2, 2\]\])
\>>> x.argmin(1)
matrix(\[\[3\],\
        \[3\],\
        \[3\]\])

Copy to clipboard

Go BackOpen In Tab

On this page