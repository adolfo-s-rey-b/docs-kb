[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matrix.ptp.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.matrix.ptp.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.matrix.ptp.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.matrix.ptp.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.matrix.ptp.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.matrix.ptp.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.matrix.ptp.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.matrix.ptp.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.matrix.ptp.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.matrix.ptp.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.matrix.ptp.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.matrix.ptp.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.matrix.ptp.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.matrix.ptp.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.matrix.ptp.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.matrix.ptp.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.matrix.ptp.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.matrix.ptp.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.matrix.ptp.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.matrix.ptp.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.matrix.ptp.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.matrix.ptp.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matrix.ptp[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.ptp.html#numpy-matrix-ptp "Link to this heading")

====================================================================================================================================

method

matrix.ptp(_axis\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/matrixlib/defmatrix.py#L765-L796)
[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.ptp.html#numpy.matrix.ptp "Link to this definition")

Peak-to-peak (maximum - minimum) value along the given axis.

Refer to [`numpy.ptp`](https://numpy.org/doc/stable/reference/generated/numpy.ptp.html#numpy.ptp "numpy.ptp")
 for full documentation.

See also

[`numpy.ptp`](https://numpy.org/doc/stable/reference/generated/numpy.ptp.html#numpy.ptp "numpy.ptp")

Notes

Same as _ndarray.ptp_, except, where that would return an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 object, this returns a [`matrix`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy.matrix "numpy.matrix")
 object.

Examples

Try it in your browser!

\>>> x \= np.matrix(np.arange(12).reshape((3,4))); x
matrix(\[\[ 0,  1,  2,  3\],\
        \[ 4,  5,  6,  7\],\
        \[ 8,  9, 10, 11\]\])
\>>> x.ptp()
11
\>>> x.ptp(0)
matrix(\[\[8, 8, 8, 8\]\])
\>>> x.ptp(1)
matrix(\[\[3\],\
        \[3\],\
        \[3\]\])

Copy to clipboard

Go BackOpen In Tab

On this page