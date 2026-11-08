[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.poly.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.poly.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.poly.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.poly.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.poly.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.poly.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.poly.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.poly.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.poly.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.poly.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.poly.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.poly.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.poly.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.poly.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.poly.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.poly.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.poly.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.poly.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.poly.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.poly.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.poly.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.poly.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.poly[#](https://numpy.org/doc/stable/reference/generated/numpy.poly.html#numpy-poly "Link to this heading")

==================================================================================================================

numpy.poly(_seq\_of\_zeros_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_polynomial_impl.py#L39-L161)
[#](https://numpy.org/doc/stable/reference/generated/numpy.poly.html#numpy.poly "Link to this definition")

Find the coefficients of a polynomial with the given sequence of roots.

Note

This forms part of the old polynomial API. Since version 1.4, the new polynomial API defined in [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
 is preferred. A summary of the differences can be found in the [transition guide](https://numpy.org/doc/stable/reference/routines.polynomials.html)
.

Returns the coefficients of the polynomial whose leading coefficient is one for the given sequence of zeros (multiple roots must be included in the sequence as many times as their multiplicity; see Examples). A square matrix (or array, which will be treated as a matrix) can also be given, in which case the coefficients of the characteristic polynomial of the matrix are returned.

Parameters:

**seq\_of\_zeros**array\_like, shape (N,) or (N, N)

A sequence of polynomial roots, or a square array or matrix object.

Returns:

**c**ndarray

1D array of polynomial coefficients from highest to lowest degree:

`c[0] * x**(N) + c[1] * x**(N-1) + ... + c[N-1] * x + c[N]` where c\[0\] always equals 1.

Raises:

ValueError

If input is the wrong shape (the input must be a 1-D or square 2-D array).

See also

[`polyval`](https://numpy.org/doc/stable/reference/generated/numpy.polyval.html#numpy.polyval "numpy.polyval")

Compute polynomial values.

[`roots`](https://numpy.org/doc/stable/reference/generated/numpy.roots.html#numpy.roots "numpy.roots")

Return the roots of a polynomial.

[`polyfit`](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html#numpy.polyfit "numpy.polyfit")

Least squares polynomial fit.

[`poly1d`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html#numpy.poly1d "numpy.poly1d")

A one-dimensional polynomial class.

Notes

Specifying the roots of a polynomial still leaves one degree of freedom, typically represented by an undetermined leading coefficient. [\[1\]](https://numpy.org/doc/stable/reference/generated/numpy.poly.html#r6c2ffae921d1-1)
 In the case of this function, that coefficient - the first one in the returned array - is always taken as one. (If for some reason you have one other point, the only automatic way presently to leverage that information is to use `polyfit`.)

The characteristic polynomial, \\(p\_a(t)\\), of an _n_\-by-_n_ matrix **A** is given by

\\(p\_a(t) = \\mathrm{det}(t\\, \\mathbf{I} - \\mathbf{A})\\),

where **I** is the _n_\-by-_n_ identity matrix. [\[2\]](https://numpy.org/doc/stable/reference/generated/numpy.poly.html#r6c2ffae921d1-2)

References

\[[1](https://numpy.org/doc/stable/reference/generated/numpy.poly.html#id1)\
\]

M. Sullivan and M. Sullivan, III, “Algebra and Trigonometry, Enhanced With Graphing Utilities,” Prentice-Hall, pg. 318, 1996.

\[[2](https://numpy.org/doc/stable/reference/generated/numpy.poly.html#id2)\
\]

G. Strang, “Linear Algebra and Its Applications, 2nd Edition,” Academic Press, pg. 182, 1980.

Examples

Try it in your browser!

Given a sequence of a polynomial’s zeros:

\>>> import numpy as np

Copy to clipboard

\>>> np.poly((0, 0, 0)) \# Multiple root example
array(\[1., 0., 0., 0.\])

Copy to clipboard

The line above represents z\*\*3 + 0\*z\*\*2 + 0\*z + 0.

\>>> np.poly((\-1./2, 0, 1./2))
array(\[ 1.  ,  0.  , -0.25,  0.  \])

Copy to clipboard

The line above represents z\*\*3 - z/4

\>>> np.poly((np.random.random(1)\[0\], 0, np.random.random(1)\[0\]))
array(\[ 1.        , -0.77086955,  0.08618131,  0.        \]) # random

Copy to clipboard

Given a square array object:

\>>> P \= np.array(\[\[0, 1./3\], \[\-1./2, 0\]\])
\>>> np.poly(P)
array(\[1.        , 0.        , 0.16666667\])

Copy to clipboard

Note how in all cases the leading coefficient is always 1.

Go BackOpen In Tab

On this page