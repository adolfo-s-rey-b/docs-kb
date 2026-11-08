[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matrix.squeeze.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.matrix.squeeze.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.matrix.squeeze.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.matrix.squeeze.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.matrix.squeeze.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.matrix.squeeze.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.matrix.squeeze.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.matrix.squeeze.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.matrix.squeeze.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.matrix.squeeze.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.matrix.squeeze.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.matrix.squeeze.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.matrix.squeeze.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.matrix.squeeze.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.matrix.squeeze.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.matrix.squeeze.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.matrix.squeeze.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.matrix.squeeze.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.matrix.squeeze.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.matrix.squeeze.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.matrix.squeeze.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.matrix.squeeze.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matrix.squeeze[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.squeeze.html#numpy-matrix-squeeze "Link to this heading")

================================================================================================================================================

method

matrix.squeeze(_axis\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/matrixlib/defmatrix.py#L328-L377)
[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.squeeze.html#numpy.matrix.squeeze "Link to this definition")

Return a possibly reshaped matrix.

Refer to [`numpy.squeeze`](https://numpy.org/doc/stable/reference/generated/numpy.squeeze.html#numpy.squeeze "numpy.squeeze")
 for more documentation.

Parameters:

**axis**None or int or tuple of ints, optional

Selects a subset of the axes of length one in the shape. If an axis is selected with shape entry greater than one, an error is raised.

Returns:

**squeezed**matrix

The matrix, but as a (1, N) matrix if it had shape (N, 1).

See also

[`numpy.squeeze`](https://numpy.org/doc/stable/reference/generated/numpy.squeeze.html#numpy.squeeze "numpy.squeeze")

related function

Notes

If _m_ has a single column then that column is returned as the single row of a matrix. Otherwise _m_ is returned. The returned matrix is always either _m_ itself or a view into _m_. Supplying an axis keyword argument will not affect the returned matrix but it may cause an error to be raised.

Examples

Try it in your browser!

\>>> c \= np.matrix(\[\[1\], \[2\]\])
\>>> c
matrix(\[\[1\],\
        \[2\]\])
\>>> c.squeeze()
matrix(\[\[1, 2\]\])
\>>> r \= c.T
\>>> r
matrix(\[\[1, 2\]\])
\>>> r.squeeze()
matrix(\[\[1, 2\]\])
\>>> m \= np.matrix(\[\[1, 2\], \[3, 4\]\])
\>>> m.squeeze()
matrix(\[\[1, 2\],\
        \[3, 4\]\])

Copy to clipboard

Go BackOpen In Tab

On this page