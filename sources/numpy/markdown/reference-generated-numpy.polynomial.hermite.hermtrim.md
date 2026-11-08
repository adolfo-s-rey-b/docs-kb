[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermtrim.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.hermite.hermtrim.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermtrim.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.hermite.hermtrim.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.hermite.hermtrim.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.hermite.hermtrim.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.hermite.hermtrim.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.hermite.hermtrim.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.hermite.hermtrim.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.hermite.hermtrim.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.hermite.hermtrim.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.hermite.hermtrim.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.hermite.hermtrim.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.hermite.hermtrim.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.hermite.hermtrim.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.hermite.hermtrim.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.hermite.hermtrim.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.hermite.hermtrim.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.hermite.hermtrim.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.hermite.hermtrim.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.hermite.hermtrim.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.hermite.hermtrim.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.hermite.hermtrim[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermtrim.html#numpy-polynomial-hermite-hermtrim "Link to this heading")

=======================================================================================================================================================================================

polynomial.hermite.hermtrim(_c_, _tol\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/polyutils.py#L144-L192)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermtrim.html#numpy.polynomial.hermite.hermtrim "Link to this definition")

Remove “small” “trailing” coefficients from a polynomial.

“Small” means “small in absolute value” and is controlled by the parameter _tol_; “trailing” means highest order coefficient(s), e.g., in `[0, 1, 1, 0, 0]` (which represents `0 + x + x**2 + 0*x**3 + 0*x**4`) both the 3-rd and 4-th order coefficients would be “trimmed.”

Parameters:

**c**array\_like

1-d array of coefficients, ordered from lowest order to highest.

**tol**number, optional

Trailing (i.e., highest order) elements with absolute value less than or equal to _tol_ (default value is zero) are removed.

Returns:

**trimmed**ndarray

1-d array with trailing zeros removed. If the resulting series would be empty, a series containing a single zero is returned.

Raises:

ValueError

If _tol_ < 0

Examples

Try it in your browser!

\>>> from numpy.polynomial import polyutils as pu
\>>> pu.trimcoef((0,0,3,0,5,0,0))
array(\[0.,  0.,  3.,  0.,  5.\])
\>>> pu.trimcoef((0,0,1e-3,0,1e-5,0,0),1e-3) \# item == tol is trimmed
array(\[0.\])
\>>> i \= complex(0,1) \# works for complex
\>>> pu.trimcoef((3e-4,1e-3\*(1\-i),5e-4,2e-5\*(1+i)), 1e-3)
array(\[0.0003+0.j   , 0.001 -0.001j\])

Copy to clipboard

Go BackOpen In Tab

On this page