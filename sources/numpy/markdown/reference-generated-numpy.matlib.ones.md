[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matlib.ones.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.matlib.ones.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.matlib.ones.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.matlib.ones.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.matlib.ones.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.matlib.ones.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.matlib.ones.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.matlib.ones.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.matlib.ones.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.matlib.ones.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.matlib.ones.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.matlib.ones.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.matlib.ones.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.matlib.ones.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.matlib.ones.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.matlib.ones.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.matlib.ones.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.matlib.ones.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.matlib.ones.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.matlib.ones.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.matlib.ones.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.matlib.ones.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matlib.ones[#](https://numpy.org/doc/stable/reference/generated/numpy.matlib.ones.html#numpy-matlib-ones "Link to this heading")

=======================================================================================================================================

matlib.ones(_shape_, _dtype\=None_, _order\='C'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/matlib.py#L66-L109)
[#](https://numpy.org/doc/stable/reference/generated/numpy.matlib.ones.html#numpy.matlib.ones "Link to this definition")

Matrix of ones.

Return a matrix of given shape and type, filled with ones.

Parameters:

**shape**{sequence of ints, int}

Shape of the matrix

**dtype**data-type, optional

The desired data-type for the matrix, default is np.float64.

**order**{‘C’, ‘F’}, optional

Whether to store matrix in C- or Fortran-contiguous order, default is ‘C’.

Returns:

**out**matrix

Matrix of ones of given shape, dtype, and order.

See also

[`ones`](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")

Array of ones.

[`matlib.zeros`](https://numpy.org/doc/stable/reference/generated/numpy.matlib.zeros.html#numpy.matlib.zeros "numpy.matlib.zeros")

Zero matrix.

Notes

If [`shape`](https://numpy.org/doc/stable/reference/generated/numpy.shape.html#numpy.shape "numpy.shape")
 has length one i.e. `(N,)`, or is a scalar `N`, _out_ becomes a single row matrix of shape `(1,N)`.

Examples

Try it in your browser!

\>>> np.matlib.ones((2,3))
matrix(\[\[1.,  1.,  1.\],\
        \[1.,  1.,  1.\]\])

Copy to clipboard

\>>> np.matlib.ones(2)
matrix(\[\[1.,  1.\]\])

Copy to clipboard

Go BackOpen In Tab

On this page