[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matrix.flatten.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.matrix.flatten.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.matrix.flatten.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.matrix.flatten.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.matrix.flatten.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.matrix.flatten.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.matrix.flatten.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.matrix.flatten.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.matrix.flatten.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.matrix.flatten.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.matrix.flatten.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.matrix.flatten.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.matrix.flatten.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.matrix.flatten.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.matrix.flatten.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.matrix.flatten.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.matrix.flatten.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.matrix.flatten.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.matrix.flatten.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.matrix.flatten.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.matrix.flatten.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.matrix.flatten.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matrix.flatten[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.flatten.html#numpy-matrix-flatten "Link to this heading")

================================================================================================================================================

method

matrix.flatten(_order\='C'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/matrixlib/defmatrix.py#L380-L415)
[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.flatten.html#numpy.matrix.flatten "Link to this definition")

Return a flattened copy of the matrix.

All _N_ elements of the matrix are placed into a single row.

Parameters:

**order**{‘C’, ‘F’, ‘A’, ‘K’}, optional

‘C’ means to flatten in row-major (C-style) order. ‘F’ means to flatten in column-major (Fortran-style) order. ‘A’ means to flatten in column-major order if _m_ is Fortran _contiguous_ in memory, row-major order otherwise. ‘K’ means to flatten _m_ in the order the elements occur in memory. The default is ‘C’.

Returns:

**y**matrix

A copy of the matrix, flattened to a _(1, N)_ matrix where _N_ is the number of elements in the original matrix.

See also

[`ravel`](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html#numpy.ravel "numpy.ravel")

Return a flattened array.

[`flat`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.flat.html#numpy.matrix.flat "numpy.matrix.flat")

A 1-D flat iterator over the matrix.

Examples

Try it in your browser!

\>>> m \= np.matrix(\[\[1,2\], \[3,4\]\])
\>>> m.flatten()
matrix(\[\[1, 2, 3, 4\]\])
\>>> m.flatten('F')
matrix(\[\[1, 3, 2, 4\]\])

Copy to clipboard

Go BackOpen In Tab

On this page