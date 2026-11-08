[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matlib.empty.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.matlib.empty.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.matlib.empty.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.matlib.empty.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.matlib.empty.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.matlib.empty.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.matlib.empty.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.matlib.empty.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.matlib.empty.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.matlib.empty.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.matlib.empty.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.matlib.empty.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.matlib.empty.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.matlib.empty.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.matlib.empty.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.matlib.empty.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.matlib.empty.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.matlib.empty.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.matlib.empty.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.matlib.empty.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.matlib.empty.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.matlib.empty.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matlib.empty[#](https://numpy.org/doc/stable/reference/generated/numpy.matlib.empty.html#numpy-matlib-empty "Link to this heading")

==========================================================================================================================================

matlib.empty(_shape_, _dtype\=None_, _order\='C'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/matlib.py#L25-L64)
[#](https://numpy.org/doc/stable/reference/generated/numpy.matlib.empty.html#numpy.matlib.empty "Link to this definition")

Return a new matrix of given shape and type, without initializing entries.

Parameters:

**shape**int or tuple of int

Shape of the empty matrix.

**dtype**data-type, optional

Desired output data-type.

**order**{‘C’, ‘F’}, optional

Whether to store multi-dimensional data in row-major (C-style) or column-major (Fortran-style) order in memory.

See also

[`numpy.empty`](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty "numpy.empty")

Equivalent array function.

[`matlib.zeros`](https://numpy.org/doc/stable/reference/generated/numpy.matlib.zeros.html#numpy.matlib.zeros "numpy.matlib.zeros")

Return a matrix of zeros.

[`matlib.ones`](https://numpy.org/doc/stable/reference/generated/numpy.matlib.ones.html#numpy.matlib.ones "numpy.matlib.ones")

Return a matrix of ones.

Notes

Unlike other matrix creation functions (e.g. [`matlib.zeros`](https://numpy.org/doc/stable/reference/generated/numpy.matlib.zeros.html#numpy.matlib.zeros "numpy.matlib.zeros")
, [`matlib.ones`](https://numpy.org/doc/stable/reference/generated/numpy.matlib.ones.html#numpy.matlib.ones "numpy.matlib.ones")
), [`matlib.empty`](https://numpy.org/doc/stable/reference/generated/numpy.matlib.empty.html#numpy.matlib.empty "numpy.matlib.empty")
 does not initialize the values of the matrix, and may therefore be marginally faster. However, the values stored in the newly allocated matrix are arbitrary. For reproducible behavior, be sure to set each element of the matrix before reading.

Examples

Try it in your browser!

\>>> import numpy.matlib
\>>> np.matlib.empty((2, 2))    \# filled with random data
matrix(\[\[  6.76425276e-320,   9.79033856e-307\], # random\
        \[  7.39337286e-309,   3.22135945e-309\]\])
\>>> np.matlib.empty((2, 2), dtype\=np.int\_)
matrix(\[\[ 6600475,        0\], # random\
        \[ 6586976, 22740995\]\])

Copy to clipboard

Go BackOpen In Tab

On this page