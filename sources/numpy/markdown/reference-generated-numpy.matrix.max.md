[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matrix.max.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matrix.max[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.max.html#numpy-matrix-max "Link to this heading")

====================================================================================================================================

method

matrix.max(_axis\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/matrixlib/defmatrix.py#L617-L650)
[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.max.html#numpy.matrix.max "Link to this definition")

Return the maximum value along an axis.

Parameters:

**See \`amax\` for complete descriptions**

See also

[`amax`](https://numpy.org/doc/stable/reference/generated/numpy.amax.html#numpy.amax "numpy.amax")
, [`ndarray.max`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.max.html#numpy.ndarray.max "numpy.ndarray.max")

Notes

This is the same as [`ndarray.max`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.max.html#numpy.ndarray.max "numpy.ndarray.max")
, but returns a [`matrix`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy.matrix "numpy.matrix")
 object where [`ndarray.max`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.max.html#numpy.ndarray.max "numpy.ndarray.max")
 would return an ndarray.

Examples

Try it in your browser!

\>>> x \= np.matrix(np.arange(12).reshape((3,4))); x
matrix(\[\[ 0,  1,  2,  3\],\
        \[ 4,  5,  6,  7\],\
        \[ 8,  9, 10, 11\]\])
\>>> x.max()
11
\>>> x.max(0)
matrix(\[\[ 8,  9, 10, 11\]\])
\>>> x.max(1)
matrix(\[\[ 3\],\
        \[ 7\],\
        \[11\]\])

Copy to clipboard

Go BackOpen In Tab

On this page