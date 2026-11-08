[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matrix.min.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.matrix.min.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.matrix.min.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.matrix.min.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.matrix.min.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.matrix.min.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.matrix.min.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.matrix.min.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.matrix.min.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.matrix.min.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.matrix.min.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.matrix.min.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.matrix.min.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.matrix.min.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.matrix.min.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.matrix.min.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.matrix.min.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.matrix.min.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.matrix.min.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.matrix.min.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.matrix.min.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.matrix.min.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matrix.min[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.min.html#numpy-matrix-min "Link to this heading")

====================================================================================================================================

method

matrix.min(_axis\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/matrixlib/defmatrix.py#L691-L724)
[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.min.html#numpy.matrix.min "Link to this definition")

Return the minimum value along an axis.

Parameters:

**See \`amin\` for complete descriptions.**

See also

[`amin`](https://numpy.org/doc/stable/reference/generated/numpy.amin.html#numpy.amin "numpy.amin")
, [`ndarray.min`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.min.html#numpy.ndarray.min "numpy.ndarray.min")

Notes

This is the same as [`ndarray.min`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.min.html#numpy.ndarray.min "numpy.ndarray.min")
, but returns a [`matrix`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy.matrix "numpy.matrix")
 object where [`ndarray.min`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.min.html#numpy.ndarray.min "numpy.ndarray.min")
 would return an ndarray.

Examples

Try it in your browser!

\>>> x \= \-np.matrix(np.arange(12).reshape((3,4))); x
matrix(\[\[  0,  -1,  -2,  -3\],\
        \[ -4,  -5,  -6,  -7\],\
        \[ -8,  -9, -10, -11\]\])
\>>> x.min()
\-11
\>>> x.min(0)
matrix(\[\[ -8,  -9, -10, -11\]\])
\>>> x.min(1)
matrix(\[\[ -3\],\
        \[ -7\],\
        \[-11\]\])

Copy to clipboard

Go BackOpen In Tab

On this page