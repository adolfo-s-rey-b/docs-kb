[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.roots.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.roots.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.roots.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.roots.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.roots.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.roots.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.roots.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.roots.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.roots.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.roots.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.roots.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.roots.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.roots.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.roots.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.roots.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.roots.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.roots.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.roots.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.roots.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.roots.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.roots.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.roots.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.roots[#](https://numpy.org/doc/stable/reference/generated/numpy.roots.html#numpy-roots "Link to this heading")

=====================================================================================================================

numpy.roots(_p_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_polynomial_impl.py#L168-L262)
[#](https://numpy.org/doc/stable/reference/generated/numpy.roots.html#numpy.roots "Link to this definition")

Return the roots of a polynomial with coefficients given in p.

Note

This forms part of the old polynomial API. Since version 1.4, the new polynomial API defined in [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
 is preferred. A summary of the differences can be found in the [transition guide](https://numpy.org/doc/stable/reference/routines.polynomials.html)
.

The values in the rank-1 array _p_ are coefficients of a polynomial. If the length of _p_ is n+1 then the polynomial is described by:

p\[0\] \* x\*\*n + p\[1\] \* x\*\*(n\-1) + ... + p\[n\-1\]\*x + p\[n\]

Copy to clipboard

Parameters:

**p**array\_like

Rank-1 array of polynomial coefficients.

Returns:

**out**ndarray

An array containing the roots of the polynomial.

Raises:

ValueError

When _p_ cannot be converted to a rank-1 array.

See also

[`poly`](https://numpy.org/doc/stable/reference/generated/numpy.poly.html#numpy.poly "numpy.poly")

Find the coefficients of a polynomial with a given sequence of roots.

[`polyval`](https://numpy.org/doc/stable/reference/generated/numpy.polyval.html#numpy.polyval "numpy.polyval")

Compute polynomial values.

[`polyfit`](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html#numpy.polyfit "numpy.polyfit")

Least squares polynomial fit.

[`poly1d`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html#numpy.poly1d "numpy.poly1d")

A one-dimensional polynomial class.

Notes

The algorithm relies on computing the eigenvalues of the companion matrix [\[1\]](https://numpy.org/doc/stable/reference/generated/numpy.roots.html#r01a8f58ef25b-1)
.

References

\[[1](https://numpy.org/doc/stable/reference/generated/numpy.roots.html#id1)\
\]

R. A. Horn & C. R. Johnson, _Matrix Analysis_. Cambridge, UK: Cambridge University Press, 1999, pp. 146-7.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> coeff \= \[3.2, 2, 1\]
\>>> np.roots(coeff)
array(\[-0.3125+0.46351241j, -0.3125-0.46351241j\])

Copy to clipboard

Go BackOpen In Tab

On this page