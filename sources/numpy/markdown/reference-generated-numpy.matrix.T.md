[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matrix.T.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.matrix.T.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.matrix.T.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.matrix.T.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.matrix.T.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.matrix.T.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.matrix.T.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.matrix.T.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.matrix.T.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.matrix.T.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.matrix.T.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.matrix.T.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.matrix.T.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.matrix.T.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.matrix.T.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.matrix.T.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.matrix.T.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.matrix.T.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.matrix.T.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.matrix.T.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.matrix.T.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.matrix.T.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matrix.T[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.T.html#numpy-matrix-t "Link to this heading")

==============================================================================================================================

property

_property_ matrix.T[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.T.html#numpy.matrix.T "Link to this definition")

Returns the transpose of the matrix.

Does _not_ conjugate! For the complex conjugate transpose, use `.H`.

Parameters:

**None**

Returns:

**ret**matrix object

The (non-conjugated) transpose of the matrix.

See also

[`transpose`](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html#numpy.transpose "numpy.transpose")
, [`getH`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.getH.html#numpy.matrix.getH "numpy.matrix.getH")

Examples

Try it in your browser!

\>>> m \= np.matrix('\[1, 2; 3, 4\]')
\>>> m
matrix(\[\[1, 2\],\
        \[3, 4\]\])
\>>> m.getT()
matrix(\[\[1, 3\],\
        \[2, 4\]\])

Copy to clipboard

Go BackOpen In Tab

On this page