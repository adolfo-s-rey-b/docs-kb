[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.det.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.det.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.det.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.det.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.det.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.det.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.det.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.det.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.det.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.det.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.det.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.det.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.det.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.det.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.det.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.det.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.det.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.det.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.det.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.det.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.det.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.det.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.det[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.det.html#numpy-linalg-det "Link to this heading")

====================================================================================================================================

linalg.det(_a_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L2355-L2408)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.det.html#numpy.linalg.det "Link to this definition")

Compute the determinant of an array.

Parameters:

**a**(…, M, M) array\_like

Input array to compute determinants for.

Returns:

**det**(…) array\_like

Determinant of _a_.

See also

[`slogdet`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.slogdet.html#numpy.linalg.slogdet "numpy.linalg.slogdet")

Another way to represent the determinant, more suitable for large matrices where underflow/overflow may occur.

[`scipy.linalg.det`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.det.html#scipy.linalg.det "(in SciPy v1.18.0)")

Similar function in SciPy.

Notes

Broadcasting rules apply, see the [`numpy.linalg`](https://numpy.org/doc/stable/reference/routines.linalg.html#module-numpy.linalg "numpy.linalg")
 documentation for details.

The determinant is computed via LU factorization using the LAPACK routine `z/dgetrf`.

Examples

Try it in your browser!

The determinant of a 2-D array \[\[a, b\], \[c, d\]\] is ad - bc:

\>>> import numpy as np
\>>> a \= np.array(\[\[1, 2\], \[3, 4\]\])
\>>> np.linalg.det(a)
\-2.0 # may vary

Copy to clipboard

Computing determinants for a stack of matrices:

\>>> a \= np.array(\[ \[\[1, 2\], \[3, 4\]\], \[\[1, 2\], \[2, 1\]\], \[\[1, 3\], \[3, 1\]\] \])
\>>> a.shape
(3, 2, 2)
\>>> np.linalg.det(a)
array(\[-2., -3., -8.\])

Copy to clipboard

Go BackOpen In Tab

On this page