[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matlib.eye.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.matlib.eye.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.matlib.eye.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.matlib.eye.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.matlib.eye.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.matlib.eye.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.matlib.eye.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.matlib.eye.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.matlib.eye.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.matlib.eye.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.matlib.eye.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.matlib.eye.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.matlib.eye.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.matlib.eye.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.matlib.eye.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.matlib.eye.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.matlib.eye.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.matlib.eye.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.matlib.eye.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.matlib.eye.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.matlib.eye.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.matlib.eye.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matlib.eye[#](https://numpy.org/doc/stable/reference/generated/numpy.matlib.eye.html#numpy-matlib-eye "Link to this heading")

====================================================================================================================================

matlib.eye(_n_, _M=None_, _k=0_, _dtype=<class 'float'>_, _order='C'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/matlib.py#L191-L231)
[#](https://numpy.org/doc/stable/reference/generated/numpy.matlib.eye.html#numpy.matlib.eye "Link to this definition")

Return a matrix with ones on the diagonal and zeros elsewhere.

Parameters:

**n**int

Number of rows in the output.

**M**int, optional

Number of columns in the output, defaults to _n_.

**k**int, optional

Index of the diagonal: 0 refers to the main diagonal, a positive value refers to an upper diagonal, and a negative value to a lower diagonal.

**dtype**dtype, optional

Data-type of the returned matrix.

**order**{‘C’, ‘F’}, optional

Whether the output should be stored in row-major (C-style) or column-major (Fortran-style) order in memory.

Returns:

**I**matrix

A _n_ x _M_ matrix where all elements are equal to zero, except for the _k_\-th diagonal, whose values are equal to one.

See also

[`numpy.eye`](https://numpy.org/doc/stable/reference/generated/numpy.eye.html#numpy.eye "numpy.eye")

Equivalent array function.

[`identity`](https://numpy.org/doc/stable/reference/generated/numpy.identity.html#numpy.identity "numpy.identity")

Square identity matrix.

Examples

Try it in your browser!

\>>> import numpy.matlib
\>>> np.matlib.eye(3, k\=1, dtype\=np.float64)
matrix(\[\[0.,  1.,  0.\],\
        \[0.,  0.,  1.\],\
        \[0.,  0.,  0.\]\])

Copy to clipboard

Go BackOpen In Tab

On this page