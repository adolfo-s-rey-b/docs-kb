[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.slogdet.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.slogdet.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.slogdet.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.slogdet.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.slogdet.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.slogdet.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.slogdet.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.slogdet.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.slogdet.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.slogdet.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.slogdet.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.slogdet.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.slogdet.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.slogdet.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.slogdet.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.slogdet.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.slogdet.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.slogdet.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.slogdet.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.slogdet.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.slogdet.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.slogdet.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.slogdet[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.slogdet.html#numpy-linalg-slogdet "Link to this heading")

================================================================================================================================================

linalg.slogdet(_a_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L2271-L2352)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.slogdet.html#numpy.linalg.slogdet "Link to this definition")

Compute the sign and (natural) logarithm of the determinant of an array.

If an array has a very small or very large determinant, then a call to [`det`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.det.html#numpy.linalg.det "numpy.linalg.det")
 may overflow or underflow. This routine is more robust against such issues, because it computes the logarithm of the determinant rather than the determinant itself.

Parameters:

**a**(…, M, M) array\_like

Input array, has to be a square 2-D array.

Returns:

A namedtuple with the following attributes:

**sign**(…) array\_like

A number representing the sign of the determinant. For a real matrix, this is 1, 0, or -1. For a complex matrix, this is a complex number with absolute value 1 (i.e., it is on the unit circle), or else 0.

**logabsdet**(…) array\_like

The natural log of the absolute value of the determinant.

If the determinant is zero, then [`sign`](https://numpy.org/doc/stable/reference/generated/numpy.sign.html#numpy.sign "numpy.sign")
 will be 0 and _logabsdet_

will be -inf. In all cases, the determinant is equal to

`sign * np.exp(logabsdet)`.

See also

[`det`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.det.html#numpy.linalg.det "numpy.linalg.det")

Notes

Broadcasting rules apply, see the [`numpy.linalg`](https://numpy.org/doc/stable/reference/routines.linalg.html#module-numpy.linalg "numpy.linalg")
 documentation for details.

The determinant is computed via LU factorization using the LAPACK routine `z/dgetrf`.

Examples

Try it in your browser!

The determinant of a 2-D array `[[a, b], [c, d]]` is `ad - bc`:

\>>> import numpy as np
\>>> a \= np.array(\[\[1, 2\], \[3, 4\]\])
\>>> (sign, logabsdet) \= np.linalg.slogdet(a)
\>>> (sign, logabsdet)
(-1, 0.69314718055994529) # may vary
\>>> sign \* np.exp(logabsdet)
\-2.0

Copy to clipboard

Computing log-determinants for a stack of matrices:

\>>> a \= np.array(\[ \[\[1, 2\], \[3, 4\]\], \[\[1, 2\], \[2, 1\]\], \[\[1, 3\], \[3, 1\]\] \])
\>>> a.shape
(3, 2, 2)
\>>> sign, logabsdet \= np.linalg.slogdet(a)
\>>> (sign, logabsdet)
(array(\[-1., -1., -1.\]), array(\[ 0.69314718,  1.09861229,  2.07944154\]))
\>>> sign \* np.exp(logabsdet)
array(\[-2., -3., -8.\])

Copy to clipboard

This routine succeeds where ordinary [`det`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.det.html#numpy.linalg.det "numpy.linalg.det")
 does not:

\>>> np.linalg.det(np.eye(500) \* 0.1)
0.0
\>>> np.linalg.slogdet(np.eye(500) \* 0.1)
(1, -1151.2925464970228)

Copy to clipboard

Go BackOpen In Tab

On this page