[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.isfortran.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.isfortran.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.isfortran.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.isfortran.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.isfortran.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.isfortran.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.isfortran.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.isfortran.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.isfortran.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.isfortran.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.isfortran.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.isfortran.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.isfortran.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.isfortran.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.isfortran.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.isfortran.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.isfortran.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.isfortran.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.isfortran.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.isfortran.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.isfortran.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.isfortran.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.isfortran[#](https://numpy.org/doc/stable/reference/generated/numpy.isfortran.html#numpy-isfortran "Link to this heading")

=================================================================================================================================

numpy.isfortran(_a_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/numeric.py#L548-L612)
[#](https://numpy.org/doc/stable/reference/generated/numpy.isfortran.html#numpy.isfortran "Link to this definition")

Check if the array is Fortran contiguous but _not_ C contiguous.

This function is obsolete. If you only want to check if an array is Fortran contiguous use `a.flags.f_contiguous` instead.

Parameters:

**a**ndarray

Input array.

Returns:

**isfortran**bool

Returns True if the array is Fortran contiguous but _not_ C contiguous.

Examples

Try it in your browser!

np.array allows to specify whether the array is written in C-contiguous order (last index varies the fastest), or FORTRAN-contiguous order in memory (first index varies the fastest).

\>>> import numpy as np
\>>> a \= np.array(\[\[1, 2, 3\], \[4, 5, 6\]\], order\='C')
\>>> a
array(\[\[1, 2, 3\],\
       \[4, 5, 6\]\])
\>>> np.isfortran(a)
False

Copy to clipboard

\>>> b \= np.array(\[\[1, 2, 3\], \[4, 5, 6\]\], order\='F')
\>>> b
array(\[\[1, 2, 3\],\
       \[4, 5, 6\]\])
\>>> np.isfortran(b)
True

Copy to clipboard

The transpose of a C-ordered array is a FORTRAN-ordered array.

\>>> a \= np.array(\[\[1, 2, 3\], \[4, 5, 6\]\], order\='C')
\>>> a
array(\[\[1, 2, 3\],\
       \[4, 5, 6\]\])
\>>> np.isfortran(a)
False
\>>> b \= a.T
\>>> b
array(\[\[1, 4\],\
       \[2, 5\],\
       \[3, 6\]\])
\>>> np.isfortran(b)
True

Copy to clipboard

C-ordered arrays evaluate as False even if they are also FORTRAN-ordered.

\>>> np.isfortran(np.array(\[1, 2\], order\='F'))
False

Copy to clipboard

Go BackOpen In Tab

On this page