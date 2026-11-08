[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matrix.argmax.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.matrix.argmax.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.matrix.argmax.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.matrix.argmax.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.matrix.argmax.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.matrix.argmax.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.matrix.argmax.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.matrix.argmax.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.matrix.argmax.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.matrix.argmax.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.matrix.argmax.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.matrix.argmax.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.matrix.argmax.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.matrix.argmax.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.matrix.argmax.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.matrix.argmax.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.matrix.argmax.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.matrix.argmax.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.matrix.argmax.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.matrix.argmax.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.matrix.argmax.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.matrix.argmax.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matrix.argmax[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.argmax.html#numpy-matrix-argmax "Link to this heading")

=============================================================================================================================================

method

matrix.argmax(_axis\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/matrixlib/defmatrix.py#L652-L689)
[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.argmax.html#numpy.matrix.argmax "Link to this definition")

Indexes of the maximum values along an axis.

Return the indexes of the first occurrences of the maximum values along the specified axis. If axis is None, the index is for the flattened matrix.

Parameters:

**See \`numpy.argmax\` for complete descriptions**

See also

[`numpy.argmax`](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html#numpy.argmax "numpy.argmax")

Notes

This is the same as [`ndarray.argmax`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.argmax.html#numpy.ndarray.argmax "numpy.ndarray.argmax")
, but returns a [`matrix`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy.matrix "numpy.matrix")
 object where [`ndarray.argmax`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.argmax.html#numpy.ndarray.argmax "numpy.ndarray.argmax")
 would return an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.

Examples

Try it in your browser!

\>>> x \= np.matrix(np.arange(12).reshape((3,4))); x
matrix(\[\[ 0,  1,  2,  3\],\
        \[ 4,  5,  6,  7\],\
        \[ 8,  9, 10, 11\]\])
\>>> x.argmax()
11
\>>> x.argmax(0)
matrix(\[\[2, 2, 2, 2\]\])
\>>> x.argmax(1)
matrix(\[\[3\],\
        \[3\],\
        \[3\]\])

Copy to clipboard

Go BackOpen In Tab

On this page