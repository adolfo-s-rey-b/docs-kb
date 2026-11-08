[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legfromroots.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.legendre.legfromroots.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legfromroots.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.legendre.legfromroots.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.legendre.legfromroots.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.legendre.legfromroots.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.legendre.legfromroots.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.legendre.legfromroots.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.legendre.legfromroots.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.legendre.legfromroots.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.legendre.legfromroots.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.legendre.legfromroots.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.legendre.legfromroots.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.legendre.legfromroots.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.legendre.legfromroots.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.legendre.legfromroots.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.legendre.legfromroots.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.legendre.legfromroots.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.legendre.legfromroots.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.legendre.legfromroots.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.legendre.legfromroots.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.legendre.legfromroots.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.legendre.legfromroots[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legfromroots.html#numpy-polynomial-legendre-legfromroots "Link to this heading")

======================================================================================================================================================================================================

polynomial.legendre.legfromroots(_roots_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/legendre.py#L268-L320)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legfromroots.html#numpy.polynomial.legendre.legfromroots "Link to this definition")

Generate a Legendre series with given roots.

The function returns the coefficients of the polynomial

in Legendre form, where the r\_n are the roots specified in [`roots`](https://numpy.org/doc/stable/reference/generated/numpy.roots.html#numpy.roots "numpy.roots")
. If a zero has multiplicity n, then it must appear in [`roots`](https://numpy.org/doc/stable/reference/generated/numpy.roots.html#numpy.roots "numpy.roots")
 n times. For instance, if 2 is a root of multiplicity three and 3 is a root of multiplicity 2, then [`roots`](https://numpy.org/doc/stable/reference/generated/numpy.roots.html#numpy.roots "numpy.roots")
 looks something like \[2, 2, 2, 3, 3\]. The roots can appear in any order.

If the returned coefficients are _c_, then

p(x) = c\_0 + c\_1 \* L\_1(x) + ... + c\_n \* L\_n(x)

The coefficient of the last term is not generally 1 for monic polynomials in Legendre form.

Parameters:

**roots**array\_like

Sequence containing the roots.

Returns:

**out**ndarray

1-D array of coefficients. If all roots are real then _out_ is a real array, if some of the roots are complex, then _out_ is complex even if all the coefficients in the result are real (see Examples below).

See also

[`numpy.polynomial.polynomial.polyfromroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyfromroots.html#numpy.polynomial.polynomial.polyfromroots "numpy.polynomial.polynomial.polyfromroots")

[`numpy.polynomial.chebyshev.chebfromroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebfromroots.html#numpy.polynomial.chebyshev.chebfromroots "numpy.polynomial.chebyshev.chebfromroots")

[`numpy.polynomial.laguerre.lagfromroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagfromroots.html#numpy.polynomial.laguerre.lagfromroots "numpy.polynomial.laguerre.lagfromroots")

[`numpy.polynomial.hermite.hermfromroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermfromroots.html#numpy.polynomial.hermite.hermfromroots "numpy.polynomial.hermite.hermfromroots")

[`numpy.polynomial.hermite_e.hermefromroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermefromroots.html#numpy.polynomial.hermite_e.hermefromroots "numpy.polynomial.hermite_e.hermefromroots")

Examples

Try it in your browser!

\>>> import numpy.polynomial.legendre as L
\>>> L.legfromroots((\-1,0,1)) \# x^3 - x relative to the standard basis
array(\[ 0. , -0.4,  0. ,  0.4\])
\>>> j \= complex(0,1)
\>>> L.legfromroots((\-j,j)) \# x^2 + 1 relative to the standard basis
array(\[ 1.33333333+0.j,  0.00000000+0.j,  0.66666667+0.j\]) # may vary

Copy to clipboard

Go BackOpen In Tab

On this page