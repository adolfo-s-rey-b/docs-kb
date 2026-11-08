[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.mapparms.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.legendre.Legendre.mapparms.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.mapparms.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.legendre.Legendre.mapparms.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.legendre.Legendre.mapparms.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.legendre.Legendre.mapparms.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.legendre.Legendre.mapparms.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.legendre.Legendre.mapparms.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.legendre.Legendre.mapparms.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.legendre.Legendre.mapparms.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.legendre.Legendre.mapparms.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.legendre.Legendre.mapparms.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.legendre.Legendre.mapparms.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.legendre.Legendre.mapparms.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.legendre.Legendre.mapparms.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.legendre.Legendre.mapparms.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.legendre.Legendre.mapparms.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.legendre.Legendre.mapparms.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.legendre.Legendre.mapparms.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.legendre.Legendre.mapparms.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.legendre.Legendre.mapparms.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.legendre.Legendre.mapparms.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.legendre.Legendre.mapparms[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.mapparms.html#numpy-polynomial-legendre-legendre-mapparms "Link to this heading")

=====================================================================================================================================================================================================================

method

polynomial.legendre.Legendre.mapparms()[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/_polybase.py#L816-L843)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.mapparms.html#numpy.polynomial.legendre.Legendre.mapparms "Link to this definition")

Return the mapping parameters.

The returned values define a linear map `off + scl*x` that is applied to the input arguments before the series is evaluated. The map depends on the `domain` and `window`; if the current `domain` is equal to the `window` the resulting map is the identity. If the coefficients of the series instance are to be used by themselves outside this class, then the linear function must be substituted for the `x` in the standard representation of the base polynomials.

Returns:

**off, scl**float or complex

The mapping function is defined by `off + scl*x`.

Notes

If the current domain is the interval `[l1, r1]` and the window is `[l2, r2]`, then the linear mapping function `L` is defined by the equations:

L(l1) \= l2
L(r1) \= r2

Copy to clipboard

On this page